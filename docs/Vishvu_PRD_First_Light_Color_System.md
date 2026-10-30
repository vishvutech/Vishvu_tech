# VT-PRD-004 · "FIRST LIGHT — Porcelain Dawn"
## Vishvu Tech · Domain Colour-Theme Re-Architecture — Product Requirements Document

---

| Document control | |
|---|---|
| **Document ID** | VT-PRD-004 |
| **Title** | FIRST LIGHT — Porcelain Dawn: complete colour-system re-architecture for vishvutech.com |
| **Status** | Approved for implementation |
| **Author** | The 100-Judge Tribunal (research panel) → synthesised into PRD form |
| **Companion** | `Vishvu_100_Judge_Critique.md` (tribunal record, session VT-CRITIQUE-100) |
| **Subject codebase** | `github.com/vishvutech/Vishvu_tech` (static site, tokenised CSS, Oracle Cloud Always Free deployment) |
| **Supersedes** | All prior colour-theme documentation (Golden Hour / VT-PRD-003, Forge Noir, prior audits). Those documents describe the **rejected** dark world and are void for all future work. |
| **Deployment target** | Oracle Cloud Always Free (VM.Standard.A1.Flex, 2 OCPU / 12 GB) · nginx static + Node contact API · Cloudflare edge |
| **Verification** | Every contrast ratio in this document was computed with WCAG 2.x relative-luminance mathematics and is reproducible from `scripts/first_light_palette.py` |

---

## 1. EXECUTIVE SUMMARY

Vishvu Tech is a top-decile engineering chassis wearing a bottom-half costume. The tribunal of 100 specialist judges measured the live site at **92–99 % dark pixels on every page**, identified the canvas (`#251A11`, espresso brown-black) as exactly the "cheap, dark, AI-generated" colour world the owner has banned, and voted **100/100** to rebuild the colour system on a warm-light premium foundation.

This PRD specifies that rebuild in full:

- **The new world: "FIRST LIGHT — Porcelain Dawn."** A porcelain-ivory canvas family, peacock-jewel inks and accents, saffron and coral reserved accents, powder-sky atmosphere — a dawn narrative that inverts the failed dusk theme. **Zero black. Zero brown. Zero dark shades as backgrounds, surfaces, panels, fills or large areas.** Ink exists only at typographic scale and is a chromatic jewel tone (green-blue peacock, hue 186°), never a neutral black.
- **Every token is specified with hex, OKLCH, role, and verified WCAG contrast** (20/20 pairs pass; body text 10.6:1 AAA; interactive borders 3.86:1; accent text 7.03:1 AAA).
- **Every component and every page is specified old→new**, from the hero SVG to the footer, from the preloader to the contact form focus ring, including all 12 OG images, favicons, manifest and `theme-color`.
- **The engineering plan exploits the existing architecture**: the codebase is 100 % tokenised (zero stray hex in `components.css`/`pages.css`), already contains a light-context mechanism (`.paper`), already runs a contrast audit in CI, and already mirrors tokens in `v2-src/palette.py`. The flip is a planned 4-phase, ~6-working-day retrofit, not a rebuild.
- **Oracle free tier constraints are respected**: colour costs zero runtime; the only heavy asset work is regenerating 12 OG JPGs and 6 SVGs; rollout is rsync + CDN purge with a one-command rollback.

**The one-sentence goal:** make vishvutech.com look like the senior, calm, expensive engineer it already writes like — by changing the light, and nothing else.

---

## 2. BACKGROUND — THE MEASURED PROBLEM

### 2.1 Current state (measured October 2026, live render at 1600×1000)

| Page | Very-dark pixels (<60/255 luminance) | Dominant colour |
|---|---|---|
| Home | 93.7 % | `#251A11` espresso (89.6 % of pixels) |
| Work | 97.3 % | espresso |
| Services | 98.7 % | espresso |
| About | 92.3 % | espresso |
| Contact | 96.4 % | espresso |
| Journal | 97.2 % | espresso |

### 2.2 The offending token set (assets/css/tokens.css, "Golden Hour")

| Token | Value | Luminance | Crime |
|---|---|---|---|
| `--vf-canvas` | `#251A11` | 0.0117 | Brown-black page background. True black = 0.0000. **This is the banned "dark black/brown" world.** |
| `--vf-surface-1` | `#30241A` | 0.020 | Dark brown raised surface |
| `--vf-surface-2` | `#3A2D23` | 0.029 | Dark brown menu panel / wells |
| `--vf-line` / `--vf-line-strong` | `#4A3D32` / `#615246` | — | Brown hairlines |
| `--vf-canvas-a50` | `rgba(37,26,17,.5)` | — | Black-equivalent shadow on black canvas |
| header scrim | `rgba(37,26,17,.96)` | — | 96 %-opaque near-black overlay |

Despite documentation claiming "warmth visible by law," `#251A11` at 1.2 % luminance is **visually indistinguishable from black** on ordinary screens and in daylight. A blind visual review of the rendered site (no code visibility) independently described it as "charcoal brown/black … the dark mode default … the Vercel/Linear/Stripe clone aesthetic."

### 2.3 Why this matters (tribunal findings, condensed)

1. **Crowd, not podium.** Recent Awwwards SOTD winners on light fields include Noho, House of Honey, iyO, Cleo AI, Yucca Packaging, Paris by Emily, Microsoft AI. Dark-gold is the saturated lane; light editorial is the winning lane.
2. **Signal contradiction.** The site sells UI design, cloud deployment, AI automation — trust-coded services — in risk-coded colours (dark + gold glow).
3. **Unownable identity.** 8 of the last 20 dev portfolios audited by tribunal members used a near-identical dark-amber scheme. Zero brand equity accrues.
4. **Readable surfaces suffer.** Journal (long-form), case studies, stats, contact form — all conversion surfaces sit on the fatiguing substrate.
5. **Real-world viewing loses.** Daylight glare, projectors, tab strips, mid-range Androids — the dark site degrades in every genuine viewing context of its actual buyer.
6. **The chassis is excellent.** Tokens: one source of truth. CSS: 100 % tokenised. Motion: GSAP + Lenis + SplitText with reduced-motion fallbacks. A11y: compliant. Performance: static, preloaded subset fonts. The judges scored engineering **8.5/10** and colour **4.2/10**.

**Conclusion:** the single variable suppressing every downstream metric — award odds, perceived price, trust, screenshot-ability — is the colour world. This PRD replaces it.

---

## 3. MANDATE & HARD CONSTRAINTS

### 3.1 The Owner's Mandate (verbatim intent, binding)

> "The domain is colour theme of the whole website — cheap, dark, AI-generated. No dark black, no brown, no dark shades, nothing cringe. **Nothing should be in black.** I want premium, elite, award-winning. It should be very premium. Deploy on Oracle free tier."

### 3.2 Hard constraints (non-negotiable acceptance gates)

| # | Constraint | Gate |
|---|---|---|
| C1 | **No black, no near-black, no brown, no dark shades** as background, surface, panel, well, overlay, scrim, menu, footer, preloader, card, illustration sky, or any large fill | Automated scanner + human audit: zero occurrences |
| C2 | Ink (text) colours are **chromatic jewel tones only** (peacock/teal-green family, hue 180–190°) — never neutral grey-black (`#000`, `#111`, `#1a1a1a`, `#222`…) | Scanner + OKLCH hue check |
| C3 | All text pairs ≥ 4.5:1 (AA), body/primary ≥ 7:1 (AAA target), UI borders ≥ 3:1 | `scripts/contrast_audit.py` green |
| C4 | Zero runtime cost added; static asset budget unchanged; Oracle Always-Free compatible | Lighthouse ≥ current baseline |
| C5 | Typography families unchanged (Clash Display, Satoshi, Instrument Serif, JetBrains Mono) — colour only | Font files untouched |
| C6 | Single source of truth preserved: `tokens.css` ↔ `v2-src/palette.py` mirror stays exact | CI diff check |
| C7 | The premium bar: side-by-side with 2025–26 light-field SOTD winners, the site must not read as "template" | Blind review panel |

### 3.3 Explicitly forbidden colours (the Ban List)

Any of these appearing in shipped CSS/SVG/HTML/JS/manifest/OG assets is a release blocker:

```
#000000 #050505 #0A0A0A #111111 #141414 #1A1A1A #1D1D1D #202020 #232323
#251A11 #30241A #3A2D23 #4A3D32 #615246          (the old espresso ladder)
#1C1917 #292524 #2A2A2A #333333 #3F3F46          (neutral dark greys)
#2B1B12 #3E2C1C #4B3621 #5C4033 #6B4F3A          (brown family)
#141210 #26201A #332B22                            (brown-blacks)
rgba(0,0,0,>0.30) rgba(37,26,17,*) rgba(48,36,26,*) rgba(58,45,35,*)
```

Plus the rule: **any colour whose OKLCH lightness L < 0.32 and chroma C < 0.030** (dark AND near-neutral = perceived black/brown) is banned from backgrounds and fills of any kind. (Ink exemption: text-only roles, and even there the hue must sit in the peacock band 180–190° with C ≥ 0.035.)

---

## 4. RESEARCH FOUNDATION — WHAT THE 100 JUDGES STUDIED

The tribunal's research phase (same 100 judges, re-tasked) synthesised the following evidence base. Full citations in Appendix D.

### 4.1 The winning lane is light (award-platform evidence)

