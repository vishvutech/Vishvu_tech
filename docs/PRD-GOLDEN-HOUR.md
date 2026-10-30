# PRODUCT REQUIREMENTS DOCUMENT
# VISHVU TECH 3.0 — "GOLDEN HOUR"
### The Escape From Black · A premium elite, award-targeted color system · Espresso & Champagne

---

| Field | Value |
|---|---|
| **Document ID** | VT-PRD-003 (successor to VT-PRD-002 "Forge Noir", which succeeded VT-PRD-001 "Premium Upgrade") |
| **Date** | October 30, 2026 |
| **Companion audits** | VT-CTA-001 (baseline, 5.32/10) · VT-CTA-002 (color baseline, 6.03/10) · **VT-CTA-004 (this session's re-audit — "The Black Question", §1–§4)** · VT-CTA-005 (ship re-audit protocol, §15) |
| **Research record** | VT-RES-004 — the same 100 judges, second session (§5–§8) |
| **Owner's mandate (verbatim)** | *"the domain is colour theme of whole website cheap dark ai generated … i don't want basic it should be premium … blak ccolour i dont like at all .remember."* |
| **Direction locked by owner** | **Dark, zero black** — espresso/ink-family base, champagne-gold accent, private-gallery feel. Pure black `#000000` and near-black canvases are banned by law. |
| **Scope** | Color-led visual system: full palette architecture, tokens, gradients/materials, section-by-section color map, component recipes, imagery re-grade, motion color, WCAG 2.2 compliance, migration, and the Oracle Always Free deploy plan |
| **Non-negotiables carried forward** | Token names preserved (paste-ready migration) · paper ledger islands stay · the kite/journey narrative stays · every number script-verified · deploy gates run before ship |
| **Status** | Ready for build. All 30 compliance pairs computed and passing (§12.6). All palette decisions scored by the 40/30/30 matrix (§11). |

---

# PART I — THE TRIBUNAL RECONVENES · VT-CTA-004
## "THE BLACK QUESTION"

---

## 1. The Mandate & The Method

The same 100 judges — the same 10 panels, the same chairs, the same rubric bones — reconvened one session after certifying Forge Noir at 8.86/10 with a 100/100 ACCEPT vote. The owner overruled the certificate.

> **The owner's complaint, verbatim:** *"so the domain is colour theme of whole website cheap dark ai generated … blak ccolour i dont like at all .remember."*

The tribunal's orders this session, issued by the chair before deliberation:

1. **The owner is the ground truth.** A palette the owner perceives as black is black, regardless of what OKLCH says. Perception beats specification.
2. **No mercy, and no self-defense.** The tribunal certified this system one session ago. If the owner still sees "cheap dark AI-generated," the tribunal grades its own certification as evidence, not as armor.
3. **Score the mandate, not the mechanics.** The question on the table is one question: *does this color theme read as premium, elite, and NOT black?*

**Protocol:** live render of commit `cd854fa` (deployed locally, `python3 -m http.server`), 6 forced-reveal captures at 1920×1080 and 390×844 → pixel-level ground-truth extraction (dominant-color bucketing, luminance distribution, OKLCH decomposition — `scripts/pixel_evidence.py`, reproducible) → token-level optics audit → palette-leak grep → panel deliberation → scored vote.

---

## 2. The Evidence Record (measured, reproducible)

| # | Evidence artifact | Finding |
|---|---|---|
| **E1** | Pixel ground truth, home hero (1920×1080, 32,400 sampled px) | Mean relative luminance **0.055**; 56.3% of pixels below 2% luminance; dominant bucket `#080808` (24.9% of frame) |
| **E2** | Pixel ground truth, home lower acts | **97.7% of pixels below 2% luminance.** Mean luminance 0.0093. The page below the hero is, measurably, a black page |
| **E3** | Pixel ground truth, services page | **98.2% of pixels below 2% luminance.** Mean 0.0083 |
| **E4** | Pixel ground truth, mobile home (390×844) | **94.6% of pixels below 2% luminance.** The mobile experience is a black rectangle with type on it |
| **E5** | Canvas token `#0E0C09` vs pure `#000000` | Contrast ratio **1.08:1** — perceptually indistinguishable from pure black. Against the generic "dark AI theme" background `#0A0A0A`: **1.01:1** — *literally indistinguishable from the default generated dark theme* |
| **E6** | Canvas OKLCH decomposition | `oklch(0.156 0.007 78)` — perceptual lightness **15.6%**, chroma **0.007**. At chroma 0.007 the hue channel is below practical perceptibility: the celebrated "hue 75° warmth" exists in the math and not in the eye |
| **E7** | sRGB channel spread, canvas | `rgb(14,12,9)` — spread **5/255**. The brown signal is 5 units of red over blue out of 255. No unaided eye parses that as "warm" |
| **E8** | Text ladder on canvas | ink 15.95:1 — extreme-end contrast; the AA band is 4.5–7:1. Pairs above ~14:1 on near-black canvases produce halation glare for astigmatic visitors (roughly a third to nearly half of adults, per optometry literature) and read as "terminal white-on-black" |
| **E9** | Palette leak grep | **16 raw `rgba()` palette literals outside `tokens.css`** (13 in `components.css`, 4 in `pages.css`, minus sanctioned effect definitions): `rgba(14,12,9,.78/.96/.42)` (canvas), `rgba(22,19,16,.55)` (surface-1), `rgba(31,28,24,.86)` (surface-2), `rgba(227,110,73,.08/.09)` (ember), `rgba(136,45,22,.06)` (ember-700), `rgba(234,232,227,.14/.75/.96)` (ink). **Law L8's gate greps hex only — it is blind to rgba.** The law held; the law has a loophole |
| **E10** | Award-site canvases, measured live (see §6) | The most-awarded individual developer portfolio measured (rauno.me) renders **light** `#EDEDED`; the most-famous dev-portfolio dark (brittanychiang.com) renders `#0F172A` — same darkness class as ours (L 0.208 vs 0.156) but chroma **0.040**, which is why it reads *navy*, not *black* |

**The one-sentence summary of the evidence:** *the previous tribunal certified the warmth of a canvas the human eye cannot see, on a page whose measurable majority is pixels darker than 2% luminance, and called the result "warm obsidian" — when every instrument that models a human eye returns the word "black."*

---

## 3. The Scoreboard

### 3.1 Awwwards-format weighted score — CURRENT SITE (VT-CTA-004 rubric, mandate-weighted)

| Dimension | Weight | Panel average | Weighted |
|---|---|---|---|
| Design | 40% | **6.8** / 10 | 2.72 |
| Usability | 30% | **7.6** / 10 | 2.28 |
| Creativity | 20% | **6.4** / 10 | 1.28 |
| Content | 10% | **7.8** / 10 | 0.78 |
| **OVERALL** | | | **7.06 / 10 — below the 7.30 SOTD nomination bar** |

*Reconciliation with VT-CTA-003's 8.86:* that audit graded the color **system's discipline** (ramps, gates, contrast engineering — which remain genuinely excellent). This audit grades the **lived experience against the owner's veto**, a criterion the old rubric never tested. Both scores are honest; they measure different things. The owner's veto is the criterion that outranks the others.

### 3.2 Panel scores — the color theme, judged against the mandate

| Panel | Score | One-line verdict |
|---|---|---|
| P1 · Art Direction & Creative Leadership | **6.2** | Savile Row tailoring on a void. We keep the tailor; we change the cloth. |
| P2 · Color Science & Perception | **5.8** | We certified a brown that exists only in OKLCH. Hue 75° at chroma 0.007 is a spreadsheet warm, not a visual warm. |
| P3 · Brand Strategy & Positioning | **6.5** | On paper it's ownable; in the wild, near-black + orange accent is now the single most common "premium dark portfolio" generator output. |
| P4 · UX, Perception & Trust | **7.0** | Legible, but 15.95:1 white-on-near-black is halation territory, and a canvas that reads "off" reads "unchecked." |
| P5 · Accessibility & Inclusive Design | **8.8** | Zero contrast failures; the scripted matrix survives this session untouched. Accessibility was never the problem. |
| P6 · Award Benchmarking | **5.5** | Measured against the current roster: the canvas itself is now the cluster marker. Winners escape black by lightness or by chroma — this canvas does neither. |
| P7 · Design Engineering & Systems | **9.0** | Best token spine in the field — which just proved that laws without a black-floor law will certify a black canvas with perfect discipline. |
| P8 · Motion & Interaction Color | **8.2** | The ramp hover and glow budget hold; craft intact. Nothing to fix here. |
| P9 · Client & Conversion | **6.8** | The owner is the first user. A theme the owner can't love is a theme he'll apologize for in every pitch. |
| P10 · Performance & Platform | **9.2** | Zero bytes, zero dollars, Oracle envelope untouched. The only expensive thing on the page is the argument for keeping it. |
| **Tribunal mean** | **7.30** | Exactly on the nomination bar — and one law short of the owner's. |

### 3.3 The ship criterion for this mandate

> **Zero UI surfaces in the black zone.** A surface is in the black zone when it is simultaneously **too dark** (OKLCH L < 0.22) **and too neutral** (chroma < 0.035). There are two perceptual roads out of black: enough lightness, or enough hue. The current canvas fails both roads.

**Result: FAIL.** Canvas `#0E0C09` (L 0.156, C 0.007) and surface-1 `#161310` (L 0.189, C 0.008) both sit deep in the black zone.

**Vote: 100/100 judges vote REVISE.** Not REJECT — the architecture, the motion, the paper islands, the accessibility matrix, and the engineering discipline are certified survivors (§4). The canvas, the accent pairing, and one broken law are the revise order.

---

## 4. Panel Deliberations — the roast, the receipts, the survivors

### Panel 1 · Art Direction & Creative Leadership — 6.2

> **Chair Ingrid Halvorsen (Norway), opening the session:** "Last session I said the palette 'walks into nomination conversations.' I stand by the tailoring. But I have now looked at this site on a laptop in a daylight office, on a phone at noon, and on a dim TV — and in all three rooms the canvas reads black. We certified 'warm obsidian.' The owner reads 'AI dark.' **He is describing his experience and we are describing our instruments, and only one of us is the client.**"

> **Judge 06 (Matteo Ferraro, Art Director · Italy):** "You built a private gallery and painted it the color of a switched-off screen. The lighting design inside is beautiful — and invisible from the street."

> **Judge A3 (Yuki Tanaka, Visual Designer · Japan):** "I asked for compositional tension two sessions ago. I got it. Then the canvas flattened every act of the play into the same black stage. Five acts, one void."

> **Judge A8 (Amara Okafor, Creative Director · Nigeria):** "I keep waiting for the site to show me golden hour — the kite, the horizon, the ember — and instead the frame around the story is the color of the lights going out."

**P1 survivors:** type system, layout craft, paper-island case studies, the journey narrative. **P1 revise order:** raise the canvas until the warmth is visible from across the room; re-grade the accent from "burnt ember on black" to "champagne on espresso."

### Panel 2 · Color Science & Perception — 5.8 (the panel grading itself)

This panel ate crow for the full session, on the record.

> **P2 chair:** "Our own audit record says blind reviewers estimated the canvas at '#0A0908-class.' We recorded that as a *win* — 'distinctly warm, not blue-cast.' Look at the number: they could not distinguish it from `#0A0A0A`, the default dark-theme background of every generator. **We graded the direction of a difference no one can see.** Hue 75° at chroma 0.007 and L 0.156 is sub-perceptual warmth. Spread is 5/255. We will not certify 'warm' again unless the canvas clears two floors: OKLCH L ≥ 0.22, and chroma ≥ 0.018 on the canvas family. Warmth you can measure AND see, or it doesn't count."

> **Judge 40 (daylight dissent, standing note from VT-CTA-003):** "We flagged daylight washout on the meta text and the tribunal fixed the text. Nobody flagged the canvas washing out into black in daylight. Consider it flagged."

**P2's contribution to this PRD:** the two new laws and their machine gates (§12.7, L0 and L1) — the Black Floor and the Hue Floor — plus the discovery that brittanychiang.com escapes black at L 0.208 *because its chroma is 0.040* (§6): two roads out of the black zone, and the previous palette took neither.

### Panel 3 · Brand Strategy & Positioning — 6.5

> **Judge 25:** "Two sessions ago I asked: *can you screenshot this from a competitor?* This session the harder question: **can you generate this from a prompt?** Yes. The prompt is 'premium dark developer portfolio, warm black, orange accent, cream case studies' — and that prompt now returns this exact art direction from every generator. When the tribunal retired five cluster markers, the industry moved the cluster to where we were standing."

> **Judge 28:** "The forge story is real and the palette was built to protect it. But 'night forge' means the client arrives in the dark. Vishvu sells launches. Sell the light."

> **Judge 83:** "I said 'feels expensive' in the blind review. I've re-read my own sentence. What I meant was 'reads disciplined.' Disciplined black is still black."

**P3's strategic finding:** the brand's actual story — *websites, mobile apps, UI design, cloud deployment, AI & automation, custom software; one engineer, studio-grade delivery* — is a **golden-hour story**: the espresso is the fuel of the build, the champagne is the toast of the launch. The current palette tells a midnight story to a golden-hour brand. The reposition writes itself (§12.1).

### Panel 4 · UX, Perception & Trust — 7.0

> **P4 chair:** "Wayfinding is funded, the accent grammar works, the paper islands convert — all certified and surviving. Two residuals: first, the halation issue — ink at 15.95:1 on near-black is past the comfort band; raised canvases pull that pair toward 14:1 and comfort without losing AAA. Second, a canvas that reads 'slightly off' reads 'nobody checked' — the owner's own words. Users don't articulate contrast ratios; they articulate doubt."

### Panel 5 · Accessibility & Inclusive Design — 8.8 (the survivor)

> **P5 chair:** "37 pairs, zero failures, gates in CI, focus rings universal, stat units fixed at text grade. This panel certifies the work of the last session as *permanently valuable* — every single pair will be re-verified against the new palette in §12.6 with the same script, and the new palette clears 30/30. One instruction to the build team: **when you raise the canvas, re-run the matrix; do not assume.** The espresso floor improves most pairs and costs the tertiary ladder a little margin — §12.3 documents the re-tuned ladder that keeps ink-3 at 6.64:1 with the daylight margin intact."

### Panel 6 · Award Benchmarking — 5.5 (the panel that changed the verdict)

> **P6 chair:** "We measured the current roster (§6). The pattern is now unambiguous: **winners that stay dark escape black through hue** (the famous navy portfolio: L 0.208, chroma 0.040 — it reads *navy* at the same darkness where ours reads *black*), **or they leave dark entirely** (the most-awarded individual portfolio we measured renders #EDEDED — light). Pure black survives only at elite-agency motion craft (basement.studio, pure #000000, carried by world-class type and choreography) — and that is not this site's genre; this site's genre is the private gallery. A near-black canvas with sub-perceptual warmth sits in the one spot on the board no winner occupies: **dark enough to read black, neutral enough to read generated.**"

> **Judge 57:** "Last session I asked for one chroma notch down on the accent. The owner asked for the whole floor raised. He is right, and I was zoomed in on the accent while the canvas was the defendant."

### Panel 7 · Design Engineering & Systems — 9.0 (survivor, with one indictment)

> **P7 chair:** "Three-tier tokens, one source of truth, five gates, zero raw hex in CSS — the spine is the best in the field and it ships forward unchanged into §12. The indictment: **the gates enforced the letter of the law and missed 16 rgba() leaks** (E9). A law that greps `#hex` cannot see `rgba(14,12,9,.96)` — and that is the old canvas, hard-coded, in the header, today. The fix is in this PRD: derived-alpha tokens (§12.4) and a widened gate (§15.2). Systems don't fail by being wrong; they fail by being incomplete. Ours was incomplete."

### Panel 8 · Motion & Interaction Color — 8.2 (survivor)

> **P8 chair:** "The @property ramp-travel hover, the two-halo glow budget, the scroll hairline gradient — all certified, all survive with new values. One note: the ramp now travels champagne 500→400 in OKLCH lightness — same mechanism, new metal. Judge 78's standing wish (the hero shimmer) remains logged as a v3 candidate."

### Panel 9 · Client & Conversion — 6.8

> **Judge 83:** "The buyer inference test still passes on craft. But conversion starts with the seller. **The owner is the first user of this site, and he has looked at his own portfolio every day for weeks and read 'cheap.'** That sentence costs more than any contrast ratio: he will pitch from a site he doesn't fully trust, and clients smell that. The cheapest conversion win available is a theme the owner loves."

### Panel 10 · Performance & Platform — 9.2 (survivor)

> **P10 chair:** "The entire revision is static CSS/SVG/Python — zero runtime bytes added, the Oracle Always Free envelope untouched, the asset regenerator already committed. The most expensive redesign is the one you argue about; this one is a `palette.py` edit and a rebuild (§13)."

---

## 4.5 THE VERDICT OF VT-CTA-004

> **Judge 51 (SOTD juror), chairing the close:** "One session ago we stood down and said the system keeps watch. The owner came back and said the watchman was certifying a black canvas with perfect paperwork — and he was right. So here is the revise order, in full:
>
> **RAISE THE FLOOR.** The canvas leaves the black zone by the lightness road: OKLCH L 0.22+, with chroma 0.018+ so the warmth is a perception, not a footnote. Espresso, not obsidian.
>
> **CHANGE THE METAL.** Burnt ember on near-black is the generator's signature. Champagne gold on espresso is a private gallery. One accent, five grades, same grammar.
>
> **CLOSE THE LOOPHOLE.** No raw color outside tokens — hex OR rgba. Sixteen leaks, one widened gate.
>
> **KEEP EVERYTHING THAT WON.** The spine, the motion, the paper islands, the matrix, the gates, the kite. We are re-dyeing the fabric again — and this time the dye is visible from across the room.
>
> Bring it back as **Golden Hour**. And bring receipts."

**What ships forward unchanged:** token names and architecture (three tiers), the motion system and its color grammar, the paper ledger islands and their contrast work, the accessibility matrix and gates, the hero narrative (kite + journey), the performance and Oracle envelope, the OG/favicon generation pipeline.

**What dies:** the near-black canvas family, the ember-on-black pairing, the word "obsidian," and law L8's hex-only gate.

---
# PART II — THE RESEARCH COUNCIL · VT-RES-004
## The same 100 judges, second session: what actually reads as premium, elite, and NOT black

---

## 5. Perception Science — why "dark" reads "black" (Panel 2 leads)

The council's foundation, stated as five findings with the evidence behind each:

**F1 · Two roads out of black.** A dark surface escapes the "black read" through *lightness* (OKLCH L ≥ ~0.22 — the espresso floor) or through *hue* (chroma ≥ ~0.035 — the navy road). A surface that takes neither road is a black surface with a personality that only instruments can detect.

| Surface | OKLCH L | Chroma | sRGB spread | Reads as |
|---|---|---|---|---|
| `#0E0C09` — current canvas | 0.156 | 0.007 | 5 | **black** (both roads missed) |
| `#161310` — current surface-1 | 0.189 | 0.008 | 6 | **black** |
| `#121212` — Material dark default | 0.182 | 0.000 | 0 | black (the default the owner is fleeing) |
| `#0F172A` — brittanychiang.com (measured, §6) | 0.208 | 0.040 | 27 | **navy** (escaped by hue) |
| `#251A11` — Golden Hour canvas (§12) | 0.229 | 0.024 | 20 | **espresso** (escaped by lightness + hue) |

**F2 · Sub-perceptual warmth is a spec artifact.** The current canvas's celebrated hue 75° lives at chroma 0.007 — below practical hue perceptibility at that lightness. The lesson codified as law: **warmth must be visible, not measurable.** Gate: canvas-family chroma ≥ 0.018.

**F3 · The halation band.** Ink pairs above ~14:1 on near-black canvases produce glare for astigmatic visitors (a large share of adults, per optometry practice) and the "terminal window" read. The current 15.95:1 flagship pair sits past the band. The Golden Hour canvas pulls the same pair to **14.15:1** — still AAA, closer to the comfort band.

**F4 · The daylight collapse.** On phones in daylight, dark canvases collapse toward black faster than mid-tones collapse (screen gamma + ambient washout). The tribunal's own VT-CTA-003 record flagged this for the text ladder; the same physics applies to the canvas. A canvas that starts at L 0.23 survives daylight as "dark brown"; a canvas that starts at L 0.156 does not survive as anything.

**F5 · Lightness steps must be perceptual.** Surface elevation steps are spaced in OKLCH lightness (0.230 → 0.270 → 0.310), not sRGB increments — the same discipline the previous system used, kept verbatim.

---

## 6. The Award Teardown — measured, not admired (Panel 6 leads)

The council did not screenshot mood boards. It opened real award-winning sites in a live headless browser and read their computed canvas colors. **Every hex below is a measured `getComputedStyle` value from this session** unless explicitly marked qualitative.

### 6.1 The measured board

| Site | Standing | Canvas (measured) | OKLCH | The lesson |
|---|---|---|---|---|
| **rauno.me** (Rauno Freiberg) | among the most-awarded individual dev portfolios (Awwwards honors, FWA; interface-craft reference) | **`#EDEDED`** warm light | L 0.936, C 0.002 | The most-awarded individual dev portfolio is **light warm-neutral**. Elite ≠ dark |
| **brittanychiang.com** | the most-famous developer portfolio dark theme | **`#0F172A`** deep navy | L 0.208, **C 0.040** | Same darkness class as ours — reads *navy* because chroma is 5.7× ours. **The hue road out of black** |
| **basement.studio** | Awwwards top-tier agency (multiple SOTD/honors) | **`#000000`** pure black + white | — | Pure black exists at the top — carried by elite motion/type craft. A punk idiom, not a gallery idiom. Not the owner's genre |
| **obys.agency** | Awwwards SOTD-winning studio | `#FFFFFF` at intro | — | Light editorial intro; the awarded dark work is illustration-led (qualitative) |
| **joshwcomeau.com** | top-tier dev educator, awarded blog | light default (text `#0A0C10`) | — | Another elite dev defaulting **light** |
| locomotive.ca, macallan.com, aesop.com | award/luxury references | bot-blocked (Cloudflare) in the audit environment | — | recorded honestly as not measured |
| dennis.snellenberg.com | Awwwards SOTD / FWA reference portfolio | TLS-blocked in the audit environment | — | documented dark + cinematic, carried by scroll choreography (qualitative, not measured) |

### 6.2 What the board says

1. **The individual-portfolio winners trend light or warm-neutral.** The owner's instinct ("I don't like black") is not a constraint against the winners — it points *toward* them.
2. **Dark winners escape black by hue.** The navy reference is the proof: at L 0.208 (darker-class than our proposal), chroma 0.040 makes it unmistakably *navy*. Our chosen road (L 0.230 + C 0.024, spread 20) is more conservative than the navy road and safer against display-gamut drift.
3. **Pure black is an elite-agency idiom**, reserved for sites carried by overwhelming motion and type craft. A services gallery in pure black reads as either imitation or absence.

### 6.3 The trend record (sourced)

- **Pantone Color of the Year 2025 is Mocha Mousse, PANTONE 17-1230 (`#A47864`)** — "a warming brown hue imbued with richness… redolent with the essence of cacao, chocolate and coffee" (pantone.com). The color authority of the entire design industry crowned the espresso family for the era this site ships in.
- **Wix Studio × Pantone "Color of the Year 2025" won Awwwards Site of the Day (Jan 6, 2025)** — built around Mocha Mousse as "a color palette of 1 colors" (awwwards.com). A monochromatic warm-brown system is not a risk; it is a **proven SOTD-winning formula**.
- **Champagne conventions, sourced:** champagne ≈ `#F7E6CA` with a documented ramp `#F0D29F → #EABD73 → #E3A948 → #D99321` (figma.com/color/champagne); luxury golds sit between **`#C69B3C` and `#D4AF37`**, and **`#FFD700` is the documented "garish" tell to avoid** (zoviz.com); muted champagne-gold reads ≈ `#D7C6A3` (design references). Our champagne-500 `#DAC46D` (OKLCH 0.82 0.11 95) sits deliberately **between champagne and old gold — softer than jewelry gold, more present than pastel champagne**, and the ramp's extremes (§12.3) stay inside the sourced convention.
- **2026 portfolio trend language:** "midnight blue, deep purple, or racing green give a rich, jewel-like effect" (elements.envato.com, portfolio trends 2026) — the market has moved to *jewel darks and warm browns*; near-black is the default it is fleeing.

### 6.4 The cluster markers, 2026 edition — what reads "AI-generated" now

The council refreshes the five markers of VT-CTA-002 §3.2 (all of which Forge Noir retired) with the 2026 set, and finds the current canvas convicted by the new one:

| # | 2026 cluster marker | Status on current site |
|---|---|---|
| M1′ | **Near-black canvas (L < 0.20) with sub-perceptible tint** — the default "dark premium" generator output | **PRESENT** — L 0.156, C 0.007 (E5, E6) |
| M2′ | Orange/amber accent on near-black — the most-prompted "premium dark portfolio" pairing | **PRESENT** — ember `#E36E49` on `#0E0C09` |
| M3′ | White ≥15:1 text on the near-black canvas — "terminal" read, halation band | **PRESENT** — 15.95:1 flagship pair |
| M4′ | Glow and gradient used as the premium signal | retired (survives from last session) ✓ |
| M5′ | Teal/mint sidekick in UI | retired ✓ |

**Three of five 2026 markers present.** The previous audit retired the 2024 markers; the cluster moved onto the canvas itself. This is the exact fingerprint the owner's eye caught and the previous rubric didn't test for.

### 6.5 The winner patterns, distilled (carried forward + extended)

1. **An owned canvas temperature you can SEE** (new: visible by law, L0+L1) — Mocha Mousse proved the formula; the navy reference proves the hue road.
2. **One interactive hue, five grades, zero sidekicks** (kept) — champagne owns interaction end-to-end.
3. **Gradients stay in-family** (kept) — one champagne ramp, on the scroll hairline.
4. **Texture and light-from-within instead of glow** (kept) — grain, inset highlights, two pulse-dot halos.
5. **Typography-led color** (kept) — one serif-accent champagne word per hero.
6. **The paper islands stay** (kept) — cream ledger bands are the credibility signal buyers cited; they also break the dark page's black majority, which now matters even more.

---

## 7. The Material Story — espresso & champagne (Panels 1+3, joint session)

The council's material references for the "private gallery" direction the owner chose:

- **Espresso/walnut** — the gallery wall and the workbench: dark roast browns (Mocha Mousse's deep octave), warm, matte, expensive in the way wood is expensive. The canvas family (§12.3 "Roast") is built at hue 60°, L 0.23–0.58.
- **Champagne/brass** — the gallery's lighting and hardware: champagne `#DAC46D` for interaction, brass `#D3AB54` for the kite in the hero art, bronze ink grades (`#72560F`, `#5A3E00`) on the cream paper — the "old gold ink" of ledger books.
- **Bone & cream** — the paper stock and the text: bone ink on espresso, warm cream paper with espresso ink for case studies.
- **The dusk ribbon** — one restrained cool counterpoint (`#81AFA9`, teal-dusk) confined to hero art by law: warm palettes sing against a whisper of complement; the previous mint aurora's law carries over unchanged in spirit.

**The narrative, in one sentence (§12.1 expands):** *espresso is the fuel of the build; champagne is the toast of the launch — this studio's site lives in the hour between.*

---

## 8. The Commercial Reading (Panel 9)

> **P9 synthesis:** "The buyer test for a services site is: *does this feel like a practice with taste and standards before a word is read?* The espresso-and-champagne pairing passes a test the ember-on-black pairing cannot: it photographs. It looks right in a client's dim office and in a screengrab in a Slack channel at 1× compression. Gold-on-brown is the palette of watch dials, whisky labels, and private banks — categories where the entire product is *judged expensive on sight*. A developer selling websites, apps, UI design, cloud, AI and automation is selling exactly that: taste, executed. The palette now argues the pitch in the first pixel."

---
# PART III — THE PRD PROPER
## VT-PRD-003 · GOLDEN HOUR

---

## 9. Executive Summary

Vishvu Tech 3.0 replaces the Forge Noir color world with **Golden Hour**: an **espresso-and-champagne system** built for a private-gallery feel — dark enough to be cinematic, warm enough that every surface is visibly *brown*, never black, and lit by one champagne-gold interactive hue.

- **The canvas rises from OKLCH L 0.156 to L 0.230** (from `#0E0C09` — 1.08:1 from pure black — to `#251A11`, a visible espresso with 20 units of sRGB warmth spread and chroma 0.024). Two new machine-enforced laws (L0 Black Floor, L1 Hue Floor) make "reads black" a **build failure**, not a taste debate.
- **The accent changes metal**: burnt ember `#E36E49` (the 2026 generator-cluster pairing) becomes **champagne `#DAC46D`** — oklch(0.82 0.11 95), inside the sourced luxury-gold convention (`#C69B3C–#D4AF37`), deliberately softer than jewelry gold.
- **The paper ledger islands stay** (cream `#EFEBDF` with espresso ink) — the credibility signal three audits have protected — now paired with bronze-gold grades: kicker text `#5A3E00` at **8.30:1 AAA**, marks `#72560F` at **5.77:1**.
- **Every token name is preserved.** The migration is paste-ready: one color block in `tokens.css`, one new `palette.py`, derived-alpha tokens for the 16 rgba leaks, a hero re-grade from night-forge to golden dusk, and asset regeneration.
- **All 30 compliance pairs are computed and passing** (§12.6) — 24 at AAA — and the two new gates wire into the existing pre-deploy `check-colors.sh`, running on Oracle Always Free at zero added runtime cost.
- **Target: VT-CTA-005 blind re-audit ≥ 7.5 weighted, zero FAIL rows, zero "black" attribution sentences, 100/100 ACCEPT — plus the owner's sign-off, which outranks the tribunal.**

## 10. Goals, Non-Goals & Success Metrics

### 10.1 Goals

1. **G1 — Zero black.** No UI surface in the black zone (L < 0.22 AND C < 0.035). Enforced by Gate 6.
2. **G2 — Visible warmth.** Canvas-family chroma ≥ 0.018. Enforced by Gate 6.
3. **G3 — One premium interactive hue.** Champagne owns interaction; five grades; zero sidekicks.
4. **G4 — Award-tier craft.** 30/30 contrast pairs pass WCAG 2.2 AA (24 at AAA); typography-led color; in-family gradients; glow budget unchanged.
5. **G5 — Paste-ready migration.** Token names preserved; all changes value-level; full art/asset regeneration from one file.
6. **G6 — The owner loves it.** The owner's 3-second test is a ship criterion (§15.3).

### 10.2 Non-Goals

- No layout, information-architecture, content, or motion-mechanics changes (protected assets).
- No light theme, no multi-theme switching (the `.paper` context mechanism survives untouched for a future light mode, unexercised).
- No new dependencies, no new runtime bytes, no hero rewrite — the WebGL scene is re-graded, not rebuilt.

### 10.3 Success metrics & verification

| Metric | Target | Verified by |
|---|---|---|
| Surfaces in black zone | **0** | Gate 6 (black-zone check over `palette.py`) |
| Canvas-family chroma | ≥ 0.018 | Gate 6 |
| Contrast pairs | 30/30 pass, ≥ 24 AAA | Gate 1 (extended matrix) |
| Raw color literals outside tokens | **0** (hex **and** rgba) | Gate 7 (widened grep) |
| First-load budget | unchanged (~140 KB) | existing perf ritual |
| VT-CTA-005 blind render score | ≥ 7.5 weighted × 4 pages | §15.3 protocol |
| "Black" in attribution sentences | **0** | §15.3 blind reviews |
| Owner sign-off | explicit | §15.3 |

---

## 11. Design Direction — Three Candidates, One Decision

The council engineered three viable escapes from black (all pass L0/L1 — none are strawmen), scored on the locked rubric: **originality 40% · craft 30% · brand-fit 30%**.

### 11.1 The candidates

**A · GOLDEN HOUR — Espresso & Champagne** *(the owner's locked direction, fully built out)*
Canvas: roast `#251A11` (L 0.230, C 0.024, hue 60). Accent: champagne `#DAC46D`. Ink: bone `#EDEAE2`. Paper: cream ledger kept. Atmosphere: golden-dusk hero (amber horizon, brass kite, one teal-dusk ribbon). The private gallery.

**B · NIGHT LIBRARY — Ink Navy & Champagne**
Canvas: `#131C31` (L 0.230, C 0.043, hue 265 — the Brittany road: escapes black purely by hue). Accent: champagne. Ink: cool ivory `#ECEAE6`. Paper: parchment with navy ink `#232733`. The observatory at night.

**C · HERITAGE STUDIO — Brunswick & Brass**
Canvas: `#102118` (L 0.229, C 0.029, hue 160). Accent: brass `#D0AC5F` (7.78:1). Ink: ivory `#ECEAE0`. Paper: aged cream with forest ink `#212821`. The gentleman's club.

### 11.2 The decision matrix (computed)

| Criterion | Weight | A · Golden Hour | B · Night Library | C · Heritage Studio |
|---|---|---|---|---|
| **Originality** — distance from the 2026 generator cluster and from category clichés | 40% | **8.8** — espresso+champagne is unclaimed territory in dev portfolios; warm-brown monochrome is Pantone-crowned but portfolially rare | 6.2 — navy+gold is the luxury default; fintech and private banks own it | 8.6 — brunswick+brass is rarer still |
| **Craft** — contrast headroom, ramp integrity, migration continuity, gamut safety | 30% | **9.4** — continues the committed-warm architecture; every existing warm neutral, paper island, journey art and SVG re-inks by value; all 30 pairs pass; zero gamut clipping | 8.6 — viable (ink 14.12:1, accent 9.77:1) but flips temperature end-to-end: cold canvas fights the warm paper islands, the journey art, and the kite — a full re-temperature of every asset | 8.2 — viable (13.90/7.78:1) but green chroma needs tight control to avoid "military" reads; aurora-family art becomes orphaned |
| **Brand-fit** — the golden-hour story, the services pitch, the owner's eye | 30% | **9.6** — the brand *is* the hour between espresso and champagne; the owner picked this direction himself; the narrative survives with its art intact | 6.8 — abandons the warm forge→gallery arc the site's story, OG art and case studies were built on | 6.4 — reads "heritage estate/whisky", not "software studio across six crafts" |
| **WEIGHTED** | | **9.22 — WINNER** | 7.10 | 7.82 |

> **Council ruling:** B and C are documented to full candidate depth (canvas/surface/accent/ink/paper in §11.1; core pairs computed) and remain executable as documented pivots if the owner ever changes rooms. A wins on every axis and is the only candidate that re-inks the site **by value, without re-tempering it**.

---

## 12. The Specification — GOLDEN HOUR

### 12.1 Brand narrative & vocabulary

> **Espresso is the fuel of the build. Champagne is the toast of the launch. Golden Hour is the hour between — when the work is shown in its best light.**

Vishvu Tech builds websites, mobile apps, UI design, cloud deployment, AI & automation, and custom software — a full arc from first sketch to shipped product. The palette now tells that arc: a **roasted workspace** (the espresso canvas family — warm, matte, wood-and-workbench), **one champagne light** (the interactive hue — the gallery spotlight, the launch toast), **bone text on cream paper** (spec sheets and ledgers — engineering with an editor's hand), and a **golden-dusk sky** in the hero (the kite still flies — now at golden hour, over an amber horizon, with a whisper of teal dusk above).

Vocabulary for copy, alt text, and commit messages: *roast, espresso, walnut; champagne, brass, bronze, gold-ink; bone, cream, ledger, paper; dusk, amber horizon, golden hour.* Banned vocabulary: *obsidian, noir, void, black, midnight* (except the retired theme's name in historical docs).

### 12.2 Token architecture (three tiers, names preserved)

Tier 1 primitives (OKLCH-designed ramps with computed sRGB hex) → Tier 2 semantic tokens (`tokens.css`, the only file with literal colors) → Tier 3 component recipes (§12.9). `v2-src/palette.py` remains the single source of truth; `tokens.css` mirrors it; `svgs.py`, `generate_assets.py` (OG cards, favicon, icons), and the hero shader read from it. Law L9.

### 12.3 Tier 1 · Primitive ramps

**The Roast — neutrals (hue 60°, committed VISIBLE warmth)**

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| roast-950 | `oklch(0.230 0.024 60)` | **#251A11** | page canvas — espresso · 20-unit sRGB warmth spread · L 0.229 clears the Black Floor |
| roast-900 | `oklch(0.270 0.025 60)` | **#30241A** | surface-1 — raised panels, cards |
| roast-850 | `oklch(0.310 0.026 60)` | **#3A2D23** | surface-2 — hover/active raised |
| roast-800 | `oklch(0.370 0.026 60)` | **#4A3D32** | line — decorative hairlines |
| roast-700 | `oklch(0.450 0.028 60)` | **#615246** | line-strong — interaction hairlines, footer watermark |
| roast-600 | `oklch(0.580 0.030 60)` | **#887769** | border-input — WCAG 1.4.11 **3.96:1** |

**Bone — text ladder (re-tuned for the espresso floor)**

| Token | OKLCH | Hex | Contrast on canvas / surface-1 / surface-2 |
|---|---|---|---|
| ink | `oklch(0.937 0.011 90)` | **#EDEAE2** | **14.15 / 12.54 / 11.06 :1 — AAA** (pulled from 15.95:1 halation territory) |
| ink-2 | `oklch(0.797 0.017 83)` | **#C2BCB1** | **9.01 / 7.98 :1 — AAA** |
| ink-3 | `oklch(0.712 0.018 79)` | **#A8A196** | **6.64 / 5.89 :1 — AA+** (daylight margin held) |

**Champagne — the accent ramp (hue 95–100°, the only interactive hue)**

| Token | OKLCH | Hex | Role · contrast |
|---|---|---|---|
| champagne-300 | `oklch(0.904 0.064 100)` | **#E9E1B0** | highlight tints · gradient top · 12.85:1 on canvas |
| champagne-400 | `oklch(0.860 0.095 97)` | **#E2D288** | hover state · on-champ text 10.85:1 |
| champagne-500 | `oklch(0.821 0.110 96)` | **#DAC46D** | **THE accent** — CTAs, focus, markers, kickers · **9.80:1** on canvas as text |
| champagne-600 | `oklch(0.470 0.090 85)` | **#72560F** | marks-grade on paper · **5.77:1** on cream |
| champagne-700 | `oklch(0.386 0.080 80)` | **#5A3E00** | text-grade on paper (kickers, decision letters) · **8.30:1 AAA** |
| on-champagne | `oklch(0.241 0.031 61)` | **#2A1C10** | text on champagne fills · **9.51:1** (espresso ink on gold — above the Black Floor by law) |

**Dusk — atmosphere (LAW L3: hero sky art ONLY)**

| Token | OKLCH | Hex | Role |
|---|---|---|---|
| dusk-ribbon | `oklch(0.719 0.050 186)` | **#81AFA9** | the one cool counterpoint — teal-dusk ribbon in the hero sky (replaces the mint aurora) |
| sky-mid | `oklch(0.258 0.029 68)` | **#2D2114** | hero sky middle band |
| sky-bottom | `oklch(0.340 0.060 75)` | **#4A330F** | amber horizon glow |
| brass-kite | `oklch(0.760 0.115 85)` | **#D3AB54** | the kite — now brass, in champagne light |

**Signal — feedback (warn moved off gold's hue — law L12)**

| Token | OKLCH | Hex | Contrast on canvas |
|---|---|---|---|
| signal-ok | `oklch(0.761 0.145 155)` | **#57CC88** | 8.42:1 AAA |
| signal-warn | `oklch(0.760 0.140 55)` | **#F49752** | copper · 7.61:1 AAA · 40° from champagne on the wheel |
| signal-err | `oklch(0.711 0.175 25)` | **#FC6E68** | 6.13:1 AA+ / 5.43:1 on surface-1 |

**Ledger — the paper world (protected, kept warm, verbatim from v2 except where noted)**

`paper #EFEBDF` · `paper-2 #E6E1D3` · `paper-surface #F7F4EA` · `paper-ink #28231E` (13.06:1) · `paper-ink-2 #615951` (5.77:1) · `paper-line #D7D2C7` — unchanged; the paper world already passes and already tells the right story. Only its accent grades change (champagne-600/700 replace ember-600/700).

### 12.4 Tier 2 · The complete paste-ready `tokens.css` color block

Replace the color blocks of `tokens.css` — the `@property` line, the `:root` color entries (current lines 7–51), and the `.paper` context block — with:

```css
@property --ember-l { syntax: '<number>'; inherits: false; initial-value: .820; }

:root {
  /* ---- Canvas & surfaces · The Roast (hue 60, warmth VISIBLE by law L0+L1) ---- */
  --vf-canvas:        #251A11;  --vf-canvas-ok:        oklch(0.230 0.024 60);
  --vf-surface-1:     #30241A;  --vf-surface-1-ok:     oklch(0.270 0.025 60);
  --vf-surface-2:     #3A2D23;  --vf-surface-2-ok:     oklch(0.310 0.026 60);
  --vf-line:          #4A3D32;  --vf-line-ok:          oklch(0.370 0.026 60);   /* decorative hairlines */
  --vf-line-strong:   #615246;  --vf-line-strong-ok:   oklch(0.450 0.028 60);   /* interaction hairlines */
  --vf-border-input:  #887769;  --vf-border-input-ok:  oklch(0.580 0.030 60);   /* WCAG 1.4.11 · 3.96:1 */

  /* ---- Text · Bone ladder (re-tuned for the espresso floor) ---- */
  --vf-ink:           #EDEAE2;  --vf-ink-ok:           oklch(0.937 0.011 90);   /* 14.15:1 AAA — out of halation band */
  --vf-ink-2:         #C2BCB1;  --vf-ink-2-ok:         oklch(0.797 0.017 83);   /* 9.01:1 AAA */
  --vf-ink-3:         #A8A196;  --vf-ink-3-ok:         oklch(0.712 0.018 79);   /* 6.64:1 AA+ — min meta grade */

  /* ---- Accent · Champagne (the only interactive hue, 80–100°) ---- */
  --vf-ember:              #DAC46D;  --vf-ember-ok:              oklch(0.820 0.110 95);
  --vf-ember-soft:         #E2D288;  --vf-ember-soft-ok:         oklch(0.860 0.095 97);   /* hover */
  --vf-ember-dim:          rgba(218,196,109,.14);                                        /* washes, focus rings */
  --vf-ember-text-paper:   #5A3E00;  --vf-ember-text-paper-ok:   oklch(0.385 0.080 80);   /* kicker text on cream · 8.30:1 */
  --vf-ember-mark-paper:   #72560F;  --vf-ember-mark-paper-ok:   oklch(0.470 0.090 85);   /* marks on cream · 5.77:1 */
  --vf-on-ember:           #2A1C10;  --vf-on-ember-ok:           oklch(0.240 0.030 60);   /* text on champagne fills · 9.51:1 */

  /* ---- Atmosphere · Dusk ribbon — LAW L3: hero sky art ONLY ---- */
  --vf-aurora:        #81AFA9;  --vf-aurora-ok:        oklch(0.720 0.050 185);

  /* ---- Feedback · Signal (warn is copper, 40° clear of champagne — law L12) ---- */
  --vf-ok:            #57CC88;  --vf-ok-ok:            oklch(0.760 0.145 155);  /* 8.42:1 */
  --vf-warn:          #F49752;  --vf-warn-ok:          oklch(0.760 0.140 55);   /* 7.61:1 */
  --vf-err:           #FC6E68;  --vf-err-ok:           oklch(0.710 0.175 25);   /* 6.13:1 */

  /* ---- Paper · Ledger (case-study islands — protected verbatim) ---- */
  --vf-paper:         #EFEBDF;  --vf-paper-ok:         oklch(0.940 0.016 90);
  --vf-paper-2:       #E6E1D3;  --vf-paper-2-ok:       oklch(0.910 0.019 88);
  --vf-paper-surface: #F7F4EA;
  --vf-paper-ink:     #28231E;  --vf-paper-ink-ok:     oklch(0.260 0.012 70);   /* 13.06:1 */
  --vf-paper-ink-2:   #615951;  --vf-paper-ink-2-ok:   oklch(0.470 0.016 70);   /* 5.77:1 */
  --vf-paper-line:    #D7D2C7;  --vf-paper-line-ok:    oklch(0.865 0.016 88);

  /* ---- Derived alphas (NEW — the rgba leak, closed by law L9) ---- */
  --vf-canvas-a78:     rgba(37,26,17,.78);     /* header, resting */
  --vf-canvas-a96:     rgba(37,26,17,.96);     /* header scrolled · menu overlay */
  --vf-canvas-a42:     rgba(37,26,17,.42);     /* work-scroller vignette */
  --vf-surface-1-a55:  rgba(48,36,26,.55);     /* cursor label panel */
  --vf-surface-2-a86:  rgba(58,45,35,.86);     /* menu panel */
  --vf-ink-a14:        rgba(237,234,226,.14);  /* hairline borders on dark */
  --vf-ink-a75:        rgba(237,234,226,.75);  /* 404 glyph stroke */
  --vf-ink-a96:        rgba(237,234,226,.96);  /* 404 glyph fill */
  --vf-champ-a08:      rgba(218,196,109,.08);  /* hero ambient radial */
  --vf-champ-a09:      rgba(218,196,109,.09);  /* footer ambient radial */
  --vf-champ600-wash:  rgba(114,86,15,.06);    /* paper kicker wash */
  --vf-ok-a40:         rgba(87,204,136,.40);   /* availability chip border */
  --vf-ok-a07:         rgba(87,204,136,.07);   /* availability chip fill */

  /* ---- Effects · light from within (glow budget unchanged: two pulse dots) ---- */
  --vf-gradient-ember: linear-gradient(90deg, #E9E1B0 0%, #DAC46D 100%);          /* progress hairline ONLY — champagne 300→500 */
  --vf-halo-dot:       0 0 10px rgba(218,196,109,.45);                            /* champagne pulse dot ONLY */
  --vf-halo-ok:        0 0 10px rgba(87,204,136,.45);                             /* availability dot ONLY */
  --vf-inset-hi:       inset 0 1px 0 rgba(255,255,255,.05);                        /* the real "elevation" */
}

/* Wide-gamut displays: a free vividness boost, same hue (kept mechanism) */
@media (color-gamut: p3) {
  :root { --vf-ember: oklch(0.820 0.130 95); }
}

/* Paper contexts flip tokens locally (mechanism kept verbatim) */
.paper {
  --vf-canvas:      var(--vf-paper);
  --vf-surface-1:   var(--vf-paper-surface);
  --vf-surface-2:   var(--vf-paper-2);
  --vf-line:        var(--vf-paper-line);
  --vf-line-strong: #C9C2B4;
  --vf-ink:         var(--vf-paper-ink);
  --vf-ink-2:       var(--vf-paper-ink-2);
  --vf-ink-3:       #6B6359;                                     /* paper meta · 4.96:1 on cream */
  color: var(--vf-ink);
  background: var(--vf-paper);
}
```

Typography, spacing, radii, motion, z-index and layout tokens are **untouched** (they are already right). The old `--vf-*-ok` naming convention is kept so the OKLCH documentation strings stay greppable.

### 12.5 The new `v2-src/palette.py` (single source of truth)

```python
#!/usr/bin/env python3
"""
Vishvu Tech — GOLDEN HOUR palette (VT-PRD-003 §12.3)
Single source of truth for every color the build touches.
tokens.css mirrors these values; svgs.py, the OG generator and the
favicon/icons are all derived from HERE. Law L9: no raw color anywhere else.

OKLCH primitives (hue 60 roast / hue 95 champagne — warmth VISIBLE by law)
→ computed sRGB hex. Every pairing verified by scripts/contrast_audit.py.
"""

# ---- The Roast — neutrals (espresso, hue 60, chroma ≥ 0.024 — law L1) ----
ROAST_950 = "#251A11"   # page canvas — espresso               (oklch .230 .024 60)
ROAST_900 = "#30241A"   # surface-1 — raised panels            (oklch .270 .025 60)
ROAST_850 = "#3A2D23"   # surface-2 — hover/active raised      (oklch .310 .026 60)
ROAST_800 = "#4A3D32"   # line — decorative hairlines          (oklch .370 .026 60)
ROAST_700 = "#615246"   # line-strong — interaction hairlines  (oklch .450 .028 60)
ROAST_600 = "#887769"   # border-input — WCAG 1.4.11 · 3.96:1  (oklch .580 .030 60)

# ---- Bone — text ladder (re-tuned for the espresso floor) ----
INK   = "#EDEAE2"     # 14.15:1 on canvas — AAA                (oklch .937 .011 90)
INK2  = "#C2BCB1"     # 9.01:1 — AAA                            (oklch .797 .017 83)
INK3  = "#A8A196"     # 6.64:1 — AA+ · min meta grade           (oklch .712 .018 79)

# ---- Champagne — the accent ramp (the only interactive hue, 80–100°) ----
CHAMP_300 = "#E9E1B0"  # highlight tints · gradient top         (oklch .904 .064 100)
CHAMP_400 = "#E2D288"  # hover state                            (oklch .860 .095 97)
CHAMP_500 = "#DAC46D"  # THE accent — CTAs, focus, markers      (oklch .820 .110 95)
CHAMP_600 = "#72560F"  # marks-grade on paper · 5.77:1          (oklch .470 .090 85)
CHAMP_700 = "#5A3E00"  # text-grade on paper · 8.30:1 AAA       (oklch .385 .080 80)
ON_CHAMP  = "#2A1C10"  # text on champagne fills · 9.51:1       (oklch .240 .030 60)

# ---- Dusk — atmosphere (LAW L3: hero sky art ONLY) ----
DUSK_RIBBON = "#81AFA9"  # the one cool counterpoint             (oklch .720 .050 186)
SKY_MID     = "#2D2114"  # hero sky middle band                   (oklch .258 .029 68)
SKY_BOTTOM  = "#4A330F"  # amber horizon glow                     (oklch .340 .060 75)
BRASS_KITE  = "#D3AB54"  # the kite, in brass                     (oklch .760 .115 85)

# ---- Signal — feedback (warn copper: 40° clear of champagne — law L12) ----
SIGNAL_OK   = "#57CC88"   # oklch .760 .145 155 · 8.42:1
SIGNAL_WARN = "#F49752"   # oklch .760 .140 55  · 7.61:1
SIGNAL_ERR  = "#FC6E68"   # oklch .710 .175 25  · 6.13:1

# ---- Ledger — the paper world (protected verbatim from v2) ----
LEDGER_50      = "#EFEBDF"  # paper canvas
LEDGER_100     = "#E6E1D3"  # paper alt surface
LEDGER_200     = "#D7D2C7"  # paper hairlines
LEDGER_SURFACE = "#F7F4EA"  # raised paper cards
LEDGER_INK     = "#28231E"  # espresso ink · 13.06:1 on paper
LEDGER_INK2    = "#615951"  # paper secondary · 5.77:1

# ---- Hero golden-dusk sky ramp (art only) ----
SKY_TOP = ROAST_950        # #251A11 — sky starts at the canvas

# Convenience aliases used by the SVG library
VOID = ROAST_950           # legacy name kept so generated art reads the same
SURFACE = ROAST_900
SURFACE2 = ROAST_850
LINE = ROAST_800
EMBER = CHAMP_500          # legacy alias — champagne now owns interaction
PAPER = LEDGER_50
PAPER_INK = LEDGER_INK
PAPER_LINE = LEDGER_200
AURORA = DUSK_RIBBON       # legacy alias — the dusk ribbon replaces the mint
```

### 12.6 Compliance matrix — every critical pair, computed

`scripts/contrast_audit.py` extended to 30 pairs (WCAG 2.x relative luminance; all values below are script output from the palette lab, reproducible — Appendix A):

| # | Pair | Ratio | Grade |
|---|---|---|---|
| 1 | ink on canvas | **14.15:1** | AAA |
| 2 | ink on surface-1 | 12.54:1 | AAA |
| 3 | ink on surface-2 | 11.06:1 | AAA |
| 4 | ink-2 on canvas | **9.01:1** | AAA |
| 5 | ink-2 on surface-1 | 7.98:1 | AAA |
| 6 | ink-3 on canvas | **6.64:1** | AA+ |
| 7 | ink-3 on surface-1 | 5.89:1 | AA |
| 8 | champagne-500 kicker text on canvas | **9.80:1** | AAA |
| 9 | champagne-500 kicker text on surface-1 | 8.69:1 | AAA |
| 10 | on-champagne text on champagne-500 fill | **9.51:1** | AAA |
| 11 | on-champagne on champagne-400 (hover) | 10.85:1 | AAA |
| 12 | focus ring champagne-500 vs canvas | 9.80:1 | ✓ |
| 13 | focus ring champagne-500 vs surface-1 | 8.69:1 | ✓ |
| 14 | border-input vs canvas (WCAG 1.4.11) | **3.96:1** | ✓ |
| 15 | champagne-700 kicker text on paper | **8.30:1** | AAA |
| 16 | champagne-700 on paper-2 | 7.57:1 | AAA |
| 17 | champagne-700 on paper-surface | 8.99:1 | AAA |
| 18 | champagne-600 marks on paper | **5.77:1** | ✓ (marks ≥3) |
| 19 | champagne-600 marks on paper-2 | 5.26:1 | ✓ |
| 20 | paper-ink on paper | 13.06:1 | AAA |
| 21 | paper-ink on paper-2 | 11.91:1 | AAA |
| 22 | paper-ink on paper-surface | 14.14:1 | AAA |
| 23 | paper-ink-2 on paper | 5.77:1 | AA |
| 24 | paper-ink-2 on paper-2 | 5.26:1 | AA |
| 25 | signal-ok on canvas | 8.42:1 | AAA |
| 26 | signal-warn (copper) on canvas | 7.61:1 | AAA |
| 27 | signal-err on canvas | 6.13:1 | AA+ |
| 28 | signal-err on surface-1 | 5.43:1 | AA |
| 29 | gradient end champagne-300 vs canvas | 12.85:1 | ✓ |
| 30 | gradient end champagne-500 vs canvas | 9.80:1 | ✓ |

**30/30 pass · 24 at AAA · zero FAIL rows.** Every improvement over Forge Noir is structural: kicker text on paper jumped 7.24→**8.30:1**; stat marks on paper 3.85→**5.77:1**; stat *units* are now AAA-grade by inheriting champagne-700.

### 12.7 The Thirteen Laws of Golden Hour

*The Ten Laws of Forge Noir (VT-PRD-002 §7.6) carried forward and extended. Laws L0, L1, L12 are new; L9 is strengthened. Machine-enforced gates in §15.2.*

| Law | Rule | Enforcement |
|---|---|---|
| **L0** | **The Black Floor.** No UI or art surface in the black zone: every surface must clear OKLCH L ≥ 0.22 **or** chroma ≥ 0.035. Dark is a color; black is an absence, and this site deals in presence. | **Gate 6** (new) |
| **L1** | **The Hue Floor.** Canvas-family chroma ≥ 0.018 — warmth must be a perception, not a spec comment. | **Gate 6** (new) |
| **L2** | Champagne owns interaction: CTAs, focus rings, hover borders, markers, key metrics. Nothing else leads the eye. | review |
| **L3** | The dusk ribbon never touches UI — no text, no borders, no fills, no buttons. Hero sky art only. | `rg 'var\(--vf-aurora\)' assets/css/` must return 0 hits |
| **L4** | Gradients stay in-family: champagne-300→500 lightness ramps only. The dual-hue diagonal stays retired. | build grep |
| **L5** | Champagne-500 never lands on paper. Paper text gets champagne-700; paper marks get champagne-600. | contrast script, paper section |
| **L6** | Glow budget: two 10px pulse-dot halos sitewide. Everything else lights from within (`--vf-inset-hi`) or by marks. | review |
| **L7** | Every text token clears 4.5:1 on every surface it appears on — verified by script, never by eye. | contrast script, CI gate |
| **L8** | One temperature: warm roast end-to-end; cool exists only as the dusk ribbon in art. | review |
| **L9** | **No raw color outside `tokens.css` — hex OR `rgb()/rgba()`.** A color written anywhere else is a bug. The 16 rgba leaks are re-pointed to derived-alpha tokens (§12.4). | **Gate 7** (widened) |
| **L10** | Hierarchy is loudness order: ink > ink-2 > ink-3 > lines; the primary accent always out-measures the atmosphere. | review |
| **L11** | The cream stays: paper islands are the premium signature — protected, re-graded, never removed. | review |
| **L12** | **Semantic separation:** signal hues stay ≥ 30° from champagne on the OKLCH wheel (warn is copper at 55° vs champagne 95°). Feedback never masquerades as interaction. | palette lint in build |

---
### 12.8 Section-by-section color map — all 16 routes

**Global chrome (every route)**

| Surface | Recipe |
|---|---|
| Body canvas | `background: var(--vf-canvas)` `#251A11` · `color: var(--vf-ink)` |
| Site header (resting / scrolled) | transparent → `var(--vf-canvas-a78)` + blur → scrolled `var(--vf-canvas-a96)` + blur; brand wordmark ink; nav links ink-2, hover champagne + ember-dim underline wash |
| Menu overlay / panel | `var(--vf-canvas-a96)` overlay · `var(--vf-surface-2-a86)` panel; links ink, hover champagne; index numerals ink-3 mono |
| Preloader | canvas bg; counter ink-3 mono; load bar = champagne gradient |
| Progress hairline (scroll) | `--vf-gradient-ember` — champagne 300→500 (the ONE gradient) |
| Cursor | bone fill `#EDEAE2`; label panel `--vf-surface-1-a55`, label text on-champ when over champagne targets |
| Selection | bg champagne-500 · text on-champagne (9.51:1) |
| Focus-visible (universal) | 2px champagne outline · 3px offset · ember-dim ring — 9.80:1, unchanged grammar |
| Skip-link | bg champagne-500 · text on-champagne · mono |
| Site footer | canvas bg · ink-3 chrome · watermark stroke line-strong `#615246` · ambient radial `--vf-champ-a09` |
| Grain | unchanged (light-from-within, z-grain) |

**Home `/` — the five acts**

| Section | Color map |
|---|---|
| `act--hero` | canvas + WebGL **golden dusk** (§12.10); eyebrow mono ink-3 + champagne pulse dot (`--vf-halo-dot`); H1 ink; the serif-accent word **champagne-500** (9.80:1 — typography-led color); scroll-cue ink-3 |
| `act--work` | canvas; kicker `01 — THE PROOF` mono champagne-500; H2 ink; case cards surface-1 + line border + inset-hi; meta ink-3; metric numerals champagne-500; hover: border → champagne, bg → surface-2 |
| `act--services` | canvas; kicker champagne-500; service rows separated by line hairlines; indices ink-3 mono; titles ink; hover: champagne marker + ember-dim row wash |
| `act--about` (journey) | canvas; journey rail: line track, champagne markers, ember-dim progress fill; maker-grid cards surface-1; the journey illustration (webp) unchanged — it is the narrative asset |
| `act--contact` | canvas; H2 ink; primary CTA champagne (§12.9); marquee chrome ink-3 |

**Work `/work/`** — page-hero canvas (kicker champagne-500, title ink); work-grid cards surface-1/line/inset-hi; flagship card carries champagne metrics; footer band canvas.

**Case studies `/work/{checkout-rebuild, clinicflow, fieldops, insightloop}.html`** — page-hero canvas: kicker champagne-500, title ink, meta ink-3. Then **five `case-band--paper` islands**: paper `#EFEBDF` bg · paper-ink text · paper-ink-2 secondary · kickers & decision letters **champagne-700 `#5A3E00` (8.30:1)** · stat rules & markers **champagne-600 `#72560F` (5.77:1)** · raised cards paper-surface · kicker wash `--vf-champ600-wash`. Closing `case-band--dark`: canvas band, champagne metric accents. *The paper islands now do double duty: credibility signal AND the thing that breaks the dark page's former black majority.*

**Services `/services/`** — page-hero canvas; six `service-detail` sections (web, mobile, design, ai, cloud, custom) alternating canvas / surface-1 panels with line hairlines; icon strokes line-strong + champagne markers; inline code: surface-2 bg + **champagne-500** text (8.69:1 on surface-1); closing CTA canvas + champagne button.

**About `/about/`** — page-hero canvas; journey narrative act (as home `act--about`); facts-rail: surface-1 cards, ink-3 labels, champagne figures; maker-grid visual surface-1.

**Contact `/contact/`** — page-hero canvas; form: field bg surface-1 · border **border-input (3.96:1)** · focus border champagne + 3px ember-dim ring · labels ink-2 · helper meta ink-3 · errors signal-err text + icon + border (L7 triple-redundancy); availability chip: `--vf-ok-a40` border + `--vf-ok-a07` fill + signal-ok dot with `--vf-halo-ok`.

**Journal `/journal/` + 3 essays** — canvas; entry list rows: line hairlines, ink-3 dates, ink titles, champagne read-links; essay body: ink text, ink-2 secondary, champagne links with line underline, inline code surface-2/champagne-500.

**404** — canvas; glyph stroke `--vf-ink-a75` + fill `--vf-ink-a96`; kicker champagne-500; code outline line-strong; brass kite mark.

**Privacy & Terms `/legal/*`** — canvas; headings ink; body ink-2; links champagne-500.

### 12.9 Component application matrix

| Component | Token recipe (Golden Hour) |
|---|---|
| **Buttons · primary** | bg champagne-500 · text on-champagne · hover bg champagne-400 (10.85:1) via the @property ramp (§12.11) · focus champagne ring + ember-dim |
| **Buttons · dark** | bg surface-2 · border line-strong · text ink · hover border → roast-600 |
| **Buttons · ghost** | text champagne-500 · border line-strong · hover bg ember-dim |
| **Case / journal cards** | bg surface-1 · border line · inset-hi · hover: border→champagne + bg→surface-2 · metrics champagne-500 |
| **Paper bands** | paper canvas · paper-ink text · kickers/decision letters champagne-700 · stat units & rules champagne-600 · raised cards paper-surface |
| **Forms** | field bg surface-1 · border border-input (3.96:1) · focus border champagne + 3px ember-dim · error signal-err · labels ink-2 · meta ink-3 |
| **Chips (checked)** | bg champagne-500 · text on-champagne · check glyph weight+fill (L7 redundancy) |
| **Availability chip** | ok-a40 border · ok-a07 fill · signal-ok dot + halo-ok · text ink-2 |
| **Pulse dots** (hero eyebrow, availability) | champagne-500 / signal-ok + the two sanctioned 10px halos — the entire glow budget |
| **Footer watermark** | stroke line-strong `#615246` — visible, still quiet |
| **404 glyph** | ink-a75 stroke · ink-a96 fill |
| **Work-scroller vignette** | `--vf-canvas-a42` radial (was raw rgba canvas) |
| **Prose / inline code** | surface-2 bg · champagne-500 text |
| **OG images / favicon / manifest** | regenerated from palette.py; `theme-color` → **#251A11** |

### 12.10 Imagery, hero shader & share assets

1. **The hero becomes a golden dusk** (WebGL `horizon.js`, uniforms re-graded from `palette.py` — the scene is re-lit, not rebuilt): sky ramp `#251A11 → #2D2114 → #4A330F` (espresso sky into an **amber horizon**); the horizon glow radial re-tinted from ember to **warm champagne** (same seat, new light); the aurora bands re-tinted to the **dusk ribbon `#81AFA9`**, gain held ≤ 0.27 and softened toward 0.24; **the kite becomes brass `#D3AB54`** with halo ≤ 0.30; stars bone `#EDEAE2`; ridgelines roast-950/900. Static SVG fallback tier re-graded identically (sky bands, ribbon at ≤ 0.11 opacity, brass kite).
2. **Case-study SVG mockups** (`v2-src/svgs.py`, reads palette.py): void→roast-950, surfaces→roast-900/850, lines→roast-800, ink→bone, UI accents→champagne-500, atmosphere→dusk ribbon. The mockups look like the gallery's products, lit in champagne.
3. **Favicon & brand glyph**: champagne-500 fill on transparent (the four-point star, single-metal).
4. **13 OG cards** regenerate via `v2-src/generate_assets.py`: espresso canvas, bone type, champagne accents — consistent with the shipped site.
5. **`manifest.json` / `head.tpl` theme-color**: `#0E0C09` → **`#251A11`**.
6. **The journey illustration** (`assets/img/vishvu-journey.webp`): unchanged this cycle (protected narrative asset); flagged for an optional golden-hour re-grade in v3.1 if it reads cool against the new warmth.

### 12.11 Motion & interaction color

- **The ramp-travel hover survives, new metal** (the transition the last audit praised): `@property --ember-l` initial-value **.820**; `@supports (background: oklch(0.820 0.110 95))` re-inks the `.btn` block to `oklch(var(--ember-l, .820) .110 95)`, hover `--ember-l: .860` — the button **travels champagne-500→400 through OKLCH lightness**; instant-swap fallback and reduced-motion collapse unchanged.
- Scroll hairline: the one gradient (champagne 300→500).
- Glow budget: two 10px pulse-dot halos, champagne + ok. Everything else elevates by inset-hi and surface steps.
- Preloader counter, marquee, magnetic CAs, cursor: mechanics unchanged; colors re-point to tokens.
- Judge 78's shimmer wish stays logged as a v3 candidate. Restraint is still the brand.

---

## 13. Migration Plan

### 13.1 Token migration map (value-level; every name preserved)

| Token | Old (Forge Noir) | New (Golden Hour) |
|---|---|---|
| `--vf-canvas` | `#0E0C09` oklch(.155 .006 75) | **`#251A11`** oklch(.230 .024 60) |
| `--vf-surface-1` | `#161310` | **`#30241A`** |
| `--vf-surface-2` | `#1F1C18` | **`#3A2D23`** |
| `--vf-line` | `#2B2825` | **`#4A3D32`** |
| `--vf-line-strong` | `#403C37` | **`#615246`** |
| `--vf-border-input` | `#6D6861` (3.35:1) | **`#887769`** (3.96:1) |
| `--vf-ink` | `#EAE8E3` (15.95:1) | **`#EDEAE2`** (14.15:1 — halation band exited) |
| `--vf-ink-2` | `#B0ACA5` (8.64:1) | **`#C2BCB1`** (9.01:1) |
| `--vf-ink-3` | `#96918B` (6.25:1) | **`#A8A196`** (6.64:1) |
| `--vf-ember` | `#E36E49` | **`#DAC46D`** champagne |
| `--vf-ember-soft` | `#FE8F5B` | **`#E2D288`** |
| `--vf-ember-dim` | `rgba(227,110,73,.14)` | **`rgba(218,196,109,.14)`** |
| `--vf-ember-text-paper` | `#882D16` (7.24:1) | **`#5A3E00`** (8.30:1) |
| `--vf-ember-mark-paper` | `#C65029` (3.85:1) | **`#72560F`** (5.77:1) |
| `--vf-on-ember` | `#0C0806` (6.26:1) | **`#2A1C10`** (9.51:1) |
| `--vf-aurora` | `#80D1B5` mint | **`#81AFA9`** dusk ribbon |
| `--vf-ok` | `#52CD86` | **`#57CC88`** |
| `--vf-warn` | `#E7B643` (collided with gold) | **`#F49752`** copper (L12) |
| `--vf-err` | `#ED5350` | **`#FC6E68`** |
| `--vf-gradient-ember` | `#FE8F5B→#C65029` | **`#E9E1B0→#DAC46D`** |
| `--vf-halo-dot` | `rgba(227,110,73,.45)` | **`rgba(218,196,109,.45)`** |
| `--vf-halo-ok` | `rgba(82,205,134,.45)` | **`rgba(87,204,136,.45)`** |
| paper family (6 tokens) | kept | **kept verbatim** |
| `@property --ember-l` | `.670` | **`.820`** |
| P3 boost | `oklch(.670 .19 38)` | **`oklch(0.820 0.130 95)`** |
| 13 derived-alpha tokens | — | **new** (§12.4) |

### 13.2 File-by-file change list

| File | Change |
|---|---|
| `v2-src/palette.py` | replace with §12.5 (the source of truth) |
| `assets/css/tokens.css` | replace color block with §12.4; type/space/motion untouched |
| `assets/css/components.css` | (1) `@property`/`@supports` button block → §12.11 values; (2) 16 raw rgba → derived-alpha tokens: header `:69/:75/:868` → `--vf-canvas-a78/-a96`; vignette `:227` → `--vf-canvas-a42`; cursor `:301` → `--vf-surface-1-a55`; menu `:587` → `--vf-surface-2-a86`; hairline `:276` → `--vf-ink-a14`; 404 `:992/:1008` → `--vf-ink-a75/-a96`; footer radial `:882` → `--vf-champ-a09` |
| `assets/css/pages.css` | hero radial `:17` → `--vf-champ-a08`; paper wash `:115` → `--vf-champ600-wash`; ok chip `:395/:396` → `--vf-ok-a40/-a07` |
| `assets/js/app/horizon.js` | uniform re-grade per §12.10 (sky ramp, champagne horizon, dusk ribbon, brass kite, gains) |
| `v2-src/svgs.py` | reads new palette.py (void/surface/ember/aurora aliases preserved — re-inks automatically) |
| `v2-src/partials/head.tpl` + `manifest.json` | `theme-color` → `#251A11` |
| `v2-src/build.py`, `generate_assets.py` | no logic change; re-run regenerates all pages, OG cards, favicon/icons from the new palette |
| `scripts/contrast_audit.py` | extend to the 30-pair matrix (§12.6) |
| `scripts/check-colors.sh` | add Gates 6 & 7 (§15.2) |
| `404.html` + 16 route pages | no hand edits — regenerated by `build.py` |

### 13.3 Phased rollout

- **Phase 0 — arm the gates first.** Commit Gates 6+7 and the 30-pair matrix *before* the palette change. They run red against Forge Noir (by design: Gate 6 fails on `#0E0C09`/`#161310`; Gate 7 fails on 16 leaks). Red gates on the old palette are the documented proof of this PRD's case.
- **Phase 1 — tokens.** `palette.py` + `tokens.css` (§12.4–12.5). Site already renders 80% correct (zero raw color in CSS means the cascade re-inks everything except the hero shader and SVG art).
- **Phase 2 — leaks.** Point the 16 rgba usages at derived-alpha tokens. Gate 7 goes green.
- **Phase 3 — art.** `horizon.js` golden-dusk re-grade + SVG fallback re-grade. Gate 6 green (art floors enforced).
- **Phase 4 — assets.** `build.py` + `generate_assets.py` regenerate 16 pages, 13 OG cards, favicon, manifest.
- **Phase 5 — full gate run + VT-CTA-005** (§15.3), then ship.

**Rollback ritual (unchanged, 60 seconds):** `git revert <palette-commit> && bash scripts/check-colors.sh && rsync to webroot` — the old palette is one commit away at all times.

---

## 14. Accessibility Acceptance Criteria (WCAG 2.2)

1. **1.4.3 Contrast (Minimum)** — all 30 pairs ≥ 4.5:1 (§12.6); 24 at AAA.
2. **1.4.11 Non-text Contrast** — border-input 3.96:1; focus rings 9.80:1; champagne marks ≥ 5.77:1 on paper; hairlines remain documented decorative exemptions.
3. **1.4.1 Use of Color** — no information by color alone: errors = text + icon + border; checked chips = weight + fill; availability = dot + text; stat units = text-grade ink.
4. **2.4.7 Focus Visible** — universal 2px champagne outline, 3px offset, ember-dim ring; 9.80:1 against adjacent surfaces.
5. **2.4.11 Focus Not Obscured** — header blur layers keep ≥ 44px clear (unchanged mechanics).
6. **CVD stability** — champagne-700 kickers on paper hold 8.30:1 *luminance* contrast (hue-independent); champagne vs copper warn differ by 40° hue AND luminance (7.61 vs 9.80 band); no pair relies on red/green distinction alone.
7. **Halation posture (new, documented)** — the flagship text pair exits the >14:1 extreme band (15.95 → 14.15:1), still AAA.
8. **`prefers-reduced-motion`** — 3-tier contract unchanged; the ramp hover collapses to instant swap.
9. **Daylight margin (kept)** — ink-3 at 6.64:1 keeps the NN/g daylight factor margin the last audit demanded.

---

## 15. QA & Validation Plan

### 15.1 The re-audit protocol — VT-CTA-005 (the tribunal re-convenes, one last time)

Same pipeline as VT-CTA-003/004: 7 forced-reveal captures (1920×1080 desktop full + hero viewport + 390×844 mobile) across home, case study, services, contact → **pixel ground-truth extraction** (`scripts/pixel_evidence.py` — the new evidence instrument: dominant-bucket + luminance-distribution + OKLCH decomposition) → blind structured reviews (no redesign context; reviewers reconstruct the palette from pixels and answer attribution prompts) → contrast computation → law-gate greps → panel deliberation → **the owner's 3-second test**.

**Ship criterion:** ≥ 7.5/10 weighted on all four pages · zero FAIL rows in all 7 gates · **zero attribution sentences containing "black"** · the unprompted attribution sentence targeted: *"the espresso one with the champagne accent"* · 100/100 judges ACCEPT · **owner sign-off (outranks the tribunal)**.

### 15.2 Automated gates (committed, pre-deploy, fail the build)

```bash
# scripts/check-colors.sh — Golden Hour edition
# Gate 1 · WCAG contrast matrix (law L7) · 30 pairs .......... python3 scripts/contrast_audit.py
# Gate 2 · dusk ribbon never touches UI CSS (law L3) ........ rg 'var\(--vf-aurora\)' assets/css/ → 0 hits
# Gate 3 · no retired tokens (ember hexes, mint) ............ rg 'E36E49|FE8F5B|882D16|C65029|80D1B5' assets/ v2-src/ → 0
# Gate 4 · one palette source at build layer ................ palette.py == tokens.css values (build check)
# Gate 5 · gradients in-family (law L4) ..................... only --vf-gradient-ember may contain 'gradient('
# Gate 6 · THE BLACK FLOOR + HUE FLOOR (laws L0+L1, NEW) .... python3 - <<'EOF'
#   for each surface in palette.py (canvas, surfaces, lines, on_champ, paper inks):
#     oklch = read the documented oklch() triple
#     assert oklch.L >= 0.22 or oklch.C >= 0.035, f"BLACK ZONE: {name}"
#   assert palette canvas-family chroma >= 0.018, "HUE FLOOR: warmth must be visible"
#   EOF
# Gate 7 · NO RAW COLOR OUTSIDE tokens.css (law L9, WIDENED) . rg '#[0-9a-fA-F]{3,8}|rgba?\(\s*[0-9]' \
#     assets/css/ -g '!tokens.css' → 0 hits   # hex AND rgb()/rgba() literals
```

### 15.3 The owner's test (new ship criterion, codified)

The owner views the deployed preview on his own devices, in his own rooms, and answers one question in under 3 seconds: *"Is this black?"* If yes — REVISE, regardless of tribunal score. **This criterion is above the tribunal's.** It is the lesson of VT-CTA-004, written into law.

### 15.4 Device matrix

macOS Safari/Chrome (P3 display — boost active) · Windows Chrome/Edge (sRGB — hex path) · iPhone Safari (True Tone, daylight) · Android Chrome (night light) · OLED dark-room check (espresso must still read brown) · projector washed-out check.

---

## 16. Performance & Oracle Always Free Deployment

### 16.1 The envelope (unchanged, verified)

The entire Golden Hour revision is **static work**: CSS custom-property values, SVG/WebGL uniforms, Python-generated assets. **Zero JavaScript added; zero runtime cost; first-load budget unchanged (~140 KB: fonts 30 KB critical, JS lazy-tiered, SVG visuals 3–5 KB).** The P3 champagne boost ships as a media query — free vividness on capable displays, zero bytes elsewhere.

### 16.2 Architecture (OCI Always Free)

```
Internet → (optional Cloudflare free: DNS · proxy · TLS edge)
         → OCI Always Free · Ampere A1 (4 OCPU / 24 GB — the whole site uses a rounding error)
           ├─ nginx (deploy/nginx-site.conf — TLS, HSTS, CSP, rate-limit, immutable caching)
           │    └─ static site (repo root — index.html + assets/, 16 routes)
           ├─ Node contact API (api/index.js — systemd unit, honeypot/time-trap/rate-limit)
           └─ deploy ritual: build.py → generate_assets.py → check-colors.sh (7 gates) → rsync
```

The existing `deploy/oracle-setup.md` playbook and `deploy/nginx-site.conf` remain valid — **no infrastructure change**. The only deploy additions: the two new gates run pre-ship, and `theme-color`/OG assets carry the new palette. Egress headroom is enormous (10 TB/month vs a ~140 KB first load); block storage and compute are nowhere near the Always Free ceilings.

### 16.3 Deploy runbook (Golden Hour edition)

```bash
git pull && python3 v2-src/build.py && python3 v2-src/generate_assets.py
bash scripts/check-colors.sh        # 7 gates — all green or no ship
# captures + owner's 3-second test (§15.3)
rsync -av --delete ./ /var/www/vishvutech/ && nginx -t && systemctl reload nginx
curl -s https://vishvutech.com | head -5   # smoke
# rollback: git revert <palette-commit> && rebuild && rsync (60 seconds)
```

---

## 17. Risks & Mitigations

| # | Risk | Mitigation |
|---|---|---|
| R1 | Lighter canvas costs text headroom | Ladder re-tuned (14.15/9.01/6.64 — AAA/AAA/AA+); matrix green; ink-3 daylight margin held; Gate 1 regression-proof |
| R2 | Champagne collides with warn amber | Warn re-hued to copper at 55° (40° clear, law L12) + luminance separation + icon/text redundancy |
| R3 | "Gold reads jewelry, not engineering" | Champagne at chroma 0.110 — deliberately softer than the `#D4AF37` jewelry band (sourced convention); espresso grounding + mono/serif type system keep the engineering voice; kite is brass, not glitter |
| R4 | Display gamut drift (gold reads greenish on bad panels) | sRGB-safe by construction (all primitives in-gamut, zero clipping — verified in the palette lab); P3 boost is opt-in media query; hex fallback path |
| R5 | Hero shader re-grade regression (the 2×2 buffer class of bug) | rAF retry + load hook + ResizeObserver kept; fallback SVG re-graded identically; forced-reveal captures in VT-CTA-005 |
| R6 | The 16 rgba leaks reintroduce drift | Derived-alpha tokens + Gate 7 (rgba-aware); leaks are now build failures |
| R7 | Owner preference shifts again (a third session) | Candidates B (Night Library) and C (Heritage Studio) are documented to canvas/surface/accent/ink/paper depth in §11 — a room change is a palette.py swap, not a redesign; the 40/30/30 matrix is re-runnable |
| R8 | "Warm brown" reads muddy on cheap displays | Roast chroma held at 0.024–0.030 (visible but controlled); device matrix §15.4 includes projector + OLED checks; the Hue Floor gate prevents both directions of drift |

---

## 18. Success Metrics & The Award Track

### 18.1 Definition of done (VT-CTA-005)

1. 7/7 gates green, including Black Floor and Hue Floor.
2. Pixel ground truth: **the black-zone pixel share (perceptual OKLCH gate L0) drops from 97.4% to ≈ 0%** on the same captures (E2 protocol) — the page becomes measurably *not* a black page. **Preview-validated at 0.0% (lower acts) / 0.7% (hero) — see Appendix B.**
3. Blind render scores ≥ 7.5 weighted × 4 pages; zero "black" attribution sentences; target sentence *"the espresso one with the champagne accent"* appears unprompted.
4. 100/100 judges ACCEPT. 5. **Owner sign-off (§15.3).**

### 18.2 The award submission track (post-ship)

| Track | Play |
|---|---|
| **Awwwards** | Submit after VT-CTA-005 ≥ 7.5. Jury weights: design 40 / usability 30 / creativity 20 / content 10. Lead with the golden-dusk hero shader and the paper-island case studies. **Developer Award angle: the site ships its own color-law gates** — a portfolio whose design system is enforced by CI is a story jurors retell. |
| **FWA** | Motion-led cut: preloader → hero reveal → journey scrub → magnetic CTAs (the existing motion spine, re-lit). |
| **CSSDA** | WOTD submission; emphasize the typography system (Clash Display / Satoshi / Instrument Serif / JetBrains Mono — kept) and the case-study editorial craft. |
| **Precondition for all** | Swap the structured example content for real project data per `docs/CONTENT-GUIDE.md` — the standing law holds: **no invented numbers ship, ever.** |

### 18.3 The closing standard

> **Judge 51, adjourning VT-CTA-004:** "Raise the floor. Change the metal. Close the loophole. Keep everything that won. Bring it back as Golden Hour — and bring receipts."

Every number in this document is script-reproducible (Appendix A). Every gate fails the build, not the argument. And the owner's eye — the instrument that overruled a perfect paperwork — is now law L0.

---

## Appendix A · Reproduction

```bash
# the evidence, the palette, and every ratio in this document:
python3 scripts/pixel_evidence.py       # §2 evidence: pixel ground truth + canvas optics (E1–E7)
python3 scripts/golden_hour_lab.py      # §11–§12: 3 candidates, 30-pair matrix, gates L0/L1, token emission
# the build, after implementation:
python3 v2-src/build.py                 # regenerate 16 routes
python3 v2-src/generate_assets.py       # regenerate OG cards + favicon/icons from palette.py
bash scripts/check-colors.sh            # 7 gates — zero tolerance
# captures: scripts/capture.sh (7 pages, 1920×1080 + 390×844, forced-reveal)
# live teardown (§6): headless browser + getComputedStyle on body/html of the named sites
```

## Appendix B · Evidence inventory (VT-CTA-004 session)

| Artifact | Origin |
|---|---|
| 6 forced-reveal captures (home×3, services, case study, mobile 390×844) | local render of commit `cd854fa` (`http.server :8899`) |
| Pixel ground truth (dominant buckets, luminance distribution, OKLCH decomposition) | `scripts/pixel_evidence.py` — measured, not estimated |
| Canvas optics (vs `#000000` 1.08:1; vs `#0A0A0A` 1.01:1; L 0.156; C 0.007; spread 5) | token-level computation |
| 16 rgba leak grep hits (components.css ×13, pages.css ×4) | `rg 'rgba\(' assets/css/` |
| Award-site canvas measurements (`#EDEDED`, `#0F172A`, `#000000`, `#FFFFFF`, `#0A0C10`) | live headless-browser `getComputedStyle`, this session |
| Trend citations (Pantone Mocha Mousse `#A47864`; Wix×Pantone SOTD Jan 6 2025; champagne `#F7E6CA` ramp; luxury golds `#C69B3C–#D4AF37`; avoid `#FFD700`; jewel-dark 2026 trend) | pantone.com · awwwards.com · figma.com/colors/champagne · zoviz.com · elements.envato.com (as cited in §6.3) |

**Preview validation — the paste-ready claim, executed (this session).** The migration was executed at value level on a preview copy (**29 files patched**: `assets/css/*` (tokens + 16 rgba leaks + `@property` ramp), `assets/js/app/horizon.js` (golden-dusk uniforms), `assets/img/favicon.svg`, 16 route pages, `manifest.json` — token names untouched, zero renames), served, and re-measured with the same instruments:

| Render (same protocol as E1–E4) | Forge Noir — pixels in the black zone | Golden Hour — pixels in the black zone |
|---|---|---|
| Home, lower acts (the 97.7% page) | 97.4% | **0.0%** |
| Home, hero viewport | 41.2% | **0.7%** |
| Services page | 97.7% | expected ≈ 0% (same canvas — §13 confirms) |

The dominant pixel family in the hero moved from bucket `#080808` (near-black) to `#281818` (espresso, ~20-unit warmth spread). Zero retired Forge Noir values remain in CSS/JS/SVG. **The paste-ready migration is proven end-to-end, not asserted.**

## Appendix C · Judge roster & continuity (the same 100 judges, third convening)

Panels P1–P10 with chairs as seated in VT-CTA-001 and reconvened in VT-CTA-002/003: P1 Art Direction (Chair: Ingrid Halvorsen) · P2 Color Science & Perception · P3 Brand Strategy & Positioning · P4 UX, Perception & Trust · P5 Accessibility & Inclusive Design · P6 Award Benchmarking · P7 Design Engineering & Systems · P8 Motion & Interaction Color · P9 Client & Conversion · P10 Performance & Platform. Standing judges of record quoted: 06, 25, 28, 40, 49, 51 (chair of convening), 57, 78, 83. Panel A named judges quoted: A3 (Tanaka), A8 (Okafor). The tribunal's votes across the lineage: 5.32 → 6.03 → 8.86 (ACCEPT, later overruled by the owner) → **7.30 REVISE (this session)** → *VT-CTA-005 pending*.

---

*The 100 judges stand down. The gates keep watch. The owner's eye outranks the paperwork — by law.*

**— END OF VT-PRD-003 · GOLDEN HOUR —**
