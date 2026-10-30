# THE 100-JUDGE TRIBUNAL · VISHVU TECH — ROUND 2
## The Layering Audit · First Light ("Porcelain Dawn") reviewed against the owner's layer mandate

**Session:** VT-CRITIQUE-100-R2 · October 2026
**Subject:** `github.com/vishvutech/Vishvu_tech` @ `5b9516f` — the FIRST LIGHT build (VT-PRD-004), deployed locally and audited live, page by page
**Focus:** the owner's second mandate — not darkness this time, but **monochrome**: *"now its ok but not award winning — see, it's overall only one colour, there is no colour combinations… background completely layer one, a colour; on the layer one now again layer two, a different colour which would be best on layer one colour; now layer 3 on the layer 1 + layer 2 — so it becomes the premium. I gave the intuition — it may have more layers also. Do deep research now properly."*
**Method:** live render + pixel-level colour measurement + token audit + vertical scroll-profile analysis, then the same tribunal of 100 independent specialist judges (10 panels × 10) that produced the First Light mandate — convened again, briefed on the new evidence.

> **Standing verdict from Round 1, preserved:** the dark world is gone; zero black, zero brown, zero dark shades — the Light-World law holds and **no judge proposes breaking it**. Round 2 judges a different failure: a light world with **no colour architecture on top of it**.

---

## PART 0 — HOW THE SITE WAS AUDITED (EVIDENCE BASE)

The FIRST LIGHT build was rendered at 1600×1000 per page. Every pixel was measured in HSV space; the homepage was additionally sliced into ten horizontal strips (top → bottom) and averaged, producing a **vertical colour profile** — the exact experience of scrolling the page.

### 0.1 — The vertical colour profile of the homepage (the scroll journey)

| Strip (top→bottom) | Average colour | Hue | Saturation | Value |
|---|---|---|---|---|
| 0 (hero) | `#E3E3D7` | 60.0° | 0.053 | 0.890 |
| 1 | `#F4F1E9` | 43.6° | 0.045 | 0.957 |
| 2 | `#F5F3EC` | 46.7° | 0.037 | 0.961 |
| 3 | `#F3F1E8` | 49.1° | 0.045 | 0.953 |
| 4 | `#F4F1E9` | 43.6° | 0.045 | 0.957 |
| 5 | `#F3F1E9` | 48.0° | 0.041 | 0.953 |
| 6 | `#F5F3EC` | 46.7° | 0.037 | 0.961 |
| 7 | `#F7F4EC` | 43.6° | 0.045 | 0.969 |
| 8 | `#F3F2EA` | 53.3° | 0.037 | 0.953 |
| 9 (footer) | `#F0EBDF` | 42.4° | 0.071 | 0.941 |

**Reading:** from the first pixel of the hero to the last pixel of the footer, hue travels **42°–60° and back** — a 17° wobble inside the warm-ivory family. Value travels 0.89–0.97. Saturation never exceeds 0.07. **The entire scroll journey of the homepage is one colour, slightly breathing.** The same profile holds on every page (dominant hue 30–60° on all six audited pages; only 4–5 of 12 hue bins hold more than 0.5% of pixels anywhere).

### 0.2 — The token audit: one hue family owns the world

| Layer (as shipped) | Tokens | Hue range | Verdict |
|---|---|---|---|
| Canvas | `#F7F4EC` | 90° | ivory |
| Surface-1 (milk) | `#FDFCF8` | 95° | ivory |
| Surface-2 (bone) | `#F0EBDF` | 88° | ivory |
| Line / line-strong | `#E2DBC8` / `#CFC6AE` | 90° | ivory |
| Washes | `#FDF3E3` `#EEF3F9` `#EAF2EF` | 85°/250°/180° | ivory-adjacent, **~1–2% lightness from canvas** |
| Ink ladder | `#123F3B` `#3E5C58` `#566A66` | 186° | peacock — typographic only |
| Accent | `#0F766E` ramp | 186° | peacock — CTAs, links |
| Reserves | coral/saffron/sky | 34°/72°/254° | rationed to near-invisibility |

Every **structural** colour (the ~95% of pixels that are backgrounds, cards, wells, hairlines) lives in hue 88–95° — one single hue family. The washes that were supposed to provide "atmosphere" sit at OKLCH L 0.955–0.960 against a canvas at L 0.967: a **1–2% lightness delta**, below the ~3% just-noticeable-difference threshold for large fields. They are invisible in practice. The only hue the eye ever meets at strength is peacock, at an estimated ≤3% pixel share (links, CTAs, dots).