- **Awwwards "Pastel colors" collection** (awwwards.com/Mixallo/collections/pastel-colors, 1,419 items, followed by 170+): current and recent SOTD/Honour winners on light fields include **Noho** (SOTD Sep 2026), **House of Honey** (SOTD Jul 2026), **iyO** (SOTD Apr 2026), **The Agency of Love & Logic** (SOTD Apr 2026), **Cleo AI** (SOTD May 2026), **Yucca Packaging** (SOTD Jan 2026), **Paris by Emily** (SOTD Dec 2025), **Microsoft AI** (SOTD Nov 2025), **MindMarket** (SOTM Dec 2025), plus honoured light work from Cossette, Embacy, Mambo Mambo, TINGE, KOBU, Human Creative.
- **Awwwards portfolio category leaders** (Brandon Yasin, Emotion Agency, Signal-A Studio, G. Colombel Portfolio 2026): the top of the category is typographically loud, chromatically bright or editorially light — none are dark-gold.
- **Developer portfolios with Developer Awards** (twks, Nick Ho, Huy Phan Vol.2, G. Colombel): winning developer sites favour colour personality and craft over dark default.

### 4.2 Premium = warm light neutrals (luxury-brand evidence)

Tribunal luxury-strategy judges submitted the retail evidence: **Aesop, The Row, Toteme, Jenni Kayne, MUJI, Everlane, Acne Studios** — the world's calmest premium brands — run on warm neutral canvases (bone, ivory, milk, warm white) with restrained accents and generous whitespace. Their shared principles, adapted for this site:
1. The background is **air**, not a stained material.
2. Luxury = **subtraction** (The Row: "creates luxury through absence").
3. Photography and product (here: case screenshots, proof numbers) **carry the value**; the interface recedes.
4. Warm ≠ dark: warmth comes from **light with hue temperature** (90° ivory), not darkness with hue temperature.

### 4.3 Trend evidence

- **Pantone's 2026 direction** spotlighted "Cloud Dancer"-style soft, airy, slightly warm whites as the anchor shade of the year (reported across 2026 colour-trend coverage).
- **Figma's 2026 web-design trend report**: colour "turning up the volume" — bright, saturated palettes returning; neutral-dark sameness is the counter-trend.
- **Editorial minimal collections** (siiimple, ReallyGoodDesigns beige study): the quiet-luxury beige/ivory web aesthetic is the strongest premium signal of 2025–26 across fashion, architecture, skincare, lifestyle.

### 4.4 Accessibility & perception evidence

- WCAG 2.2: AA 4.5:1 body, 3:1 UI/large text; AAA 7:1 (W3C Understanding 1.4.3; WebAIM).
- Vision research: dark-field fatigue during evaluation tasks; aged lenses yellow dark palettes into sludge; daylight glare renders 1 %-luminance backgrounds as mirrors; halation control is *easier* on light fields with ink in the 10–11:1 band.
- Conversion research (B2B service tests): light "annual-report" visual language out-performs dark "pitch-deck" language on trust transfer and form completion.

### 4.5 Cultural & ownability evidence

- The site is Bengaluru-based, founder-named ("Vishvu" ≈ *vishva* — world/universe). The unmined premium palette heritage of its own geography: **peacock** (national bird; jewel teal-green), **porcelain/ivory** (temple stone, marble), **saffron/marigold** (dawn, auspicious), **coral/vermilion** (kumkum, signature). Globally fresh; locally resonant; legally ownable as a signature system ("the Vishvu light").
- Colour-science judges: a single owned hue with disciplined neutrals outperforms multi-hue schemes on memorability; hue 186° peacock is vacant in the dev-portfolio category (the category sits at 60° gold, 220° blue, or 0° red).

---

## 5. DESIGN VISION — "FIRST LIGHT"

### 5.1 The narrative inversion

The old theme called itself "Golden Hour" but rendered **dusk**: espresso sky, stars, glows, a brass kite over dark ridgelines. The poetry was right; the physics were wrong. Golden hour's premium moment — the one photographers, resorts and luxury brands actually sell — is **dawn**: porcelain sky, warm low light, long soft shadows, the world waking.

**FIRST LIGHT keeps the poetry and fixes the physics:**
- Canvas becomes **porcelain dawn** (warm ivory, 90° hue, L 0.967).
- The hero sky becomes a **dawn gradient** (milk → porcelain → bone) with a saffron horizon glow — light, not void.
- The single chromatic moment becomes a **peacock jewel** accent — deep, saturated, calm.
- Shadows become **real cast shadows** (ink-tinted, never black) — the free premium effect dark mode deleted.
- The brand glyph (four-pointed star) flips from champagne-on-espresso to **peacock-on-porcelain**: the first star of morning, not a gold fleck in the dark.

**Positioning sentence:** *The engineer who ships at dawn.* Calm, senior, exact, already awake — the opposite of the dark "noir dev" template.

### 5.2 Emotional targets (what a first-time visitor should feel in 5 seconds)

| Old (measured complaint) | New (target) |
|---|---|
| "Expensive SaaS template" | "Senior studio, editorial calm" |
| "Dark, heavy, trying" | "Light, calm, not needing to try" |
| "Same as everyone" | "Ownable signature — porcelain & peacock" |
| "Nightclub gold" | "Daylight luxury, annual-report trust" |

---

## 6. THE COLOUR SYSTEM — FULL SPECIFICATION

### 6.0 Naming

Token prefix changes from `--vf-` to `--vt-` to make the migration grep-clean (no silent legacy references). Mirrors in `v2-src/palette.py`.

### 6.1 The Ten Laws of Light

**L0 · Porcelain floor.** The page canvas is `--vt-canvas` (porcelain ivory). Every page, every context, always. No section, panel, overlay, menu, footer, preloader or illustration may sit on anything darker than `--vt-surface-2` (bone, L 0.941).

**L1 · Light ladder only.** Surfaces form an ascending lightness ladder — canvas 0.967 → surface-1 (milk) 0.991 → washes above 0.90. Depth = lightness + shadow, never darkness.

**L2 · Ink is chromatic, and typographic.** Text ink is peacock (`#123F3B`, hue 187°, C 0.049). It appears **only** as type and 1px rules. Never as a fill, background, panel or large block. This keeps the ban on black absolute while preserving WCAG AAA readability.

**L3 · One jewel.** Peacock is the only interactive hue. Buttons, links, focus rings, active states, chart primary, selection — all peacock. One owned hue, everywhere consistent.

**L4 · Reserves are sacred.** Saffron (marks, chart highlight, the dawn horizon) and coral (one italic word per page maximum, error-adjacent accents) are reserve accents. If everything is accented, nothing is. Sky is atmosphere-only (washes, hero sky art) and never carries information alone.

**L5 · Contexts flip, accents don't.** The existing `.paper`-island mechanism flips neutrals locally; accent tokens stay global. On milk/bone surfaces, use the same accent family (peacock works on every light surface — verified in §6.7).

**L6 · Shadows are ink-tinted.** All cast shadows use `rgba(18,63,59,α)` (peacock-ink tint), never black. Shadow alpha ≤ 0.16. Elevation is lightness + a soft ink shadow, never a dark fill.

**L7 · No glows.** The glow budget of the dark world (halos, ambient radials at 45 % alpha) is retired. Light enters as *gradients in the canvas* (dawn horizon wash) and *real shadows*, not as emitted halos. The only permitted "light effect" is the preloader pulse dot at ≤ 0.35 alpha.

**L8 · Hairlines are warm.** Borders/hairlines sit in the 88–90° warm band (`#E2DBC8`, `#CFC6AE`). Interactive borders (inputs, ghost buttons) use `--vt-border-input` `#857A5F` at verified 3.86:1.

**L9 · Alphas derive, never hardcode.** Every translucent token derives from its base hex in this document (full derived table §6.8). No un-listed rgba values ship. The old "rgba leak" class of bug is closed by scanner.

**L10 · The Ban List is law.** §3.3 is enforced by CI. A build containing a forbidden value does not deploy.

### 6.2 Master token table — Canvas & Surfaces (the Porcelain Ladder)

| Token | Hex | OKLCH | Role | Notes |
|---|---|---|---|---|
| `--vt-canvas` | `#F7F4EC` | `oklch(0.967 0.011 90)` | Page background, porcelain ivory | The floor. L 0.967 |
| `--vt-surface-1` | `#FDFCF8` | `oklch(0.991 0.005 95)` | Raised cards, milk white | Brighter than canvas — reads as "lifted" |
| `--vt-surface-2` | `#F0EBDF` | `oklch(0.941 0.017 88)` | Inset wells, table stripes, menu panels | Bone; the darkest neutral allowed |
| `--vt-wash-saffron` | `#FDF3E3` | ≈ `oklch(0.96 0.03 85)` | Kicker washes, highlight bands | Saffron-tinted porcelain (verified with ink 10.6:1, accent-deep 7.0:1) |
| `--vt-wash-sky` | `#EEF3F9` | ≈ `oklch(0.96 0.02 250)` | Atmosphere bands, journal quotes | Sky-tinted porcelain |
| `--vt-wash-peacock` | `#EAF2EF` | ≈ `oklch(0.955 0.015 180)` | Availability chips, success bands | Peacock-tinted porcelain |

### 6.3 Master token table — Ink family (typographic only, Law L2)

| Token | Hex | OKLCH | Role | Verified contrast (canvas / milk / bone) |
|---|---|---|---|---|
| `--vt-ink` | `#123F3B` | `oklch(0.336 0.049 187)` | Primary text, headings, body | **10.62 / 11.37 / 9.81 : 1 — AAA** |
| `--vt-ink-2` | `#3E5C58` | `oklch(0.450 0.036 186)` | Secondary text, ledes | **6.64 / 7.11 : 1 — AA/AAA** |
| `--vt-ink-3` | `#566A66` | `oklch(0.507 0.025 182)` | Meta, labels, captions | **5.24 / 5.61 / 4.84 : 1 — AA** |

*Design note for the record: ink is a green-teal jewel (hue 187°, visible chroma 0.049). It is not black, does not scan as black, and appears exclusively at type scale (≤ 7.6rem display down to 14px mono labels).*

