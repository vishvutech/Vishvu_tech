# CONTENT GUIDE — replace before (or right after) launch

> **The honesty contract.** The v2 site ships with structured *example data* so every system (case studies, metrics, testimonials, facts) is demonstrated at full quality. Nothing here is a real client claim yet. This file catalogues every piece of example content with its exact location. Work through it top to bottom; when a row is done, delete it.

**The rule from the PRD:** *No invented numbers ship, ever.* If a metric is unverifiable, make it qualitative ("cut loading time from noticeable to invisible") — or delete it.

---

## 1. Case studies (4 files)

| File | Example content to replace |
|---|---|
| `work/checkout-rebuild.html` | Client "Confidential D2C retail", all metrics (+31%, 4.2→0.9s, 3 steps, $0/mo, 62% tickets, 71% abandonment), founder quote, decision rows |
| `work/insightloop.html` | Client "B2B SaaS · 12 people", metrics (6h/wk, +22% Tuesday, 3 churn accounts, 11% open rate), decision rows |
| `work/clinicflow.html` | Client "Healthcare group · 3 clinics", metrics (41s, −53% calls, 7→4 fields, 92% task success), clinic director quote |
| `work/fieldops.html` | Client "Field services · 40 crews", metrics (98.6% sync, −38% admin, 4.8★, 0 lost reports), ops lead quote |

Each case study has: hero meta band, 4-stat band, problem section, decision table (4 rows), 2-figure gallery, outcome + honest retro, testimonial, 3 next-actions. **Keep the structure; swap the content.** The "What I'd do differently" sections are the trust magnets — keep them honest when you rewrite them.

## 2. Testimonials (3 quotes, 3 locations)

1. `index.html` — Act IV testimonials grid (3 cards: "F" Founder / "O" Operations Lead / "C" Clinic Director)
2. `about/index.html` — same three, repeated
3. Inside each case study — matched quote per project

Replace with real client words **with written consent**, real names/roles/companies, and photos if available (swap the initial-avatar for a photo). Until then, the role-only attribution ("Founder, D2C retail brand") is the honest ceiling.

## 3. Personal & business facts

| Location | Current example value |
|---|---|
| `index.html` hero proof strip | `14+ products · 6 services · 0 abandoned launches · 24h response` |
| `index.html` "Now shipping" card | Current project / stack / availability / last deploy |
| `index.html` + `about/` facts rail | `Bengaluru · since 2019 · 14+ live · <24h` |
| `about/index.html` timeline | 2019→now year rows |
| `about/index.html` stack table | The 6-layer stack lists |
| `contact/` + footer | `hello@vishvutech.com` · `wa.me/919999999999` (placeholder number!) · availability "December — 2 slots" |
| Footer | GitHub + LinkedIn URLs (`vishvutech` — verify handles) |
| All pages | Local time city "Bengaluru" + IST |

**The WhatsApp number `919999999999` is a placeholder — replace or remove it.**

## 4. Services pricing anchors

`services/index.html` — six "starting from" figures ($3.5k/$8k/$4k/$2.5k/$600/$3k/$800/$1.5k/$5k/$900). These anchor expectations; set them to your real floors or soften them to ranges. Also in the OG descriptions (`assets/img/og/` are generated — regenerate after content changes via `v2-src/`).

## 5. Journal essays (3)

Written as genuine, publishable field pieces (no client data, no invented engagements). Read them, edit them in `v2-src/pages/essay-*.html`, rebuild — or keep them as-is; they are honest.

## 6. Legal pages

`legal/privacy.html` and `legal/terms.html` describe the actual architecture (cookieless, 24-month retention, IP transfer) — accurate for the shipped stack. Have a human review before relying on them.

## 7. Brand & identity

- The maker's name appears as **"Vishvu"** (about, home Act IV). If you go by another name, it's in `v2-src/pages/home.html` + `about.html`.
- Photography: the About "maker visual" intentionally uses the ink journey illustration. A real duotone portrait (per PRD) is the single highest-trust upgrade you can make — drop it in `assets/img/` and swap the `<img>`.

---

## Rebuild after editing

The `v2-src/` directory holds the sources (page bodies + partials + `build.py` + `svgs.py`). After editing content there:

```bash
cd v2-src
python3 build.py        # rebuilds ../site → copy into repo root
```

Direct HTML edits to the built pages also work — the sources are for wholesale changes.

---

*Last audit of this guide: October 2026, v2.0 launch build.*
