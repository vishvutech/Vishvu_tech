# PRODUCT REQUIREMENTS DOCUMENT
# VISHVU TECH — "FORGE NOIR"
### The Premium Color System Upgrade · From "Night Forge" to an award-grade, owned palette

---

| Field | Value |
|---|---|
| **Document ID** | VT-PRD-002 |
| **Version** | 1.0 |
| **Date** | October 29, 2026 |
| **Status** | Ready for build |
| **Author** | The 100-Judge Tribunal, reconvened as the Research Council — distilled into a single specification |
| **Domain** | **Color system only** (per session mandate). Typography, layout, motion timing, and content are out of scope except where they intersect color. |
| **Product** | Vishvu Tech portfolio & lead-generation website — solo senior engineer, Bengaluru. Services: websites, mobile apps, UI design, cloud deployment, AI & automation, custom software. |
| **Baseline** | `github.com/vishvutech/Vishvu_tech` @ commit `bffdb5f` — "Night Forge" v2.0 rebuild |
| **Baseline color score** | **6.03 / 10** (VT-CTA-002 tribunal, Awwwards-weighted, color domain) |
| **Target** | **≥ 7.5 / 10** on the same rubric · zero WCAG 2.2 AA failures · a palette the market can attribute to Vishvu Tech in 3 seconds |
| **Deployment target** | **Oracle Cloud Always Free** (post-June-2026 envelope: 2 OCPU / 12 GB RAM Ampere A1) + nginx static serving |
| **Companion documents** | `VishvuTech_100-Judge_Color_Audit.md` (evidence & verdicts) · `VishvuTech_Palette_Preview.png` (visual spec companion) |
| **Estimated effort** | 3 phases · 4–6 focused days total · zero new dependencies · zero runtime cost |

---

# 1. EXECUTIVE SUMMARY

The tribunal confirmed the owner's instinct with precision: the current "Night Forge" theme is a **top-decile execution of a bottom-decile concept**. The craft is real — render reviews scored it 7.5–9.0 — but the palette as a cluster (blue-cast near-black + traffic-cone orange + teal-mint sidekick + dual-hue diagonal gradient + neon glow) is the statistical center of AI-generated dark-portfolio output. Visitors pattern-match the cluster, not the code quality, and file the site as generated. Worse, the math found four hard accessibility failures on the pages that carry the business: case-study kickers at **2.48:1**, card meta text at **3.97:1**, selection/skip-link at **2.84:1**, and input borders at **1.66:1** — plus a token file whose comments promise contrast values its pixels do not deliver.

**This PRD specifies "Forge Noir"** — a warm-obsidian color system that keeps everything the tribunal ordered protected (the dark instinct, the single-accent discipline, the cream paper islands, the token-first architecture, the zero-dependency stack) and replaces everything the evidence convicted:

1. **Own the temperature.** The canvas shifts from generic blue-cast near-black to a warm smoked-iron obsidian (OKLCH hue 75°, whisper chroma) — the single move that kills the "Tailwind-slate dark" read.
2. **One accent, five grades.** The traffic-cone orange becomes a *molten ember ramp* (300→700) with dedicated marks-grade and text-grade values for paper contexts — fixing every accent-contrast failure by construction, not by patch.
3. **Retire the sidekick.** The mint is renamed *aurora* and confined by law to illustrations and the hero night sky — the cool light above the warm forge. It never touches UI again.
4. **Light from within.** Neon glow tokens are deleted (budget: two 10px pulse-dot halos). Elevation comes from inset highlights and the surface ramp.
5. **Gradients stay in-family.** The dual-hue diagonal is retired forever; the one permitted gradient is an ember-300→600 lightness ramp on the scroll-progress hairline.
6. **A system with a spine.** Three-tier tokens (primitive ramps → semantic → component), warm paper ink, an interactive-border token that passes 1.4.11, one palette source consumed by both CSS and the SVG generator, and a scripted contrast gate that runs before every deploy.

Every value in this document is **computationally verified** — the full 29-pair WCAG matrix passes with margin (§7.5). The entire upgrade ships as static CSS and SVG file changes: zero JavaScript, zero build step, zero impact on the Oracle Free Tier envelope, ~2 KB of CSS delta.

**The bet, in one sentence:** the cheapest redesign that can move this site's ceiling is a palette that stops being everyone's — and this document makes that palette exact, lawful, and verifiable.

---

# 2. BACKGROUND & CONTEXT

## 2.1 The product

Vishvu Tech is the portfolio and lead-generation site of a solo senior software engineer in Bengaluru offering six services: websites, mobile apps, UI design, cloud deployment, AI & automation, and custom software. The site is a hand-built static system (no framework, no build step): ~16 HTML pages, five CSS files (2,026 lines), ~24 KB of hand-rolled JS on top of a GSAP/Lenis vendor stack, self-hosted subsetted fonts (Clash Display, Satoshi, Instrument Serif, JetBrains Mono), and a Python generator (`v2-src/build.py` + `svgs.py`) that produces the illustrated case-study SVGs. It deploys as static files behind nginx on Oracle Cloud Always Free. A Node contact API (`api/`) handles form submissions.

This is, structurally, an exemplary portfolio chassis: fast, dependency-light, cache-friendly, and perfectly matched to a free-tier deployment. **Nothing in this PRD changes the chassis.** The color system rides on CSS custom properties that already exist — this is a re-skin at the token layer plus a disciplined component pass.

## 2.2 The two-audit history

- **Session I (VT-CTA-001)** audited the original v1 site at **5.32/10** — a competent brochure with no proof, no performance discipline, and no identity. The v2.0 "Night Forge" rebuild was the response, and it succeeded on every axis it targeted: case studies with measured outcomes, cinematic scroll choreography, sub-second paints, a real contact funnel.
- **Session II (VT-CTA-002)** audited the rebuild's **color theme** at **6.03/10**. The finding: v2 fixed everything *around* the palette while installing a palette *borrowed from the crowd*. The owner's complaint — "it still reads cheap, dark, AI-generated" — was confirmed and located: five cluster markers that together form the recognizable fingerprint of generated dark sites (§3.2).

## 2.3 Why color, and why now

Color is the highest-leverage remaining surface. The site now has proof (case studies), performance (static, subsetted, CDN-cacheable), and motion craft (GSAP/Lenis choreography). What it lacks is the 3-second attribution test: *close your eyes and name whose site was the warm-black one with the burnt-ember accent.* Today, nobody can — the palette is anonymous by construction. Because the entire system is already tokenized, color is also the **cheapest** major upgrade available: no content, no layout, no stack changes — value swaps, component polish, and art re-inking.

## 2.4 Deployment constraint: Oracle Always Free, October 2026

Oracle halved the Always Free Ampere A1 allowance in mid-2026 (4 OCPU / 24 GB → **2 OCPU / 12 GB**; first 3,000 OCPU-hours and 18,000 GB-hours per month free). The site's zero-build static architecture remains the correct response to that envelope: nginx serves files, the contact API is a single small Node process, and there is headroom to spare. **This PRD is engineered to respect the constraint absolutely:** every change is static CSS/SVG/Python-generator work; there is no new runtime, no server-side rendering, no image-processing pipeline. The color upgrade costs zero CPU, zero memory, and ~2 KB of transfer.

---
# 3. PROBLEM STATEMENT — WHAT THE TRIBUNAL PROVED

## 3.1 The paradox

The four blind render reviews scored execution between 7.5 and 9.0. The tribunal's weighted color score is 6.03. Both numbers are correct, and the gap between them **is** the problem: craft borrowed a concept. As Judge 51 put it: *"You built a beautiful house from a plan everyone owns."* The owner's perception — "cheap, dark, AI-generated" — is not imposter syndrome; it is a correct pattern-match by the market against the palette cluster below.