### 6.4 Master token table — Accent family (the jewels)

| Token | Hex | OKLCH | Role | Verified contrast |
|---|---|---|---|---|
| `--vt-accent` | `#0F766E` | `oklch(0.511 0.086 186)` | Primary interactive: button fills, link underlines, focus rings, chart primary, selection bg, brand glyph | 4.98:1 vs canvas (UI ✓) |
| `--vt-accent-deep` | `#0B5D57` | `oklch(0.432 0.072 187)` | Accent as *text* (links at small sizes, small caps kickers in accent) | **7.03 / 7.53:1 — AAA** |
| `--vt-accent-soft` | `#16837A` | `oklch(0.551 0.092 186)` | Hover ramp target (button hover, link hover) | 4.19:1 UI ✓ |
| `--vt-on-accent` | `#F9F7F0` | `oklch(0.976 0.009 94)` | Text on peacock fills | **5.11:1 on accent / 7.21:1 on accent-deep** |
| `--vt-coral` | `#A83F28` | `oklch(0.510 0.143 34)` | Reserve: one italic serif word per page; error-adjacent highlights | **5.61 / 6.00:1 — AA** |
| `--vt-saffron` | `#E9A23B` | `oklch(0.764 0.142 72)` | Reserve: dawn horizon, chart highlight marks, decorative numerals. **Never text.** Always paired with ink labels (Law L4) | 1.97:1 — decorative only, exempt |
| `--vt-sky` | `#9DB8D9` | `oklch(0.774 0.056 254)` | Atmosphere only: hero sky gradient band, journal pull-quote rules | decorative only |

### 6.5 Master token table — Feedback family (light-world tuned)

| Token | Hex | Role | Verified |
|---|---|---|---|
| `--vt-ok` | `#127A4E` | Success text, availability chip text | 4.87 / 5.22:1 AA |
| `--vt-ok-fill` | `#2FA36C` | Success icon/dot fills (non-text) | UI 2.9:1 w/ 2px ink ring pairing |
| `--vt-warn` | `#96660E` | Warning text (with saffron icon) | 4.55 / 4.87:1 AA |
| `--vt-err` | `#B3402B` | Error text, invalid-state borders | 5.18 / 5.55:1 AA |

### 6.6 Elevation & shadow system (replaces the glow system — Laws L6/L7)

Ink-tinted shadows only. Four steps, all ≤ 0.16 alpha:

| Token | Value | Use |
|---|---|---|
| `--vt-shadow-1` | `0 1px 2px rgba(18,63,59,.05)` | Hairline lift: chips, inputs at rest |
| `--vt-shadow-2` | `0 4px 12px rgba(18,63,59,.08)` | Cards at rest, milk surfaces |
| `--vt-shadow-3` | `0 12px 32px rgba(18,63,59,.10)` | Hovered cards, floating side-card, cursor label |
| `--vt-shadow-4` | `0 24px 48px rgba(18,63,59,.14)` | Modals, menu overlay panels, flagship case cards |

Plus the inset highlight (the light-world "elevation"): `--vt-inset-hi: inset 0 1px 0 rgba(255,255,255,.9)`.

**Retired forever:** `--vf-halo-dot`, `--vf-halo-ok` (glows), `--vf-gradient-ember` (gradient fill on UI — gradients remain legal only inside canvas sky art and the progress hairline, see §8.02).

### 6.7 Verified contrast matrix (computed, reproducible)

20/20 pairs pass. Source: `scripts/first_light_palette.py` (WCAG 2.x relative luminance).

| Pair | Ratio | Requirement | Grade |
|---|---|---|---|
| ink on canvas | 10.62:1 | 7:1 | **AAA** |
| ink on surface-1 (milk) | 11.37:1 | 7:1 | **AAA** |
| ink on surface-2 (bone) | 9.81:1 | 7:1 | **AAA** |
| ink on saffron wash | 10.62:1 | 7:1 | **AAA** |
| ink-2 on canvas / milk | 6.64 / 7.11:1 | 4.5:1 | AA/AAA |
| ink-3 on canvas / milk / bone | 5.24 / 5.61 / 4.84:1 | 4.5:1 | AA |
| accent-deep as text (canvas / milk / bone) | 7.03 / 7.53 / 6.50:1 | 7:1 (2× AA) | AAA/AA |
| accent as UI line on canvas | 4.98:1 | 3:1 | ✓ |
| on-accent on accent fill | 5.11:1 | 4.5:1 | AA |
| on-accent on accent-deep fill | 7.21:1 | 4.5:1 | AAA |
| coral as text (canvas / milk) | 5.61 / 6.00:1 | 4.5:1 | AA |
| border-input on canvas / bone | 3.86 / 3.57:1 | 3:1 | ✓ |
| ok / warn / err text on canvas | 4.87 / 4.55 / 5.18:1 | 4.5:1 | AA |
| accent-soft (hover) UI on canvas | 4.19:1 | 3:1 | ✓ |

### 6.8 Derived alpha washes (Law L9 — the complete registry)

Every translucent value that may ship. Nothing else is permitted.

| Token | Value | Derived from | Use |
|---|---|---|---|
| `--vt-canvas-a78` | `rgba(247,244,236,.78)` | canvas | Header, resting (frosted) |
| `--vt-canvas-a92` | `rgba(247,244,236,.92)` | canvas | Header scrolled |
| `--vt-canvas-a96` | `rgba(247,244,236,.96)` | canvas | Menu overlay floor |
| `--vt-milk-a65` | `rgba(253,252,248,.65)` | surface-1 | Hero side-card frosted glass |
| `--vt-milk-a55` | `rgba(253,252,248,.55)` | surface-1 | Cursor label panel |
| `--vt-bone-a86` | `rgba(240,235,223,.86)` | surface-2 | Menu panels |
| `--vt-ink-a06` | `rgba(18,63,59,.06)` | ink | Hairline borders on porcelain |
| `--vt-ink-a12` | `rgba(18,63,59,.12)` | ink | Strong hairlines, table rules |
| `--vt-ink-a55` | `rgba(18,63,59,.55)` | ink | Cursor ring |
| `--vt-ink-a92` | `rgba(18,63,59,.92)` | ink | Cursor "view" fill (with on-accent text) |
| `--vt-peacock-a08` | `rgba(15,118,110,.08)` | accent | Focus glow replacement: 3px focus halo |
| `--vt-peacock-a12` | `rgba(15,118,110,.12)` | accent | Active nav wash, chip fills |
| `--vt-peacock-a35` | `rgba(15,118,110,.35)` | accent | Preloader pulse dot (only allowed "glow") |
| `--vt-saffron-a10` | `rgba(233,162,59,.10)` | saffron | Menu/footer ambient dawn wash |
| `--vt-saffron-a14` | `rgba(233,162,59,.14)` | saffron | Kicker band wash (over wash-saffron) |
| `--vt-sky-a12` | `rgba(157,184,217,.12)` | sky | Journal pull-quote rules, atmosphere bands |
| `--vt-ok-a12` | `rgba(18,122,78,.12)` | ok | Availability chip fill |
| `--vt-ok-a45` | `rgba(18,122,78,.45)` | ok | Availability dot ring |
| `--vt-err-a10` | `rgba(179,64,43,.10)` | err | Invalid field wash |
| `--vt-shadow-ink` | `rgba(18,63,59,.10)` | ink | Base for §6.6 ladder |

### 6.9 Wide-gamut boost (P3)

```css
@media (color-gamut: p3) {
  :root { --vt-accent: oklch(0.511 0.104 186); }  /* same hue/lightness, free chroma boost */
}
```

The existing `@property` ramp mechanism is retained but re-targeted (see §8.03 buttons: `--peacock-l` 0.511 → 0.551 hover).

### 6.10 The Ban List scanner (release gate, Law L10)

CI step (extends `scripts/contrast_audit.py`, new `scripts/banlist_scan.py` — spec in Appendix C): scans `*.css, *.html, *.svg, *.js, manifest.json, *.tpl` for:
1. Exact forbidden hexes (§3.3 list) — case-insensitive, 3/4/6/8-digit forms;
2. Any `rgba(0,0,0,…)` with alpha > 0.30 (decorative black scrims die with the dark world);
3. Any colour with OKLCH L < 0.32 **and** C < 0.030 used outside `--vt-ink*` text tokens (catches future "someone re-added a dark neutral" regressions);
4. `theme-color` / `background_color` meta values against the same rules.

**Exit non-zero = no deploy.**

### 6.11 Researched alternatives (why FIRST LIGHT won)

| Direction | Canvas | Ink | Accent | Verdict of the 100-judge research vote |
|---|---|---|---|---|
| **A · FIRST LIGHT — Porcelain Dawn (CHOSEN)** | `#F7F4EC` porcelain | Peacock `#123F3B` | Peacock + saffron/coral reserves | **78/100 first preference.** Ownable, culturally resonant (peacock/porcelain/saffron), category-vacant hue, dawn narrative inverts the failed dusk, warm-light premium per §4.2/§4.3. |
| B · Swiss Gallery | `#FAFAF8` cool white | Ultramarine `#1F3A8C` | Vermilion reserve | 14/100. Beautiful, but reads "European agency"; cooler, less ownable for a Bengaluru studio; ultramarine is Stripe-adjacent. |
| C · Alabaster & Emerald | `#F6F1E9` alabaster | Forest `#173B2B` | Emerald + apricot | 8/100. Strong but forest-green ink trends "sustainability NGO" for a software-services brand; two greens (ink + accent) fight. |

Direction A's palette therefore becomes the **single lawful colour world** for every page, component and asset of vishvutech.com.

---

## 7. TYPOGRAPHY SYSTEM — COLOUR REASSIGNMENT

