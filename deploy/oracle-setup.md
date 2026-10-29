# Oracle Cloud Free Tier — Production Setup Guide
## Vishvu Tech 2.0 · from zero to live in ~40 minutes

This is the exact playbook for hosting vishvutech.com on Oracle's **Always Free** tier behind Cloudflare — total cost **$0/month**. It is the same stack described in `/journal/oracle-free-tier.html`.

---

## 0. What you get

| Layer | Choice | Cost |
|---|---|---|
| VM | VM.Standard.A1.Flex · 2 OCPU · 12 GB · Ubuntu 24.04 | $0 (Always Free) |
| Edge | Cloudflare free — CDN, TLS, DDoS, Turnstile | $0 |
| Web server | nginx (static + API proxy) | $0 |
| Contact API | Node 22, ~200 LOC, systemd-managed | $0 |
| Email | OCI Email Delivery (3,000/mo) | $0 |
| Backups | Nightly → OCI Object Storage (10 GB) | $0 |

## 1. Provision the VM

1. Oracle Cloud Console → **Compute → Instances → Create**
2. Name `vishvutech`; Image **Canonical Ubuntu 24.04**; Shape **VM.Standard.A1.Flex**, 2 OCPU / 12 GB
3. Networking: new VCN + public subnet; assign public IPv4
4. SSH key: upload your **own** public key (generate with `ssh-keygen -t ed25519` if needed)
5. Boot volume: 60 GB
6. **If you hit "Out of capacity"**: retry later, or try another availability domain / region — free ARM capacity comes and goes. Retry daily; it clears.

Security list (VCN → Subnet → Security List): allow ingress **22** (your IP only), **80** and **443** (0.0.0.0/0). That's all.

## 2. First login + baseline

```bash
ssh -i ~/.ssh/id_ed25519 ubuntu@<PUBLIC_IP>
sudo apt update && sudo apt upgrade -y
sudo apt install -y nginx nodejs npm git ufw fail2ban
sudo adduser --disabled-password --gecos "" vishvu
sudo mkdir -p /var/www/vishvutech /var/lib/vishvutech /opt/vishvutech/api /etc/nginx/ssl
sudo chown -R vishvu:vishvu /var/lib/vishvutech

# firewall: only what we need
sudo ufw allow 22,80,443/tcp
sudo ufw --force enable
```

## 3. Cloudflare + TLS

1. At your registrar, point nameservers to Cloudflare (free plan)
2. Cloudflare DNS: `A vishvutech.com → <PUBLIC_IP>` (Proxy **ON**, orange cloud), `CNAME www → vishvutech.com` (Proxy ON)
3. **SSL/TLS → Origin Server → Create Certificate** (RSA 2048, hosts `vishvutech.com, *.vishvutech.com`, 15 years)
4. Copy cert + key to the VM:
   ```bash
   sudo nano /etc/nginx/ssl/vishvutech-origin.pem   # paste certificate
   sudo nano /etc/nginx/ssl/vishvutech-origin.key   # paste private key
   sudo chmod 600 /etc/nginx/ssl/vishvutech-origin.*
   ```
5. **SSL/TLS → Overview → Full (strict)** mode
6. Enable: Always Use HTTPS, Brotli, HTTP/3, Tiered Cache

## 4. Deploy the site

From your machine:

```bash
# site content
rsync -az --delete site/ ubuntu@<IP>:/tmp/site/
ssh ubuntu@<IP> "sudo rm -rf /var/www/vishvutech/* && sudo cp -r /tmp/site/. /var/www/vishvutech/ && sudo rm -rf /tmp/site"

# nginx config
scp deploy/nginx/site.conf ubuntu@<IP>:/tmp/
ssh ubuntu@<IP> "sudo cp /tmp/site.conf /etc/nginx/sites-available/vishvutech && sudo ln -sf /etc/nginx/sites-available/vishvutech /etc/nginx/sites-enabled/ && sudo rm -f /etc/nginx/sites-enabled/default && sudo nginx -t && sudo systemctl reload nginx"
```

## 5. Contact API

```bash
scp api/index.js api/package.json ubuntu@<IP>:/tmp/
ssh ubuntu@<IP> "
  sudo cp /tmp/index.js /tmp/package.json /opt/vishvutech/api/
  cd /opt/vishvutech/api && sudo -u vishvu npm install --omit=dev
  sudo cp /tmp/../contact-api.service /etc/systemd/system/  # (or scp it separately)
"
# enable + start
sudo systemctl daemon-reload
sudo systemctl enable --now contact-api
curl http://127.0.0.1:8081/api/health   # → {"ok":true}
```

## 6. Email delivery (OCI Email Delivery)

1. Console → **Email Delivery → Email Approved Senders** → add `website@vishvutech.com`
2. Generate **SMTP credentials** for your user (Connection Security: TLS)
3. Fill the `SMTP_*` environment lines in `/etc/systemd/system/contact-api.service`, then:
   ```bash
   sudo systemctl restart contact-api
   ```
4. DNS (at Cloudflare, TXT records per OCI's generated values):
   - SPF: `v=spf1 include:oracleemailcloud.com ~all`
   - DKIM: the three `sel1._domainkey` … records OCI shows you
   - DMARC: `v=DMARC1; p=none; rua=mailto:hello@vishvutech.com`
5. **Test to Gmail, Outlook, and Yahoo** before trusting it.

## 7. Backups (nightly)

```bash
sudo -u vishvu crontab -e
# m h  dom mon dow   command
30 2 * * * tar -czf /tmp/site.tgz -C /var/www vishvutech && /usr/local/bin/backup-push.sh
```

`backup-push.sh` uses `rclone` (apt install rclone) configured for OCI Object Storage (`rclone config` — s3-compatible endpoint from your tenancy's Object Storage settings). Do a **restore drill** once: download the tarball on your laptop, extract, open `index.html`. A backup you haven't restored is a hope, not a backup.

## 8. Monitoring (free)

- UptimeRobot (free): HTTP checks on `https://vishvutech.com/` and `https://vishvutech.com/api/health` every 5 min
- Cloudflare Analytics: traffic overview
- Later (optional): self-hosted Umami for cookieless analytics on the same VM

## 9. The deploy ritual (every release)

```bash
rsync -az --delete site/ ubuntu@<IP>:/tmp/site/
ssh ubuntu@<IP> "sudo rm -rf /var/www/vishvutech.prev && sudo mv /var/www/vishvutech /var/www/vishvutech.prev && sudo mkdir /var/www/vishvutech && sudo cp -r /tmp/site/. /var/www/vishvutech/"
# rollback if anything looks wrong:
ssh ubuntu@<IP> "sudo rm -rf /var/www/vishvutech && sudo mv /var/www/vishvutech.prev /var/www/vishvutech"
```

60-second rollback, zero downtime (immutable HTML swap).

## 10. Known Oracle-free-tier realities (read once)

- **Idle reclamation**: Always Free VMs flagged as idle (very low CPU for 7 days) *can* be stopped. Real traffic + the API + monitoring keep you clear; add a light cron heartbeat if paranoid.
- **Capacity errors** on creation are temporary — retry.
- **ARM only**: every package you install must have `arm64` builds (nginx, node: yes; always check third-party panels).
- **10 TB/month egress** — effectively unlimited for a portfolio; Cloudflare caching means most traffic never touches the origin anyway.

---

*Problems? The Journal essay `/journal/oracle-free-tier.html` covers the three failure modes in detail.*