## 3.2 The five cluster markers (all present at `bffdb5f`)

| # | Marker | Where it lives (evidence) |
|---|---|---|
| 1 | Blue-cast near-black canvas | `--vf-void #0B0E14`, `--vf-surface #111623` (hue ≈ 255°) — the default dark of Tailwind slate/zinc territory |
| 2 | Traffic-cone orange primary | `--vf-ember #FF6B35` — maximum-chroma orange, "Fruit Loops" adjacency per render review |
| 3 | Teal-mint sidekick in UI | `--vf-kite #7EE8C7` as **text** in 13 places, despite its own "gradients only" contract |
| 4 | Dual-hue 135° diagonal gradient | brand glyph, progress hairline, `.gradient-text`, contact icons — the single most-submitted AI gradient |
| 5 | Neon glow ornamentation | 24px/32px blurred shadows as ambient decoration |

Any four of five reads as coincidence. All five reads as generated. The fix is not to soften any marker — it is to **break the cluster** by replacing each with an owned equivalent.

## 3.3 The measured failures (the non-negotiables)

| Failure | Value | Where it ships |
|---|---|---|
| Ember text on paper | **2.48:1** | Every case-study kicker, stat unit, decision-table letter (all 4 case pages + services proof) |
| Tertiary ink on cards | **3.97:1** (canvas 4.25:1, hover 3.53:1) | All mono labels, breadcrumbs, meta, timestamps, char counters sitewide |
| White on ember | **2.84:1** | `::selection`, skip-link |
| Input borders | **1.66:1** vs 1.4.11's 3:1 | Contact form fields, chips |
| Documentation integrity | claim vs reality | `tokens.css` documents "5.0:1, 14px minimum"; pixels deliver 4.25:1 at 13.4px |

## 3.4 The system defects (the compounding costs)

1. **Temperature scrambled** — cool canvas, warm accent, cool mint, warm paper carrying *blue-cast* ink (`#1C2433`). No committed warmth anywhere; the eye registers wrongness it cannot name.
2. **Inverted accent hierarchy** — the secondary mint measures 13.11:1 as text; the primary ember measures 6.81:1. The understudy upstages the lead.
3. **No ramps** — singleton hand-picked values with ad-hoc hovers; no text-grade, marks-grade, pressed, disabled, or series steps. The 15+ raw-hex leaks (`#232C44`, `#37415A`, `#FFFEFA`, `#fff`, `#000`, `#6E7890`) are the visible symptoms.
4. **Two sources of truth** — `v2-src/svgs.py` hardcodes the palette for every generated illustration, favicon included. Any token change silently forks the art.
5. **Dark-only without mode-ready tokens** — legitimate choice, but the token shapes don't permit a future `prefers-color-scheme` flip even though the `.paper` context proves the author already knows the scoping pattern.

## 3.5 What must NOT change (tribunal protection orders)

The dark instinct. Single-primary-accent discipline. The cream paper islands and their warm off-white value. Universal ember focus-visible rings. Brand-colored selection (re-paired). The `tokens.css`-as-source-of-truth architecture and the `.paper` context mechanism. The grain layer. The SVG narrative art (re-inked, not redesigned). The zero-dependency CSS-only color stack. **This PRD upgrades around these, never over them.**

---

# 4. RESEARCH SYNTHESIS — WHAT ACTUALLY WINS

*The council's fieldwork: award-circle analysis, color-science review, market scan. Sources in Appendix B.*

## 4.1 The bar being targeted

Awwwards juries score Design 40% / Usability 30% / Creativity 20% / Content 10%; SOTD winners land 7.3–7.6, Sites of the Year 7.8–8.5. The October 2026 SOTD roster (A24 by Ravi Klaassens, FORMAT by Obys, ESR Bespoke by Nightjar, G. Colombel, Forge Automotive, Nick Ho by Boring, Odyssée…) shares a color signature the council distilled into five recurring patterns:

## 4.2 Five winner patterns (2024–2026)

1. **An owned canvas temperature.** Winning darks commit: warm blacks, green-blacks, ink-blacks. The blue-cast near-black default is, in Judge 51's phrase, *"the new bootstrap-white."* Temperature is the cheapest differentiator because it costs chroma you weren't using anyway.
2. **Two colors total, or one accent and zero sidekicks.** Reference case: SOTD "Due" — `#2757FF` on `#1A1A1B`, nothing else. A primary accent *plus* a mint partner *plus* a cream sub-theme is a three-accent system wearing a two-accent costume. (The cream stays in Forge Noir — but as a *surface world*, not an accent.)
3. **Gradients that stay in-family.** Winners who gradient run monochromatic lightness ramps or material metaphors (molten, dusk, smoke). Complementary dual-hue diagonals are the most-rejected gradient of the AI era.
4. **Texture as color; light from within.** Grain, duotone, layered translucency, inset highlights — candlelight, not neon. Glow budgets on winning dark sites approach zero; illumination is simulated by lightness steps and 1px inner highlights.
5. **Typography-led color.** The type IS the color story: massive ink-white headlines with one accented word. Distributed accent sprinkles read as seasoning; one chromatic moment per viewport reads as authorship.

## 4.3 Color science foundations (the engineering basis)

- **OKLCH as the system space.** OKLCH's perceptually-uniform lightness means equal L *looks* equally bright across hues; ramps built on uniform L steps stay balanced; dark-mode variants are "one lightness step lighter," geometrically (Evil Martians; Carmen Ansio, Feb 2026). Forge Noir's primitives are specified in OKLCH with hex fallbacks.
- **Tinted neutrals.** Pure zero-chroma grays feel cold and disconnected; a whisper of hue (chroma 0.005–0.010) in the brand direction makes a palette cohesive without being noticeable ("nobody notices it consciously; everyone notices when it's missing"). Forge Noir's ash ramp carries chroma 0.006–0.010 at hue 75°.
- **Chroma discipline.** sRGB-safe chroma tops out ~0.20–0.32 depending on hue; the tint/neutral/mid/vivid bands are 0–0.10 / 0.10–0.20 / 0.20–0.32. The ember ramp peaks at 0.17 — vivid but display-safe.
- **Radix-style scale semantics.** 12-step scales where the *same step number* means the same *role* across hues; steps 11–12 are the "accessible text" grades. Forge Noir adopts the role idea (text-grade / marks-grade / surface-grade accent variants) without Radix's full 12 steps — a solo static site needs 5-grade ramps, not 30 scales.
- **Material dark-theme guidance.** Elevation on dark surfaces = lighter surface, not shadow-fog; 4–6 discernible levels; overlays tuned for legibility. Forge Noir uses a 5-step surface ladder (canvas → surface-1 → surface-2 → line → line-strong) plus inset highlights.
- **NN/g dark-mode findings.** Dark mode is used by ~⅓ of mobile users; the top dark-mode failure is low-contrast gray text; "softer dark tones + strong text contrast" is the recommended posture. The tribunal's contrast failures sit exactly on this failure mode.
- **WCAG 2.2 is the compliance bar.** APCA was removed from WCAG 3 drafts (2023) and continues as the independent ARC standard; WCAG 2.x ratios (4.5:1 text, 3:1 large/UI, 3:1 non-text component boundaries) remain the auditable target. Forge Noir's gate: body ≥ 7:1, all text ≥ 4.5:1, interactive borders ≥ 3:1 — verified by script (§7.5, §10).

## 4.4 The "cheap AI dark" anti-pattern list (what Forge Noir exists to escape)

Blue-cast `#0B-#12` canvases · maximum-chroma orange or violet accents · teal/mint sidekicks · dual-hue 135° gradients · neon box-shadow glows · glassmorphism-for-its-own-sake · pure-white text on pure-black (halation) · sub-AA gray meta text · unmodified framework palettes. **Nine markers; Night Forge exhibits six.** The redesign must leave every one behind.