**In 60-30-10 terms the site is 97–2–1: ivory, ivory, ivory.** The classic ratio didn't fail — it was never applied.

### 0.3 — What the layering theory says (the research base, summarised)

The tribunal's research panel reviewed how layered colour is practised by the systems that set the standard:

- **Material Design 3** builds every screen from paired, stacked roles — surface → container → on-container — and explicitly warns that colour must be applied "in the intended pairs or layering orders"; layering is not decoration, it is the *structure* of hierarchy ([m3.material.io/styles/color/roles](https://m3.material.io/styles/color/roles)).
- **Atlassian Design System** defines UI as four stacked elevations — sunken, default, raised, overlay — where "elevations are layered surfaces that form the foundation of UI" and each level is a *different surface colour*, not just a shadow ([atlassian.design/foundations/elevation](https://atlassian.design/foundations/elevation)).
- **Atmos.style's colour-system guide** shows the working light-mode pattern: `bg.default`, `bg.subtle`, `bg.surface` — three distinct background layers — with WCAG pairs engineered per layer ([atmos.style/blog/how-to-build-a-color-system-for-ui-design](https://atmos.style/blog/how-to-build-a-color-system-for-ui-design)).
- **Scroll-driven background-colour transitions** (section bands that change as the visitor scrolls) are now a first-class premium-site feature, not an exotic one.

The pattern repeats across every source: **premium light interfaces are stacks of distinct, harmonious colour layers — not one immaculate colour.** First Light built the light world; it never built the stack.

---

## PART 1 — THE 100 JUDGES

The same hundred judges who demanded the light world return. Ten panels, ten judges each, Awwwards-derived scoring. They were shown the pixel evidence above before speaking.

---

### PANEL A — COLOUR SCIENCE & COLOUR THEORY (Judges 1–10)

**Judge 01 · Dr. Hilda Okonkwo — Colour Scientist, ex-Pantone Color Institute** — 6/10
"Round 1 gave you light. Round 2 exposes what light alone cannot do: a 42°–53° hue lock across an entire page is a **monochromatic field**, and monochrome at high lightness reads as *absence of decision*, not serenity. The eye needs hue travel to perceive richness — you gave it a 17° wobble."

**Judge 02 · Jean-Luc Marchand — Colour Theorist, École de la Chambre Syndicale** — 6/10
"The Porcelain Ladder is a *value* ladder wearing a hue costume. Six neutrals at hue 88–95° differ only in lightness. That is greyscale with perfume. A true colour system stratifies **hue** as deliberately as it stratifies lightness."

**Judge 03 · Prof. Aki Tanaka — Vision Scientist, perceptual contrast lab** — 6/10
"Your washes are scientifically invisible. A 1–2% OKLCH lightness delta on a large field is under the JND; you computed atmosphere and shipped a placebo. Layer perception requires ≥3% lightness steps *or* a hue step of ≥30° at equal lightness. Choose per layer — you chose neither."

**Judge 04 · Dr. Ingrid Solberg — Colour Psychologist, Nordic design institutes** — 5/10
"Dawn — your own metaphor — is the most layered light event in nature: zenith blue, blush band, gold horizon. You shipped the zenith and called it dawn. The metaphor demands strata; the build refuses them."

**Judge 05 · Ramón Vidal — Master colourist, gallery conservation** — 6/10
"Turner built skies in five glazes. Each glaze changed hue *and* depth. One glaze — however immaculate — is underpainting. This site is a beautiful underpainting waiting for its glazes."

**Judge 06 · Dr. Fatima Al-Rashid — Colour-system researcher, OKLCH working group** — 6/10
"In OKLCH terms: your backgrounds occupy a single point (L≈.96, C≈.01, H≈90). A layered system occupies a *constellation* — same lightness neighbourhood, deliberately spread hues at low chroma. The constellation is what reads as 'combination'."

**Judge 07 · Heinrich Baumann — Optical physicist, display calibration** — 6/10
"On a wide-gamut display this page is nearly achromatic. You reserved your one chroma boost for a token nobody fills with. Spread the chroma across bands and the same screen finally shows a *colourful* site without a single dark pixel."

**Judge 08 · Colette Duret — Textile colour director, maison heritage** — 5/10
"In couture, tone-on-tone is a *statement made by contrast* — a cream on an oyster on a bone, each visibly its own colour. Your cream, oyster and bone are spectroscopically distinct and optically identical. The eye is your customer, not the spectroscope."

**Judge 09 · Dr. Yuen Park — Colour semiotics researcher** — 6/10
"Peacock-as-only-hue makes peacock mean *everything* — link, button, marker, mood. When one colour means everything it means nothing. Bands would let peacock mean *action*, precisely because the sections around it mean *place*."

**Judge 10 · Marguerite Osei — Colour historian, pigment trade archives** — 6/10
"Even the great ivory periods — Kangxi porcelain, Sèvres blanc — earned their reputation against *coloured mounts*: celadon stands, giltwood, painted grounds. Ivory lives by its company. This ivory has none."

**Panel A consensus (avg 5.8):** the science of layer perception — JND thresholds, hue travel, chroma distribution — is absent, and it is computable in advance. The fix is engineering, not taste.

---

### PANEL B — AWARD-SITE JURORS (Judges 11–20)

**Judge 11 · Marc-Antoine Lefèvre — Awwwards Site-of-the-Day juror, 6 years** — 6/10
"I scroll SOTD winners weekly. The light-theme winners are never one colour. They run a **band rhythm** — the background itself changes character act by act, so the scroll has chapters. Your scroll has pages, not chapters."

**Judge 12 · Sonia Kowalska — FWA juror, creative director** — 6/10
"FWA lighting: the light winners feel *painted* — a ground, then fields of colour laid on it, then paper elements floating on those. You have the paper. You forgot the fields."

**Judge 13 · Tobias ren Vries — CSS Design Awards juror** — 6/10
"Colour zones are cheap to ship and impossible to fake afterwards. Winners discovered this years ago; the technique even ships in page builders now — scroll-driven band transitions. An engineer-portfolio that doesn't use the single most available premium device is leaving points on the table."

**Judge 14 · Aiko Morita — Webby judge, editorial design** — 6/10
"Magazines sectionise with tinted grounds — the feature opener on a sage ground, the interview on a blush ground. It signals *you are somewhere new now*. Your site signals *you are somewhere, still*."

**Judge 15 · Daniel Okafor — Awwwards Developer Award juror** — 7/10
"Craft-wise this is top decile: tokens, audits, contrast discipline, OG art, JSON-LD. The bones would survive any jury. But jurors score the *screen*, and the screen is one colour. Craft got you to the final; the palette decides it."

**Judge 16 · Isabelle Fontaine — European Design Awards, brand juries** — 5/10
"Brand recall test: after one visit, describe the colours. For this site: 'cream, I think? And a teal button.' That is not a palette; that is a default with one accent. Winners get described in colour *sequences*."

**Judge 17 · Rahul Mehta — Bay Area product-design award juror** — 6/10
"Layered grounds also photograph. Every award submission is a set of stills; banded sections make thumbnails that look like a system, not a document."

**Judge 18 · Clara Voss — a11y-in-design award juror** — 7/10
"Note what I am *not* saying: no judge here wants dark mode or heavy contrast. The layered-light approach — distinct light bands, deepened wells, one disciplined accent — is fully compatible with AA/AAA. You can have both; you currently have neither layering nor a reason your AA discipline should impress anyone."

**Judge 19 · Erik Sandström — Motion-arts juror, Cannes Lions shortlist** — 6/10
"Colour should *participate* in the scroll narrative — the world warming as you approach the contact act is storytelling. Right now colour refuses the invitation; the narrative is carried by type alone."

**Judge 20 · Paloma Reyes — Independent juror, 40+ award juries** — 6/10
"My one-line scorecard for light sites: *does the background have a biography?* Dawn → work → craft → maker → beginning is a five-act biography. Ship five grounds and the biography becomes visible."

**Panel B consensus (avg 6.0):** the award circuit's light-theme winners run visible multi-band colour journeys; this build runs one. This is the single largest score gap to close, and it is closeable with existing craft.

---

### PANEL C — BRAND & IDENTITY STRATEGISTS (Judges 21–30)

**Judge 21 · Nadia Kapur — Brand strategist, identity systems** — 5/10
"A colour identity is what remains after greyscale-testing your screenshots. This site fails the greyscale test in reverse: it is *already* nearly greyscale. No brand owns 'slightly warm ivory #F7F4EC.' Many rent it."

**Judge 22 · Grant Whitfield — Verbal/visual identity director** — 6/10
"First Light named a moment. Strata would name a *structure*. The upgrade writes itself: the same dawn, decomposed into layers the visitor can walk through. Own 'the layered dawn' — nobody else has it."

**Judge 23 · Amara Diallo — Positioning strategist, solo-studio practices** — 6/10
"You sell six services and ship one colour. A layered system can *assign* colour zones to service families — instant mental shelf-space for visitors choosing between them."

**Judge 24 · Søren Vestergaard — Design-ops lead, Fortune-500 rebrands** — 6/10
"Token architecture is already single-source-of-truth. Adding a band layer is a ~1-day change *because the bones are this good*. The audit scripts even exist. This is the cheapest premium upgrade the brand will ever get."

**Judge 25 · Yumiko Sato — Colour-brand researcher, Tokyo** — 5/10
"Kisetsu — season-sense — is layered colour time. Your dawn metaphor is seasonal; a flat ivory page is seasonless. Bands give the page its kisetsu."

**Judge 26 · Ben Okello — CMO-turned-juror, B2B services** — 6/10
"Buyers remember journeys in colour blocks: 'the green part was services, the pink part was contact.' Chromatic wayfinding shortens the path to the form. One colour lengthens it."

**Judge 27 · Francesca Lombardi — Luxury-house digital director** — 5/10
"Luxury light sites layer materials: parchment on silk on lacquer. Digital equivalents are tinted grounds at distinct lightness with hairline separations. You have paper on paper on paper."

**Judge 28 · Devika Menon — Personal-brand consultant, engineering portfolios** — 6/10
"Your differentiator is end-to-end seniority. The site should *feel* engineered in its colour. A documented, measured, contrast-verified layer stack is colour-as-engineering — a portfolio piece about how you build."

**Judge 29 · Jakob Halvorsen — Naming and sensory brand strategist** — 6/10
"STRATA. Name the system and it becomes proprietary. Unnamed, it is 'some backgrounds I tinted.'"

**Judge 30 · Renata Aquino — Cultural colour strategist, LATAM markets** — 6/10
"Layered light reads as *morning optimism with structure* — precisely the emotional register a solo senior engineer should project. Flat ivory reads as caution."

**Panel C consensus (avg 5.7):** no ownable identity without visible colour architecture; the layer system converts an aesthetic preference into a brand asset.

---

### PANEL D — UX, HIERARCHY & WAYFINDING (Judges 31–40)

**Judge 31 · Dr. Lena Fischer — UX researcher, scroll behaviour studies** — 6/10
"Without background landmarks, scroll position is unmoored — users can't tell how far they've come or what region they're in. Bands are landmarks; they measurably improve orientation."

**Judge 32 · Marcus Chen — Design-systems lead, enterprise SaaS** — 6/10
"Atlassian got this right years ago: sunken / default / raised / overlay, each a different surface colour. You implemented the elevation shadows and skipped the elevation colours. Half the spec, half the effect."

**Judge 33 · Priya Raghavan — Accessibility & UX auditor** — 7/10
"Your contrast discipline is genuinely excellent — 10.6:1 ink, verified pairs. Now extend the same rigour to the band layer: every ink verified against every stratum. You've proven you can; do it once more."

**Judge 34 · Tomás Ferreira — Interaction designer, onboarding flows** — 6/10
"Distinct section grounds reduce cognitive load: the eye localises content by colour before reading a word. One ground forces the type to do all the work."

**Judge 35 · Hana Jansen — Usability lab director, eye-tracking** — 6/10
"Heatmaps on single-ground pages show uniform skim. Tinted bands produce *zone dwell* — the gaze pauses at each transition. That pause is where your section-index labels finally get read."

**Judge 36 · Omar Haddad — UX writer & information architect** — 6/10
"You numbered your acts — 01 proof, 02 craft, 03 maker, 04 beginning — then rendered the numbers in the same world. Chapter numbers deserve chapter colours."

**Judge 37 · Grete Lindqvist — Wayfinding specialist, spatial design** — 5/10
"Airports colour-code terminals; hospitals colour-code floors. Any journey longer than three screens needs the same mercy."

**Judge 38 · Kwame Asante — Product designer, fintech** — 6/10
"Cards-on-white is the default of every admin panel ever shipped. Cards-on-tinted-grounds is the signature of every portfolio worth remembering. Same components; different planet."

**Judge 39 · Dr. Miriam Katz — Cognitive psychologist, visual memory** — 6/10
"Memory encodes colour-context pairs. Mono-ground pages encode as one memory: 'a nice cream site.' Banded pages encode five — recall doubles."

**Judge 40 · Lucía Navarro — Service designer, journey mapping** — 6/10
"Your own copy says 'One connected journey, idea to launch.' Then the visuals refuse to travel. Make the colour travel with the copy."

**Panel D consensus (avg 6.0):** layering is a usability device as much as an aesthetic one; the current build outsources wayfinding entirely to typography.

---

### PANEL E — VISUAL & SYSTEMS DESIGNERS (Judges 41–50)

**Judge 41 · Victor Alamanni — Design-systems architect (ex-agency)** — 7/10
"The `.milk` context-class pattern you already use is *exactly* the mechanism bands need — override the context tokens per section and every component re-tints automatically. You invented the tool and never used it at scale."

**Judge 42 · Sasha Petrova — Design-token specialist, W3C community** — 7/10
"Semantic layering done right: `--vt-band` + per-band well/line overrides keeps raw hex out of components — your Law L9 survives intact. Most teams break their token law adding sections; you can keep yours."

**Judge 43 · Diego Ramos — Art director, editorial sites** — 6/10
"Give me five grounds and I'll give you a front page. The current one has the typography of a magazine and the paper stock of a fax."

**Judge 44 · Anne-Sophie Brou — Layout designer, print-to-digital** — 6/10
"In print we'd never run a feature across uniform stock. We change paper, we ink a solid, we flood a panel. Web bands are the same 400-year-old instincts."

**Judge 45 · Kevin Park — Principal designer, design-tooling company** — 6/10
"Chroma escalation with depth is the trick nobody names: bands slightly more chromatic than the canvas, wells slightly more chromatic than the bands. Depth and colour reinforce each other. Your chroma is flat at 0.01 everywhere — depth carries no colour information."

**Judge 46 · Beatriz Costa — Visual designer, surface & material research** — 5/10
"A milk plane floating on sage, floating on porcelain: three depths, three temperatures, one glance reads all of it. A milk plane on porcelain reads as… a margin."

**Judge 47 · Anders Nielsen — CSS architect** — 7/10
"Implementation cost is trivial: one new token block, four band classes, an act-class re-skin. The build script and audit scripts need no structural change. I've rarely seen a bigger visual return per line of CSS."

**Judge 48 · Zoe Bennett — Design QA lead** — 6/10
"Your banlist and contrast audits already gate deploys. Add a band audit — assert each act's computed background differs from its neighbour by ≥3% luminance or ≥25° hue — and the layering can never silently regress. That's a premium *process*, not just a premium look."

**Judge 49 · Hiro Yamada — Design engineer, motion systems** — 6/10
"Bands also upgrade motion for free: reveal animations can ease the band in slightly after the content, and hover states can borrow the band's well colour. The system compounds."

**Judge 50 · Caterina Rossi — Design-systems director, consultancy** — 6/10
"Every layer you add must be *chosen against the stack below it* — that is the whole art. Not 'a nice green': the green that is optimal ON this ivory, at this lightness step, with this well tint beneath its cards. The owner's instinct is textbook; honour it literally."

**Panel E consensus (avg 6.1):** the implementation path is already paved by the codebase's own patterns; the selection law (each layer optimal on the composite below) is the design work to document.

---

### PANEL F — ART DIRECTION & MOOD (Judges 51–60)

**Judge 51 · Odile Garnier — Art director, fashion campaigns** — 5/10
"A dawn without a blush band and a gold horizon is a fog. You wrote the sky and rendered the fog."

**Judge 52 · Jun-seo Park — Art director, Korean beauty brands** — 6/10
"K-beauty palettes: cream base, celadon wash, blush glow, gold fleck — all light, all visible. That is the register. Your peacock-and-ivory is two notes of a seven-note scale."

**Judge 53 · Maren Holt — Editorial art director, interiors magazines** — 6/10
"Interior photography styles rooms exactly as your sections should be styled: wall colour, then upholstery on the wall colour, then accents on the upholstery. Room by room, a hue journey. You styled one wall colour and called every room the same."

**Judge 54 · Luca Farinelli — Cinematographer, colour grading** — 6/10
"Every colourist grades in zones — sky, mids, skin, highlights — each pushed differently. A one-LUT page is an ungraded page. Where is your tri-mood journey: cool morning → warm midday → golden evening?"

**Judge 55 · Tabitha Osei — Set designer, theatre** — 5/10
"Acts need ground. The stage floor changes with every act — that is how the audience knows the world changed. Your stage floor never changes."

**Judge 56 · Ravi Chandran — Illustration director** — 6/10
"Your own journey illustration — the winding path — understands layers: sky, hills, path, kite. The site around it forgot."

**Judge 57 · Elena Marchetti — Packaging art director, premium foods** — 6/10
"Shelf-standout is 3-layer: substrate, ground ink, detail ink. Single-layer packs look store-brand regardless of typography. This site is typed like a maison and grounded like a store-brand."

**Judge 58 · Felix Braun — Museum exhibition designer** — 5/10
"Galleries paint walls per exhibition — sage for the ceramics room, oxblood— no, forgive me, *rose* for the textiles (the light law stands). Wall colour is curation. Unpainted walls are storage."

**Judge 59 · Mina Aoki — Trend forecaster, colour houses** — 6/10
"The next award cycle's light-theme language is already visible: layered pastel strata with disciplined deep accents. Early adopters win the cycle; late adopters inherit the cliché. You are early — for once."

**Judge 60 · Børge Dahl — Art director emeritus, Scandinavian design** — 6/10
"Our whole school is light + layer: one snow field, ten blues of shadow. The lesson was never 'use one light'; it was 'many lights, one world.' Take the lesson."

**Panel F consensus (avg 5.6):** the dawn metaphor is under-rendered; the palette has the notes but never plays the chord.

---

### PANEL G — ACCESSIBILITY & INCLUSIVE DESIGN (Judges 61–70)

**Judge 61 · Dr. Amara Ochieng — Accessibility researcher, low-vision studies** — 7/10
"Contrast is not the enemy of layering — *unmeasured* layering is. Your ink ladder holds 10.6:1/6.6:1/5.2:1 headroom; spending 2–4 points of it on tinted bands still lands AA/AAA everywhere. The headroom was banked for exactly this day."

**Judge 62 · Peter Novák — WCAG auditor, EU public sector** — 7/10
"Verify the full matrix — every ink on every stratum, every well, every plane — and layering becomes an accessibility *asset*: section boundaries become perceptible without relying on headings."

**Judge 63 · Rukhsana Khan — Assistive-tech tester, screen readers** — 7/10
"Colour zones change nothing for non-visual users — landmarks and headings already work. No harm, pure gain for sighted low-vision users who lose their place on uniform fields."

**Judge 64 · David Lindgren — Colour-vision-deficiency simulator specialist** — 6/10
"Deuteranopia check: sage vs powder can collapse — so differentiate bands by *lightness as well as hue*, never hue alone. Your instinct for lightness ladders makes this easy."

**Judge 65 · Amélie Rousseau — Inclusive design lead, civic tech** — 6/10
"Bands aid cognitive accessibility: predictable colour-to-meaning mapping reduces processing load. Just keep the mapping stable — same service, same family, everywhere."

**Judge 66 · Jide Afolayan — Auditor, motor accessibility** — 7/10
"Nothing here touches keyboard or pointer behaviour. Ship it."

**Judge 67 · Wen Li — Contrast-tooling engineer** — 7/10
"Automate the matrix in CI — you already have scripts; extend the surface list. A PRD that specifies which tokens may sit on which surfaces is auditable forever."

**Judge 68 · Gustav Berg — Print accessibility, dyslexia studies** — 6/10
"Uniform low-contrast cream fields are harder for dyslexic readers than gently banded structure — edges help tracking. Wells give text regions a containing shape."

**Judge 69 · Norah Ellis — Inclusive brand consultant** — 6/10
"The light-world mandate and accessibility are allies, not rivals. The ban on dark was a ban on *unreadable*; this upgrade must not smuggle contrast erosion back in via pastels."

**Judge 70 · Dr. Kofi Mensah — Ophthalmologist, digital eye strain** — 6/10
"Gentle hue travel across a page reduces fixational fatigue versus a single achromatic field. Layering is literally restful."

**Panel G consensus (avg 6.5):** layering is compatible with the WCAG discipline already in place, provided the full ink×surface matrix is recomputed — which this codebase is uniquely positioned to do.

---

### PANEL H — CONVERSION & BUSINESS (Judges 71–80)

**Judge 71 · Sofia Almeida — CRO strategist, services funnels** — 6/10
"Colour zones guide: warm blush ground under the contact act primes approach behaviour; sage under services primes 'considered, calm competence.' One ground primes nothing."

**Judge 72 · James Whitcombe — B2B lead-gen consultant** — 6/10
"Buyers scan, then dive. Bands make the scan phase legible: 'the green section had the six services' is a buying committee's shared language after the call."

**Judge 73 · Ananya Iyer — SaaS marketing director** — 6/10
"Every landing-page test I've run: tinted section grounds lift scroll-depth 5–15% versus uniform white. It is the cheapest conversion win on the page."

**Judge 74 · Mikkel Sørensen — Agency owner, 20-person studio** — 6/10
"When I hire subcontractors, a layered, documented colour system signals process maturity. It closes deals with people who never notice colour consciously."

**Judge 75 · Grace Njeri — Solo-consultant brand coach** — 6/10
"Premium is felt in 3 seconds. In that window, layered colour reads as 'designed'; monochrome reads as 'typed.' You have 3 seconds to say premium — say it with strata."

**Judge 76 · Tomás Aguilar — Pricing-page specialist** — 6/10
"Your honest starting prices sit on the same ground as everything else. A calm sage plane under pricing is the classic de-risking move — quiet context for numbers."

**Judge 77 · Hélène Dubois — Enterprise buyer, retail-tech** — 6/10
"I shortlist from portfolios at 11pm, tired. The ones I remember next morning had colour journeys. I remembered yours as 'nice cream.' Fix that."

**Judge 78 · Raj Patel — Founder, D2C brand (his checkout case study)** — 7/10
"He rebuilt my checkout and conversion rose 31%. Now his own site has a conversion problem: it doesn't convert its own quality into memory. Layers would."

**Judge 79 · Emma Kovács — Content strategist** — 6/10
"Case studies open with drama — your case pages deserve their own ground colour per project, like album covers in a record bin."

**Judge 80 · Dara Wilson — Growth lead, marketplaces** — 6/10
"Attention decays predictably down a page; hue changes reset it. You are leaving free attention on the table at every act boundary."

**Panel H consensus (avg 6.1):** layered colour is measurable revenue infrastructure for a services site, not decoration.

---

### PANEL I — MOTION, SCROLL & CRAFT (Judges 81–90)

**Judge 81 · Noa Kirschenbaum — Scroll-experience designer** — 6/10
"Your GSAP reveals move content against a static world. Let the world itself change between acts and every existing animation gets a stage."

**Judge 82 · Filippo Conti — Creative technologist** — 7/10
"A 700ms cross-fade of the page ground between acts is 15 lines of JS against your existing motion tokens — or zero JS if each act simply owns its band. Either way: cinematic."

**Judge 83 · Asta Bergmann — Motion systems lead** — 6/10
"Respect reduced-motion: static bands by default, transitions only for those who opt in. Your preloader discipline shows you already think this way."

**Judge 84 · Kenji Watanabe — WebGL artist (your horizon shader)** — 7/10
"The shader already owns the dawn: zenith, ribbon, glow. Extend the ramp with a blush stop and the hero teaches the page's layer grammar before the first scroll."

**Judge 85 · Marta Ruiz — Front-end performance engineer** — 7/10
"Zero JS cost, zero layout cost, ~40 lines of CSS. Largest Contentful Paint unaffected. Show me another premium signal with this cost profile."

**Judge 86 · Oskar Lindholm — Type designer** — 6/10
"Your serif italics pop beautifully on tinted grounds — blush behind 'shipped.' is the hero moment your type is asking for."

**Judge 87 · Deepa Nair — Design engineer, documentation systems** — 7/10
"A PRD with per-layer selection laws, contrast matrices and audits is your résumé in document form. Clients pay retainers to teams that write like this."

**Judge 88 · Caleb Wright — Portfolio reviewer, 500+ reviewed** — 6/10
"The 'one connected journey' rail is your best composition — and it's the one begging for its own powder ground. Give the centrepiece its own sky."

**Judge 89 · Siri Halvorsen — Interaction sound & feel designer** — 6/10
"Multisensory coherence: sections should 'sound' different. Colour zones are the visual equaliser."

**Judge 90 · Bram Visser — Site-of-the-month curator** — 6/10
"Feature this: 'An engineer who grades his own colours in OKLCH and publishes the audit.' The story writes the award submission."

**Panel I consensus (avg 6.3):** the layering upgrade compounds with every existing strength — motion, type, craft documentation — at near-zero performance cost.

---

### PANEL J — THE OWNER'S PANEL (Judges 91–100)

*Ten judges channel the mandate verbatim — the intuition given by the owner, stated as formal findings.*

**Judge 91 · The Instinct** — 5/10
"'Background completely layer one, a colour; on layer one, layer two — a different colour best on layer one; layer three on layer one plus layer two.' The build ships none of this. Verdict: mandate unimplemented."

**Judge 92 · The Layer Count** — 5/10
"'It may have more layers also.' A six-layer stack — ground, stratum, plane, well, marks, ink — is the minimum that reads as premium. Current visible layers: two (ivory, peacock)."

**Judge 93 · The Combination Test** — 5/10
"'There is no colour combinations.' Measured: 97% of pixels in one hue family. Combinations present in tokens, absent from the screen."

**Judge 94 · The Not-Award-Winning Test** — 6/10
"'Now it's OK but not award winning.' The tribunal agrees precisely: 6/10 average — a technically excellent, emotionally uniform site."

**Judge 95 · The Research Demand** — 6/10
"'Do deep research now properly.' The systems that define layering — Material 3 roles, Atlassian elevations, semantic bg layering — are documented and citable. This round, they're cited."

**Judge 96 · The Light Law** — 9/10
"'No dark, black, brown — anywhere, including background.' Round 1's achievement stands unbroken; this panel guards it while layering proceeds. Highest score on the site."

**Judge 97 · The Premium Bar** — 5/10
"'I don't want basic, it should be premium.' Basic is one colour done well. Premium is many colours done as one."

**Judge 98 · The Oracle Constraint** — 8/10
"'I'll deploy on Oracle free tier.' Static bands cost nothing to serve; the upgrade survives the $0 stack perfectly."

**Judge 99 · The Full-Stack Claim** — 6/10
"'Web, mobile, UI, AI, cloud, custom.' Six services deserve at least four grounds. Colour arithmetic."

**Judge 100 · The Final Word** — 6/10
"The owner said 'I gave the intuition.' The tribunal returns it as law: **every layer must be chosen against every layer beneath it — and every layer must be visible.** Build the STRATA system."

**Panel J consensus (avg 6.1):** the mandate is unambiguous, achievable, and fully compatible with every standing constraint.

---

## PART 2 — THE VERDICT

### 2.1 — Score summary (theme-domain score, /10)

| Panel | Focus | Avg |
|---|---|---|
| A | Colour science & theory | 5.8 |
| B | Award-site jurors | 6.0 |
| C | Brand & identity | 5.7 |
| D | UX & wayfinding | 6.0 |
| E | Visual & systems design | 6.1 |
| F | Art direction & mood | 5.6 |
| G | Accessibility & inclusion | 6.5 |
| H | Conversion & business | 6.1 |
| I | Motion, scroll & craft | 6.3 |
| J | The owner's panel | 6.1 |
| **TRIBUNAL AVERAGE** | | **6.0 / 10** |

Round 1 scored the dark theme ~2.4/10. First Light rescued it to **6.0 — "competent, calm, and forgettable."** The gap from 6.0 to the 8.5+ award zone is, by the tribunal's agreement, almost entirely the **missing layer architecture**.

### 2.2 — The unified finding

> **First Light built a flawless floor and forgot to build the room.** The craft (tokens, audits, motion, type, content) is top-decile and every judge says so. But 97% of every rendered pixel sits in one hue family; the washes are measurably sub-perceptual; the scroll journey has no colour chapters; the dawn metaphor is rendered without its bands. The site is *OK* — the owner's own word — and OK is the enemy of award-winning.

### 2.3 — The directive (unanimous, 100/100)

1. **Keep** the light world and all standing laws: no black, no brown, no dark shades — anywhere, backgrounds included.
2. **Build STRATA** — a formal layered colour system: L1 ground → L2 tinted strata bands → L3 milk planes → L4 band-tinted wells → L5 marks & hairlines → L6 ink. Each layer's colour *chosen against the composite of all layers beneath it*, per the owner's instinct, with documented selection laws.
3. **Make the layers visible**: band-vs-ground ≥3% luminance delta or ≥25° hue step; plane-vs-band ~10%+; well-vs-band ~7%. No more sub-JND washes.
4. **Run a band rhythm** through every page: the homepage acts get distinct grounds (dawn hero → porcelain proof → sage craft → powder maker → blush beginning); inner pages inherit their theme's ground.
5. **Re-verify everything**: full ink×surface contrast matrix, banlist, link QA, pixel audit — then re-audit with a measured colour-variety gate so layering can never silently regress.
6. **Ship it as engineering**: tokens.css + palette.py single-source, band context classes, audits in CI — colour as infrastructure, matching the site's own thesis.

*The tribunal adjourns and reconvenes as the research board for VT-PRD-005 — STRATA, the Layered Light System.*
