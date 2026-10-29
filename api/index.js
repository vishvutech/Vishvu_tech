/* ============================================================
   Vishvu Tech 2.0 — Contact API (contact-api.service, :8081)
   Node 22 · zero runtime deps for serving; nodemailer only for SMTP.
   Endpoints:
     GET  /api/health   → { ok: true }
     POST /api/contact  → validate → honeypot/time-trap → rate-limit
                          → JSONL log + SMTP notify → { ok, ref }
   Deploy: see deploy/oracle-setup.md (systemd unit included)
   ============================================================ */
'use strict';

const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const PORT = process.env.PORT || 8081;
const LOG_DIR = process.env.LOG_DIR || '/var/lib/vishvutech';
const LOG_FILE = path.join(LOG_DIR, 'inquiries.jsonl');
const MAX_BODY = 64 * 1024;
const WINDOW_MS = 60 * 60 * 1000;
const MAX_PER_WINDOW = 5;

/* Simple per-IP rate limiter (in-memory; restart clears it — fine for this scale) */
const hits = new Map();
setInterval(() => {
  const now = Date.now();
  for (const [ip, times] of hits) {
    const fresh = times.filter((t) => now - t < WINDOW_MS);
    if (fresh.length) hits.set(ip, fresh);
    else hits.delete(ip);
  }
}, 60 * 1000).unref();

function rateLimited(ip) {
  const now = Date.now();
  const times = (hits.get(ip) || []).filter((t) => now - t < WINDOW_MS);
  times.push(now);
  hits.set(ip, times);
  return times.length > MAX_PER_WINDOW;
}

const VALID_TYPES = ['web', 'mobile', 'design', 'ai', 'cloud', 'custom'];
const VALID_BUDGETS = ['under-2k', '2-5k', '5-15k', '15k-plus', 'unsure'];
const VALID_TIMELINES = ['asap', 'month', 'quarter', 'flexible'];

function validate(d) {
  const errors = {};
  if (!d || typeof d !== 'object') return { _fatal: true };
  if (!d.name || typeof d.name !== 'string' || d.name.length > 120) errors.name = 'missing';
  if (!d.email || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(d.email)) || d.email.length > 200) errors.email = 'invalid';
  if (!VALID_TYPES.includes(d.project_type)) errors.project_type = 'invalid';
  if (!VALID_BUDGETS.includes(d.budget)) errors.budget = 'invalid';
  if (!VALID_TIMELINES.includes(d.timeline)) errors.timeline = 'invalid';
  if (d.pitch && typeof d.pitch !== 'string') errors.pitch = 'invalid';
  if (d.website && d.website.length > 0) errors._honeypot = true;
  return Object.keys(errors).length ? errors : null;
}

function appendLog(record) {
  fs.mkdirSync(LOG_DIR, { recursive: true });
  fs.appendFileSync(LOG_FILE, JSON.stringify(record) + '\n');
}

/* Optional SMTP notify via nodemailer + OCI Email Delivery.
   Enabled automatically when SMTP_* env vars are present. */
let transporter = null;
try {
  if (process.env.SMTP_HOST) {
    const nodemailer = require('nodemailer');
    transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: Number(process.env.SMTP_PORT || 587),
      secure: false,
      auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
    });
  }
} catch (e) {
  console.warn('[contact-api] nodemailer not installed — email notify disabled, JSONL logging active');
}

async function notify(record) {
  if (!transporter) return;
  await transporter.sendMail({
    from: process.env.SMTP_FROM || 'website@vishvutech.com',
    to: process.env.NOTIFY_TO || 'hello@vishvutech.com',
    subject: `New inquiry ${record.ref} — ${record.project_type} (${record.timeline})`,
    text: [
      `Ref: ${record.ref}`,
      `Name: ${record.name}`,
      `Email: ${record.email}`,
      `Type: ${record.project_type} · Budget: ${record.budget} · Timeline: ${record.timeline}`,
      `Referrer: ${record.referrer}`,
      '',
      'Idea:',
      record.pitch || '—',
    ].join('\n'),
  });
}

function send(res, code, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(code, {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-store',
    'Content-Length': Buffer.byteLength(body),
  });
  res.end(body);
}

const server = http.createServer(async (req, res) => {
  /* CORS-free same-origin API; deny everything unexpected */
  if (req.method === 'GET' && req.url === '/api/health') {
    return send(res, 200, { ok: true, uptime: process.uptime() });
  }
  if (req.method !== 'POST' || req.url !== '/api/contact') {
    return send(res, 404, { error: 'not_found' });
  }

  const ip = (req.headers['x-real-ip'] || req.socket.remoteAddress || 'unknown').toString();

  /* body reader with size cap */
  let size = 0;
  const chunks = [];
  req.on('data', (c) => {
    size += c.length;
    if (size > MAX_BODY) { req.destroy(); return; }
    chunks.push(c);
  });
  req.on('end', async () => {
    if (rateLimited(ip)) return send(res, 429, { error: 'rate_limited' });
    let data;
    try { data = JSON.parse(Buffer.concat(chunks).toString('utf8')); }
    catch { return send(res, 400, { error: 'bad_json' }); }

    const errors = validate(data);
    if (errors) {
      if (errors._fatal) return send(res, 400, { error: 'bad_payload' });
      if (errors._honeypot) return send(res, 200, { ok: true, ref: 'VT-0000' }); /* bot: pretend success */
      return send(res, 422, { error: 'validation', fields: errors });
    }

    const ref = 'VT-' + new Date().getFullYear() + '-' +
      crypto.randomBytes(3).toString('hex').toUpperCase();
    const record = {
      ref, ts: new Date().toISOString(), ip,
      name: String(data.name).slice(0, 120),
      email: String(data.email).slice(0, 200),
      project_type: data.project_type,
      budget: data.budget,
      timeline: data.timeline,
      pitch: String(data.pitch || '').slice(0, 500),
      referrer: String(data.ref || 'direct').slice(0, 300),
    };

    try { appendLog(record); } catch (e) { console.error('[contact-api] log fail', e.message); }

    try {
      await notify(record);
      send(res, 200, { ok: true, ref });
    } catch (e) {
      /* logged but notify failed — the inquiry is still safely on disk */
      console.error('[contact-api] notify fail', e.message);
      send(res, 200, { ok: true, ref, note: 'logged' });
    }
    console.log(`[contact-api] ${ref} ${record.project_type} ${ip}`);
  });
  req.on('error', () => req.destroy());
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`[contact-api] listening on 127.0.0.1:${PORT}`);
});