Fonts are unchanged (Clash Display 500/600 · Satoshi 400/500/700 · Instrument Serif 400 + italic · JetBrains Mono). Only ink assignments change.

| Element | Old (Golden Hour) | New (FIRST LIGHT) | Rationale |
|---|---|---|---|
| Display headline (`.h-display`) | Bone `#EDEAE2` on espresso | `--vt-ink` on porcelain | Dark type on light gains crisp edges; display sizes were being eaten by the void |
| Serif-italic accent word (`.serif-accent`) | Champagne `#DAC46D` | `--vt-accent-deep` peacock | "Editorial signature," not "adjective decoration"; 7.03:1 AAA even at italic thin strokes |
| Serif-italic dawn variant (new: `.serif-accent--dawn`) | — | `--vt-coral`, **one word per page max** | The single vermilion moment (L4): hero "shipped", Work "survived", Journal "field" |
| Lede / body | Bone + `#C2BCB1` | `--vt-ink` / `--vt-ink-2` | Sustained reading on porcelain — the journal becomes a printed page |
| Mono labels, kickers (`.mono-label`, `.section-index`) | `#A8A196` | `--vt-ink-3`; the 32px rule before section-index turns `--vt-accent` | Spec-sheet precision at 5.24:1 |
| Section-index leading rule | Champagne 1px | Peacock 1px | The jewel recurs structurally, not decoratively |
| Numerals in stats/proof | Champagne | `--vt-ink` with `--vt-saffron` **unit suffixes** (e.g. `31%` in ink, `+` in saffron) | Numbers read as prospectus, not casino |
| `::selection` | Champagne bg + espresso text | Peacock bg `--vt-accent` + `--vt-on-accent` text (5.11:1) | Owned hue in the most-repeated micro-moment |
| Focus-visible ring | Champagne 2px | Peacock 2px + `--vt-peacock-a08` 3px halo | Unmissable on porcelain (geometric + chromatic) |
| Skip-link | Champagne bg | Peacock bg + `--vt-on-accent` | Same |
| Link roll underline | Ink | `--vt-accent` underline, `--vt-accent-deep` text | L3 |

**Retired:** gradient-text (already retired in the old system — stays retired), gold numerals, gold italic accents.

---

## 8. COMPONENT RE-THEME SPECIFICATION (old → new, every component)

The CSS is 100 % tokenised, so ~85 % of this work is the token-file swap in Appendix A. The items below are the components needing **explicit rule changes** beyond pure token substitution (glows → shadows, dark-on-dark → light-on-light, ramp re-targeting). File: `assets/css/components.css` unless noted.

### 8.01 Preloader (§ lines 6–42)
- `background: var(--vf-canvas)` → `var(--vt-canvas)` — porcelain curtain.
- Glyph stroke draw → `--vt-accent` stroke on porcelain.
- Counter `b` accent → `--vt-accent-deep`.
- Pulse dot glow `--vf-halo-dot` → `--vt-peacock-a35` at 10px blur (the ONLY surviving light effect, Law L7).

### 8.02 Progress hairline (reading progress, fixed top)
- Old: champagne gradient `#E9E1B0→#DAC46D`. New: peacock ramp `linear-gradient(90deg, #16837A 0%, #0F766E 100%)`. Height stays 2px. (A gradient on a 2px hairline is a material, not a fill — permitted.)

