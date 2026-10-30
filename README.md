# Vishvu Tech 3.0 — "Golden Hour"

The premium rebuild of vishvutech.com. A warm, cinematic, scroll-choreographed portfolio built to award-tier standards — and deployed on infrastructure that costs **$0/month**.

> Designed against the full PRD lineage (`docs/`) following a 100-judge audit of v1 (5.3 → 8.3 internal review), re-audited for the Forge Noir color system (6.03 → 8.86, later overruled by the owner's eye), then condemned by VT-CTA-004 (**7.30 — REVISE: "the dark theme reads black"**) — and rebuilt as Golden Hour: espresso & champagne, the escape from black (`docs/PRD-GOLDEN-HOUR.md`).

---

## What's inside

| Area | Implementation |
|---|---|
| **Design system** | "Golden Hour" — espresso roast `#251A11` (OKLCH 0.230 0.024 60 — warmth **visible** by law) + champagne ramp `#E9E1B0→#5A3E00` (accent `#DAC46D`, deliberately softer than the `#D4AF37` jewelry band) + bone text `#EDEAE2/#C2BCB1/#A8A196` + ledger cream `#EFEBDF` with warm ink; dusk ribbon `#81AFA9` confined to hero-sky art by law; the kite is brass `#D3AB54`. Clash Display / Satoshi / Instrument Serif italic / JetBrains Mono. Three-tier tokens: primitives → semantic → component (`assets/css/tokens.css`, single source: `v2-src/palette.py`) |
| **Signature hero** | WebGL fragment-shader golden dusk (stars, dusk ribbon, champagne horizon, amber-glow ridgelines, the brass kite) with static SVG fallback tier |
| **Motion engine** | GSAP + ScrollTrigger + Lenis (self-hosted, ~66 KB gz total): preloader, split-text reveals, scroll-scrubbed journey rail, magnetic CTAs, custom cursor, marquee, scroll progress hairline |
| **Pages** | 16 routes — home (5 acts), work index + 4 case studies (paper-island design), services (6 detail sections), about, contact (60-second form), journal + 3 essays, 404, privacy, terms |
| **Performance** | ~140 KB first load (fonts 30 KB critical, JS lazy-tiered, SVG visuals 3–5 KB each), self-hosted fonts, zero third-party requests — unchanged by the re-grade (pure static work) |
| **SEO & sharing** | Per-route OG images + Twitter cards, JSON-LD (Organization, Service, Article, CreativeWork), sitemap, robots, favicon suite, manifest (`theme-color #251A11`) |
| **Accessibility** | WCAG 2.2 AA **verified by script** (`scripts/contrast_audit.py` — the 30-pair matrix, zero failures, 24 AAA-level): skip link, focus-visible champagne rings (9.80:1), 1.4.11-compliant form borders (3.96:1), 44px targets, `prefers-reduced-motion` contract (3-tier), keyboard-operable everything. Seven law gates run before every deploy (`scripts/check-colors.sh`) |
| **Deploy kit** | `deploy/` — nginx config (TLS, HSTS, CSP, rate-limit, immutable caching) + `api/` contact service (Node, systemd, honeypot/time-trap/rate-limit) + `deploy/oracle-setup.md` — the full Oracle Always-Free playbook |

## Run locally

Zero build step — the site in this repo is fully static:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

The contact form tries `POST /api/contact`; on a static host with no API it gracefully falls back to a prefilled `mailto:`.

## The color system (Golden Hour)

One palette, one source of truth — `v2-src/palette.py` feeds the CSS tokens, the SVG art, the favicon/icons and all 13 OG cards:

```bash
python3 v2-src/build.py             # rebuild pages from sources
python3 v2-src/generate_assets.py  # regenerate icons + OG cards from palette.py
bash scripts/check-colors.sh       # 7 gates incl. the Black Floor + Hue Floor (fails deploy on violation)
```

Thirteen laws govern every color decision (see `docs/PRD-GOLDEN-HOUR.md` §12.7). The short version: **the Black Floor** (no surface in the black zone — OKLCH L ≥ 0.22 or C ≥ 0.035) and **the Hue Floor** (canvas-family chroma ≥ 0.018 — warmth must be a perception, not a spec comment); champagne owns interaction; the dusk ribbon never touches UI; gradients stay in-family (champagne 300→500); paper text gets champagne-700, paper marks get champagne-600; signal hues stay 30° clear of champagne (warn is copper); no raw color — hex **or** rgba — outside `tokens.css`; every text pair clears 4.5:1, verified by script, never by eye.

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
├─ docs/                      # PRDs · 100-judge audits (v1, color, verdict) · content guide
├─ scripts/                   # contrast_audit.py · check-colors.sh · capture.sh (the color gate toolchain)
└─ v2-src/                    # build sources (partials + page bodies + palette.py + build.py + generate_assets.py)
```

## ⚠️ Before this goes fully live — read `docs/CONTENT-GUIDE.md`

All case studies, testimonials, metrics, and personal facts currently use **structured example data** chosen to demonstrate the system at full quality. They are catalogued in the content guide with exact locations. Replace them with your real project data — the PRD's rule stands: *no invented numbers ship, ever*.

## Credits

- Fonts: Clash Display & Satoshi (Fontshare, free commercial), Instrument Serif & JetBrains Mono (Google Fonts, OFL/Apache)
- Motion: GSAP 3.13 (Webflow, standard license), Lenis
- The kite, the journey, and every line of the golden dusk — hand-built.

© 2026 Vishvu Tech. Built & deployed by the same pair of hands you'd hire.