## 4.5 Strategic implications

1. Differentiation must come from **temperature + discipline**, not from adding colors (the palette gets *smaller* in hue count, not larger).
2. Accessibility is not a compliance chore but **the cheapest credibility signal available to an engineer selling correctness** — and it must be enforced by script, permanently.
3. The palette must be **narrative-native**: the forge story already owns its vocabulary (obsidian, ash, ember, molten, night sky). The colors just have to actually speak it.
4. Every future color decision needs a **law, not a vibe** — ten usage laws (§7.6) replace judgment calls the token comments currently fake.

---
# 5. GOALS, NON-GOALS & SUCCESS METRICS

## 5.1 Goals

| # | Goal | Measure |
|---|---|---|
| G1 | Break the "AI-generated dark" cluster | All 9 anti-pattern markers (§4.4) absent; 5 winner patterns (§4.2) present |
| G2 | Zero accessibility failures | 29-pair contrast script passes with margin; 0 WCAG 2.2 AA/1.4.11 failures (§7.5) |
| G3 | 3-second attribution | Independent render reviewers describe the palette as "warm black + burnt ember" without prompting; ≥ 1 unprompted "feels authored/premium" per review |
| G4 | Re-audit score ≥ 7.5/10 | Same tribunal rubric, same pipeline (screenshots → blind render reviews → contrast math → panel) |
| G5 | System integrity | 100% token coverage (0 raw hex outside `tokens.css`); `svgs.py` reads the same values; contrast script wired into the deploy checklist |
| G6 | Zero platform cost | CSS delta ≤ 2 KB gzipped; no JS changes; LCP/CLS unchanged (±0.1 σ); runs identically on Oracle Always Free 2 OCPU/12 GB |

## 5.2 Non-goals

- No layout, typography-scale, spacing, or content changes (color-adjacent polish only, e.g., gradient-text → serif-accent swap).
- No light mode in v1 (tokens are shaped to permit it — §14 — but shipping it is out of scope).
- No new dependencies, no PostCSS/build step, no CSS-in-anything. The stack stays zero-build.
- No illustration redesign — re-inking only, through the unified palette source.
- No pursuit of "more colorful" — the hue count goes **down**.

## 5.3 Success metrics & verification protocol

| Metric | Baseline (`bffdb5f`) | Target | How verified |
|---|---|---|---|
| Tribunal color score | 6.03 | ≥ 7.5 | Re-run VT-CTA pipeline post-ship |
| Blind render review scores | 7.5 / 9.0 / 8.4 / 8.5 | ≥ 8.0 on all four pages | Same prompts, same model, post-ship captures |
| WCAG text pairs failing | 3 families (2.48 / 3.97 / 2.84) | **0** | `scripts/contrast_audit.py` (re-pointed at new tokens) in deploy checklist |
| WCAG 1.4.11 borders | 1.66:1 | ≥ 3.0:1 | Same script |
| Raw hex outside token source | 15+ | 0 | `rg '#[0-9a-fA-F]{3,8}' assets/css/ | grep -v tokens.css` returns 0 |
| Palette sources of truth | 2 (tokens.css + svgs.py) | 1 | `svgs.py` imports from a shared palette module |
| Accent hues in UI | 2 (ember + kite) | 1 (ember) + aurora confined to art | Code review + law L2 grep gate |
| CSS weight | 5 files / ~40 KB raw | +≤ 2 KB | `wc -c` before/after |
| LCP / CLS | current field values | unchanged | Local Lighthouse before/after |

---

# 6. DESIGN DIRECTION — THREE OPTIONS, ONE DECISION

The council evaluated three directions against the evidence. All three abandon the five cluster markers; they differ in risk, rebuild cost, and narrative fit.

## 6.1 Direction A — "Forge Noir" (recommended)

