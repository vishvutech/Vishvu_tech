# Vishvu Tech 5.0 — "STRATA · The Layered Light System"

The premium rebuild of vishvutech.com. A calm, editorial, scroll-choreographed portfolio built to award-tier standards — and deployed on infrastructure that costs **$0/month**.

> The layered dawn is here. First Light banished the dark world (92–99% dark pixels → zero) — but shipped as **one colour**: 97% of pixels in a single ivory hue family, the washes sub-perceptual, the scroll without colour chapters. The Round-2 tribunal measured it and voted **100/100** for **STRATA**: a formal six-layer colour architecture — porcelain ground → tinted strata bands (sage services, powder about, blush contact, gold journal, dawn hero) → milk planes → host-tinted wells → marks → peacock ink — *each layer chosen against the composite below it*, exactly as the owner intuited. **Zero black. Zero brown. Zero dark shades — still.** Full record: `docs/Vishvu_100_Judge_Critique.md` → `docs/Vishvu_PRD_First_Light_Color_System.md` → `docs/Vishvu_100_Judge_Critique_R2_Strata.md` → `docs/Vishvu_PRD_005_Strata_Layered_Color_System.md` (VT-PRD-005; all prior colour-theme documents are void).

---

## What's inside

| Area | Implementation |
|---|---|
| **Design system** | "STRATA — Layered Light" (VT-PRD-005) — six layers: L1 porcelain ground `#F7F4EC` · L2 strata bands dawn `#FFEBE6` / gold `#FDECCF` / sage `#E7F5E7` / powder `#E3F3FF` / blush `#FFE9EA` (one dawn family, L 0.950–0.958) · L3 milk planes `#FDFCF8` (+10% lift on every band) · L4 host wells `#DCEEDC/#D8EAFD/#FCE1E0/#F7E6CA` · L5 band hairlines · L6 peacock ink `#123F3B/#3E5C58/#506561` + accent ramp `#0F766E→#0B5D57` + reserves coral/saffron/sky. Clash Display / Satoshi / Instrument Serif italic / JetBrains Mono. Single source: `assets/css/tokens.css` ↔ `v2-src/palette.py` |
| **Signature hero** | WebGL fragment-shader **strata dawn** (milk zenith → porcelain → blush band → gold-mid → warm horizon — the sky itself is a five-stop layer stack that teaches the page's grammar, powder-sky ribbon, saffron dawn glow, paper-cut ridgelines, the peacock kite) with static SVG fallback tier |
| **Motion engine** | GSAP + ScrollTrigger + Lenis (self-hosted, ~66 KB gz total): preloader, split-text reveals (**color-preserving** — accent spans survive the split), scroll-scrubbed journey rail, magnetic CTAs, custom cursor, marquee, scroll progress hairline; shadows animate instead of glows |
| **Pages** | 16 routes — home (5 acts), work index + 4 case studies (milk islands, bone wells), services (6 detail sections), about, contact (60-second form), journal + 3 essays, 404, privacy, terms |
| **Performance** | ~140 KB first load (fonts 30 KB critical, JS lazy-tiered, SVG visuals 3–5 KB each), self-hosted fonts, zero third-party requests — the flip added zero runtime cost |
| **SEO & sharing** | Per-route OG images + Twitter cards (13, regenerated on porcelain, ≤ 60 KB each), JSON-LD (Organization, Service, Article, CreativeWork), sitemap, robots, favicon suite (peacock glyph on porcelain), manifest (`theme-color #F7F4EC`) |
| **Accessibility** | WCAG 2.2 AA/AAA **verified by script** (`scripts/contrast_audit.py` — 126-pair matrix across 14 legal surfaces, zero failures; body ink 8.9–11.4:1 on every layer): skip link, peacock focus rings + halo, 1.4.11-compliant form borders (3.86:1), 44px targets, `prefers-reduced-motion` contract (3-tier), keyboard-operable everything. **Nine law gates** run before every deploy (`scripts/check-colors.sh` — incl. `scripts/banlist_scan.py` (the Ban List has no exceptions) and `scripts/band_audit.py`, which fails the deploy if the layered band rhythm ever regresses) |
| **Deploy kit** | `deploy/` — nginx config (TLS, HSTS, CSP, rate-limit, immutable caching) + `api/` contact service (Node, systemd, honeypot/time-trap/rate-limit) + `deploy/oracle-setup.md` — the full Oracle Always-Free playbook |

## Run locally

Zero build step — the site in this repo is fully static:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

The contact form tries `POST /api/contact`; on a static host with no API it gracefully falls back to a prefilled `mailto:`.

## The color system (FIRST LIGHT)

One palette, one source of truth — `v2-src/palette.py` feeds the CSS tokens, the SVG art, the favicon/icons and all 13 OG cards:

```bash
python3 v2-src/svgs.py              # regenerate the case/hero SVG art from palette.py
python3 v2-src/build.py             # rebuild pages from sources
python3 v2-src/generate_assets.py   # regenerate icons + OG cards from palette.py
bash scripts/check-colors.sh        # 8 gates incl. the Ban List + Porcelain Floor (fails deploy on violation)
```

The Ten Laws of Light govern every color decision (see `docs/Vishvu_PRD_First_Light_Color_System.md` §6.1). The short version: **the Porcelain Floor** (every canvas/surface/wash clears OKLCH L ≥ 0.94 — depth is lightness + cast shadow, never darkness); **ink is chromatic and typographic only** (peacock band 180–190°, never a neutral black, never a fill); **one jewel** (peacock owns all interaction); **reserves are sacred** (one coral italic word per page; saffron never as text); **shadows are ink-tinted** (`rgba(18,63,59,α)`, α ≤ 0.16 — never black); **no glows** (light enters as sky gradient + real shadows); **hairlines are warm** (`#E2DBC8/#CFC6AE`, interactive borders at verified 3.86:1); **alphas derive, never hardcode**; and **the Ban List is law** — any forbidden hex or dark-and-neutral colour fails the deploy (`scripts/banlist_scan.py`).

## Deploy for $0/month (production)

Follow **`deploy/oracle-setup.md`** — Oracle Cloud Always Free (ARM Ampere A1) + Cloudflare free tier. ~40 minutes from zero, 60-second rollback ritual included.

GitHub Pages also works instantly (repo root *is* the site): Settings → Pages → Deploy from `main` / root.

## Repository map

```
├─ index.html …               # the live site (static, deployable as-is)
├─ assets/
│  ├─ css/                    # tokens → base → components → pages (design system)
│  ├─ js/app/                 # motion.js · horizon.js (WebGL dawn) · form.js
│  ├─ js/vendor/              # gsap · ScrollTrigger · lenis (self-hosted)
│  ├─ img/og/                 # 13 per-route share cards (porcelain)
│  └─ fonts/                  # 8 self-hosted woff2 (latin subsets)
├─ api/                       # contact API (Node + systemd unit)
├─ deploy/                    # nginx site.conf + oracle-setup.md
├─ docs/                      # PRDs · 100-judge critique & tribunal records · content guide
├─ scripts/                   # contrast_audit.py · banlist_scan.py · check-colors.sh (the color gate toolchain)
└─ v2-src/                    # build sources (partials + page bodies + palette.py + build.py + generate_assets.py)
```

## ⚠️ Before this goes fully live — read `docs/CONTENT-GUIDE.md`

All case studies, testimonials, metrics, and personal facts currently use **structured example data** chosen to demonstrate the system at full quality. They are catalogued in the content guide with exact locations. Replace them with your real project data — the PRD's rule stands: *no invented numbers ship, ever*.

## Credits

- Fonts: Clash Display & Satoshi (Fontshare, free commercial), Instrument Serif & JetBrains Mono (Google Fonts, OFL/Apache)
- Motion: GSAP 3.13 (Webflow, standard license), Lenis
- The kite, the journey, and every line of the porcelain dawn — hand-built.

© 2026 Vishvu Tech. Built & deployed by the same pair of hands you'd hire.
