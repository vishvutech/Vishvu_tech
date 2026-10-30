# VT-PRD-005 · STRATA — The Layered Light System
## Vishvu Tech · Premium colour-layering architecture on the First Light world

**Version:** 5.0 · October 2026
**Status:** Authoritative implementation spec — supersedes VT-PRD-004 §6 (Porcelain Dawn palette) as the *colour architecture*; inherits and preserves every standing constraint of VT-PRD-004.
**Commissioned by:** The 100-Judge Tribunal, Round 2 (`Vishvu_100_Judge_Critique_R2_Strata.md`, unanimous directive 100/100)
**Owner's mandate, verbatim:** *"background completely layer one a colour on the layer one now again layer two a different colour which would be best on layer one colour now layer 3 on the layer 1 + layer 2 so it become the premium i gave the intution it may have more layers also"*
**Engineering source of truth:** `v2-src/palette.py` (primitives) → mirrored to `assets/css/tokens.css` → consumed by `components.css` / `pages.css` / `svgs.py`. Law L9 (no raw colour anywhere else) survives unchanged.

---

## 0 · WHAT THIS PRD IS

First Light (VT-PRD-004) built a flawless light world and banished black, brown and every dark shade. It then shipped that world as **one colour**: 97% of rendered pixels sit in a single warm-ivory hue family (88–95°), the "atmosphere washes" measure 1–2% below the canvas in lightness (sub-perceptual), and the homepage's vertical colour profile holds hue 42–53° from hero to footer. The owner's verdict — *"ok but not award winning… only one colour… no colour combinations"* — is confirmed by measurement.