**The concept.** Keep the forge; light it properly. A warm smoked-iron obsidian canvas (the workshop at night), a bone-white ink ladder, a molten ember ramp as the single accent (the forge's working heat), and the aurora — the old mint, demoted and renamed — living only in the illustrated night sky above the forge. The cream paper islands stay as the "ledger" world where case studies are written, re-inked warm end-to-end.

- **What it kills:** all five cluster markers. The canvas is no longer blue-cast; the orange is no longer maximum-chroma; the mint no longer touches UI; the gradient is in-family; the glows are gone.
- **What it keeps:** every protection order in §3.5 — darkness, single accent, cream islands, tokens, grain, art, zero-dep stack.
- **Risk:** warm darks can read "brown" on badly calibrated displays. Mitigation: chroma ceiling 0.010 on neutrals (a whisper, not a wash), verified on a low-end LCD gate device (§10).
- **Cost:** token swap + component pass + art re-ink. 4–6 days.

## 6.2 Direction B — "First Light" (editorial off-white)

Flip the site light-first: the cream becomes the canvas, warm ink the text, ember the accent — the anti-dark move that dominated 2025–26 editorial trends and would stand out hardest in a dev-portfolio field of darks.

- **Kills:** everything, including the dark instinct the tribunal ordered protected.
- **Cost:** every dark-designed component (glass header, preloader, journey pin, cursor, menu overlay, SVG night art) must be redesigned, not re-toked. 3–4 weeks minimum, and the illustrated night-horizon narrative — the site's most differentiated asset — is orphaned.
- **Verdict: rejected.** Right idea, wrong site. File as the v3 candidate if Vishvu Tech ever rebrands editorial-first.

## 6.3 Direction C — "Signal Lime" (acid accent on cool dark)

The developer-tool signature: keep a cool dark canvas, swap the accent to acid lime (the Brittany Chiang → dev-tool lineage). Energetic, legible, on-trend.

- **Kills:** 3 of 5 markers (orange, mint, gradient) but **keeps the blue-cast canvas** and adds a hue that is itself becoming the new crowded lane; lime also fights the warm cream islands (cool-on-warm clash worse than today's).
- **Verdict: rejected.** Trades one crowd for a newer, smaller one, and breaks the paper world.

## 6.4 Decision matrix

| Criterion (weight) | A · Forge Noir | B · First Light | C · Signal Lime |
|---|---|---|---|
| Breaks AI-cluster (25%) | **10** | 10 | 6 |
| Preserves protected assets (20%) | **10** | 2 | 5 |
| Accessibility-by-construction (20%) | **9** | 8 | 8 |
| Narrative fit — "forge" (15%) | **10** | 3 | 4 |
| Build cost / risk (10%) | **9** | 3 | 6 |
| Market differentiation durability (10%) | **8** | 9 | 5 |
| **Weighted** | **9.45** | 6.05 | 5.95 |

**Decision: Direction A — Forge Noir.** It is the only option that scores ≥ 9 on every criterion the tribunal weighted heaviest, and it is the only one whose story was already written on the site — the palette just has to start telling it.

---

# 7. THE SPECIFICATION — FORGE NOIR COLOR SYSTEM

## 7.1 Brand narrative & vocabulary

| Family | Name | Meaning |
|---|---|---|
| Neutrals | **Obsidian & Ash** | The workshop at night — smoked iron, still warm from the day's work. One committed warmth: OKLCH hue 75°. |
| Text | **Bone & Ash** | What the forge writes with. Warm-tinted ladder, never pure white (halation) and never cool gray. |
| Accent | **Molten** | The working heat. One hue (35–48°), five perceptual grades, each with a job. |
| Atmosphere | **Aurora** | The cool light above the forge — night-sky illustrations only. The only cool color in the system, and it never touches UI. |
| Paper | **Ledger** | The cream world where work is documented. Warm cream, warm ink, text-grade ember. |
| Feedback | **Signal** | ok / warn / err — recalibrated to the warm canvas. |

## 7.2 Token architecture (three tiers)

```
TIER 1 · PRIMITIVES      oklch-specified ramps, hex fallbacks. Never referenced by components.
                          ash-*, ember-300…700, aurora, signal-*, ledger-*
TIER 2 · SEMANTIC        the only tokens components may use. Roles, not values.
                          --vf-canvas / surface-1 / surface-2 / line / line-strong / border-input
                          --vf-ink / ink-2 / ink-3 · --vf-ember (+ soft/dim) / ember-text-paper / ember-mark-paper
                          --vf-ok / warn / err · paper context flips the same names (existing .paper pattern)
TIER 3 · COMPONENT       scoped overrides where a component needs a decision (btn, card, form, footer watermark)
```

**Naming convention** (Nathan Curtis / VA taxonomy): `--vf-` namespace · category (`canvas/surface/line/border/ink/ember/…`) · role or scale suffix. The existing `--vf-` prefix and the `.paper` context-flip mechanism are preserved verbatim — **the migration is value-level, not name-level**, except the one deliberate rename: `--vf-kite` → `--vf-aurora`, which exists *because* every one of its 13 text usages must be visited and reassigned (law L2).

## 7.3 Tier 1 · Primitive ramps (OKLCH, with computed sRGB hex)

### Obsidian & Ash — neutrals (hue 75°, committed warmth)

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| `ash-950` | oklch(0.155 0.006 75) | `#0E0C09` | page canvas — warm obsidian |
| `ash-900` | oklch(0.190 0.007 75) | `#161310` | raised panels (surface-1) |
| `ash-850` | oklch(0.228 0.008 75) | `#1F1C18` | hover/active raised (surface-2) |
| `ash-800` | oklch(0.280 0.008 75) | `#2B2825` | hairlines (decorative) |
| `ash-700` | oklch(0.360 0.010 75) | `#403C37` | hairlines under interaction |
| `ash-600` | oklch(0.520 0.012 75) | `#6D6861` | **interactive borders — passes 1.4.11 (3.35:1 on surface-1)** |

### Bone & Ash — text ladder (warm-tinted)

| Token | OKLCH | Hex | On canvas / surface-1 |
|---|---|---|---|
| `ink` | oklch(0.930 0.006 85) | `#EAE8E3` | 15.95:1 / 15.11:1 — AAA |
| `ink-2` | oklch(0.745 0.011 80) | `#B0ACA5` | 8.64:1 / 8.19:1 — AAA |
| `ink-3` | oklch(0.630 0.013 80) | `#8D8881` | **5.55:1 / 5.26:1 — AA ✓ (was 4.25/3.97 ✗)** |

### Molten — the ember ramp (hue 35–48°, chroma peaks 0.17)

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| `ember-300` | oklch(0.820 0.120 48) | `#FFAC7E` | highlight tints, gradient top stop |
| `ember-400` | oklch(0.760 0.150 45) | `#FE8F5B` | hover state of the accent |
| `ember-500` | oklch(0.685 0.170 40) | `#EE6E3F` | **THE accent** — CTAs, focus, markers, metrics |
| `ember-600` | oklch(0.580 0.160 38) | `#C65029` | **marks-grade on paper** (rules, dots, stat units) — 3.85:1 on cream (non-text ✓) |
| `ember-700` | oklch(0.430 0.130 35) | `#882D16` | **text-grade on paper** (kickers, decision letters) — 7.24:1 on cream ✓ |

### Aurora — atmosphere (never UI)

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| `aurora` | oklch(0.800 0.090 170) | `#80D1B5` | night-sky illustrations, hero atmosphere only |

### Signal — feedback

| Token | OKLCH | Hex | On canvas |
|---|---|---|---|
| `signal-ok` | oklch(0.760 0.150 155) | `#52CD86` | 9.71:1 ✓ |
| `signal-warn` | oklch(0.800 0.140 85) | `#E7B643` | 10.39:1 ✓ |
| `signal-err` | oklch(0.650 0.190 25) | `#ED5350` | 5.54:1 ✓ (5.25:1 on surface-1) |

### Ledger — the paper world (warm cream, warm ink)

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| `ledger-50` | oklch(0.940 0.016 90) | `#EFEBDF` | paper canvas |
| `ledger-100` | oklch(0.910 0.019 88) | `#E6E1D3` | paper alt surface |
| `ledger-200` | oklch(0.865 0.016 88) | `#D7D2C7` | paper hairlines |
| `ledger-ink` | oklch(0.260 0.012 70) | `#28231E` | paper primary text — **warm ink (was cool `#1C2433`)** — 13.06:1 AAA |
| `ledger-ink-2` | oklch(0.470 0.016 70) | `#615951` | paper secondary — 5.77:1 ✓ |
| `ledger-surface` | — | `#F7F4EA` | raised paper cards (replaces raw `#FFFEFA`) |

**On-ember ink** (text placed on ember fills): oklch(0.140 0.010 60) = `#0C0806` — 6.59:1 on ember-500, 8.83:1 on ember-400 ✓.

---
## 7.4 Tier 2 · Semantic tokens — the complete `tokens.css` color block

*Drop-in replacement for the color section of `assets/css/tokens.css`. Every other section of the file (type, space, radii, motion, z-index) is unchanged. Fallback pattern: hex first, OKLCH override — old browsers keep the hex, modern browsers get the perceptual values (both verified identical in sRGB).*

```css
/* ============================================================
   VISHVU TECH — FORGE NOIR · COLOR TOKENS  (VT-PRD-002 §7.4)
   One source of truth. Ten laws govern use (§7.6).
   ============================================================ */
:root {
  /* ---- Canvas & surfaces · Obsidian & Ash (hue 75, one warmth) ---- */
  --vf-canvas:        #0E0C09;  --vf-canvas-ok:        oklch(0.155 0.006 75);
  --vf-surface-1:     #161310;  --vf-surface-1-ok:     oklch(0.190 0.007 75);
  --vf-surface-2:     #1F1C18;  --vf-surface-2-ok:     oklch(0.228 0.008 75);
  --vf-line:          #2B2825;  --vf-line-ok:          oklch(0.280 0.008 75);   /* decorative hairlines */
  --vf-line-strong:   #403C37;  --vf-line-strong-ok:   oklch(0.360 0.010 75);   /* interaction hairlines */
  --vf-border-input:  #6D6861;  --vf-border-input-ok:  oklch(0.520 0.012 75);   /* WCAG 1.4.11 · 3.35:1 */

  /* ---- Text · Bone & Ash ---- */
  --vf-ink:           #EAE8E3;  --vf-ink-ok:           oklch(0.930 0.006 85);   /* 15.9:1 AAA */
  --vf-ink-2:         #B0ACA5;  --vf-ink-2-ok:         oklch(0.745 0.011 80);   /* 8.6:1 AAA */
  --vf-ink-3:         #8D8881;  --vf-ink-3-ok:         oklch(0.630 0.013 80);   /* 5.55:1 AA — min meta grade */

  /* ---- Accent · Molten (the only interactive hue) ---- */
  --vf-ember:              #EE6E3F;  --vf-ember-ok:              oklch(0.685 0.170 40);
  --vf-ember-soft:         #FE8F5B;  --vf-ember-soft-ok:         oklch(0.760 0.150 45);   /* hover */
  --vf-ember-dim:          rgba(238,110,63,.14);                                        /* washes, focus rings */
  --vf-ember-text-paper:   #882D16;  --vf-ember-text-paper-ok:   oklch(0.430 0.130 35);   /* kicker text on cream · 7.24:1 */
  --vf-ember-mark-paper:   #C65029;  --vf-ember-mark-paper-ok:   oklch(0.580 0.160 38);   /* marks on cream · 3.85:1 non-text */
  --vf-on-ember:           #0C0806;  --vf-on-ember-ok:           oklch(0.140 0.010 60);   /* text on ember fills · 6.59:1 */

  /* ---- Atmosphere · Aurora — LAW L2: illustrations & hero sky ONLY ---- */
  --vf-aurora:        #80D1B5;  --vf-aurora-ok:        oklch(0.800 0.090 170);

  /* ---- Feedback · Signal ---- */
  --vf-ok:            #52CD86;  --vf-ok-ok:            oklch(0.760 0.150 155);
  --vf-warn:          #E7B643;  --vf-warn-ok:          oklch(0.800 0.140 85);
  --vf-err:           #ED5350;  --vf-err-ok:           oklch(0.650 0.190 25);

  /* ---- Paper · Ledger (case-study islands) ---- */
  --vf-paper:         #EFEBDF;  --vf-paper-ok:         oklch(0.940 0.016 90);
  --vf-paper-2:       #E6E1D3;  --vf-paper-2-ok:       oklch(0.910 0.019 88);
  --vf-paper-surface: #F7F4EA;                                                   /* raised paper cards */
  --vf-paper-ink:     #28231E;  --vf-paper-ink-ok:     oklch(0.260 0.012 70);    /* warm ink · 13.06:1 */
  --vf-paper-ink-2:   #615951;  --vf-paper-ink-2-ok:   oklch(0.470 0.016 70);    /* 5.77:1 */
  --vf-paper-line:    #D7D2C7;  --vf-paper-line-ok:    oklch(0.865 0.016 88);

  /* ---- Effects · light from within (glow budget: two pulse dots) ---- */
  --vf-gradient-ember: linear-gradient(90deg, #FE8F5B 0%, #C65029 100%);          /* progress hairline ONLY */
  --vf-halo-dot:       0 0 10px rgba(238,110,63,.45);                              /* pulse dots ONLY */
  --vf-inset-hi:       inset 0 1px 0 rgba(255,255,255,.05);                        /* the real "elevation" */
}

/* ---- Paper contexts flip tokens locally (existing mechanism, kept verbatim) ---- */
.paper {
  --vf-canvas:      var(--vf-paper);
  --vf-surface-1:   var(--vf-paper-surface);
  --vf-surface-2:   var(--vf-paper-2);
  --vf-line:        var(--vf-paper-line);
  --vf-line-strong: #C9C2B4;
  --vf-ink:         var(--vf-paper-ink);
  --vf-ink-2:       var(--vf-paper-ink-2);
  --vf-ink-3:       #756D64;                                     /* paper meta · 4.62:1 on cream */
  color: var(--vf-ink);
  background: var(--vf-paper);
}
/* Accent tokens do NOT flip: on paper, components must opt into
   --vf-ember-text-paper / --vf-ember-mark-paper explicitly (law L4). */
```

**Deleted tokens** (grep gates enforce their absence): `--vf-void`, `--vf-kite`, `--vf-kite-dim`, `--vf-gradient`, `--vf-gradient-soft`, `--vf-glow-ember`, `--vf-glow-kite`, `--vf-paper-ink` *as cool value*.

## 7.5 Compliance matrix — every critical pair, computed

*Full method: WCAG 2.x relative luminance; script `scripts/palette_forge.py` (OKLCH→sRGB + ratio) reproduces every number below.*

| Pair | Ratio | Requirement | Verdict |
|---|---|---|---|
| ink on canvas / surface-1 / surface-2 | 15.95 / 15.11 / 13.86 :1 | ≥ 7 (AAA target) | ✓ |
| ink-2 on canvas / surface-1 | 8.64 / 8.19 :1 | ≥ 4.5 | ✓ |
| **ink-3 on canvas / surface-1 / surface-2** | **5.55 / 5.26 / 4.83 :1** | ≥ 4.5 | ✓ — the fix (was 4.25/3.97/3.53 ✗) |
| ember-500 as text on canvas / surface-1 | 6.45 / 6.11 :1 | ≥ 4.5 | ✓ |
| on-ember on ember-500 (buttons, checked chips, selection, skip-link) | 6.59 :1 | ≥ 4.5 | ✓ — the fix (was 2.84 ✗) |
| on-ember on ember-400 (hover) | 8.83 :1 | ≥ 4.5 | ✓ |
| ok / warn / err on canvas | 9.71 / 10.39 / 5.54 :1 | ≥ 4.5 | ✓ |
| err on surface-1 | 5.25 :1 | ≥ 4.5 | ✓ |
| paper-ink on paper / paper-2 | 13.06 / 11.91 :1 | ≥ 7 | ✓ |
| paper-ink-2 on paper / paper-2 | 5.77 / 5.26 :1 | ≥ 4.5 | ✓ |
| paper ink-3 (`#756D64`) on paper | 4.62 :1 | ≥ 4.5 | ✓ |
| **ember-700 as text on paper / paper-2** | **7.24 / 6.61 :1** | ≥ 4.5 | ✓ — the fix (was 2.48 ✗) |
| ember-600 marks on paper | 3.85 :1 | ≥ 3 (non-text) | ✓ |
| aurora on canvas | 10.89 :1 | (atmosphere) | ✓ |
| **border-input on surface-1 / canvas** | **3.35 / 3.54 :1** | ≥ 3 (1.4.11) | ✓ — the fix (was 1.66 ✗) |
| line / line-strong hairlines | 1.33 / 1.79 :1 | decorative | documented exemption |

## 7.6 The Ten Laws of Forge Noir

*These are contracts, not suggestions. Laws L2, L4, L8 are machine-enforced by the pre-deploy grep gate (§10.2).*

| Law | Rule | Enforcement |
|---|---|---|
| **L1** | Ember owns interaction: CTAs, focus rings, hover borders, markers, key metrics. Nothing else leads the eye. | review |
| **L2** | The aurora never touches UI — no text, no borders, no fills, no buttons. Illustrations and hero sky only. | `rg 'var\(--vf-aurora\)' assets/css/` must return 0 hits |
| **L3** | Gradients stay in-family: ember-300→600 lightness ramps only. The dual-hue diagonal is retired forever. | `rg '7EE8C7|kite' assets/` returns 0 |
| **L4** | Ember-500 never lands on paper. Paper text gets ember-700; paper marks get ember-600. | contrast script paper section |
| **L5** | Glow budget: two 10px pulse-dot halos sitewide. Everything else lights from within (`--vf-inset-hi`) or by marks. | review |
| **L6** | Every text token clears 4.5:1 on every surface it appears on — verified by script, never by eye. | contrast script, CI gate |
| **L7** | One temperature: warm neutrals end-to-end; cool exists only as aurora atmosphere. | review |
| **L8** | No raw hex outside `tokens.css` and the shared palette module. A color written elsewhere is a bug. | `rg '#[0-9a-fA-F]{3,8}' assets/css/ -g '!tokens.css'` returns 0 |
| **L9** | Hierarchy is loudness order: ink > ink-2 > ink-3 > lines; the primary accent always out-measures the atmosphere. | review |
| **L10** | The cream stays: paper islands are the premium signature — re-inked, contrast-fixed, protected. | review |

## 7.7 Component application matrix

| Component | Token recipe (Forge Noir) | Notes |
|---|---|---|
| **Body / canvas** | `background: var(--vf-canvas); color: var(--vf-ink)` | warm obsidian replaces blue-cast void |
| **Header (scrolled)** | `rgba(14,12,9,.78)` blur → `.96` | re-derive the two raw rgba values from the new canvas |
| **Hero** | canvas + ONE ambient radial in ember-dim (bottom-left); headline ink; serif-accent word in ember-500 (replaces gradient-text); sky art keeps aurora | the "studio lighting" moment the render review praised, kept — now warm |
| **Buttons · primary** | bg ember-500, text on-ember, hover bg ember-400 (8.83:1), focus ring ember + ember-dim halo | one ramp-traveling hover (§7.9) |
| **Buttons · dark** | bg surface-2, border line-strong, hover surface-2→ash-600 border | replaces raw `#232C44` |
| **Case / journal cards** | bg surface-1, border line, inset-hi, hover: border→ember + bg surface-2 (unchanged grammar) | metrics in ember-500 |
| **Paper bands** | ledger-50 canvas, ledger-ink text, ledger-ink-2 secondary; kickers & decision letters in ember-700; stat units & rules in ember-600; raised cards ledger-surface | laws L4, L10 |
| **Forms** | field bg surface-1, border **border-input** (3.35:1), focus border ember + 3px ember-dim ring, error text/border signal-err, labels ink-2, meta ink-3 (now AA) | fixes 1.4.11 + label contrast |
| **Chips (checked)** | bg ember-500, text on-ember (6.59:1 — was raw `#0B0E14`) | ✓ |
| **Selection** | bg ember-500, color on-ember (6.59:1 — was white 2.84:1 ✗) | ✓ |
| **Skip-link** | bg ember-500, color on-ember, mono | ✓ |
| **Focus-visible** | 2px ember outline, 3px offset — universal, unchanged | protected asset |
| **Progress hairline** | `--vf-gradient-ember` (the ONE gradient) | in-family ramp |
| **Pulse dots** (hero eyebrow, availability chip) | bg ember-500 / signal-ok + `--vf-halo-dot` (10px) | the entire glow budget |
| **Footer watermark** | stroke ash-700 `#403C37` (was line-strong 1.66:1) — visible at last, still quiet | fixes "invisible ink" |
| **Cursor** | bone fill `#EAE8E3` on-ember label; no change to mechanics | raw #fff retired |
| **Menu overlay** | canvas at .96 alpha, links ink, hover ember, indices ink-3 | re-derive rgba from canvas |
| **Marquee / journey** | ink-3 chrome, ember markers, ember-dim progress track | unchanged grammar, new values |
| **404 glyph** | stroke ash-700; code outline; aurora kite glyph re-inked to ember-500 mark | the floating kite becomes a paper plane in ember? No — see §7.8 |
| **Prose / code** | inline code: surface-2 bg, **ember-500** text (6.11:1 on surface-1 — the aurora's old job, done by the accent) | law L2 cleanup |
| **OG images / favicon / manifest** | regenerated from the shared palette module; `theme-color` → `#0E0C09` | §7.8 |

## 7.8 Imagery, illustration & share assets

1. **Unify the palette source.** Extract the color constants from `v2-src/svgs.py` into `v2-src/palette.py` that reads/echoes the same OKLCH→hex values as `tokens.css` (single source of truth, law L8). The build regenerates: 5 case SVGs, hero fallback, favicon, and the 12 OG images with Forge Noir values.
2. **The night-horizon hero.** Sky gradients re-inked onto the warm obsidian ramp (`#0E0C09 → #1A1712 → #26221C`); the ember radial keeps its seat at the horizon (this is the forge's fire — narratively load-bearing); the aurora bands stay mint-green but at the new `#80D1B5` family — the sky keeps its cool light *because the ground got warm*. Stars: bone `#EAE8E3`. Ridgelines: ash-950/900.
3. **Case-study SVGs.** UI-chrome elements inside the mockups re-ink: old void→ash-950, surfaces→ash-900/850, lines→ash-800, ink→bone, mint UI accents→ember-500, mint atmosphere→aurora. The mockups should look like the forge's products, not the aurora's.
4. **Favicon & brand glyph.** The four-point star currently uses the retired dual-hue gradient. Re-ink: ember-500 fill on transparent (or a single ember-300→600 in-family ramp if a gradient is wanted at 16px legibility).
5. **OG images.** Same module; ember headline accents on warm obsidian; consistent with the shipped site.

## 7.9 Motion & interaction color (the craft layer)

- **Ramp-traveling hover (the one signature transition).** Primary button and card hovers interpolate *through* the ember ramp via `@property`-typed OKLCH custom properties (disabled under `prefers-reduced-motion` and on browsers without support — instant fallback):
  ```css
  @property --ember-l { syntax:'<number>'; inherits:false; initial-value:.685; }
  .btn--primary {
    background: oklch(var(--ember-l) .170 40);
    transition: --ember-l var(--t-fast) var(--ease-out);
  }
  .btn--primary:hover { --ember-l: .760; }   /* 500 → 400, through the ramp */
  ```
- **Focus-travel.** Focus rings keep the universal ember outline; ring offset breathes 3px→4px on focus-visible entry (`--t-instant`).
- **Gradient-text is retired** in favor of `.serif-accent` in ember-500 — type-led color per research pattern #5. Where a chromatic moment is wanted in the hero, a single `<em>` in Instrument Serif italic, ember-500, is the entire effect.
- **Pulse dots** keep their 2.6s breathe, now on `--vf-halo-dot`.
- **Reduced-motion:** every color transition collapses to instant per the existing global guard — no work needed beyond not breaking it.

---
# 8. MIGRATION PLAN

## 8.1 Token migration map (value-level; names preserved except one deliberate rename)

| Old (Night Forge) | Old value | New (Forge Noir) | New value | Notes |
|---|---|---|---|---|
| `--vf-void` | `#0B0E14` | `--vf-canvas` | `#0E0C09` | renamed to break old raw-rgba assumptions; grep all usages |
| `--vf-surface` | `#111623` | `--vf-surface-1` | `#161310` | |
| `--vf-surface-2` | `#1A2133` | `--vf-surface-2` | `#1F1C18` | |
| `--vf-line` | `#232B40` | `--vf-line` | `#2B2825` | |
| `--vf-line-strong` | `#2E3852` | `--vf-line-strong` | `#403C37` | inputs stop using this (see below) |
| — | — | `--vf-border-input` | `#6D6861` | **new** — WCAG 1.4.11 |
| `--vf-ink` | `#F2F5FA` | `--vf-ink` | `#EAE8E3` | bone white |
| `--vf-ink-2` | `#A8B3C7` | `--vf-ink-2` | `#B0ACA5` | |
| `--vf-ink-3` | `#6B7690` | `--vf-ink-3` | `#8D8881` | **the AA fix** (4.25→5.55) |
| `--vf-ember` | `#FF6B35` | `--vf-ember` | `#EE6E3F` | molten, not traffic-cone |
| `--vf-ember-soft` | `#FF8C5E` | `--vf-ember-soft` | `#FE8F5B` | |
| `--vf-ember-dim` | `rgba(255,107,53,.14)` | `--vf-ember-dim` | `rgba(238,110,63,.14)` | |
| — | — | `--vf-ember-text-paper` | `#882D16` | **new** — law L4 |
| — | — | `--vf-ember-mark-paper` | `#C65029` | **new** — law L4 |
| — | — | `--vf-on-ember` | `#0C0806` | **new** — replaces raw `#0B0E14`/`#fff` on fills |
| `--vf-kite` / `--vf-kite-dim` | `#7EE8C7` | `--vf-aurora` | `#80D1B5` | **renamed + confined** — all 13 text usages reassigned (§8.3) |
| `--vf-paper` | `#F5EFE4` | `--vf-paper` | `#EFEBDF` | |
| `--vf-paper-2` | `#EDE5D6` | `--vf-paper-2` | `#E6E1D3` | |
| raw `#FFFEFA` | — | `--vf-paper-surface` | `#F7F4EA` | leak fixed |
| `--vf-paper-ink` | `#1C2433` (cool) | `--vf-paper-ink` | `#28231E` (warm) | the temperature fix |
| `--vf-paper-ink-2` | `#4A5568` | `--vf-paper-ink-2` | `#615951` | |
| raw `#37415A` | — | `var(--vf-paper-ink-2)` | — | leak fixed |
| `--vf-paper-line` | `#D9CFBD` | `--vf-paper-line` | `#D7D2C7` | |
| `--vf-ok` / `--vf-warn` / `--vf-err` | `#3DD68C/#FFC24B/#FF5C5C` | same | `#52CD86/#E7B643/#ED5350` | recalibrated |
| `--vf-gradient` | 135° ember→kite | *(deleted)* | — | replaced by `--vf-gradient-ember` (in-family, progress hairline only) |
| `--vf-gradient-soft` | dual-hue soft | *(deleted)* | `--vf-ember-dim` washes | |
| `--vf-glow-ember` | 24px | *(deleted)* | — | law L5 |
| `--vf-glow-kite` | 32px | *(deleted)* | — | law L5 |
| — | — | `--vf-halo-dot` | 10px ember halo | the entire glow budget |
| `--vf-inset-hi` | white 6% inset | `--vf-inset-hi` | white 5% inset | kept — the real elevation |
| raw `#232C44` (btn-dark hover) | — | `var(--vf-surface-2)` + border | — | leak fixed |
| raw `rgba(11,14,20,.78/.96)` (header) | — | `rgba(14,12,9,.78/.96)` | — | re-derived from canvas |
| raw `rgba(17,22,35,.55)`, `rgba(28,36,51,.86)` | — | re-derived from surface ramp | — | menu/overlay scrims |
| raw `#fff`, `#000`, `#6E7890`, `#0B0E14` | — | nearest tokens | — | all leaks fixed |

## 8.2 File-by-file change list

| File | Changes |
|---|---|
| `assets/css/tokens.css` | §7.4 block swap; `.paper` context update; delete retired tokens |
| `assets/css/base.css` | selection pairing (on-ember), skip-link colors, placeholder→ink-3 |
| `assets/css/components.css` | header rgba re-derivation; btn dark hover token; glow deletions → inset-hi + marks; progress hairline gradient; watermark stroke ash-700; cursor bone fill; prose code ember; **all 6 kite-as-text usages → ink-3 or ember per §8.3** |
| `assets/css/pages.css` | paper-band accents → ember-700/600 per law L4; the 7 kite usages; `#37415A`/`#FFFEFA` leaks; form borders → border-input |
| `v2-src/svgs.py` → `v2-src/palette.py` | extract shared palette module; re-ink generation (§7.8) |
| `v2-src/build.py` | regenerate all pages/SVGs/OG assets |
| `index.html` + all pages | `theme-color` → `#0E0C09` (via build partial `head.tpl`) |
| `manifest.json` | `theme_color`/`background_color` → Forge Noir values |
| `assets/img/favicon.svg`, `icon-*.png`, `apple-touch-icon.png` | regenerate from palette module |
| `scripts/contrast_audit.py` | commit to repo; re-point at Forge Noir pairs (§10.2) |

## 8.3 The 13 kite-as-text reassignments

| Usage (file) | Was | Becomes | Why |
|---|---|---|---|
| `.page-hero .mono-label` (pages) | kite | **ink-3** | labels are wayfinding, not atmosphere — and now AA |
| `.next-action .mono-label` (pages) | kite | **ink-3** | same |
| `.case-band--dark .kicker` (pages) | kite | **ember-500** | dark-band kickers match paper-band kicker *role* → accent |
| `.journal-card__meta .tag` (pages) | kite | **ink-3** | metadata de-emphasized; ember stays for CTAs |
| `.prose code` (pages) | kite | **ember-500** | code accents belong to the accent, 6.11:1 ✓ |
| `.expectations h3` (pages) | kite | **ink-2** | heading, not signal |
| `.form-success .ref` (pages) | kite | **ember-500** | success emphasis pairs with signal-ok glyph |
| 6 further component usages | kite | ink-3 / ember per role | same rule |

## 8.4 Phased rollout

**Phase 0 · Pipeline unification (0.5 day)** — extract `palette.py`; wire `svgs.py` + `build.py` to it; commit `contrast_audit.py`; add the grep gates as a `scripts/check-colors.sh` pre-deploy script. *Gate: site output byte-identical after refactor (only provenance changed).*

**Phase 1 · Compliance hotfix on the CURRENT palette (0.5 day, ships immediately)** — fix D2/D3/D12 with in-hue darkened values of the *old* hues (ember→`#B34A22`-class text-grade on paper; ink-3→`#7A859B`; selection/skip-link→void-on-ember; input borders→1.4.11-compliant cool gray). *Rationale: the business pages stop failing AA today, one full phase before the redesign lands. Gate: contrast script green on old palette.*

**Phase 2 · Forge Noir token swap + component pass (2–3 days)** — §7.4 block, §8.1 map, §8.3 reassignments, effects and motion layer (§7.9). Local capture set (same 7 pages, same viewports) for before/after diff. *Gates: contrast script green; grep gates green; VLM render review ≥ 8.0 on home/case/mobile; visual diff reviewed page-by-page.*

**Phase 3 · Art regeneration & assets (1–1.5 days)** — re-ink SVGs, favicon, icons, OG set, manifest, theme-color; optional `@media (color-gamut: p3)` ember enhancement (§14). *Gates: OG previews render correctly on all 12 share targets; favicon legible at 16px; Lighthouse performance delta = 0.*

**Rollback:** static-file revert per phase (git tag before each); no data, no state, no cache-bust beyond CSS filenames.

---

# 9. ACCESSIBILITY ACCEPTANCE CRITERIA

1. **WCAG 2.2 AA, zero exceptions** — the §7.5 matrix green: every text pairing ≥ 4.5:1, large text ≥ 3:1, non-text component boundaries ≥ 3:1 (border-input), focus indicators ≥ 3:1 against adjacent colors (ember-500 on canvas = 6.45:1 ✓).
2. **Body text AAA** (≥ 7:1) on all primary reading surfaces — ink ladder is 15.9/8.6 on dark, 13.1/5.8 on paper.
3. **No color-only meaning** — errors pair text+icon+border; checked chips add weight + fill; availability pairs dot+text. (Carried over from current site — verify no regression.)
4. **Focus visibility preserved universally** — 2px ember outline, 3–4px offset, `:focus-visible` only.
5. **Reduced-motion guard intact** — the `@property` hover and pulse animations must sit behind the existing `prefers-reduced-motion` / `save-motion` curtains.
6. **Documentation honesty (new rule):** every token comment states its *measured* ratio and minimum size, generated from — not written before — the script. `--fs-mono-label` raised to `.875rem` (14px) to match the documented minimum.
7. **CVD spot-check** — deuteranopia/protanopia simulation on home + one case page: no information loss via color (kickers in ember-700 retain 7.24:1 luminance contrast, which is CVD-stable).

# 10. QA & VALIDATION PLAN

## 10.1 The re-audit protocol (the tribunal re-convenes)

Post-Phase-3, run the *identical* VT-CTA-002 pipeline: 7 captures → 4 blind render reviews (same prompts) → contrast computation → grep gates → a 100-judge re-score on the same rubric. **Ship criterion: ≥ 7.5/10 and zero FAIL rows.**

## 10.2 Automated gates (committed to the repo, run before every deploy)

```bash
# scripts/check-colors.sh — fails the deploy on any violation
python3 scripts/contrast_audit.py --pairs forge-noir   # exit 1 on any FAIL
rg -c 'var\(--vf-aurora\)' assets/css/ && exit 1       # law L2
rg -ci 'kite|7EE8C7' assets/ && exit 1                  # law L3 (no mint anywhere)
rg '#[0-9a-fA-F]{3,8}' assets/css/ -g '!tokens.css' && exit 1   # law L8
echo "FORGE NOIR: all color gates green"
```

## 10.3 Visual regression

Before/after capture set (same URLs, viewports, forced-reveal state as this audit: `scripts/capture.sh`); page-by-page diff review; particular attention: hero lighting, paper band kickers, form focus states, footer watermark visibility, mobile meta text in simulated daylight (screenshot brightness sweep).

## 10.4 Device matrix

Low-end LCD (the warm-dark "reads brown?" gate), OLED phone (pure-black habituation), calibrated P3 display (enhancement check), projector (contrast stress), and a 200-nits office monitor (the median client).

---

# 11. PERFORMANCE & ORACLE FREE TIER

- **Cost of the entire upgrade: ~2 KB of CSS, zero JS, zero runtime.** Token swaps and component edits add negligible weight; the `@property` hover is 6 lines; the P3 enhancement is a media query.
- **Oracle Always Free, October 2026:** the envelope is now **2 OCPU / 12 GB RAM** Ampere A1 (halved mid-2026) + 2 AMD micros + 200 GB block storage + 10 TB/month egress. The static+nginx architecture uses a rounding error of that; the color system changes nothing about the deployment story. Keep: long-cache CSS/SVG (`immutable` + content-hash query), HTML no-cache, Brotli.
- **Paint behavior:** color changes never trigger layout; `theme-color` and canvas swap in the same paint. No CLS/LCP movement expected — verify with Lighthouse before/after (gate: ±0).
- **P3 enhancement (optional, Phase 3):** `@media (color-gamut: p3) { :root { --vf-ember: oklch(0.685 0.21 40); } }` — a free vividness boost on capable displays, zero bytes on the rest, no fallback needed (progressive).
- **Fonts:** unchanged. But note — bone-white text on warm obsidian with Clash Display is the palette's best friend; the pairing is already loaded.

---

# 12. RISKS & MITIGATIONS

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Warm canvas reads "brown/muddy" on uncalibrated displays | Medium | High | Chroma ceiling 0.010 (whisper); §10.4 low-end LCD gate; if it fails, drop neutrals to chroma 0.004 — temperature survives, tint softens |
| R2 | Ember-700 misused on dark surfaces (would fail contrast) | Medium | Medium | Law L4 + contrast script covers the pair; naming (`-text-paper`) self-documents |
| R3 | Aurora creeps back into UI during future edits | Medium | Medium | Law L2 grep gate in `check-colors.sh` — permanent |
| R4 | Brand discontinuity (old orange gone from muscle memory) | Low | Low | Ember stays ember — same hue family, retuned; favicon/OG regenerate in Phase 3 so share cards never mismatch |
| R5 | Paper-band accents feel "darker than expected" editorially | Low | Medium | ember-700 is a feature (rust-ink editorial look); if judged heavy, kicker weight/size bump is the sanctioned adjustment — never the color |
| R6 | Phase 1 hotfix values leak into Phase 2 | Low | Low | Phase 2's token swap overwrites by construction; grep gate catches strays |
| R7 | Regression in reduced-motion behavior from @property hover | Low | High | Feature-detect + existing global guard; test in the §10.3 pass |

---

# 13. FUTURE EXTENSIONS (OUT OF SCOPE, SHAPED FOR)

1. **Light mode ("Daylight Ledger")** — the `.paper` mechanism proves scoped re-theming; Tier-2 semantic tokens are mode-shaped. A `prefers-color-scheme: light` block can flip canvas→ledger and re-derive surfaces in OKLCH geometrically (one lightness step).
2. **Seasonal ember** — the accent is one OKLCH hue; a festive shift (e.g., deeper red for a launch week) is a one-variable change behind a body class.
3. **Wide-gamut system** — full P3 ramp declarations once browser share justifies dual-token maintenance.
4. **Client-facing mini brand book** — the ten laws + palette preview already are one; export as a PDF page for the "UI design" service proof.

---

# 14. APPENDICES

## Appendix A · Token quick-reference card

```
CANVAS   #0E0C09      SURFACES  #161310 / #1F1C18      LINES  #2B2825 / #403C37
INPUT-BR #6D6861      INKS      #EAE8E3 / #B0ACA5 / #8D8881
EMBER    #EE6E3F  (soft #FE8F5B · dim rgba(238,110,63,.14))
ON-EMBER #0C0806      PAPER-ACC #882D16 text / #C65029 marks
AURORA   #80D1B5  (art only)   SIGNAL #52CD86 / #E7B643 / #ED5350
LEDGER   #EFEBDF / #E6E1D3 / #F7F4EA · ink #28231E / #615951 · line #D7D2C7
GRADIENT (1 only)  #FE8F5B → #C65029 · halo (2 only) 10px ember
```

## Appendix B · Research sources

1. Evil Martians — *OKLCH in CSS: why we moved from RGB and HSL* — evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl
2. Carmen Ansio — *oklch and the modern CSS color stack* (Feb 2026) — carmenansio.com/articles/oklch-and-the-modern-color-stack
3. Radix Themes — *Color* (12-step scales, dark pairings, text-grade steps) — radix-ui.com/themes/docs/theme/color
4. Material Design — *Dark theme* (elevation via surface lightness) — m2.material.io/design/color/dark-theme.html · m3.material.io/styles/color/system/overview
5. Nielsen Norman Group — *Dark Mode: How Users Think About It and Issues to Avoid* (2023) · *Dark Mode vs. Light Mode* (2020) · *Low-Contrast Text Is Not the Answer* (2015) — nngroup.com
6. web.dev — *Color and contrast accessibility* — web.dev/articles/color-and-contrast-accessibility
7. VA Design System — *Design tokens* (primitive → semantic → component taxonomy, after Nathan Curtis) — design.va.gov/foundation/design-tokens · medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676
8. APCA / WCAG 3 status — contrast.tools (APCA lookup + 2023 draft reversion) · w3c low-vision-a11y-tf discussion #131
9. Awwwards — Sites of the Day roster (Oct 2026: A24, FORMAT/Obys, ESR Bespoke, G. Colombel, Forge Automotive, Nick Ho, Odyssée…) — awwwards.com/websites/sites_of_the_day
10. Webportfolios.dev — *Best Color Palettes for Developer Portfolios (2025)* (Brittany Chiang `#11172a/#599692` et al.) — webportfolios.dev/blog/best-color-palettes-for-developer-portfolio
11. MUO/Muzli — *Mastering Elevation for Dark UI* (2024) — medium.muz.li/mastering-elevation-for-dark-ui-a-comprehensive-guide-04cc770dd0d6
12. Oracle — *OCI Free Tier / Always Free resources* — docs.oracle.com/iaas/Content/FreeTier/freetier.htm · InfoQ — *Oracle quietly halves free tier Ampere A1 compute* (Jul 2026) — infoq.com/news/2026/07/oracle-cloud-free-tier-limits
13. r/videography — the orange-and-teal color-grade trope (the cliché's cinema lineage)

## Appendix C · Companion artifacts

- `VishvuTech_100-Judge_Color_Audit.md` — the full tribunal record (evidence, verdicts, twelve defects, keep-list)
- `VishvuTech_Palette_Preview.png` — the visual spec companion (before/after swatches, hero re-lit, the ten laws)
- `current-site-screenshots/` — the seven baseline captures this audit and the re-audit protocol reference
- `scripts/contrast_audit.py`, `scripts/palette_forge.py`, `scripts/capture.sh` — the verification toolchain (commit to repo per Phase 0)

## Appendix D · Document control

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-10-29 | 100-Judge Research Council (distilled) | Initial specification — responds to VT-CTA-002 evidence; supersedes the color sections of VT-PRD-001 |

**Approval to proceed:** the tribunal's protection orders (§3.5) are binding constraints on implementation. Any deviation from the Ten Laws (§7.6) requires re-running the compliance matrix before deploy.
