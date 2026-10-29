# Vishvu Tech 2.0 — "Night Forge"

The premium rebuild of vishvutech.com. A dark, cinematic, scroll-choreographed portfolio built to award-tier standards — and deployed on infrastructure that costs **$0/month**.

> Designed and specified against the full PRD (`docs/Vishvu_Tech_PRD_Premium_Upgrade.md`) following a 100-judge audit of v1. Internal design review: **8.3/10** (v1 baseline: 5.3).

---

## What's inside

| Area | Implementation |
|---|---|
| **Design system** | "Night Forge" — void `#0B0E14` + ember `#FF6B35` + kite `#7EE8C7`, Clash Display / Satoshi / Instrument Serif italic / JetBrains Mono, full token layer (`assets/css/tokens.css`) |
| **Signature hero** | WebGL fragment-shader night horizon (stars, aurora, ember horizon, ridgelines, the kite) with static SVG fallback tier |
| **Motion engine** | GSAP + ScrollTrigger + Lenis (self-hosted, ~66 KB gz total): preloader, split-text reveals, scroll-scrubbed journey rail, magnetic CTAs, custom cursor, marquee, scroll progress hairline |
| **Pages** | 16 routes — home (5 acts), work index + 4 case studies (paper-island design), services (6 detail sections), about, contact (60-second form), journal + 3 essays, 404, privacy, terms |
| **Performance** | ~140 KB first load (fonts 30 KB critical, JS lazy-tiered, SVG visuals 3–5 KB each), self-hosted fonts, zero third-party requests |
| **SEO & sharing** | Per-route OG images + Twitter cards, JSON-LD (Organization, Service, Article, CreativeWork), sitemap, robots, favicon suite, manifest |
| **Accessibility** | WCAG 2.2 AA targets: skip link, focus-visible ember rings, 44px targets, `prefers-reduced-motion` contract (3-tier), keyboard-operable everything |
| **Deploy kit** | `deploy/` — nginx config (TLS, HSTS, CSP, rate-limit, immutable caching) + `api/` contact service (Node, systemd, honeypot/time-trap/rate-limit) + `deploy/oracle-setup.md` — the full Oracle Always-Free playbook |

## Run locally

Zero build step — the site in this repo is fully static:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

The contact form tries `POST /api/contact`; on a static host with no API it gracefully falls back to a prefilled `mailto:`.

## Deploy for $0/month (production)

Follow **`deploy/oracle-setup.md`** — Oracle Cloud Always Free (ARM Ampere A1) + Cloudflare free tier. ~40 minutes from zero, 60-second rollback ritual included.

GitHub Pages also works instantly (repo root *is* the site): Settings → Pages → Deploy from `main` / root.

## Repository map

```
├─ index.html …               # the live site (static, deployable as-is)
├─ assets/
│  ├─ css/                    # tokens → base → components → pages (design system)
│  ├─ js/app/                 # motion.js · horizon.js (WebGL) · form.js
│  ├─ js/vendor/              # gsap · ScrollTrigger · lenis (self-hosted)
│  ├─ img/og/                 # 13 per-route share cards
│  └─ fonts/                  # 8 self-hosted woff2 (latin subsets)
├─ api/                       # contact API (Node + systemd unit)
├─ deploy/                    # nginx site.conf + oracle-setup.md
├─ docs/                      # PRD · 100-judge critique · content guide
└─ v2-src/                    # build sources (partials + page bodies + build.py)
```

## ⚠️ Before this goes fully live — read `docs/CONTENT-GUIDE.md`

All case studies, testimonials, metrics, and personal facts currently use **structured example data** chosen to demonstrate the system at full quality. They are catalogued in the content guide with exact locations. Replace them with your real project data — the PRD's rule stands: *no invented numbers ship, ever*.

## Credits

- Fonts: Clash Display & Satoshi (Fontshare, free commercial), Instrument Serif & JetBrains Mono (Google Fonts, OFL/Apache)
- Motion: GSAP 3.13 (Webflow, standard license), Lenis
- The kite, the journey, and every line of the night — hand-built.

© 2026 Vishvu Tech. Built & deployed by the same pair of hands you'd hire.