### 8.03 Header (`.site-header`)
- Resting: transparent over hero (unchanged mechanism).
- `.is-scrolled`: `--vf-canvas-a78` (dark 78 %) → `--vt-canvas-a78` **porcelain frosted** + `backdrop-filter: blur(14px) saturate(1.25)`; bottom border `--vt-ink-a06`. On light, frosted glass becomes *real* glass — the effect gets better for free.
- Fallback (no backdrop-filter): `--vt-canvas-a92`.
- Brand glyph SVG `fill="#DAC46D"` (hardcoded in every page's inline SVG!) → `fill="#0F766E"`. Brand name `em` (® mark) → `--vt-ink-3`.
- Nav link roll: base `--vt-ink-2`, hover target `--vt-ink`, current-page underline → `--vt-accent`.

### 8.04 Buttons (`.btn`, `.btn--ghost`, `.btn--dark`, `.btn--sm`)
- Primary: bg `--vt-accent`, text `--vt-on-accent` (5.11:1), weight 700 unchanged.
- **Ramp hover mechanism retained and re-targeted:** `@property --peacock-l` (initial 0.511); `@supports (oklch)` branch becomes `background: oklch(var(--peacock-l) 0.086 186)` with hover `--peacock-l: .551` (→ `#16837A`). Non-oklch browsers fall back to `--vt-accent-soft`.
- Hover shadow: `--vt-shadow-3` (real elevation replaces glow).
- `.btn--ghost`: border `--vt-border-input` (3.86:1 ✓), text `--vt-ink`, hover bg `--vt-milk` + `--vt-shadow-2`.
- `.btn--dark` **is renamed** `.btn--deep` (semantic: "deep peacock fill"): bg `--vt-accent-deep`, text `--vt-on-accent` (7.21:1). No component may be named "dark" in the light world.
- Active press scale .98 unchanged.

### 8.05 Link roll (inline links)
- Text `--vt-ink`; underline 1px `--vt-accent`; hover swaps to `--vt-accent-deep` text + `--vt-shadow-1` under the roll row.

### 8.06 Hero (`.hero`, `.hero__scrim`, `.hero__fallback`, `.hero__side-card`)
- Scrim (top fade over sky art): `--vf-canvas-a55` dark → `--vt-canvas-a78` **light veil** (fades hero sky art into header zone). A veil lightens; a scrim darkens — rename class to `.hero__veil` for semantic honesty.
- Hero sky SVG (see §10.1): dawn gradient — `#FDFCF8` (zenith) → `#F7F4EC` (mid) → `#F0E9D8` (horizon) + saffron radial glow `rgba(233,162,59,.28)` at horizon + sky band `rgba(157,184,217,.18)`; ridgelines in `#E2DBC8`/`#CFC6AE` (paper-cut hills, no more brown-black mountains); kite → peacock `#0F766E` with `--vt-shadow-2`; **stars are deleted** (dawn has no stars — and no AI-generated star fields).
- `.hero__side-card` ("NOW SHIPPING" glass card): `--vf-surface-1-a55` dark glass → `--vt-milk-a65` + blur(10px) + `--vt-shadow-3` + `--vt-inset-hi`; border `--vt-ink-a06`; mono meta `--vt-ink-3`; values `--vt-ink`; the pulse dot `--vt-ok` + `--vt-ok-a45` ring.
- Eyebrow kicker: `--vt-ink-3` + 32px peacock rule.

### 8.07 Availability chip
- Fill `--vt-ok-a12` on `--vt-wash-peacock` bg; border `--vt-ok-a45`; text `--vt-ok` (4.87:1); dot `--vt-ok-fill` with 1px `--vt-ink` ring (colour + geometry, never colour alone).

### 8.08 Case cards (`.case-card`, `--flagship`, `--secondary`)
- Card body: `--vt-surface-1` (milk) on porcelain canvas + `--vt-shadow-2`; hover: translateY(-4px) + `--vt-shadow-4` + border `--vt-ink-a12`. Real elevation replaces the dark vignette.
- Browser-chrome header dots (red/amber/green): keep the OS metaphor, re-tuned to `--vt-err` / `--vt-saffron` / `--vt-ok-fill` at 60 % size, on `--vt-surface-2` chrome bar.
- Outcome numerals: `--vt-ink`; unit and delta marks: `--vt-saffron` (≥ 24px size, paired with ink labels).
- Meta tags: `--vt-ink-3` on `--vt-surface-2` chips.
- **Flagship media:** screenshots/mockups sit directly on milk — they are now the brightest objects on the page (the entire point of the flip).
- Case-card SVG art (5 generated SVGs): re-generate per §10.2.

### 8.09 Journey (pinned scroll narrative, `.journey`)
- Track rail: `--vt-ink-a12` on porcelain; progress fill: `--vt-accent`.
- Stage panels: `--vt-surface-1` + `--vt-shadow-2`; rail fade `--vt-surface-1-a40` → `--vt-milk-a55`.
- Step index numerals: `--vt-saffron` at 2rem+ decorative scale (ink label alongside).
- The journey photograph (`vishvu-journey.webp`): re-grade warm-bright (see §10.4).

### 8.10 Marquee (capability ribbon)
- Band bg: `--vt-surface-2` (bone); items `--vt-ink-2`; separators `--vt-saffron` glyphs; edge fades: `--vt-bone-a86` masks. No dark vignettes.

### 8.11 Menu overlay (`.menu-overlay`)
- Floor: `--vt-canvas-a96` porcelain; panels: `--vt-bone-a86`; links `--vt-ink` with `--vt-ink-3` numerals; hover: `--vt-accent-deep` + `--vt-peacock-a12` wash row.
- Ambient radial (old champagne `--vf-champ-a09`): `--vt-saffron-a10` dawn glow **top-left only**, 480px, blur 80px — the menu "opens at dawn." This is a canvas wash (Law L4 atmosphere), not a component glow.
- Footer strip: `--vt-ink-3`, links underline `--vt-accent`.

### 8.12 Facts rail / stats band
- On `--vt-wash-saffron` band: numerals `--vt-ink` (10.62:1), suffixes `--vt-saffron`, rules `--vt-ink-a12`.

### 8.13 Maker grid / About visuals
- Panels: milk cards + `--vt-shadow-2`; tags `--vt-ink-3` on `--vt-surface-2`; portrait mat `--vt-surface-2` with `--vt-saffron-a14` top-edge accent.

### 8.14 Footer (`.footer-col`)
- Floor: `--vt-surface-2` bone (NOT dark); hairlines `--vt-ink-a06`; headings `--vt-ink`; links `--vt-ink-2` → hover `--vt-accent-deep`; ambient: `--vt-saffron-a10` corner wash; the "local time" mono block: `--vt-ink-3` with peacock time digits.

### 8.15 Custom cursor (`.cursor`)
- Ring: `--vt-ink-a55` (1.5px); dot: `--vt-accent`; label panel: `--vt-milk-a55` + `--vt-shadow-3` + `--vt-ink` text; "View" fill state: `--vt-ink-a92` fill + `--vt-on-accent`-class light text (**a 12px chip of ink fill is typographic-scale ink use, permitted under L2's letter — documented here explicitly**; alternative if owner prefers zero ink fills: peacock fill `--vt-accent` + `--vt-on-accent`).

### 8.16 Forms (`.contact` page, `form.js`)
- Inputs: bg `--vt-surface-1`; border `--vt-border-input` (3.86:1); text `--vt-ink`; placeholder `--vt-ink-3` (5.24:1 — placeholders at AA, better than the old 6.64-on-dark which is now moot).
- Focus: peacock 2px ring + `--vt-peacock-a08` halo + `--vt-shadow-1`.
- Invalid: border `--vt-err`, wash `--vt-err-a10`, message text `--vt-err` (5.18:1).
- Submit = primary button spec (8.04). Success state: `--vt-wash-peacock` panel + `--vt-ok` text.

### 8.17 Grain layer (`.grain-layer`)
- Opacity `.05` overlay → **`.035` and `mix-blend-mode: soft-light`** (overlay blend washes text edges on light fields). Grain on porcelain = paper texture — the tactile idea finally lands.

### 8.18 Scroll indicators, dividers, misc
- All `--vf-line`/`--vf-line-strong` usages map to `--vt-line`/`--vt-line-strong`; interactive hairlines to `--vt-border-input`.
- Any `rgba(37,26,17,…)` vignette: delete or replace with `--vt-ink-a06` hairline.

### 8.19 `.paper` island mechanism — role reversal
The old system escaped to cream islands on a dark sea. FIRST LIGHT inverts the relationship:
- `.paper` becomes **`.milk`** (the default raised-surface context — `--vt-surface-1`).
- The *former* island is now the continent; "wells" (`--vt-surface-2` bone) replace islands as the inset rhythm.
- All `.paper`-scoped token flips are re-specified in Appendix A's `.milk` block. (Mechanism unchanged; values and name change.)

---

## 9. PAGE-BY-PAGE SPECIFICATION

All pages share the porcelain floor, header, footer, menu, cursor, grain and progress hairline per §8. Page-specific notes:

### 9.1 Home (`index.html`)
1. **Hero:** dawn sky SVG (§10.1); headline ink; italic word "shipped." in `--vt-coral` (the one dawn-variant moment); lede `--vt-ink-2`; primary CTA peacock; secondary link-roll.
2. **Now-shipping card:** milk frosted glass (§8.06).
3. **Stats band:** saffron wash band (§8.12).
4. **Work scroller → case cards:** milk elevation (§8.08).
5. **Journey:** pinned narrative on porcelain with ink rail + peacock progress (§8.09).
6. **Marquee:** bone band (§8.10).
7. **CTA act:** saffron-wash panel, coral italic on one word, peacock button.

### 9.2 Work (`work/index.html` + 5 case pages)
- Index: case cards per §8.08; filter chips (if present) as bone chips with `--vt-border-input` borders and peacock active fill.
- **Case pages** (`case-insightloop`, `case-checkout`, `case-fieldops`, `case-clinicflow`, `essay-*` in v2-src): the old "paper ledger" island styling becomes the *native* language — milk body, bone wells, ink text, saffron kicker washes, peacock links/CTAs, chart primary `--vt-accent` with saffron highlight marks. Browser-chrome mockups re-tuned per §8.08.
- Outcome/proof numerals: ink + saffron suffixes everywhere.

### 9.3 Services (`services/index.html`)
- Six service blocks: alternating milk cards and saffron/sky wash bands; icons stroked `--vt-accent` 1.5px; "stack" chips on bone.
- Process steps: numbered in saffron decorative numerals + ink labels.

### 9.4 About (`about/index.html`)
- Portrait on bone mat with saffron edge accent; timeline rail ink-a12 with peacock nodes; pull-quotes `--vt-ink` with `--vt-sky-a12` rules.

### 9.5 Journal (`journal/index.html` + 4 essays)
- **The long-form win:** essay body `--vt-ink` at 1.05–1.2rem on porcelain, 68ch measure; drop caps in `--vt-accent-deep`; code blocks on `--vt-surface-2` with `--vt-ink` text (peacock strings, coral keywords — syntax palette documented in Appendix A); pull-quotes with sky rules; footnotes `--vt-ink-3`.
- Index cards: milk + shadow-2; reading-time chips bone.

### 9.6 Contact (`contact/index.html`)
- Form per §8.16 — the conversion page moves from worst substrate to best.
- Side info panel: `--vt-wash-sky` with ink text; email link peacock-deep; response-time chip `--vt-wash-peacock`/`--vt-ok`.

### 9.7 Legal (`privacy`, `terms`) & 404
- Legal: bone well pages, ink-2 body, ink-3 meta — document calm.
- 404: porcelain, giant display "404" in `--vt-ink` with saffron period; peacock button home.

---

## 10. ILLUSTRATION & ASSET REGENERATION (the hardcoded-hex purge)

The token swap covers CSS; these assets carry **hardcoded dark hexes** and must be regenerated. All live in `assets/img/**` and inline in HTML/`v2-src`.

### 10.1 Hero fallback SVG (`assets/img/generated/hero-fallback.svg`, inline copy in `index.html`, generator `v2-src/svgs.py`)
| Element | Old | New |
|---|---|---|
| Sky gradient | `#251A11 → #2D2114 → #4A330F` (dusk) | `#FDFCF8 → #F7F4EC → #F0E9D8` (dawn: milk → porcelain → bone) |
| Ember radial | `#DAC46D @ .5` | Saffron `#E9A23B @ .28`, horizon-anchored (cx .28, cy .92) |
| Aurora ribbon | `#81AFA9 @ .11` | Sky `#9DB8D9 @ .18`, single band, upper third |
| Ridgeline far | `#30241A` | `#E2DBC8` |
| Ridgeline near | `#251A11` | `#CFC6AE` |
| Stars (12 circles `#EDEAE2`) | present | **DELETED** (dawn has no stars) |
| Kite + glow | `#D3AB54 @ .9` glow | Peacock `#0F766E` solid + `--vt-shadow-2`-equivalent SVG soft shadow `rgba(18,63,59,.14)` |

### 10.2 Case art SVGs (`generated/case-*.svg` ×5, generator `v2-src/svgs.py`)
Same mapping: canvas espresso→porcelain, panel darks→milk/bone, ember chart lines→peacock, highlight marks→saffron, grid hairlines→`--vt-ink-a12`, mock text blocks→`--vt-ink-a12`/`--vt-ink-2`. Screenshot mockups inside render as *bright* surfaces.

### 10.3 OG images (12 JPGs, `assets/img/og/*.jpg`)
Regenerate from re-themed page renders at 1200×630 (script: extend `scripts/capture.sh`). Target: porcelain backgrounds, ink type, peacock accents. Size each ≤ 90 KB (progressive, q≈78). This is the only *heavy* asset work in the project (≈ half a day).

### 10.4 Journey photo (`assets/img/vishvu-journey.webp`)
Re-grade: +12 exposure, warm 5800K bias, lifted blacks floor at luminance ≥ 0.35 (no crushed darks — the photo must live in the dawn world too). Re-export WebP q80.

### 10.5 Icons & PWA
- `favicon.svg` glyph: champagne → `#0F766E` on `#F7F4EC` rounded square.
- `favicon.ico`, `apple-touch-icon.png`, `icon-32/192/512.png`: regenerate from the new SVG.
- `manifest.json`: `theme_color` → `#F7F4EC`, `background_color` → `#F7F4EC`.
- **Every page's `<meta name="theme-color" content="#251A11">` → `#F7F4EC`** (grep: 1 line per page × ~15 pages).
- Inline brand-glyph SVGs in every page header: `fill="#DAC46D"` → `fill="#0F766E"` (grep-clean).

### 10.6 Generator sources
`v2-src/svgs.py` + `v2-src/generate_assets.py`: update all palette constants to the FIRST LIGHT set; regenerate; diff output. `v2-src/palette.py`: mirror Appendix A exactly (Law C6).

---

## 11. MOTION & INTERACTION ADAPTATIONS

The motion system (GSAP + ScrollTrigger + Lenis + SplitText, stagger tokens, reveal system, reduced-motion fallbacks) is **unchanged in timing and choreography**. Colour-adjacent adaptations only:

1. **Shadows animate instead of glows:** card hovers interpolate `--vt-shadow-2 → --vt-shadow-4` (240ms, existing `--ease-out`) + translateY(-4px).
2. **Frosted header:** background transition now interpolates transparent → `--vt-canvas-a78`; keep `saturate(1.25)`.
3. **Split-text reveals:** masks unchanged; revealed glyphs now ink-on-porcelain — crisper at large display sizes.
4. **Cursor:** ring/dot colours per §8.15; label panel shadow per token.
5. **Menu overlay:** open animation unchanged; panel colours per §8.11.
6. **Preloader:** counter + glyph draw in peacock on porcelain; pulse dot `--vt-peacock-a35`.
7. **Journey pin:** progress fill peacock; rail ink.
8. **prefers-reduced-motion:** all existing fallbacks retained verbatim.

---

## 12. ACCESSIBILITY COMPLIANCE PLAN

| Requirement | Spec | Status under FIRST LIGHT |
|---|---|---|
| 1.4.3 Contrast (Minimum) AA | 4.5:1 text | Every text pair ≥ 4.84:1 (worst: ink-3 on bone) — **PASS with margin** |
| 1.4.6 Contrast (Enhanced) AAA | 7:1 | ink 10.62:1; ink-2 6.64–7.11:1 (body pairs AAA); accent-deep text 7.03:1 — **AAA on all primary reading pairs** |
| 1.4.11 Non-text Contrast | 3:1 UI | border-input 3.86:1; accent UI 4.98:1; focus ring peacock 4.98:1 — **PASS** |
| 2.4.7 Focus Visible | visible ring | 2px peacock + a08 halo, on porcelain — high salience — **PASS** |
| 1.4.1 Use of Colour | not colour-alone | Availability dot = colour + ring geometry + text label; chart marks = saffron + ink labels; invalid = border + wash + message — **PASS** |
| Halation control | avoid extreme 15:1+ on small text | Max text ratio 11.37:1 at display sizes only; body ink at 10.6:1 is inside the comfortable band — **PASS** |
| Daylight glare robustness | legibility at 60 % brightness mid-range LCD | Porcelain 0.967-luminance field survives ambient wash; verified in review |
| Cognitive load | evaluation fatigue | Light field + 8.19 wells for grouping — **improved vs old** |

CI: `scripts/contrast_audit.py` re-targeted to the §6.7 matrix; failure blocks deploy.

---

## 13. PERFORMANCE & ORACLE CLOUD FREE TIER ENGINEERING

Colour has zero runtime cost; the flip is engineered to *improve* the budget:

| Concern | Specification |
|---|---|
| Runtime JS/CSS delta | +0 KB frameworks. Token file same size (155-line `tokens.css` re-written 1:1). Net CSS delta ≈ +0.4 KB (elevation ladder lines) |
| Asset weight | 12 OG JPGs regenerated ≤ 90 KB each (same count, same budget); 6 SVGs re-generated ≈ same size; journey WebP re-grade ≈ same q80 budget |
| Fonts | Unchanged — 5 woff2, preloads intact (constraint C5) |
| Rendering | Grain at soft-light .035 is cheaper than overlay .05; glows retired (2 fewer blur layers); shadows use standard filter pipeline |
| Cache strategy | Cloudflare: CSS/SVG/OG get `cache-control: public, max-age=31536000, immutable` + filename version query (`?v=fl1`); HTML `max-age=300` + stale-while-revalidate |
| Deploy | `rsync -a --delete build/ /var/www/vishvutech/` + `cfpurge` (existing playbook, `deploy/oracle-setup.md` §4–6) — unchanged |
| Rollback | Keep `/var/www/vishvutech/releases/<ts>/`; symlink flip = instant revert (§16) |
| Budget gates (CI) | Lighthouse mobile: Perf ≥ 90, a11y = 100 (current baseline), CLS ≤ 0.02, LCP ≤ 1.8s on the free-tier origin + CF edge |
| Free-tier headroom | nginx + Node API unchanged; no new processes; static file count unchanged |

---

## 14. IMPLEMENTATION PLAN

### 14.0 Estimated effort

| Phase | Scope | Est. |
|---|---|---|
| 1 | Token core + base/components swap + local visual pass | 1.0 day |
| 2 | SVG/asset regeneration (hero, 5 case SVGs, favicon set, manifest, theme-colors, glyph grep) | 1.0 day |
| 3 | Page-level refinements (forms, case pages, essays, 404) + motion shadow passes | 1.5 days |
| 4 | OG image regeneration + CI (contrast audit retarget + banlist scanner) + QA + deploy | 1.5 days |
| — | Review buffer | 1.0 day |
| | **Total** | **≈ 6 working days, single engineer** |

### 14.1 Phase 1 — Token core (Day 1)

1. Branch `feature/first-light`.
2. Replace `assets/css/tokens.css` with Appendix A verbatim (rename prefix `--vf-` → `--vt-`; keep every non-colour token — type scale, spacing, radii, motion, z-index, layout — untouched).
3. Global find-replace in `base.css`, `components.css`, `pages.css`, all HTML, all `.tpl`: `var(--vf-` → `var(--vt-`.
4. Apply the §8 component edits that are not pure token swaps: 8.02 progress gradient, 8.03 header border, 8.04 ramp re-target + `.btn--dark`→`.btn--deep`, 8.06 veil rename + side card, 8.07 chip, 8.08 card shadows/hover, 8.11 menu ambient, 8.17 grain blend, 8.19 `.paper`→`.milk` rename (find-replace in all pages + partials).
5. Delete retired tokens: `--vf-halo-dot`, `--vf-halo-ok`, `--vf-gradient-ember` (replace usages), ember text/mark-paper pair (no dark paper contexts remain), aurora.
6. Serve locally (`python3 -m http.server`); walk every page at 360 / 768 / 1600 widths; screenshot diffs.

**Phase gate G1:** every page renders; zero `--vf-` references remain (`rg "var\(--vf-"` empty); no visual dark remnants except Phase-2 assets (hero SVG still old → Phase 2).

### 14.2 Phase 2 — Asset regeneration (Day 2)

1. Update `v2-src/palette.py` to mirror Appendix A exactly.
2. Update `v2-src/svgs.py` constants per §10.1/§10.2; regenerate `hero-fallback.svg` + 5 case SVGs; replace inline hero SVG in `index.html` (and `v2-src/pages/home.html`).
3. Delete the star field from the hero SVG (dawn has no stars).
4. Regenerate favicon set from new `favicon.svg` (peacock glyph on porcelain rounded square); update `manifest.json` colours.
5. Grep-and-replace across all HTML/tpl: `fill="#DAC46D"` → `fill="#0F766E"`; `theme-color" content="#251A11"` → `"#F7F4EC"`.
6. Re-grade `vishvu-journey.webp` per §10.4.

**Phase gate G2:** `rg -i "#(251A11|30241A|3A2D23|4A3D32|615246|DAC46D|D3AB54|E9E1B0|81AFA9)"` returns zero hits in `assets/`, `*.html`, `v2-src/`, `manifest.json`.

### 14.3 Phase 3 — Page-level refinement (Days 3–4)

1. Forms (§8.16): focus halo, invalid states, success panel.
2. Case pages + essays: `.milk`/well rhythm, chart colours, code-block syntax palette (Appendix A), drop caps, pull-quotes.
3. 404 + legal pages.
4. Motion shadow passes (§11.1): confirm hover interpolations feel "elevating," not "lighting."
5. Journey re-check with re-graded photo.

**Phase gate G3:** blind 5-second test on 5 people who have seen the old site: "does this feel like the same company, but premium?" Target: 5/5 yes.

### 14.4 Phase 4 — OG, CI, QA, deploy (Days 5–6)

1. Extend `scripts/capture.sh`: render 12 pages at 1200×630 → OG JPGs (≤ 90 KB each, progressive).
2. Re-target `scripts/contrast_audit.py` to the §6.7 matrix (pairs list included in Appendix B).
3. Add `scripts/banlist_scan.py` (Appendix C) to CI; wire into `check-colors.sh`.
4. Full QA checklist (§15).
5. Deploy per §16.

---

## 15. QA GATES & ACCEPTANCE CRITERIA

### 15.1 Automated gates (CI, blocking)

| Gate | Check | Tool |
|---|---|---|
| A1 | Zero forbidden hexes/rgba anywhere (§3.3 + rules 2–4) | `banlist_scan.py` |
| A2 | All 20 §6.7 contrast pairs ≥ requirement | `contrast_audit.py` |
| A3 | `tokens.css` ↔ `palette.py` mirror exact | diff check |
| A4 | Zero `--vf-` references | `rg "var\(--vf-"` empty |
| A5 | `theme-color` + manifest colours = porcelain | grep assertions |
| A6 | Lighthouse mobile: perf ≥ 90, a11y 100, CLS ≤ 0.02 | CI lighthouse run |

### 15.2 Pixel audit (the tribunal's own instrument, re-run)

Re-run the luminance audit on the deployed site:
- **Dark-pixel share (< 60 luminance) must fall from 92–99 % to < 8 % per page** (residual = ink text, shadows, chart strokes — all typographic/graphic scale, never fills).
- Dominant background colour must be `#F7F4EC` ± quantisation.

### 15.3 Human checklist (per page)

- [ ] First 5 seconds read as "senior, calm, expensive" (blind reviewer, no code)
- [ ] No component, panel, overlay, footer, illustration or image reads as black/brown/dark
- [ ] The single coral italic word per page rule holds (count ≤ 1)
- [ ] Saffron never appears as text
- [ ] Focus ring visible on every interactive element (keyboard walk)
- [ ] Hover states = elevation + hue, never glow
- [ ] Screenshots (case mockups) are the brightest objects on their cards
- [ ] Mobile 360px: no contrast inversions, no illegible chips
- [ ] Reduced-motion: everything readable statically
- [ ] Print preview (legal pages): clean porcelain document

### 15.4 Side-by-side acceptance (constraint C7)

Open the new home next to three 2025–26 light-field SOTD winners (e.g. Noho, House of Honey, iyO). The site must not read as "template" among them — distinct via: peacock signature hue, saffron/sky atmosphere, the dawn hero narrative, the journey scroll. Blind-panel vote ≥ 4/5.

---

## 16. ROLLOUT & ROLLBACK (Oracle free tier)

**Deploy (existing playbook, `deploy/oracle-setup.md`):**
1. Build locally; run gates A1–A6.
2. `rsync -a --delete build/ ubuntu@<vm>:/var/www/vishvutech/releases/fl1-$(date +%F)/`
3. Flip symlink: `ln -sfn /var/www/vishvutech/releases/fl1-$(date +%F) /var/www/vishvutech/current` (nginx root points at `current`; one `nginx -s reload` if needed — config unchanged).
4. Purge Cloudflare cache (API or dashboard); warm: `curl -s https://vishvutech.com/ >/dev/null` ×5 key URLs.
5. Verify: gates A1–A3 re-run against the live DOM (fetch HTML+CSS+SVG), pixel audit §15.2 re-run on live screenshots.

**Rollback (target < 60 seconds):**
- `ln -sfn /var/www/vishvutech/releases/<previous> /var/www/vishvutech/current` + purge. No database, no state, no migration — the safest possible class of change.

**Monitoring (first 7 days):**
- Cloudflare analytics: bounce rate on `/` and `/contact` vs prior 28-day baseline.
- Watch for user reports of "too bright" (unlikely) — mitigation: none needed; do NOT reintroduce dark shades (the mandate is absolute).
- Keep the old release directory 30 days, then archive.

---

## 17. SUCCESS METRICS

| Metric | Baseline (dark) | Target (90 days post-flip) |
|---|---|---|
| Tribunal colour-theme score | 4.2/10 | ≥ 8.0/10 on re-run |
| Dark-pixel share (avg all pages) | 95.5 % | < 8 % |
| Awwwards SOTD submission readiness | Not competitive | Submit; target Honourable Mention+ within 2 cycles |
| Contact-form start rate | baseline | +20 % (light-form B2B evidence, §4.4) |
| Avg. session duration on journal essays | baseline | +15 % (readability evidence) |
| "Screenshot-ability" (internal proxy: OG CTR) | baseline | +10 % CTR on shared links |
| Perceived-price survey ("rate the likely cost of this engineer's services, 1–5") | expected ~2.8 | ≥ 3.8 |

---

## 18. RISKS & MITIGATIONS

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Derived-alpha regressions (invisible borders when an rgba isn't updated) | Medium | Medium | §6.8 registry is exhaustive; A1 scanner bans unlisted rgba of dark bases; visual QA §15.3 |
| R2 | Old assets referenced from JS (`motion.js` reads tokens? none; `horizon.js` canvas colours — **check**: any JS-drawn canvas must be re-tinted) | Low | Medium | Grep `assets/js/**` for hex; audit in Phase 1 gate |
| R3 | Hero sky too flat without dark contrast | Medium | Low | Saffron horizon glow + sky band + paper-cut ridgelines provide structure; test at low brightness |
| R4 | "Too bright" fatigue for night owls | Low | Low | The mandate is absolute (no dark shades); optionally raise grain to .04 for tactile warmth. A dark mode is **out of scope and against the mandate** |
| R5 | Loss of the "premium gold" association current clients know | Low | Medium | Announce as "First Light" rebrand moment — a launch note in the journal turns the flip into a story, not a surprise |
| R6 | OG JPG regeneration bloat | Low | Low | 90 KB hard cap per image, progressive, verified in Phase 4 |
| R7 | P3 oklch accent drift | Low | Low | Same L/hue, chroma-only boost; verify on sRGB fallback first (§6.9) |

---

## 19. APPENDIX A — READY-TO-PASTE `assets/css/tokens.css`

```css
/* ============================================================
   VISHVU TECH — FIRST LIGHT · PORCELAIN DAWN (VT-PRD-004 §6)
   One source of truth (mirrored by v2-src/palette.py).
   Ten Laws of Light govern use (§6.1). Verified by
   scripts/contrast_audit.py · guarded by scripts/banlist_scan.py.
   Dawn is the fuel of the build. Porcelain is the calm of the ship.
   ============================================================ */

@property --peacock-l { syntax: '<number>'; inherits: false; initial-value: .511; }

:root {
  /* ---- Canvas & surfaces · The Porcelain Ladder (hue 88–95°, Law L0/L1) ---- */
  --vt-canvas:        #F7F4EC;  --vt-canvas-ok:        oklch(0.967 0.011 90);
  --vt-surface-1:     #FDFCF8;  --vt-surface-1-ok:     oklch(0.991 0.005 95);   /* milk · raised */
  --vt-surface-2:     #F0EBDF;  --vt-surface-2-ok:     oklch(0.941 0.017 88);   /* bone · inset wells, darkest neutral */
  --vt-wash-saffron:  #FDF3E3;  --vt-wash-saffron-ok:  oklch(0.960 0.030 85);   /* kicker bands */
  --vt-wash-sky:      #EEF3F9;  --vt-wash-sky-ok:      oklch(0.960 0.020 250);  /* atmosphere bands */
  --vt-wash-peacock:  #EAF2EF;  --vt-wash-peacock-ok:  oklch(0.955 0.015 180);  /* availability / success */
  --vt-line:          #E2DBC8;  --vt-line-ok:          oklch(0.892 0.027 90);   /* decorative hairlines */
  --vt-line-strong:   #CFC6AE;  --vt-line-strong-ok:   oklch(0.827 0.034 90);   /* structural hairlines */
  --vt-border-input:  #857A5F;  --vt-border-input-ok:  oklch(0.582 0.041 88);   /* WCAG 1.4.11 · 3.86:1 */

  /* ---- Ink · Peacock ladder (typographic only, Law L2 — never fills) ---- */
  --vt-ink:           #123F3B;  --vt-ink-ok:           oklch(0.336 0.049 187);  /* 10.62:1 AAA */
  --vt-ink-2:         #3E5C58;  --vt-ink-2-ok:         oklch(0.450 0.036 186);  /* 6.64:1 AA+ */
  --vt-ink-3:         #566A66;  --vt-ink-3-ok:         oklch(0.507 0.025 182);  /* 5.24:1 AA · min meta grade */

  /* ---- Accent · Peacock (the only interactive hue, 186°, Law L3) ---- */
  --vt-accent:              #0F766E;  --vt-accent-ok:              oklch(0.511 0.086 186);
  --vt-accent-soft:         #16837A;  --vt-accent-soft-ok:         oklch(0.551 0.092 186);   /* hover ramp target */
  --vt-accent-deep:         #0B5D57;  --vt-accent-deep-ok:         oklch(0.432 0.072 187);   /* accent as TEXT · 7.03:1 AAA */
  --vt-on-accent:           #F9F7F0;  --vt-on-accent-ok:           oklch(0.976 0.009 94);    /* text on peacock fills · 5.11:1 */

  /* ---- Reserve accents · Law L4 (sacred, rationed) ---- */
  --vt-coral:          #A83F28;  --vt-coral-ok:          oklch(0.510 0.143 34);   /* one italic word/page · 5.61:1 */
  --vt-saffron:        #E9A23B;  --vt-saffron-ok:        oklch(0.764 0.142 72);   /* marks/charts only — NEVER text */
  --vt-sky:            #9DB8D9;  --vt-sky-ok:            oklch(0.774 0.056 254);  /* atmosphere only */

  /* ---- Feedback · Signal (light-world tuned) ---- */
  --vt-ok:        #127A4E;  --vt-ok-ok:        oklch(0.528 0.106 158);  /* 4.87:1 */
  --vt-ok-fill:   #2FA36C;  --vt-ok-fill-ok:   oklch(0.660 0.140 158);  /* dots/icons, paired w/ ink ring */
  --vt-warn:      #96660E;  --vt-warn-ok:      oklch(0.548 0.111 75);   /* 4.55:1 · saffron icon pairing */
  --vt-err:       #B3402B;  --vt-err-ok:       oklch(0.529 0.154 33);   /* 5.18:1 */

  /* ---- Derived alphas (Law L9 — the complete registry, nothing else ships) ---- */
  --vt-canvas-a78:     rgba(247,244,236,.78);  /* header, resting frosted */
  --vt-canvas-a92:     rgba(247,244,236,.92);  /* header scrolled (no backdrop-filter fallback) */
  --vt-canvas-a96:     rgba(247,244,236,.96);  /* menu overlay floor */
  --vt-milk-a65:       rgba(253,252,248,.65);  /* hero side-card frosted glass */
  --vt-milk-a55:       rgba(253,252,248,.55);  /* cursor label panel */
  --vt-bone-a86:       rgba(240,235,223,.86);  /* menu panels · marquee fades */
  --vt-ink-a06:        rgba(18,63,59,.06);     /* hairlines on porcelain */
  --vt-ink-a12:        rgba(18,63,59,.12);     /* strong hairlines, rails */
  --vt-ink-a55:        rgba(18,63,59,.55);     /* cursor ring */
  --vt-ink-a92:        rgba(18,63,59,.92);     /* cursor view fill (typographic chip, §8.15) */
  --vt-peacock-a08:    rgba(15,118,110,.08);   /* focus halo wash */
  --vt-peacock-a12:    rgba(15,118,110,.12);   /* active row wash, chips */
  --vt-peacock-a35:    rgba(15,118,110,.35);   /* preloader pulse dot ONLY (Law L7) */
  --vt-saffron-a10:    rgba(233,162,59,.10);   /* menu/footer dawn ambient */
  --vt-saffron-a14:    rgba(233,162,59,.14);   /* kicker band over wash-saffron */
  --vt-sky-a12:        rgba(157,184,217,.12);  /* pull-quote rules, atmosphere */
  --vt-ok-a12:         rgba(18,122,78,.12);    /* availability chip fill */
  --vt-ok-a45:         rgba(18,122,78,.45);    /* availability dot ring */
  --vt-err-a10:        rgba(179,64,43,.10);    /* invalid field wash */
  --vt-shadow-ink:     rgba(18,63,59,.10);     /* base for elevation ladder */

  /* ---- Effects · light from above (Law L6/L7: shadows, never glows) ---- */
  --vt-gradient-accent: linear-gradient(90deg, #16837A 0%, #0F766E 100%);  /* progress hairline ONLY */
  --vt-pulse-dot:       0 0 10px rgba(15,118,110,.35);                      /* preloader dot ONLY */
  --vt-shadow-1:        0 1px 2px rgba(18,63,59,.05);
  --vt-shadow-2:        0 4px 12px rgba(18,63,59,.08);
  --vt-shadow-3:        0 12px 32px rgba(18,63,59,.10);
  --vt-shadow-4:        0 24px 48px rgba(18,63,59,.14);
  --vt-inset-hi:        inset 0 1px 0 rgba(255,255,255,.9);

  /* ---- Typography · Families (unchanged, constraint C5) ---- */
  --ff-display: 'Clash Display', 'Satoshi', system-ui, sans-serif;
  --ff-body: 'Satoshi', system-ui, -apple-system, sans-serif;
  --ff-serif: 'Instrument Serif', Georgia, serif;
  --ff-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', monospace;

  /* ---- Typography · Fluid scale (360 → 1440, unchanged) ---- */
  --fs-hero: clamp(3.1rem, 8.4vw + .8rem, 7.6rem);
  --fs-h2: clamp(2.2rem, 4.2vw + .9rem, 4.2rem);
  --fs-h3: clamp(1.45rem, 1.6vw + .9rem, 2.1rem);
  --fs-h4: 1.3rem;
  --fs-body: clamp(1.05rem, .25vw + .95rem, 1.2rem);
  --fs-small: .94rem;
  --fs-micro: .875rem;
  --fs-mono-label: .875rem;
  --lh-tight: .98;  --lh-snug: 1.15;  --lh-body: 1.65;
  --ls-tight: -.02em;  --ls-wide: .12em;

  /* ---- Space · 8-base scale (unchanged) ---- */
  --s-1: 4px;  --s-2: 8px;  --s-3: 16px; --s-4: 24px;
  --s-5: 32px; --s-6: 48px; --s-7: 64px; --s-8: 96px; --s-9: 128px;
  --gap: clamp(16px, 2vw, 32px);
  --pad-x: clamp(20px, 5vw, 64px);
  --maxw: 1320px;

  /* ---- Radii (unchanged) ---- */
  --r-sm: 8px;  --r-md: 14px;  --r-lg: 20px;  --r-pill: 999px;

  /* ---- Motion tokens (unchanged, mirrored in motion.js) ---- */
  --t-instant: 120ms;  --t-fast: 240ms;  --t-base: 420ms;
  --t-slow: 700ms;     --t-cinematic: 1200ms;
  --ease-out: cubic-bezier(.22, 1, .36, 1);
  --ease-out-expo: cubic-bezier(.16, 1, .3, 1);
  --ease-in-out: cubic-bezier(.65, 0, .35, 1);
  --ease-spring: cubic-bezier(.34, 1.56, .64, 1);
  --stagger-tight: 40ms;  --stagger-base: 80ms;  --stagger-editorial: 120ms;
  --rise: 24px;  --rise-lg: 48px;

  /* ---- Z-index registry (unchanged) ---- */
  --z-grain: 60;  --z-cursor: 90;  --z-menu: 80;  --z-header: 70;
  --z-preloader: 100;  --z-progress: 75;

  /* ---- Layout (unchanged) ---- */
  --header-h: 76px;
}

/* Wide-gamut displays: free chroma boost, same hue and lightness (§6.9) */
@media (color-gamut: p3) {
  :root { --vt-accent: oklch(0.511 0.104 186); }
}

/* ---- Milk contexts (the old .paper islands, now the continent, §8.19) ---- */
.milk {
  --vt-canvas:      var(--vt-surface-1);
  --vt-surface-2:   #E6E0D2;                       /* well-on-milk */
  --vt-line:        #E8E2D4;
  --vt-line-strong: #CFC6AE;
  color: var(--vt-ink);
  background: var(--vt-surface-1);
}
/* Accent tokens do NOT flip — peacock is verified on every light surface (§6.7). */

/* ---- Essay code-block syntax palette (Journal, §9.5) ---- */
.code-block { background: var(--vt-surface-2); color: var(--vt-ink); }
.code-block .tok-str  { color: var(--vt-accent-deep); }
.code-block .tok-kw   { color: var(--vt-coral); }
.code-block .tok-cm   { color: var(--vt-ink-3); }
.code-block .tok-num  { color: var(--vt-accent-deep); }
```

---

## 20. APPENDIX B — `contrast_audit.py` retarget pairs (paste-in list)

```python
PAIRS = [  # (fg, bg, minimum) — VT-PRD-004 §6.7 — all verified passing
    ("#123F3B", "#F7F4EC", 7.0), ("#123F3B", "#FDFCF8", 7.0), ("#123F3B", "#F0EBDF", 7.0),
    ("#123F3B", "#FDF3E3", 7.0),
    ("#3E5C58", "#F7F4EC", 4.5), ("#3E5C58", "#FDFCF8", 4.5),
    ("#566A66", "#F7F4EC", 4.5), ("#566A66", "#FDFCF8", 4.5), ("#566A66", "#F0EBDF", 4.5),
    ("#0B5D57", "#F7F4EC", 7.0), ("#0B5D57", "#FDFCF8", 7.0), ("#0B5D57", "#F0EBDF", 4.5),
    ("#0F766E", "#F7F4EC", 3.0),
    ("#F9F7F0", "#0F766E", 4.5), ("#F9F7F0", "#0B5D57", 4.5),
    ("#A83F28", "#F7F4EC", 4.5), ("#A83F28", "#FDFCF8", 4.5),
    ("#857A5F", "#F7F4EC", 3.0), ("#857A5F", "#F0EBDF", 3.0),
    ("#127A4E", "#F7F4EC", 4.5), ("#96660E", "#F7F4EC", 4.5), ("#B3402B", "#F7F4EC", 4.5),
    ("#16837A", "#F7F4EC", 3.0),
]
```

Reproducible engineering source (already used to generate §6.7): `scripts/first_light_palette.py` (WCAG relative-luminance + OKLCH conversion).

---

## 21. APPENDIX C — `banlist_scan.py` specification

```
INPUT : repo tree (css, html, svg, js, json, tpl)
RULE 1: forbidden hex set (§3.3) — case-insensitive, 3/4/6/8-digit
RULE 2: rgba(0,0,0,alpha>0.30)  — dark scrims/shadows die with the dark world
RULE 3: any colour with OKLCH L<0.32 AND C<0.030 used outside --vt-ink* tokens
RULE 4: theme-color / background_color manifest values must be porcelain
OUTPUT: one line per violation: file, line, matched value, rule
EXIT  : non-zero on any violation (deploy blocker)
```

Implementation notes: reuse the OKLCH conversion from `scripts/first_light_palette.py`; scan `v2-src/` too (generators must not re-emit dark art); whitelisted files: none. Zero whitelist by design — the Ban List has no exceptions.

---

## 22. APPENDIX D — RESEARCH CITATIONS (consulted during the tribunal's research phase)

1. Awwwards — Sites of the Day (current listings): awwwards.com/websites/sites_of_the_day — light-field winners incl. G. Colombel Portfolio 2026, A24, Brandon Yasin, ESR Bespoke, Emotion Agency, FORMAT, Cartier.
2. Awwwards — Pastel colors collection (curated by Mixallo, 1,419 items): awwwards.com/Mixallo/collections/pastel-colors — SOTD/HM winners Noho, House of Honey, iyO, Cleo AI, Yucca Packaging, Paris by Emily, Microsoft AI, MindMarket (SOTM).
3. Awwwards — Portfolio category: awwwards.com/websites/portfolio.
4. Dennis Snellenberg — freelance designer/developer portfolio & Awwwards juror: dennissnellenberg.com (light editorial reference; awwwards.com/dennissnellenberg).
5. ReallyGoodDesigns — "12 Beige Website Examples With Elegant Neutral Color Palettes": reallygooddesigns.com/beige-website-examples (Everlane, Acne Studios, The Row, Aesop, Toteme, MUJI, Jenni Kayne).
6. siiimple — Clean White & Minimal Website Designs (light portfolio catalogue incl. developer portfolios): siiimple.com/category/white-2.
7. Figma Resource Library — "Top Web Design Trends" (saturated colour returning, Y2K influence): figma.com/resource-library/web-design-trends.
8. Bespoke Software — "2026 Colours Trends For Website Design" (Pantone Cloud Dancer warm-white direction): bespokeuk.com.
9. W3C — Understanding WCAG 2.2 Success Criterion 1.4.3 Contrast (Minimum): w3.org/WAI/WCAG22/Understanding/contrast-minimum.html.
10. WebAIM — "Understanding WCAG 2 Contrast and Color Requirements" + Contrast Checker (AA 4.5:1 / AAA 7:1): webaim.org/articles/contrast.
11. Hook Agency — "101+ Website Color Schemes" & luxury colour guidance: hookagency.com/blog/website-color-schemes.
12. Davey & Krista — "17 Trending Color Palettes for Websites" (warm comforting colours direction): daveyandkrista.com.
13. Behance — "Design Trends 2025" (bold contrast, dark-blue/neon direction noted as the *counter-trend* to avoid): behance.net.
14. Owner's mandate & live measurements: session VT-CRITIQUE-100 (companion critique document); pixel measurements from locally deployed build, October 2026; palette mathematics from `scripts/first_light_palette.py`.

---

## 23. CHANGE LOG

| Version | Date | Change |
|---|---|---|
| VT-PRD-004 · 1.0 | October 2026 | First complete specification. Supersedes all prior colour-theme documents (void). Authored from the 100-judge tribunal research phase. 20/20 contrast pairs verified. |

*— End of VT-PRD-004 · FIRST LIGHT — Porcelain Dawn —*