STRATA is the corrective architecture. It does **not** repaint the site; it decomposes the existing dawn world into **six formal layers**, assigns each layer a colour *chosen against the composite of every layer beneath it* (the owner's instinct, stated as engineering law), and runs those layers as a **band rhythm** — visible colour chapters through every page.

**Non-negotiables carried forward from every prior mandate:**
- N1 · Zero black. Zero brown. Zero dark shades. Anywhere — including backgrounds, shadows, overlays, art. (Unbroken since Round 1; re-verified by audit.)
- N2 · The result must read premium/elite — measured, not asserted.
- N3 · Oracle Cloud Free Tier deployment: static, cheap, fast (no new runtime cost).
- N4 · All typography discipline, motion system, content and structure from the current build remain.

---

## 1 · MISSION & SUCCESS CRITERIA

**Mission:** convert a monochrome light site into a layered light site — many colours behaving as one world — without a single dark pixel and without breaking a single existing WCAG pair.

**Success criteria (all measurable, all gated in QA):**

| # | Criterion | Gate |
|---|---|---|
| S1 | Visible layer separation | band-vs-ground ≥3% relative-luminance delta **or** ≥25° hue step; plane-vs-band ≥10%; well-vs-band ≥6% |
| S2 | Scroll has colour chapters | Homepage vertical profile spans ≥4 distinct hue families; no two adjacent acts share a ground |
| S3 | Light-world law holds | Every fill ≥ OKLCH L 0.89; dark-pixel share (<60/255 luminance) ≤ 2% per page (type + marks only) |
| S4 | Accessibility holds | Full ink×surface matrix: INK ≥7:1 everywhere (AAA), INK2/INK3/PEACOCK-600/CORAL ≥4.5:1 on legal surfaces, non-text UI ≥3:1 |
| S5 | Token discipline holds | Raw hex appears only in `palette.py` + `tokens.css`; band audit asserts every act's computed background differs from neighbours |
| S6 | Performance unchanged | No new JS on the critical path; CSS delta < 6KB raw; LCP/CWV budgets intact |
| S7 | Premium verdict | Blind visual review describes the site in colour *sequences* (≥3 colour words), not one |

---

## 2 · RESEARCH BASE (THE 100-JUDGE RESEARCH BOARD)

The tribunal's research panel — the same hundred judges — reviewed how layered colour is practised by the systems and industries that set the standard. Findings that shaped STRATA:

### 2.1 · Layered colour roles — Material Design 3
Google's colour system builds every screen from **paired, stacked roles**: surface → container → on-container, with primary/secondary/tertiary emphasis tiers. Its core rule: colours must be applied *"in the intended pairs or layering orders"* — improper stacking breaks both visual results and accessibility ([m3.material.io/styles/color/roles](https://m3.material.io/styles/color/roles)).
**Adopted:** the legal-surface law (§4, Law S7) — every token declares which layers it may sit on; the contrast matrix is computed only over legal composites, and those pairs are published.

### 2.2 · Elevation as stacked surface *colours* — Atlassian Design System
Atlassian defines UI as four stacked elevations — sunken, default, raised, overlay — where *"elevations are layered surfaces that form the foundation of the UI"* and each level is a **different surface colour**, not merely a shadow; sunken wells appear only on the default level ([atlassian.design/foundations/elevation](https://atlassian.design/foundations/elevation)).
**Adopted:** the four functional depth levels (ground → stratum → plane → well) map directly to sunken/default/raised/sunken-in-raised; wells are legal only inside their host stratum or plane.

### 2.3 · Semantic background layering — Atmos.style
The working light-mode pattern is a three-deep background stack — `bg.default`, `bg.subtle`, `bg.surface` — with accessibility *"built into the palette, not checked after"* and WCAG thresholds (4.5:1 text, 3:1 UI) engineered per layer ([atmos.style/blog/how-to-build-a-color-system-for-ui-design](https://atmos.style/blog/how-to-build-a-color-system-for-ui-design)).
**Adopted:** ground/stratum/plane as three distinct semantic backgrounds; every new pair is verified before shipping, not after (§6).

### 2.4 · Scroll-driven band transitions — premium-site practice
Section backgrounds that change colour as the visitor scroll — start/mid/end colour stops along the scroll sequence — are now a first-class feature of premium site builders (e.g. YOOtheme's scroll-driven background-colour animations) and a recurring device in Awwwards light-theme winners.
**Adopted:** the band rhythm (§7) ships as static per-act grounds (zero-JS, reduced-motion safe); the optional future enhancement (cross-fading grounds) is specified but off by default.

### 2.5 · Layered light precedents — the art record
Turner's five-glaze skies; Kangxi porcelain displayed on celadon stands; Scandinavian "one snow field, ten blues of shadow"; gallery walls painted per exhibition; couture tone-on-tone built from *visibly* distinct creams. The unanimous art-direction finding: **light reads as premium through layered company, never through solitary perfection.** The dawn metaphor itself — zenith blue, blush band, gold horizon — is a natural strata system.
**Adopted:** the strata hues are drawn from one coherent "dawn family" (§5) so many colours still behave as one world.

### 2.6 · What the research forbids
- Colour layering by hue alone (fails colour-vision deficiency) → every band separation carries lightness as well as hue (Judge 64).
- Pastel washes below perceptual thresholds → the visibility law (§4, Law S4) with numeric floors.
- One accent meaning everything → peacock remains the *only interactive* hue; bands carry place, peacock carries action (Judge 09).

---

## 3 · THE LAYER THEORY — THE STACK

The owner's intuition, formalised. Every composition on the site is a **stack**; each layer's colour is selected to be optimal *on the composite of all layers below it* — not in isolation.

```
L6  INK        the peacock typographic ladder          (sits on: everything below)
L5  MARKS      peacock + rationed reserves, hairlines   (sits on: planes, wells, strata)
L4  WELL      sunken insets, tinted by host hue         (sits in: strata, planes)
L3  PLANE     milk cards — the raised paper             (sits on: any stratum)
L2  STRATUM   visible tinted section bands              (sits on: the ground)
L1  GROUND    porcelain — the page floor                (sits on: nothing)
```

**Composite law, worked example (the owner's three layers):**
- *Layer 1* — GROUND `#F7F4EC` (warm porcelain, OKLCH 0.967/0.011/90°).
- *Layer 2* — a STRATUM **best on** porcelain: sage `#E7F5E7`. Selected because: lightness −2.7% (perceptible band, still premium-quiet), hue +55° (clear colour change, same dawn family), chroma ×2.4 (visible tint, not grey).
- *Layer 3* — a PLANE **best on ground+stratum composite**: milk `#FDFCF8`. Selected because: +10.5% luminance over sage (unmissable lift), near-neutral hue (paper on any coloured ground), 1px host-tinted hairline to stitch the composite.
- *Layer 4* — a WELL **best inside the stratum**: sage-well `#DCEEDC`. Selected because: −7.4% inside the sage field (reads sunken, not dirty), hue identical to host (belongs to the band), chroma slightly raised (depth carries colour information).
- *Layer 5* — MARKS **on the plane**: peacock (action) + host-band line. *Layer 6* — INK `#123F3B`, 10.3:1 on sage.

The stack repeats this pattern per band hue. **Six layers — "it may have more layers also": yes, six, and each is individually specified, measured, and audited.**

---

## 4 · THE SELECTION LAWS (S1–S8)

The laws every layer colour must satisfy. These supersede VT-PRD-004's Laws L0/L1/L4 for backgrounds while preserving all others.

**Law S1 · THE LIGHT-WORLD LAW (inviolable).** Every fill, ground, band, well, overlay and art colour ≥ OKLCH L 0.89. Zero black, zero brown, zero dark shades — including shadows (ink-tinted alphas only, ≤14% opacity), cursors, code blocks, menus. *Inherited verbatim from Round 1; audited by `banlist_scan.py`.*

**Law S2 · THE HUE-KINSHIP LAW.** All strata belong to the dawn family — hues 15°–250° at OKLCH L 0.955–0.960, chroma 0.024–0.036. No stratum may introduce a hue outside the family; the family is what makes many colours read as one world.

**Law S3 · THE COMPOSITE LAW.** A layer's colour is chosen against **every layer beneath it** in its actual composition: plane on stratum on ground; well inside stratum; mark on plane on stratum. Isolated swatch approval is prohibited; QA renders the full composite.

**Law S4 · THE VISIBILITY LAW.** Perceptible steps, numerically gated:
- stratum vs ground: ≥3% relative-luminance delta **or** ≥25° hue step (both, wherever possible);
- plane vs stratum: ≥10% luminance delta;
- well vs host: 6–9% delta (sunken, never muddy);
- line vs host: 5–8% delta.
Sub-perceptual washes (the Round-2 finding) are banned from band duty.

**Law S5 · THE CHROMA-ESCALATION LAW.** Chroma rises gently with depth: ground 0.011 → stratum 0.024–0.036 → well 0.030–0.042 → line 0.030–0.040. Depth must carry colour information (Judge 45); flat chroma across depths is the "greyscale with perfume" failure.

**Law S6 · THE BAND-RHYTHM LAW.** No two adjacent acts share a ground. Homepage order: dawn-gradient hero → porcelain proof → sage craft → powder maker → blush beginning (+ gold horizon seal). Inner pages inherit their theme ground (§7). Bands alternate warm/cool so no two neighbours are adjacent on the hue wheel.

**Law S7 · THE LEGAL-SURFACE LAW.** Every token declares legal hosts; contrast is verified only over legal composites (mirroring Material's pairing rule):
- INK ladder: any layer. · PEACOCK-500: fills/icons on strata/planes; text uses PEACOCK-600.
- SIGNAL_OK/WARN/ERR: strata and planes only (never wells — their text context).
- SAFFRON/SKY: decorative marks, charts, atmosphere only — never text (unchanged).
- CORAL: one italic word per page, on strata/planes (unchanged).

**Law S8 · THE RESTRAINT LAW.** Strata are the *only* new visible hues. No new accent hues, no gradients on components (hero sky art excepted), no band-on-band nesting beyond the six layers. The variety budget is spent on large quiet surfaces, not loud details — that is what reads premium.

---

## 5 · THE PALETTE (COMPUTED & VERIFIED)

Generated by `scripts/strata_palette.py` (OKLCH primitives → sRGB hex; WCAG ratios recomputed from the hex). These values are canonical; `palette.py` mirrors them.

### 5.1 · L1 — GROUND

| Token | Hex | OKLCH | Role |
|---|---|---|---|
| `--vt-canvas` (porcelain) | `#F7F4EC` | 0.967 0.011 90 | page floor, work act ground |

### 5.2 · L2 — STRATA (the bands; hue kin: 15°–250°)

| Token | Hex | OKLCH | ΔL vs ground | Hosts |
|---|---|---|---|---|
| `--vt-stratum-dawn` (dawn-blush) | `#FFEBE6` | 0.958 0.026 35 | −4.1% rel-lum | hero mid-sky · contact |
| `--vt-stratum-gold` (dawn-gold) | `#FDECCF` | 0.950 0.042 82 | −5.7% | journal · horizon glow |
| `--vt-stratum-sage` | `#E7F5E7` | 0.956 0.024 145 | −2.7% | services act/page |
| `--vt-stratum-powder` | `#E3F3FF` | 0.956 0.026 248 | −3.2% | about act/page · journey |
| `--vt-stratum-blush` | `#FFE9EA` | 0.957 0.030 15 | −5.6% | contact act · 404 |
| `--vt-stratum-gold-deep` | `#FEEFD7` | 0.958 0.036 80 | −3.1% | essays pull-quotes |

### 5.3 · L3 — PLANE (raised paper; universal)

| Token | Hex | OKLCH | Δ vs strata |
|---|---|---|---|
| `--vt-surface-1` (milk) | `#FDFCF8` | 0.991 0.005 95 | **+10.5% … +13.8%** on all strata |

### 5.4 · L4 — WELLS (sunken insets, tinted by host — Law S5)

| Token | Hex | OKLCH | Δ inside host |
|---|---|---|---|
| `--vt-well-porcelain` (bone) | `#F0EBDF` | 0.941 0.017 88 | −6.6% in porcelain |
| `--vt-well-sage` | `#DCEEDC` | 0.930 0.030 145 | −7.4% in sage |
| `--vt-well-powder` | `#D8EAFD` | 0.930 0.032 248 | −8.1% in powder |
| `--vt-well-blush` | `#FCE1E0` | 0.931 0.030 20 | −6.5% in blush |
| `--vt-well-gold` | `#F7E6CA` | 0.932 0.042 82 | −8.1% in gold |
| `--vt-well-milk` (in-card) | `#E6E0D2` | — | −23% in milk (existing) |

### 5.5 · L5 — LINES & MARKS

| Token | Hex | OKLCH | Use |
|---|---|---|---|
| `--vt-line-sage` | `#D1E2D0` | 0.895 0.030 145 | hairlines in sage bands |
| `--vt-line-powder` | `#CCDFF1` | 0.895 0.032 248 | hairlines in powder bands |
| `--vt-line-blush` | `#F0D6D3` | 0.896 0.030 24 | hairlines in blush bands |
| `--vt-line-gold` | `#EADBC0` | 0.897 0.040 84 | hairlines in gold bands |
| `--vt-line` (porcelain) | `#E2DBC8` | 0.892 0.027 90 | default hairlines |
| `--vt-line-strong` | `#CFC6AE` | 0.827 0.034 90 | structural (unchanged) |

**Marks (unchanged from First Light):** `--vt-accent` `#0F766E` · `--vt-accent-deep` `#0B5D57` · `--vt-coral` `#A83F28` · `--vt-saffron` `#E9A23B` · `--vt-sky` `#9DB8D9`. No new accent hues (Law S8).

### 5.6 · L6 — INK (one half-grade adjustment)

| Token | Hex | Change | Reason |
|---|---|---|---|
| `--vt-ink` | `#123F3B` | unchanged | 8.9–11.4:1 everywhere |
| `--vt-ink-2` | `#3E5C58` | unchanged | 5.6–7.1:1 everywhere |
| `--vt-ink-3` | `#506561` | **was `#566A66`** | half-grade darker so meta text holds ≥4.5:1 inside the new deeper wells (4.44→4.61 on well-milk) |

### 5.7 · Signals (legal-surface scoped — Law S7)

| Token | Hex | Was | Legal on |
|---|---|---|---|
| `--vt-ok` | `#0E7447` | `#127A4E` | strata + planes (forms, chips) |
| `--vt-warn` | `#8F610C` | `#96660E` | strata + planes |
| `--vt-err` | `#AC3B27` | `#B3402B` | strata + planes |

### 5.8 · The hero dawn ramp (5 stops, zenith → horizon)

`#FDFCF8` (milk zenith) → `#F7F4EC` (porcelain) → `#FFEBE6` (dawn-blush band) → `#FFEBD2` (gold-mid, OKLCH 0.950 0.040 75) → `#EFE3C2` (warm horizon). The hero *teaches the page's layer grammar* before the first scroll (Judge 84): the sky itself is now a strata composition. All stops ≥ OKLCH L 0.94 — light world intact.

---

## 6 · CONTRAST & ACCESSIBILITY MATRIX

Recomputed from hex over the **full legal surface set** (13 surfaces). Minima:

| Foreground | Worst legal surface | Ratio | Threshold | Verdict |
|---|---|---|---|---|
| INK `#123F3B` | well-milk | **8.87:1** | 7:1 (AAA) | ✅ AAA everywhere (10.1–11.4:1 on strata) |
| INK2 `#3E5C58` | well-milk | **5.55:1** | 4.5:1 | ✅ |
| INK3 `#506561` | well-milk | **4.61:1** | 4.5:1 | ✅ (was 4.37 — fixed) |
| PEACOCK-600 | well-milk | **5.87:1** | 4.5:1 (text) | ✅ |
| PEACOCK-500 | well-milk | **4.16:1** | 3:1 (UI/large) | ✅ UI-role only |
| CORAL | well-milk | **4.68:1** | 4.5:1 | ✅ |
| SIGNAL_OK/WARN/ERR | planes/strata worst | **≥4.55:1** | 4.5:1 | ✅ on legal surfaces |
| MILK on PEACOCK fill | — | **5.33:1** | 4.5:1 | ✅ |
| SAFFRON / SKY | decorative | — | n/a | marks/atmosphere only (Law S7) |

**Colour-vision deficiency (Judge 64):** every band separation carries lightness as well as hue — sage/powder differ −2.7%/−3.2% luminance and 103° hue; no boundary relies on hue alone.

**Reduced motion:** bands ship static (no transition dependence); all existing motion prefs unchanged.

---

## 7 · BAND ARCHITECTURE — THE PAGE MAPS

### 7.1 · Homepage — the five-act colour journey

| Act | Section | Ground (L2) | Raised (L3) | Sunken (L4) | Narrative |
|---|---|---|---|---|---|
| I | Hero | 5-stop dawn ramp (§5.8) | milk side-card (frosted) | — | *the idea arrives at dawn* |
| II | Work / proof | porcelain `#F7F4EC` | milk case-cards | bone wells | *the calm record* |
| III | Services / craft | **sage** `#E7F5E7` | milk rows (hover) | sage-well marquee `#DCEEDC` | *the green of making* |
| IV | About / journey | **powder** `#E3F3FF` | milk testimonials, maker card | powder-well journey rail `#D8EAFD` | *the wide sky of the maker* |
| V | Contact / beginning | **blush** `#FFE9EA` + gold horizon seal | milk form card | — | *the warm invitation* |
| — | Footer | bone floor `#F0EBDF` | — | — | *the earth below the dawn* (unchanged) |

Band boundaries: hard cuts stitched by 1px host-tinted hairlines (`--vt-line-*`). No two adjacent acts share a ground (Law S6). Warm → neutral → cool → warm rhythm: the page *warms* as it approaches the contact act — colour participates in the funnel (Judge 71/73/80).

### 7.2 · Inner pages

| Page | Ground | Notes |
|---|---|---|
| `work/` index | porcelain | cards milk; meta chips wash-sky |
| case studies | porcelain | stats band → powder-well inset; pull-quotes → gold-deep wash `#FEEFD7`; next-action cards milk |
| `services/` | **sage** page-wide | mirrors the home craft act; service rows hover → milk; per-service chips wash-peacock |
| `about/` | **powder** page-wide | mirrors the home maker act |
| `contact/` | **blush** page-wide | form card milk; channel cards milk; availability chip wash-peacock (unchanged) |
| `journal/` index | **gold** `#FDECCF` | essay cards milk; kicker bands wash-saffron |
| essays | porcelain body | alternating band rhythm: intro porcelain → argument bands gold-deep wash → stats powder-well → outro blush |
| `404` | blush | the kite page gets the dawn's warmest ground |
| legal | porcelain | documents stay on the calm floor |

### 7.3 · Band seam treatment

Each band's top edge carries `border-top: 1px solid var(--vt-line-<host>)` where it meets the previous act; the marquee (in sage) and the journey rail (in powder) act as *inner seams* — well-tinted strips that deepen the band's own hue. The footer seam is the existing `--vt-ink-a06` hairline over bone.

---

## 8 · COMPONENT APPLICATION RULES

Context mechanism (already proven by `.milk`, Judge 41): **band classes override context tokens**, so every existing component re-tints automatically — components never gain raw hex (Law L9 preserved).

```css
.band--sage, .band--powder, .band--blush, .band--gold, .band--dawn {
  background: var(--vt-stratum);
  --vt-canvas:      var(--vt-stratum);   /* header frost, veils, cue adapt */
  --vt-surface-2:   var(--vt-well);      /* wells re-tint to host hue */
  --vt-line:        var(--vt-line-band); /* hairlines re-tint */
  color: var(--vt-ink);
}
/* Accent, ink, milk tokens do NOT flip — verified on every band (§6). */
```

| Component | Rule |
|---|---|
| Case cards | milk plane + host hairline + `--vt-shadow-3`; media wells use band well |
| Service rows | transparent on sage; hover → milk plane + shadow-2 (lift reads as paper) |
| Marquee | sage-well strip, ink-a06 rails (the craft act's inner seam) |
| Journey steps | powder-well cards; active step = milk plane + saffron stroke (existing) |
| Testimonials | milk planes on powder |
| Hero side-card | frosted milk-a65 over the dawn ramp (unchanged mechanics, new sky behind) |
| Header | frosted `--vt-canvas-a78` — resolves to a *tinted* frost over each band (the band bleeds through) |
| Availability chip | wash-peacock + ok border (unchanged) on blush — the one cool note in the warm act, deliberate contrast for the CTA path |
| Chips / kickers | wash tokens re-aimed per band: meta chips wash-sky on porcelain; service chips wash-peacock on sage; journal kickers wash-saffron on gold |
| Forms | fields on milk card; focus halo peacock-a08; error wash err-a10 (signals scoped to planes, Law S7) |
| Code blocks | well of local context; syntax palette unchanged |
| Footer | bone floor + saffron ambient (unchanged) — the constant earth under the variable dawn |

---

## 9 · THE HERO — DAWN AS STRATA

- **SVG fallback** (`svgs.py`): 3-stop sky becomes the 5-stop ramp (§5.8); ridgelines and kite unchanged (peacock).
- **WebGL shader** (`horizon.js`): sky gradient gains the blush stop between porcelain and gold-mid — zenith milk → porcelain → blush `vec3(1.0, 0.922, 0.902)` → gold-mid → horizon; saffron glow and powder ribbon unchanged; kite peacock unchanged. No new uniforms; cost unchanged.
- The hero thus *demonstrates* L1→L2 layering (sky bands) with L3 (frosted side-card) floating on it before the visitor scrolls — the layer grammar is taught, then practised.

---

## 10 · ENGINEERING PLAN

1. **`v2-src/palette.py`** — add STRATA section (ground, 6 strata, 5 wells, 4 lines, ramp, adjusted INK3/signals); keep every legacy alias compiling (VOID/SURFACE/EMBER… unchanged meanings).
2. **`assets/css/tokens.css`** — new `--vt-stratum-*`, `--vt-well-*`, `--vt-line-*` tokens + the five `.band--*` context classes (mechanism above); INK3/signal values updated; comment header re-branded STRATA.
3. **`assets/css/components.css`** — add `band--*` classes to home acts; marquee/journey/testimonials seam rules; header frost already token-driven (no change).
4. **`assets/css/pages.css`** — page-wide band classes for services/about/contact/journal; case-study band insets; essay pull-quote gold wash; 404 blush.
5. **`v2-src/svgs.py`** — hero fallback ramp update (reads palette constants).
6. **`assets/js/app/horizon.js`** — sky ramp constants (§9).
7. **`build.py`** — no structural change; manifest `background_color` stays porcelain (the floor).
8. **Audits** (§11) extended, then green, then build.

Estimated delta: ~180 lines CSS, ~40 lines JS, ~70 lines Python. Zero new dependencies. Zero runtime cost.

---

## 11 · QA & AUDIT PROTOCOL (GATES, NOT CHECKS)

1. **`contrast_audit.py` (extended):** matrix = {INK, INK2, INK3, PEACOCK-600, CORAL, SIGNAL×3} × {porcelain, 6 strata, milk, 6 wells}; thresholds 7/4.5/4.5 per role; legal-surface scoping encoded. Gate: zero failures.
2. **`banlist_scan.py` (unchanged):** zero black/brown/dark hex anywhere; plus new floor: every fill ≥ OKLCH L 0.89. Gate: zero.
3. **NEW `band_audit.py`:** for each page, assert computed act backgrounds differ from neighbours (≥3% rel-lum or ≥25° hue) — the visibility law, enforced forever (Judge 48). Gate: homepage ≥4 distinct grounds; inner pages match §7.2.
4. **Pixel audit (`fl_pixel_audit.py` updated):** dark-pixel share ≤2% per page; homepage vertical profile spans ≥4 hue families (S2). Gate: pass.
5. **Link/alt QA:** `build.py` built-in gate. Zero broken.
6. **Blind visual review:** describe-the-colours test (S7) — expect ≥3 colour words including green, blue, pink/gold.

---

## 12 · ROLLOUT & VERIFICATION

1. Implement §10 → run §11 gates → `python3 v2-src/build.py` (repo root is the deploy tree).
2. Sync `repo-vishvu/` → preview project `public/site/`; restart preview server; confirm live.
3. Screenshot every page; run pixel + band audits on the *rendered* result (not just source).
4. Blind visual review (S7) — recorded.
5. Commit `feat: STRATA — layered light colour architecture (VT-PRD-005)` with docs; push as the owner.
6. Oracle Free Tier: unchanged static deploy; the PRD adds no runtime requirements (N3).

---

## 13 · THE TEN LAWS OF STRATA (THE WALL CARD)

1. **Light world, no exceptions** — nothing below OKLCH L 0.89, ever.
2. **Six layers, one stack** — ground, stratum, plane, well, marks, ink.
3. **Every layer is chosen on the composite below it** — never on a swatch.
4. **Every layer is visible** — 3% / 10% / 7% floors; sub-perceptual washes banned.
5. **One dawn family** — strata hues 15°–250°, L 0.955–0.960; many colours, one world.
6. **Chroma rises with depth** — depth carries colour information.
7. **Peacock means action; bands mean place** — no new accent hues.
8. **No two neighbours share a ground** — the scroll has chapters.
9. **Legal surfaces only** — every token declares its hosts; contrast is verified over composites.
10. **The audits are the law** — contrast, banlist, band, pixel gates in every build.

---

## 14 · APPENDIX — CANONICAL VALUES (single export)

```
GROUND     porcelain #F7F4EC
STRATA     dawn #FFEBE6 · gold #FDECCF · sage #E7F5E7 · powder #E3F3FF · blush #FFE9EA · gold-deep #FEEFD7
PLANE      milk #FDFCF8
WELLS      bone #F0EBDF · sage #DCEEDC · powder #D8EAFD · blush #FCE1E0 · gold #F7E6CA · in-milk #E6E0D2
LINES      porcelain #E2DBC8 · sage #D1E2D0 · powder #CCDFF1 · blush #F0D6D3 · gold #EADBC0 · strong #CFC6AE
INK        #123F3B / #3E5C58 / #506561
ACCENT     #0F766E / #0B5D57 · reserves coral #A83F28 · saffron #E9A23B · sky #9DB8D9
SIGNALS    ok #0E7447 · warn #8F610C · err #AC3B27
HERO RAMP  #FDFCF8 → #F7F4EC → #FFEBE6 → #FFEBD2 → #EFE3C2
```

*STRATA — the dawn, decomposed into layers the visitor can walk through.*
