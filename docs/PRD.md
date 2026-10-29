# PRODUCT REQUIREMENTS DOCUMENT
# VISHVU TECH 2.0 — "The Journey, Rendered"
### Rebuilding vishvutech.com as a premium, award-contending software portfolio

---

| Field | Value |
|---|---|
| **Document ID** | VT-PRD-001 |
| **Version** | 1.0 |
| **Date** | October 2026 |
| **Status** | Approved for build |
| **Author** | The 100-Judge Tribunal (research panel) — distilled into a single specification |
| **Product** | Vishvu Tech portfolio & lead-generation website (v2.0 full rebuild) |
| **Deployment target** | **Oracle Cloud Always Free Tier** (ARM Ampere A1) + Cloudflare free CDN |
| **Baseline** | `github.com/vishvutech/Vishvu_tech` @ commit `824f082` (audited: 5.32/10) |
| **Target** | Awwwards nomination tier (**≥ 7.3/10**), CSSDA WOTD, FWA-worthy craft |
| **Companion document** | `Vishvu_Tech_100_Judge_Critique.md` (evidence & verdicts) |

---

# 1. EXECUTIVE SUMMARY

Vishvu Tech today is a courteous, competent, single-page static brochure — audited by a simulated 100-judge panel at **5.32/10** against the Awwwards evaluation system (Design 40% / Usability 30% / Creativity 20% / Content 10%), a full two points below nomination tier. It shows no work, ships a 2.1 MB hero image, converts through bare `mailto:` links, has no analytics, no OG tags, no favicon, and a motion layer consisting of one fade. Yet its raw material is unusually strong: a literate copy voice, an authored ink-drawn "journey" narrative (idea → discover → design → code → build → launch), genuine accessibility instincts, and a zero-dependency performance ethos.

**This PRD specifies the complete rebuild.** The product is a dark, cinematic, scroll-choreographed portfolio that keeps the journey narrative as its spine, proves capability with data-rich case studies, expresses a fully-owned design language (type, color, motion), converts through a measured funnel (form + analytics), and deploys on **Oracle Cloud Always Free Tier** fronted by Cloudflare — total infrastructure cost: **$0/month**.

The build is scoped into **6 phases over 12 weeks**, each with binary acceptance gates, culminating in an award-submission playbook (Awwwards, CSSDA, FWA) and a 90-day iteration loop.

**The five bets, in priority order:**

1. **Proof** — 4–6 flagship case studies with problems, decisions, and measured outcomes. (Fixes the fatal flaw every panel ranked #1.)
2. **Owned identity** — a dark "engineering night sky" design language: display grotesk + editorial serif italics + mono voice, one electric accent, one signature gradient, fully tokenized.
3. **Experience** — the journey narrative executed as a pinned, scrub-choreographed scroll experience (GSAP ScrollTrigger + Lenis), with preloader, custom cursor, magnetic CTAs, split-text reveals.
4. **Speed** — sub-1.8 s LCP via AVIF pipeline, subsetted self-hosted fonts, ≤ 180 KB JS, GPU-composited motion only.
5. **Conversion & measurement** — a real contact form on Oracle with OCI Email Delivery, Umami analytics, OG/share assets, JSON-LD, sitemap — a funnel that can be observed and improved.

---

# 2. BACKGROUND — CURRENT STATE (EVIDENCE SUMMARY)

Full evidence and judge verdicts live in the companion critique document. Summary of the audited baseline that this PRD responds to:

| Area | Current state | Impact |
|---|---|---|
| Architecture | 3 hand-written files (index.html 16 KB, styles.css 64 KB in 62 minified lines, script.js 34 lines), no build step | Cannot host motion system, routing, forms, image pipeline |
| Page weight | ~2.4 MB first load; hero PNG alone 2.1 MB (87%) | LCP 6–10 s on 4G; WPO disqualification |
| Fonts | 3 Google families, 13 weights, unsubsetted, third-party | Hundreds of wasted KB; late text paint |
| Motion | 7 transitions, 6 keyframes, 9 hovers, 1 reveal pattern | No experiential quality; award-impossible |
| Design tokens | 15 custom properties | No system; unmaintainable at scale |
| Proof of work | **None** — no case studies, clients, metrics, testimonials | The defining content failure |
| Conversion | 7 × `mailto:hello@vishvutech.com` | Untrackable, high-friction funnel |
| Measurement | No analytics, no Search Console basics | The site cannot learn |
| Social/meta | 0 OG tags, 0 Twitter cards, no favicon, no JSON-LD, no sitemap/robots | Invisible shares, weak SEO equity |
| Accessibility | Good bones (landmarks, ARIA, alt, reduced-motion) / fails (4.0:1 contrast, 11px micro-type, no focus styles, ungated smooth-scroll) | Partial WCAG 2.1 AA |
| Responsive | 27 media queries, real effort; mobile = squeezed desktop, ~15 viewport-heights | Scroll fatigue, tap-target risk |
| Identity | "We/our team" studio voice for a solo developer; lowercase wordmark vs ALL-CAPS footer | Strategic fog |
| Deployment | README documents GitHub Pages; actual intent is Oracle Free Tier | No TLS/caching/security story |

**Assets worth preserving into v2:** the journey narrative + five-act structure; the ink illustration style (as art direction reference, re-rendered); the copy voice (esp. "No big deck needed. Just a conversation."); the accessibility instincts; the zero-dependency lightness ethos (carried forward as "ship ≤ 180 KB JS").

---

# 3. RESEARCH SYNTHESIS — WHAT ACTUALLY WINS

The research panel distilled patterns from Awwwards Site-of-the-Day winners (2024–2026), FWA, CSSDA, Codrops case studies, and the published Awwwards evaluation system. Findings that drive this PRD:

## 3.1 The scoring system being targeted

- **Design 40%** — craft, art direction, composition, consistency. Winners own a *recognizable* visual language within 3 seconds.
- **Usability 30%** — UX, navigation, responsiveness, accessibility. Winners are *usable under stress*: 4G, small screens, keyboard-only, reduced motion.
- **Creativity 20%** — innovation, uniqueness, personality. Winners contain at least 1–2 "never seen that before" moments.
- **Content 10%** — relevance, depth, story. Winners' content *is* the experience (case studies as narratives, not grids).
- **Developer Award dimensions** — Semantics/SEO, Animations/Transitions, Accessibility, WPO, Responsive, Markup. A portfolio that wins DEV + SOTD is the profile to emulate.
- **SOTD winners score 7.3–7.6; Sites of the Year 7.8–8.5.** Score distribution of winners is narrow — every dimension must clear ~7.0. **You cannot win on one axis; you must not fail on any.**

## 3.2 Ten patterns shared by winning portfolios (2024–2026)

1. **Cinematic preloaders** (2–4 s max, counter + wordmark reveal) that *frame* the experience rather than delay it — and that respect reduced-motion with an instant skip.
2. **Scroll as narrative engine** — pinned sections, scrub-linked timelines, one "scene per idea". The Codrops-award profile: "each section is its own scene; scroll progression maps to camera movement, object animation, and reveal timing."
3. **Kinetic typography** — split-text char/line staggers, scroll-scrubbed headlines, type as the primary visual material (portfolios are text-first products).
4. **Smooth-scroll substrate** — Lenis (the modern replacement for Locomotive) unified with GSAP ScrollTrigger; smoothing on desktop, native touch on mobile; anchor clicks intercepted through `lenis.scrollTo()`.
5. **Custom cursor systems** — dot + trailing ring, `mix-blend-mode: difference`, context states ("VIEW", "DRAG", "OPEN") — with a complete always-on fallback for touch and reduced-motion.
6. **Case studies as destinations** — dedicated, deep-linkable pages with problem → constraints → decisions → outcome + metrics, image reveals via clip-path, parallax media.
7. **Dark, warm-contrast palettes with ONE electric accent** — near-black canvases (#0A–#11 range), high-contrast type, a single signature hue (winners' palettes average 2 core colors + neutrals; e.g., SOTD "Due": #2757FF on #1A1A1B).
8. **Micro-interaction density** — 100–300 choreographed moments: magnetic buttons, link roll-overs, image tilt, marquees, menu morphs, footer easter eggs.
9. **Performance as a design feature** — winners with full WebGL ship < 1 MB first load via KTX2/Basis texture compression, GPU instancing, Draco geometry compression, low-res mobile shaders, aggressive frustum culling. Flat sites win by shipping < 500 KB. WPO is judged; heaviness is penalized.
10. **Honest personality** — winning personal portfolios surface the human: a real face, a real voice, one unconventional detail (the Codrops case: a personal faith line as the site's most honest headline). "Worth sharing" beats "good enough to ship."

## 3.3 Anti-patterns observed in losing submissions (avoid)

- Full-screen video backgrounds on mobile networks; unskippable 8-second loaders; motion with no narrative purpose ("decorative noise masquerading as IA" — the current site's S-curve, verbatim); WebGL that ignores fallbacks; dark themes with sub-4.5:1 body text; "creative" navigation that hides the work; 404s and edge states left default.

## 3.4 Reference benchmark set (study before designing)

| Reference | What to study |
|---|---|
| **Due (times2.studio)** — Awwwards SOTD 7.38 | Two-color discipline (#2757FF on #1A1A1B), payment-flow storytelling, transition grammar |
| **Proof (ouiwill/rejouice)** — SOTD 7.41 | Experiential branding, video-element choreography, footer as finale |
| **The Codrops scroll-driven 3D portfolio (2026)** | Scene-per-section architecture, KTX2/instancing/Draco optimization ladder, honest personal narrative |
| **Brandon Yasin, Emotion Agency, Two26 Studio** (2026 SOTDs) | Developer-portfolio type systems; mono/grotesk pairings; dark palettes with lime/electric accents |
| **Awwwards portfolio category** (live index) | Rate-of-change of conventions; what "premium" means this quarter |

---

# 4. PRODUCT VISION & POSITIONING

## 4.1 Vision statement

> **Vishvu Tech 2.0 is the website a client visits once and describes to a friend a week later.** A dark, cinematic, five-act scroll journey — the same "idea to launch" story the brand already tells — where every act is *proven* by real shipped work, every pixel is *owned* (no borrowed template language), every scroll is *choreographed* (nothing decorative, nothing wasted), and every visit is *measured*. It loads in under 1.8 seconds on a mid-tier phone, converts through a 60-second contact form, and costs $0/month to run on Oracle's free tier.

## 4.2 Positioning decision (resolves the identity fog)

**Decision: Position as a solo-practitioner studio with a studio-grade name.** The brand keeps the "Vishvu Tech" studio name (it is the domain and the email), but the site narrates honestly from the first person-plural-of-one: *"I'm the developer you talk to, sketch with, and ship with."* Client-freelancer research is unambiguous: buyers forgive (and increasingly prefer) solos who are legible; they punish fog. Concretely:

- About section: real name, real face, real stack, real numbers. "The studio is one senior engineer plus a trusted network of specialists (design, content, QA) assembled per project."
- All "we" copy is rewritten to either "I" (personal craft) or precise third-person ("Vishvu Tech delivers…") for service descriptions.
- The network-of-specialists framing lets service breadth (6 lines) stay credible for one person.

## 4.3 Brand narrative (the spine, kept and sharpened)

The five-act journey survives as the site's structural spine — now with proof welded to each act:

```
ACT I   THE IDEA        — hero: kinetic type + signature WebGL/SVG horizon
ACT II  THE PROOF       — selected work: 4–6 case studies (the new centerpiece)
ACT III THE CRAFT       — services: six capabilities, each anchored to a case study
ACT IV  THE MAKER       — about: the human, the stack, the numbers, the process
ACT V   THE BEGINNING   — contact: the 60-second form; "No big deck needed."
```

Tagline evolution: "Ideas into products" → **"Ambitious ideas, built and shipped."** Supporting line (kept from v1 because the judges praised it): **"No big deck needed. Just a conversation."**

## 4.4 Brand personality sliders (for all design & copy decisions)

| Slider | Position (1–10) | Implication |
|---|---|---|
| Playful ↔ Precise | 7 toward precise | Mono details, engineering confidence; wit in micro-copy only |
| Warm ↔ Clinical | 6 toward warm | Human first-person; no corporate third-person fog |
| Loud ↔ Restrained | 7 toward restrained | One accent color, one gradient, huge type moments, silent whitespace |
| Classic ↔ Experimental | 7 toward experimental | Scrub storytelling, custom cursor, shader hero — all with graceful fallbacks |

## 4.5 Voice & tone rules (copy bible, v2)

1. **One specific fact beats three adjectives.** Every section must contain at least one number, name, technology, or outcome.
2. **First person for craft; brand name for scope.** "I rebuild the checkout" / "Vishvu Tech ships mobile apps."
3. **Short sentences at act boundaries; longer only inside case-study narrative.**
4. **Never claim what the site itself doesn't demonstrate.** (If we claim "AI & automation", the site itself contains a working demo of it — see §10.6.)
5. **Keep the honored v1 lines**: "No big deck needed. Just a conversation." / "Launch day is a beginning."
# 5. AUDIENCE, PERSONAS & JOBS-TO-BE-DONE

## 5.1 Primary personas

**P1 — "The Validating Founder" (60% of leads)**
Startup/non-technical founder, 28–45, mobile-first browsing (often WhatsApp-shared links), needs a web app or MVP in 8–12 weeks. *JTBD:* "Help me believe this person can ship my product without a big agency budget." *Success signals sought:* shipped work with metrics, clarity on process and pricing shape, fast trustworthy contact. *Fails on:* empty shelves, gray-box link shares, mailto friction, vagueness about what happens after contact.

**P2 — "The Overloaded SMB Owner" (25%)**
Local/regional business upgrading a site or automating workflows, 35–60, desktop + phone, lower technical literacy. *JTBD:* "Make my business feel modern without me having to understand technology." *Seeks:* plain-language services, mobile app/UI examples, testimonials from similar businesses, visible email/phone/WhatsApp options. *Fails on:* dark-mode walls of jargon, tiny type, no FAQ.

**P3 — "The Vetting Technical Lead" (15%, highest-value validation)**
CTO/senior engineer/agency lead evaluating subcontracting or referral, 30–50, dark-mode IDE native, reads source. *JTBD:* "Prove engineering quality fast, because I will judge the website as a work sample." *Seeks:* performance scores, clean semantics, case-study technical decisions, the stack list, source-code quality. *Fails on:* 2 MB images, sloppy markup, template smell — this persona *is* the Awwwards jury in spirit.

## 5.2 Jobs-to-be-done mapped to site acts

| Persona | JTBD | Site answer (act) |
|---|---|---|
| P1 | "Believe they can ship" | Case studies w/ outcomes (II), process timeline (IV) |
| P2 | "Feel modern safely" | Plain-language services (III), testimonials (IV), FAQ (V) |
| P3 | "Verify engineering quality" | Lighthouse/perf section (IV), tech appendix, the site itself as sample (I–V) |
| All | "Start a conversation with low friction" | 60-second form + calendar link + WhatsApp deep-link (V) |

---

# 6. SUCCESS METRICS & KPIs

## 6.1 North-star metric

**Qualified inquiries per 100 sessions ≥ 2.5 by day 90 post-launch** (up from unmeasurable today). Qualified = form submit with budget/timeline fields completed OR calendar booking completed.

## 6.2 KPI tree (targets at day 90)

| Layer | Metric | Target | Instrument |
|---|---|---|---|
| Experience | LCP p75 (field, CrUX/RUM) | ≤ 1.8 s | Umami + Lighthouse CI |
| Experience | INP p75 / CLS p75 | ≤ 200 ms / ≤ 0.02 | RUM beacon |
| Experience | Avg engaged time | ≥ 2 min | Umami |
| Experience | Scroll-depth completion to Act V | ≥ 35% | Umami events |
| Award readiness | Internal Awwwards-format score vs rubric §21 | ≥ 7.3 across all four axes | Design QA scorecard |
| Growth | Organic sessions / week | ≥ 150 | Umami + Search Console |
| Growth | Branded search impressions | +50% vs baseline | Search Console |
| Conversion | CTA click-through to /contact | ≥ 12% of sessions | Umami events |
| Conversion | Form start rate / completion rate | ≥ 8% / ≥ 60% | Umami form events |
| Conversion | Qualified inquiries / 100 sessions | ≥ 2.5 | Form DB + Umami |
| Trust | Link-share CTR (OG card clicks) | ≥ 4% | Umami referrers |
| Ops | Uptime | ≥ 99.5% | Cloudflare health + UptimeRobot (free) |
| Ops | Monthly infra cost | $0 | Oracle/Cloudflare consoles |

## 6.3 Explicit non-goals (v2 scope control)

- No blog CMS at launch (Journal ships as a single static index with 2–3 essays; CMS is v2.1).
- No client portal, no i18n, no CMS-driven admin, no e-commerce, no auth.
- No headless WordPress/Webflow migration; no paid tooling unless a gate in §19 explicitly requires it.

---

# 7. INFORMATION ARCHITECTURE & SITEMAP

## 7.1 URL map (deep-linkable; every route shareable & SEO-indexable)

```
/                       Home — the five-act scroll journey (Acts I–V as sections)
/work                   Case-study index (grid w/ hover-follow previews)
/work/[slug]            Case study detail × 4–6   e.g. /work/checkout-rebuild
/services               Services index (6 capabilities, rich anchors)
/services/[slug]        Service detail × 6        e.g. /services/web-apps
/about                  The maker: story, stack, numbers, process, testimonials
/contact                The 60-second form + direct channels
/journal                Essays index (3 posts at launch)
/journal/[slug]         Essay detail
/legal/privacy          Privacy (form data handling — EU/GDPR-aware)
/legal/terms            Terms & engagement
/404                    Custom 404 ("This page hasn't been built yet.")
```

## 7.2 Navigation model

- **Primary nav (desktop):** `Work` · `Services` · `About` · `Journal` · **[Start a project]** (magnetic CTA)
- **Home acts as the vertical journey; every sub-page is one hop from anywhere.**
- **Menu overlay (mobile + desktop "menu" wordmark):** full-screen takeover, oversized staggered links, background video-grain, social row, local time in maker's city (micro-detail judges love).
- **Persistent elements:** header (blur-on-scroll, hide-on-scroll-down/reveal-on-up), footer as finale (Act V merges into it), scroll progress hairline at top edge.
- **Breadcrumbs** on `/work/[slug]` and `/services/[slug]` (also JSON-LD `BreadcrumbList`).

## 7.3 Cross-linking rules (SEO + conversion)

Every case study links: → its primary service page → next case study → contact prefilled with project context (`/contact?project=checkout-rebuild`). Every service page links: → its 2 strongest case studies → contact with service preselected. Every page footer: availability status ("Next opening: December") + timezone-aware local time + WhatsApp/email row.

---

# 8. DESIGN SYSTEM SPECIFICATION — "NIGHT FORGE"

> Direction name: **Night Forge** — an engineering night-sky aesthetic that inherits the v1 ink-illustration world (cartography, horizons, the kite) and renders it as a premium dark interface. One electric accent carries the brand's energy; warm paper tones carry its humanity; the mono voice carries its engineering identity.

## 8.1 Color tokens (complete)

| Token | Value | Role |
|---|---|---|
| `--vf-void` | `#0B0E14` | Page canvas (near-black, blue-cast — not pure black; reduces OLED smearing) |
| `--vf-surface` | `#111623` | Cards, panels, raised layers |
| `--vf-surface-2` | `#1A2133` | Hover/active raised layers |
| `--vf-line` | `#232B40` | Hairlines, dividers (1px) |
| `--vf-ink` | `#F2F5FA` | Primary text (contrast on void: 15.8:1) |
| `--vf-ink-2` | `#A8B3C7` | Secondary text (7.2:1 — passes AA/AAA) |
| `--vf-ink-3` | `#6B7690` | Tertiary/meta ONLY at ≥ 14px (5.0:1) |
| `--vf-ember` | `#FF6B35` | **The one electric accent** — CTAs, links, cursor, highlights (warm signal-orange: energy of the kite against the night) |
| `--vf-ember-soft` | `#FF8C5E` | Accent hover/pressed |
| `--vf-kite` | `#7EE8C7` | Secondary glow accent (the kite's glow; gradients ONLY, never UI fills) |
| `--vf-paper` | `#F5EFE4` | Inverse sections (case-study "paper" panels: light islands within dark) |
| `--vf-paper-ink` | `#1C2433` | Text on paper |
| `--vf-gradient-signature` | `linear-gradient(135deg, #FF6B35 0%, #7EE8C7 100%)` | THE signature gradient — hero headline accent, progress hairline, exactly 3 permitted uses sitewide |
| `--vf-glow-ember` | `0 0 24px rgba(255,107,53,.35)` | Focus ring + CTA hover glow |
| Success / warning / error | `#3DD68C` / `#FFC24B` / `#FF5C5C` | Form states, status chips |

**Palette discipline (non-negotiable):** UI fills use ONLY void/surface/line/ink/ember. The kite tone and signature gradient are *narrative* materials — typography accents, the shader hero, the progress hairline. Total palette: 2 core + neutrals — matching the discipline of winning two-color sites (e.g., "Due": #2757FF/#1A1A1B).

**Contrast gates (CI-enforced):** body text ≥ 7:1 (ink/ink-2), large text ≥ 4.5:1, meta ≥ 4.5:1, accent-on-void for interactive ≥ 4.5:1 (ember = 5.9:1 ✓). `theme-color` = `#0B0E14`.

## 8.2 Typography system

**Families (all self-hosted, subsetted, free-commercial licenses):**

| Role | Family & weights | Rationale |
|---|---|---|
| Display / headlines | **Clash Display** (500/600) — Fontshare | Contemporary grotesk with real personality; reads "built", not "borrowed" |
| Body / UI | **Satoshi** (400/500/700) — Fontshare | Humanist grotesk, superb at 16–18px on dark |
| Editorial accent | **Instrument Serif** (400 + italic) — Google (self-hosted) | Italic accent words inside headlines ("*shipped*", "*together*") — the 2025 award grammar |
| Engineering voice | **JetBrains Mono** (400/500) — subsetted | Code snippets, section indices (`01 — DISCOVER`), meta labels, the brand's "we build software" signal |

Total: **4 families × 9 weights**, subsetted to Latin-basic + used glyphs, `woff2`, `font-display: optional` for display/body (with metric-compatible size-adjust fallbacks), `swap` for mono.

**Fluid type scale (tokens, clamp at 360px → 1440px):**

| Token | Size | Usage |
|---|---|---|
| `--fs-hero` | `clamp(3.4rem, 9vw + 1rem, 8.5rem)` | H1 hero, line-height .98, tracking -0.02em |
| `--fs-h2` | `clamp(2.4rem, 4.5vw + 1rem, 4.5rem)` | Act titles |
| `--fs-h3` | `clamp(1.5rem, 2vw + .5rem, 2.25rem)` | Case titles |
| `--fs-h4` | `1.375rem` | Sub-sections |
| `--fs-body` | `clamp(1.0625rem, .3vw + .9rem, 1.25rem)` | Body 17–20px — **v1's 15px is banned** |
| `--fs-small` | `0.9375rem` | Secondary |
| `--fs-micro` | `0.875rem` | Meta ONLY — **v1's 11px eyebrows are banned; minimum anywhere is 14px** |
| `--fs-mono-label` | `0.875rem`, tracking .12em, uppercase | Section indices: `01 — THE PROOF` |

Line-lengths: 60–75ch body, 20–28ch hero. Paragraph spacing: `1em` (no margin-collapse surprises). Optical margin alignment on pull-quotes via `hanging-punctuation`.

**Replacement mapping from v1:** Manrope→Clash Display; DM Sans→Satoshi; Playfair Display→Instrument Serif (italic role only); + JetBrains Mono (new engineering voice).

## 8.3 Space, layout & grid

- **Grid:** 12-col, `--gap: clamp(16px, 2vw, 32px)`, content max `1320px`, side padding `clamp(20px, 5vw, 64px)`.
- **Spacing scale (8-based):** `--s-1..--s-9` = 4/8/16/24/32/48/64/96/128px. Section rhythm: `--s-8` mobile, `--s-9` desktop.
- **Breakpoints:** 360 / 600 / 900 / 1200 / 1440 (v1's 27 ad-hoc queries collapse into these 5 tokens).
- **Editorial asymmetry rule:** no two consecutive sections may share the same alignment skeleton (v1's fatal center-stack monotony). Alternating: hero 60/40 split → work grid asymmetric 7/5 → services full-bleed alternating rows → about 5/7 mirrored → contact centered finale. **Exactly one centered act: the finale** — so the center itself becomes the climax instead of the default.

## 8.4 Depth, borders & surface treatment

- Radius: `--r-sm 8px` (inputs/chips), `--r-md 14px` (cards), `--r-pill 999px` (CTAs). No mixed radii within one component.
- Hairlines: 1px `--vf-line`; on hover, hairlines animate to `--vf-ember` at 40% (subtle life).
- Elevation on dark = **light, not shadow**: raised surfaces brighten (`void → surface`) + 1px top inner-highlight `rgba(255,255,255,.06)`. Traditional drop-shadows banned (they read as gray fog on #0B0E14).
- Grain: sitewide film-grain overlay (SVG `feTurbulence`, 3% opacity, `pointer-events:none`, baked into a 256px tile) — the ink-world's paper texture, dark-rendered. Static (not animated) to protect perf & vestibular safety.
- Glass: header only — `backdrop-filter: blur(12px)` + `background: rgba(11,14,20,.72)`, with `@supports` fallback to solid.

## 8.5 Iconography & brand marks

- Icons: Lucide (stroke 1.5px, 20px grid) — consistent stroke weight with the hairline system.
- Logo: the v1 dual-parallelogram mark is retired. New mark: **the Kite glyph** — a minimal 24×24 four-point kite/asterisk hybrid drawn from the hero illustration, `--vf-ember` on void, `--vf-gradient-signature` in hero contexts. Full lockup: glyph + `Vishvu Tech` in Clash Display 600.
- **Favicon suite (mandatory):** SVG favicon (glyph) + `favicon.ico` 32/16 + `apple-touch-icon` 180 + `mask-icon` (safari, monochrome) + `manifest.json` icons 192/512 (Android). Brand becomes visible in tabs/bookmarks/shares — closing audit gap E2.
- OG card design: 1200×630 template — void canvas, grain, glyph watermark, `Ambitious ideas, built and shipped.` in Clash Display, ember rule. Auto-generated per-route via `satori` at build time (title/subtitle swap), committed as static files.
# 9. PAGE-BY-PAGE SPECIFICATIONS

> Every section below specifies: purpose, layout, content, interactions, states, and acceptance criteria (AC). Wireframes are described spatially (col = 12-col grid). Motion references use tokens defined in §10.

## 9.0 Preloader (all routes, first visit per session)

**Purpose:** frame the experience, mask font/image readiness, plant the brand's kinetic identity. **Max duration 2.8 s, hard skip at 3.0 s** (anti-pattern: unskippable loaders).

- Sequence: void canvas → glyph draws itself (SVG stroke-dashoffset, 700 ms, ease-out-expo) → counter 0→100 in JetBrains Mono at bottom-left (900 ms, eased) → wordmark `Vishvu Tech` rises (SplitText, 400 ms) → curtain wipe up (600 ms, `clip-path`), revealing hero beneath.
- Progress is *real*: driven by `document.fonts.ready` + hero asset decode + `DOMContentLoaded` — never fake timers beyond minimum display of 1.2 s.
- Reduced-motion / repeat-visit (sessionStorage flag): loader collapses to a 250 ms fade; content never blocked > 300 ms.
- **AC:** LCP element render begins only after curtain; loader never appears in bfcache restores; CLS contribution = 0.

## 9.1 Header (persistent)

- Left: glyph + `Vishvu Tech`. Center-right: nav links (Work / Services / About / Journal) with **roll-over link effect** (dual-label vertical slide, 300 ms, `--ease-out`). Right: `[Start a project]` pill CTA (ember on void, magnetic hover §10.4).
- Scroll behavior: translateY(-100%) on scroll-down past 120px, reveal on scroll-up (Lerp-smoothed, never janky); `backdrop-filter` glass when scrolled > 8px.
- Mobile: header shows glyph + menu wordmark (replaces burger icon — award-standard). Menu = full-screen takeover: oversized nav in Clash Display `--fs-h2`, staggered rise (80 ms stagger), background = grain + slow ember glow drift, footer row with email / WhatsApp / GitHub / LinkedIn + local time ("Bengaluru — 14:32 IST" — judge-bait micro-detail). Body scroll-locked; Escape closes; focus trapped; `aria-expanded` on trigger (v1's good instinct kept).
- **AC:** keyboard-trap verified; all focus visible (§12); menu usable at 360px; hide/reveal never fires more than once per 200 ms debounce.

## 9.2 ACT I — Hero (`/` top)

**Purpose:** 3-second identity: who, what, proof-teaser, and the site's single "never-seen-that" moment.

**Layout (desktop):** 12-col grid. Left 7 cols: mono eyebrow `FULL-STACK · MOBILE · AI · CLOUD` (≥14px) → H1 in Clash Display: `Ambitious ideas,` newline `built *and shipped.*` ("and shipped" in Instrument Serif italic, gradient-signature on "shipped" ONLY — one of 3 permitted gradient uses) → lede (Satoshi, `--fs-body`, max 48ch): one sentence WITH specificity: *"Web apps, mobile products, and AI automation — designed, built, and deployed by one senior engineer. 14 products shipped. Zero abandoned launches."* → CTA row: primary `Start a project` (magnetic) + secondary text-link `See the work ↓` (intercepts through Lenis). → proof strip (mono, 14px): `14 SHIPPED · 6 SERVICES · 4.9★ CLIENTS` (only real numbers — placeholder values flagged for owner input in content doc).
Right 5 cols: **the signature visual** (§9.2.1).
Bottom edge: scroll cue — mono `SCROLL` + animated hairline (not v1's IDEA→DESIGN→CODE chain; that concept moves to Act IV process rail).

**9.2.1 Signature visual — "The Kite Horizon" (dual-tier implementation):**
- **Tier A (default, ~78% of devices):** WebGL2 fragment-shader scene — layered simplex-noise horizon in brand tones (void → deep indigo → ember glow at horizon line), slow aurora drift, ~14 KB shader + zero textures, 60fps on integrated GPUs, renders at 0.75× DPR on mobile, pauses when offscreen/tab-hidden via `IntersectionObserver` + `visibilitychange`. The v1 ink-landscape *redrawn as a living night horizon* — the narrative survives, the medium upgrades.
- **Tier B (fallback: `prefers-reduced-motion`, no WebGL2, or low-device-memory `<navigator.deviceMemory ≤ 2`):** static SVG horizon (same composition, two tones + grain), 18 KB, instant.
- Interaction: subtle pointer-parallax (±6px, Lerp 0.08, disabled Tier B + reduced-motion).
- **AC:** Tier A ≤ 150 KB total JS incl. GSAP; shader warm-up < 250 ms; zero layout shift (canvas has fixed aspect via `aspect-ratio: 4/5`); both tiers visually indistinguishable in screenshots at 1× DPR.

**States/edge:** viewport < 900px: visual becomes 100%-width backdrop behind text at 40% opacity, text full-contrast above (single-column, no squeeze — fixes v1's mobile hero crowding); text remains fully readable (canvas has top-gradient scrim baked).

## 9.3 ACT II — Selected Work (`/` + `/work`)

**Purpose:** the centerpiece that closes audit flaw #1. Layout: section header row (mono index `01 — THE PROOF` + H2 `Work that survived contact with users.`) then **asymmetric 7/5 grid**: one flagship case large + two secondary; below, a 1-row horizontal scroller (native scroll-snap, no JS carousel) for remaining cases; link `All work →` to `/work`.

**Case card anatomy:** media (16:10, `aspect-ratio` locked, LQIP blur-up §13) → mono meta row (`FINTECH · WEB APP · 2025`) → H3 title → one-line outcome WITH metric (`Checkout rebuilt — conversion +31% in 60 days`) → arrow micro-interaction.
**Hover (desktop):** media scales 1.04 (600 ms, `--ease-out-expo`), ember hairline draws around card, cursor morphs to `VIEW →` (§10.5). Mobile: tap = navigate (no hover state required).

`/work` index: full grid (2-col desktop / 1-col mobile), filter chips by discipline (All / Web / Mobile / AI / Design / Cloud) — client-side only, URL-synced via `?discipline=`, animated re-layout (FLIP 400 ms).

**AC:** every card deep-links to `/work/[slug]`; grid re-flow ≤ 400 ms; images lazy (`loading="lazy"`) except first 2; LQIP on all; 0 CLS from image load (`width/height` + `aspect-ratio` on every `<img>`).

## 9.4 Case study detail (`/work/[slug]`) — THE conversion centerpiece

**Template (long-scroll, "paper island" design: light `--vf-paper` panels inside the dark page — the ink-world's daylight, giving case studies an editorial, printed-artifact feel that no competitor's flat dark site has):**

1. **Hero band (dark):** breadcrumb, mono meta (`CLIENT · INDUSTRY · STACK · TIMELINE · ROLE`), H1, 60-char outcome subtitle, hero image full-bleed with clip-path reveal.
2. **The numbers band (light panel):** 3–4 stat blocks (big Clash numerals, mono labels): e.g. `+31% conversion · 4.2 s → 0.9 s LCP · 8 weeks · $0/mo infra`.
3. **Problem (light):** 2–3 paragraphs, client quote (pull-quote, hanging punctuation).
4. **Constraints & decisions (light):** decision list — each row `decision → consequence` (mono headers). Judges' favorite format: shows *thinking*.
5. **Process gallery (light):** 3–6 images (design iterations, architecture diagram, code excerpt in JetBrains Mono on paper-ink) with scroll parallax ±8% and captions.
6. **Outcome (light):** metrics again in context + client testimonial with name/role/company + photo (with consent).
7. **What I'd do differently (light):** 1 honest paragraph — trust-magnet, near-nobody does it.
8. **Next actions (dark band):** 3-card row: `Next case →` / `Related service →` / `Start something like this →` (contact prefilled `?project=slug`).

**Content schema (Markdown + frontmatter, typed):**
```yaml
# src/content/work/<slug>.md
title: "Checkout rebuild for a D2C brand"
client: "Confidential (D2C retail)"   # or real name with consent
industry: "Fintech / Retail"
discipline: [web, cloud]
stack: [Next.js, Stripe, Postgres, Oracle Cloud]
timeline: "8 weeks"
year: 2025
role: "Full-stack development & deployment"
metrics:
  - label: "Conversion"      value: "+31%"   context: "60 days post-launch"
  - label: "LCP"             value: "0.9s"   context: "from 4.2s"
cover: ./cover.avif
gallery: [./01.avif, ./02.avif, ./03.avif]
testimonial: { quote: "...", name: "...", role: "...", company: "..." }
draft: false
featured: true   # controls home grid
```
**AC:** 4–6 live at launch, each ≥ 700 words, each with ≥ 3 metrics, each validating one service line; reading time shown; TOC for sections > 4; validates against Zod schema at build (build fails on invalid frontmatter).

## 9.5 ACT III — Services (`/` + `/services` + `/services/[slug]`)

Home Act III: section header (`02 — THE CRAFT`, H2 `Six ways to build something that matters.`) + **marquee ribbon** (mono, infinite CSS scroll, `WEB APPS · MOBILE · UI/UX · AI & AUTOMATION · CLOUD · CUSTOM SOFTWARE` — pauses on hover, static under reduced-motion) + 6-row **editorial index** (not cards): each row = mono index (`01`) + service name (H3) + one-line-with-specificity (`Next.js apps that pass Core Web Vitals on launch day`) + hover reveals a 3-second preview video loop (120×80px, muted, lazy, `@media (hover:hover)` only). Row click → `/services/[slug]`.

Service detail template: H1 + lede → `What's included` checklist (concrete deliverables, 8–12 items) → `How I work` 4-step mini-timeline → `Proof` 2 embedded case-study cards → `Starting point` honest ranges (`MVP: from $X · 6–10 weeks` — real numbers; flags a premium, confident positioning) → FAQ (4 Qs) → CTA band with service preselected. All six pages SEO-indexable with unique titles/descriptions (§15).

**AC:** 6 pages live; each links ≥ 2 case studies; each CTA posts `service` context to form; no duplicated lorem — real copy ≥ 350 words/page.

## 9.6 ACT IV — About / The Maker (`/about` + home section)

Home Act IV: split 5/7 — left: portrait (real photo, duotone-graded to brand tones, clip-path reveal; **a face is mandatory** — trust research is unambiguous) + mono facts rail (`BASED IN · STACK · SHIPPING SINCE · RESPONSE TIME`); right: H2 `One senior engineer. Studio-grade delivery.` + 3-paragraph honest story (identity decision §4.2 realized in copy) + **the process rail**: v1's IDEA→DESIGN→CODE→BUILD→LAUNCH chain reborn as a horizontal scroll-scrubbed timeline (§10.2, the v1 asset preserved and finally honored) + testimonial slider (3 quotes, keyboard-accessible, auto-advance 6 s pause-on-focus).

`/about` adds: full bio, timeline history (year rows), the full stack table (grouped by layer — P3 persona magnet), certifications/education, "the network" (specialist collaborators, first names + roles), photography of workspace (optional, 2–3), and a playful footer easter egg (konami-code triggers the kite glyph flight across screen — reduced-motion-safe; judges remember sites with wit).

**AC:** face present; every claim in facts rail maps to a real number; process rail scrubs smoothly at 60fps and degrades to static stepped timeline under reduced-motion.

## 9.7 ACT V — Contact (`/contact` + home finale) — the 60-second form

Home finale: centered (the one sanctioned centered act): H2 `Have an idea you can't stop thinking about?` (kept from v1 — judges praised it) + `No big deck needed. Just a conversation.` as sub-line + primary CTA + direct row (email / WhatsApp / calendar). Below: **live availability chip** (`● Next opening: December — 2 slots`, ember pulse-dot, static under reduced-motion).

`/contact` page: left column = form; right = expectations panel (mono: `WHAT HAPPENS NEXT — reply within 24h · discovery call 30 min · proposal in 3 days · no obligation`), plus direct channels, timezone-aware local time, and the availability chip.

**Form spec (the conversion core):**
- Fields: Name* · Email* · Project type* (chips: Web / Mobile / UI-UX / AI & Automation / Cloud / Custom — prefilled via `?project=`) · Budget band* (chips: `<$2k / $2–5k / $5–15k / $15k+ / Not sure`) · Timeline* (chips: ASAP / 1 month / Quarter / Flexible) · One-line pitch (textarea, 500-char counter) · honeypot field (visually hidden) · optional file attach (5 MB).
- UX: single column, 56px inputs, floating labels, inline validation (on blur), submit → optimistic "Sending…" with morph → success state (in-page, not alert): `✔ Received. Reply within 24h. — Vishvu` + reference ID + "add to calendar" link. Error state: field-level, ember border + `role=alert` message; server 5xx: human message + mailto fallback link.
- Anti-spam: honeypot + time-trap (< 2 s submit rejected) + Cloudflare Turnstile (invisible, free) + rate limit 5/hr/IP (server) + ` Discussions` none — v2 has no comments.
- Submission → POST `/api/contact` (Node/Hono on Oracle, §14.4) → OCI Email Delivery (SMTP) to owner + JSON append to SQLite + optional Telegram webhook for instant push.
- Every step instrumented: `form_start`, `form_submit`, `form_success`, `form_error` (§16).

**AC:** full form completable in ≤ 60 s (usability test, 5 users); keyboard-only + screen-reader pass; submission e2e tested (Playwright) incl. Turnstile bypass in CI; 0 data loss (SQLite + email dual-write); GDPR note links privacy page.

## 9.8 Footer (site-wide finale)

Big-type easter-egg footer (award grammar): `VISHVU TECH` at `--fs-h2` as watermark; columns: Sitemap / Services (top 4) / Direct (email, WhatsApp, calendar, GitHub, LinkedIn, X) / `© 2026 — Built & deployed by the same pair of hands you'd hire.` (the site-as-proof thesis in one line) + `Lighthouse 98/100` live badge link + uptime chip. Hover: watermark letters rise 4px staggered. Local time + "Made in Bengaluru" mono row.

## 9.9 404

`This page hasn't been built yet.` + kite glyph drifting slowly + search-free 3-link rescue (Home / Work / Contact) + HTTP 404 status. **AC:** exists, styled, returns 404 (audit gap G10 closed).

## 9.10 Journal (`/journal`)

3 launch essays (spec'd in content doc): `How I ship Core-Web-Vitals-green Next.js apps` · `Oracle Free Tier: hosting a production site for $0` · `What "AI & automation" actually means for an SMB`. Plain-prose MD → static. **AC:** RSS feed; reading time; no CMS dependency.
# 10. INTERACTION & MOTION SPECIFICATION

> Motion is v2's core experiential bet (audit flaw #4: 7 transitions / 6 keyframes / 1 reveal). This section is the complete motion contract. Implementation substrate: **GSAP 3 (ScrollTrigger + SplitText — free since v3.13) + Lenis 1.x**. Total motion budget: **GSAP core + plugins + Lenis ≤ 90 KB gzipped** (§13 budget).

## 10.1 Motion token system (design + code shared vocabulary)

```css
/* durations */
--t-instant: 120ms;  --t-fast: 240ms;  --t-base: 420ms;  --t-slow: 700ms;  --t-cinematic: 1200ms;
/* easings */
--ease-out:      cubic-bezier(.22, 1, .36, 1);      /* out-expo feel: standard reveals */
--ease-out-expo: cubic-bezier(.16, 1, .3, 1);       /* media, curtains */
--ease-in-out:   cubic-bezier(.65, 0, .35, 1);      /* scrub-linked states */
--ease-spring:   cubic-bezier(.34, 1.56, .64, 1);   /* playful pops: chips, cursor scale — only on feedback elements */
/* staggers */
--stagger-tight: 40ms;  --stagger-base: 80ms;  --stagger-editorial: 120ms;  /* per char/line/card */
/* distance grammar */
--rise: 24px;  --rise-lg: 48px;   /* reveal translations — never more; v1-style full-viewport slides banned */
```

**Rules:** every animated property must be compositor-only (`transform`, `opacity`, `clip-path`, `filter`) — **no width/top/left/margin animations, ever**. `will-change` applied on `:hover`-enter via JS, removed on animationend (0 persistent will-change layers). Durations > `--t-cinematic` require design sign-off. Motion tokens are CSS vars AND a TS `motion.ts` export — one source, two runtimes.

## 10.2 Scroll architecture (the narrative engine)

- **Lenis config:** `{ smoothWheel: true (desktop only), syncTouch: false, lerp: 0.1, wheelMultiplier: 1 }`. Mobile = native touch scrolling (research consensus: smoothing on touch reads as resistance). **Known pitfall encoded:** anchor links intercepted → `lenis.scrollTo(target, { offset: -80 })`; ScrollTrigger.refresh() on `window.load` + after every image `load` event + after route transitions (the #1 source of "mystery broken" award sites — research-documented).
- **The journey rail (Act IV):** horizontally-scrubbed process timeline — container pinned (`ScrollTrigger pin: true, scrub: 1` — numeric scrub per research: `scrub:1` gives the follow-lag that reads as polish), rail translates X over 1.5 viewport-heights of scroll; the five stages light up ember as a progress hairline crosses them; each stage's v1 micro-copy ("Start with a good question.") preserved.
- **Act sequencing:** each act title uses SplitText line-reveal on enter (once; no re-trigger). Case-study galleries parallax ±8% (scrub-linked). Section-index labels (`01 — THE PROOF`) slide horizontally ±32px against scroll direction (counter-motion depth cue).
- **Snap policy:** NO snap-scroll globally (freedom preserved); snap ONLY inside the horizontal rail (scroll-snap-x on the native scroller fallback).
- **Progress hairline:** top-edge 2px `--vf-gradient-signature` bar, width = scroll progress (transform scaleX — the gradient's 2nd permitted use).

## 10.3 Text system

- SplitText (chars for hero + act titles; lines for body paragraphs — chars never on body text). Char reveal: `y: 100% → 0, opacity 0→1, --stagger-tight, --ease-out`, masked with overflow-clip per line (award-standard "rise from the line").
- Headline scroll-scrub: hero H1 chars drift apart ±2px on scroll-away (subtle; the site "exhales").
- Link roll-overs: dual-label stack (label duplicates, first slides up-out, second slides up-in, 300 ms, `--ease-out`).
- Mono counters (stats, preloader): tabular-nums, eased count-up on enter (900 ms), `sfx` none (no audio — v2 scope decision; audio is a v2.1 experiment behind explicit user toggle only, per research anti-pattern list).

## 10.4 Pointer & tactile micro-interactions

- **Magnetic CTAs:** translate toward cursor within 120px radius (max 8px, Lerp 0.15, `--ease-out`); label counter-translates 4px (parallax-lie depth); disabled for touch + reduced-motion; keyboard focus triggers a single attention-pulse (scale 1→1.02→1, 240 ms).
- **Card hovers:** media scale 1.04 + ember hairline draw (scaleX 0→1, origin left) + meta-row arrow slides 6px.
- **Chip hovers (form/filters):** `--ease-spring` scale 1.03 + surface-2 swap.
- **Cursor-follow glow:** cards get a radial ember glow (8%, 320px) tracking cursor via `background: radial-gradient at var(--mx) var(--my)` on a pseudo-element — GPU-cheap, distinctive.

## 10.5 Custom cursor (Tier: desktop-hover-capable only)

- Dot (6px, ember) + trailing ring (28px, 1px ink-2 border, Lerp 0.12 follow) — ring is `mix-blend-mode: difference` so it lives on both dark and paper panels.
- Context states: `VIEW →` (over case media — ring expands to 72px, label fades in, Clash 12px), `DRAG` (journal scroller), `●` default. State transitions 200 ms.
- Native cursor NEVER fully hidden on interactive elements (`cursor: pointer` retained as fallback; custom layer is additive) — accessibility-first cursor design. Disabled entirely: touch devices, `pointer: coarse`, reduced-motion, Tab-key navigation detected.
- **AC:** cursor layer ≤ 2 KB JS, zero main-thread work when idle (rAF loop suspended on no-delta).

## 10.6 The AI demonstration (builds credibility for the "AI & automation" service)

A tiny, honest, on-device AI moment in the contact page: **"Describe your project in one line" textarea → local char-count + a heuristic project-type guesser ("sounds like a web app MVP…")** — rule-based (no API cost, no privacy issue, works offline) but presented as automation. Budget: ≤ 3 KB JS. This closes the "never claim what the site doesn't demonstrate" copy rule with a wink. (LLM-powered upgrade is explicitly out of scope for v2.)

## 10.7 Route transitions (multi-page)

- Cross-fade + 8px rise (350 ms out / 450 ms in), curtain wipe (600 ms `--ease-out-expo`) for Home↔Work only; all others cross-fade. View Transitions API where supported (Chrome/Edge) with manual GSAP fallback. Scroll position restored per route; `history.scrollRestoration = 'manual'`.

## 10.8 The reduced-motion contract (vestibular safety — audit fix for v1's ungated smooth-scroll)

One global gate, three tiers:
1. `prefers-reduced-motion: no-preference` → full experience.
2. `prefers-reduced-motion: reduce` → Lenis off; all scrub/pin/parallax/cursor/magnetic off; reveals become ≤ 200 ms opacity fades; preloader = 250 ms fade; marquee static; shader → Tier B SVG.
3. **`Save-motion` toggle** (footer, persisted to localStorage, default follows OS) — lets motion-sensitive users keep *some* life (opacity-only) while disabling movement. aria-live announcement on change.

**AC (motion):** 100% of §10 effects individually killable; `save-motion` state survives reload; zero animation runs while `document.hidden`; rAF loops all share one central ticker (GSAP ticker) — no orphan rAFs.

---

# 11. CONTENT STRATEGY & INFORMATION DESIGN

## 11.1 The evidence hierarchy (every page obeys)

`Outcome metric > Client name > Named technology > Process detail > Philosophy` — in that order of prominence. Philosophy without evidence is what v1 shipped; v2 inverts it.

## 11.2 Case-study narrative framework (per project, ≥ 700 words)

| Section | Length | Must contain |
|---|---|---|
| TL;DR band | 40 words | 3–4 metrics |
| Problem | 150 w | Client context, the business pain, 1 quote |
| Constraints & decisions | 200 w | ≥ 4 `decision → consequence` rows |
| Build narrative | 200 w | Stack names, 1 architecture diagram, 1 code excerpt |
| Outcome | 100 w | Metrics repeated in context + testimonial |
| Honest retro | 60 w | "What I'd do differently" |

**Launch inventory (owner homework, blocking gate for Phase 3):** 4–6 projects with: client permission status, 2–4 metrics each, 3–5 screenshots each, 1 testimonial each. Placeholder policy: **no invented numbers ship, ever** — if a metric is unverifiable it becomes qualitative ("cut loading time from noticeable to instant" is acceptable; "+31%" is not, unless true).

## 11.3 Services copy formula

Every service: `Capability sentence (what) → Deliverables checklist (8–12 concrete items) → Proof (2 case links) → Starting point (range + duration) → FAQ (4)`. Banned words: *thoughtful, passionate, journey (outside the act names), innovative, cutting-edge, solutions* (v1's fog vocabulary). Required: at least one number per service page.

## 11.4 Testimonials

3 at launch (name, role, company, photo w/ consent); 2 more as screenshots-row in About. No anonymous stars.

## 11.5 Micro-copy inventory (the personality layer)

Availability chip, expectations panel (`WHAT HAPPENS NEXT`), 404 line, footer lines, form success line, konami easter egg, local time — the wit layer judges quote. All listed in `content/microcopy.md` with exact strings (single source).

## 11.6 Homepage word budget

Home: ≤ 600 words (v1: ~600 — keep the discipline, change the *density of evidence*: v2 home carries ≥ 10 numbers vs v1's 0).
# 12. TECHNICAL ARCHITECTURE

## 12.1 Stack decision (decision matrix, options scored 1–5)

| Criterion (weight) | Vanilla (v1++) | **Astro 5 (chosen)** | Next.js 15 | Nuxt 3 |
|---|---|---|---|---|
| Zero-JS default / JS budget headroom (×3) | 5 | **5** | 3 | 3 |
| Componentization + content collections (×3) | 1 | **5** | 4 | 4 |
| Build-time image/font optimization (×2) | 1 | **5** | 4 | 3 |
| Motion library integration (GSAP/Lenis) (×2) | 3 | **5** | 4 | 4 |
| Oracle static-serving simplicity (×2) | 5 | **5** | 2 (needs Node runtime or export) | 2 |
| Markdown case studies (×2) | 1 | **5** | 4 | 4 |
| Team-of-one maintainability (×2) | 3 | **4** | 3 | 3 |
| **Weighted total** | 27 | **44** | 30 | 28 |

**Decision: Astro 5, static output (`output: 'static'`), TypeScript strict, zero UI framework by default.** Interactivity = Astro islands mounted only where needed: preloader, menu, cursor, hero shader, journey rail, form, filters, testimonials slider. Islands share one GSAP/Lenis core via a `<MotionRoot />` singleton. Astro ships **0 KB JS by default** — the v1 lightness ethos, preserved with structure. Contact API is a separate tiny service (§14.4), NOT part of the site build.

**Runtime libraries (complete, frozen list):** `gsap` (core+ScrollTrigger+SplitText) · `lenis` · `three` (hero shader only — tree-shaken, target ≤ 150 KB gz with shader; if over budget at Phase-2 gate, drop to raw WebGL or 2D canvas — budget wins, always) · `astro-icon` (Lucide) · `zod` (build-time content validation). **No jQuery. No Locomotive. No Barba (View Transitions suffice). No analytics SDK (Umami script is 1 KB, self-hosted).**

## 12.2 Repository structure

```
vishvu-tech/
├─ astro.config.mjs           # integrations: image, sitemap, icon, compress
├─ src/
│  ├─ components/             # Header, Footer, Preloader, Cursor, KiteHero,
│  │  ├─ motion/              #   MotionRoot, Reveal, SplitHeading, Magnetic, Marquee
│  │  ├─ work/                #   CaseCard, StatsBand, DecisionTable, Testimonial
│  │  └─ form/                #   ContactForm, Chip, Expectations
│  ├─ layouts/                # Base.astro (meta/OG/JSON-LD head), Paper.astro
│  ├─ content/                # work/*.md, services/*.md, journal/*.md (+ config.ts, zod schemas)
│  ├─ pages/                  # index, work/index, work/[slug], services/…, about, contact, 404, legal/*
│  ├─ styles/                 # tokens.css, base.css, components.css, motion.css (cascade layers)
│  ├─ scripts/                # site islands (TS)
│  └─ content.config.ts
├─ public/                    # fonts/(self-hosted woff2), favicon suite, og/(generated), robots.txt
├─ api/                       # Hono contact service (separate deploy, Docker arm64)
│  ├─ src/index.ts  Dockerfile  compose.yaml
├─ .github/workflows/         # ci.yml, deploy.yml, lighthouse.yml
├─ deploy/                    # nginx/ (site.conf, mime, security-headers), oracle-setup.md
└─ docs/                      # this PRD, content-guide.md, runbook.md
```

## 12.3 Rendering & content pipeline

- All routes pre-rendered at build (`dist/`); case studies from Markdown collections typed by Zod — **build fails on invalid frontmatter** (no silent bad data).
- Images: Astro `<Image>` → AVIF (quality 60) + WebP fallback, auto-sized `srcset`, LQIP blur-up, EXIF-stripped, hashed filenames (`/ _astro/cover.a1b2c3.avif`). The 2.1 MB PNG → target **≤ 110 KB AVIF** hero equivalent.
- Fonts: self-hosted woff2, `@font-face` with `unicode-range: U+0000-00FF` subsets, `size-adjust`/`ascent-override` metric fallbacks (zero CLS on swap), preloaded (2 critical weights only: Clash 600 + Satoshi 400).
- OG images: `satori`-generated at build → `public/og/{route}.png` (1200×630, per-route title) — zero runtime cost.

---

# 13. PERFORMANCE ENGINEERING

## 13.1 Budgets (CI-enforced via `@lhci` + `size-limit`; a failing budget fails the deploy)

| Budget | Limit |
|---|---|
| LCP (lab, Moto G Power, 4G throttle) | ≤ 1.8 s |
| CLS | ≤ 0.02 |
| INP (lab proxy: TBT) | TBT ≤ 150 ms |
| **Total JS (gzipped, first load, home)** | **≤ 180 KB** |
| — of which: GSAP+plugins+Lenis | ≤ 90 KB |
| — of which: hero shader bundle (three) | ≤ 150 KB (lazy, post-LCP, only Tier-A devices) |
| Total CSS (gzipped) | ≤ 45 KB |
| Hero visual asset | ≤ 110 KB (AVIF) or shader bundle above |
| First-load transfer (home, cold) | ≤ 900 KB target / 1.2 MB hard cap |
| Font transfer (critical path) | ≤ 90 KB (2 preloaded weights) |
| Requests before LCP | ≤ 14 |

## 13.2 Optimization checklist (the audit fixes, itemized)

- [x] AVIF/WebP pipeline with LQIP (replaces 2.1 MB PNG — audit flaw #2)
- [x] Subsetted self-hosted fonts, metric-matched, 2 preloads (flaw #12)
- [x] `width`/`height` + `aspect-ratio` on every image; no unsized media (flaw: CLS risk)
- [x] Hashed filenames + 1-year immutable cache + HTML no-cache (flaw: stale-asset race)
- [x] Brotli static (level 11 pre-compressed at build) + gzip fallback (flaw: no compression story)
- [x] HTTP/2 + TLS 1.3 + 0-RTT via nginx/Cloudflare (§14)
- [x] Lazy three.js: hero shader loads post-LCP via `requestIdleCallback` + Tier gating; Tier B = 18 KB SVG
- [x] Fonts `font-display: optional` for critical, `swap` for mono/serif accents
- [x] Preload: hero AVIF + 2 fonts + critical CSS inline (14 KB critical CSS, rest deferred)
- [x] Partytown/reserve: none needed (no heavy 3rd-party; Umami script deferred, 1 KB)
- [x] `prefers-reduced-motion` short-circuits ALL JS motion init (parse cost, not just runtime)
- [x] rAF unified on GSAP ticker; every listener passive except form inputs
- [x] Font/hero readiness drive preloader — first paint is *complete*, never mid-swap

## 13.3 Field measurement

Umami events + custom RUM beacon (FID/CLS/LCP via `web-vitals` attribution build, ~2 KB, batches to `/api/vitals`, sampled 100% — traffic is small; P75 dashboards in Umami).

---

# 14. DEPLOYMENT ARCHITECTURE — ORACLE CLOUD ALWAYS FREE TIER

> Owner constraint: **$0/month, permanently.** The architecture below respects every Always-Free limit with headroom, and adds Cloudflare's free tier in front for CDN/TLS/DDoS — a combination researched as the canonical free-hosting stack for exactly this class of site.

## 14.1 Always-Free inventory (verified limits, 2026)

| Resource | Always-Free allowance | Our allocation |
|---|---|---|
| **Ampere A1 (ARM)** | 1,500 OCPU-hrs + 9,000 GB-hrs/month | **1 VM: 2 OCPU / 12 GB RAM / 60 GB boot** (24/7 = 1,460 OCPU-hrs + 8,760 GB-hrs — fits the halved 2026 allowance with ~3% headroom; 4-OCPU/24GB config is NOT always-free since the 2026 limit change) |
| AMD micro VMs | 2 × (1/8 OCPU / 1 GB) | Reserved: 1 as failover/static-mirror, 1 spare (monitoring agent optional) |
| Block storage | 200 GB total | 60 GB boot + 20 GB volumes (site, SQLite, Umami) + 120 GB spare |
| Outbound transfer | 10 TB/month | Effectively unlimited for this traffic class; Cloudflare further reduces origin egress |
| Flexible Load Balancer | 1 × 10 Mbps | **Not used** — Cloudflare fronts the VM directly; LB kept as documented failover path |
| Email Delivery | 3,000 sends/month | Contact-form notifications (~50/mo expected) |
| Object Storage | 10 GB + 10 GB archive | Nightly backups (site tar + SQLite + Umami DB) |
| Autonomous DB | 2 instances | **Not used** — SQLite suffices; one less moving part |
| VCNs | 2 | 1 VCN, 1 public subnet, security-list locked to 22 (admin CIDR) + 80/443 |

**Known platform risks, pre-mitigated (documented in runbook):** (a) *A1 capacity errors* in popular regions — mitigation: capacity-retry script (`oci compute instance launch` retry loop) or pick home region with availability; (b) *idle-instance reclamation* for Always-Free (95th-percentile CPU < ~20% over 7 days can flag a VM) — mitigation: real traffic + Umami + API keep baseline; scheduled lightweight health-job as belt-and-braces; (c) ARM-only → all Docker images pulled with `:aarch64`-compatible tags (verified list in runbook).

## 14.2 Architecture

```
                        ┌──────────────────────────┐
  Visitor ── HTTPS ──▶  │  CLOUDFLARE FREE         │  CDN cache (static, 1y immutable)
                        │  • Universal SSL (edge)  │  WAF + DDoS + Bot fight
                        │  • DNS, proxy, cache     │  Turnstile (form)
                        └──────────┬───────────────┘  Origin lock: CF-IP allowlist
                                   │ HTTPS (Origin CA cert, TLS 1.3)
                        ┌──────────▼───────────────────────────────┐
                        │  ORACLE VM.Standard.A1.Flex (ARM)        │
                        │  2 OCPU · 12 GB · Ubuntu 24.04 LTS       │
                        │  ┌─────────────┐   ┌──────────────────┐  │
                        │  │ nginx       │──▶│ /var/www (dist/) │  │
                        │  │ :80→443     │   │ static, brotli   │  │
                        │  │ security    │   │ immutable cache  │  │
                        │  │ headers,    │   └──────────────────┘  │
                        │  │ rate-limit  │   ┌──────────────────┐  │
                        │  └──────┬──────┘   │ contact API       │  │
                        │         │ proxy    │ Hono + SQLite     │  │
                        │         ▼          │ :8080 (localhost) │  │
                        │  ┌─────────────┐   └──────────────────┘  │
                        │  │ Umami       │   OCI Email Delivery    │
                        │  │ analytics   │   (SMTP → inbox)         │
                        │  └─────────────┘   rclone → Object Storage│
                        └──────────────────────────────────────────┘
```

## 14.3 nginx (complete, in `deploy/nginx/site.conf`)

- TLS: **Cloudflare Origin CA cert** (15-year, free, avoids Let's Encrypt renewal automation on ARM) — full (strict) mode at edge; TLS 1.2/1.3, modern ciphers only, OCSP stapling, session tickets.
- `http2 on;` · `brotli_static on;` (pre-compressed at build) + gzip fallback · `sendfile + tcp_nopush`.
- **Security headers (grade-A target):** HSTS (1y, preload) · CSP `default-src 'self'; script-src 'self' 'unsafe-inline' (Astro inline islands; nonce-migration Phase 5+); style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' https://umami.vishvutech.com; frame-ancestors 'none'; base-uri 'none'; form-action 'self'` · X-Content-Type-Options nosniff · Referrer-Policy strict-origin-when-cross-origin · Permissions-Policy `camera=(), microphone=(), geolocation=()` · COOP/CORP same-origin.
- **Caching:** `location /_astro/ { add_header Cache-Control "public, max-age=31536000, immutable"; }` · HTML: `no-cache` (always fresh HTML + immutable hashed assets = zero stale races) · fonts: 1y.
- **Rate limits:** `limit_req_zone` 5 r/s general, `location /api/` 10 r/m with burst 5 (form abuse shield #3).
- **Origin lock:** `allow` Cloudflare IP ranges only + `deny all` (plus fail2ban on 4xx floods); SSH on non-standard port, key-only, ufw allow admin CIDR only.
- **API proxy:** `location /api/ { proxy_pass http://127.0.0.1:8080; }` — site and API share one origin/domain (no CORS).

## 14.4 Contact API (`api/` — Hono on Node 22 LTS, ~120 LOC)

- `POST /api/contact`: zod-validate payload → honeypot + time-trap checks → Turnstile siteverify (server-side) → rate-limit (per-IP, in-memory bucket + SQLite log) → **dual-write**: OCI Email Delivery SMTP (owner inbox, SPF/DKIM/DMARC configured per Oracle docs) + SQLite `inquiries` table → 200 with reference ID (`VT-2026-0001`). Errors: typed JSON `{error, field?}`, 0 data leaks, request body capped 64 KB, 20 s timeout, structured logs to journald.
- `POST /api/vitals`: RUM beacon sink (zod-validated, sampled, appended to SQLite).
- Runs as **systemd service** under dedicated `vishvu` user (docker optional; systemd = fewer moving parts on ARM) — `Restart=always`, `MemoryMax=300M`.
- **Test contract (CI):** Playwright e2e happy-path + honeypot rejection + rate-limit 5th-request 429 + Turnstile mock.

## 14.5 Analytics — self-hosted Umami (privacy-first, free forever)

- Umami (Node + its own SQLite) as second systemd service on same VM, subdomain `umami.vishvutech.com` via second nginx server-block (CF-proxied). Script: 1 KB, cookieless, GDPR-friendly ("no cookies" line in privacy page). Events taxonomy in §16.
- **Alternates rejected:** GA4 (bloat + consent banner burden + brand-credibility cost with P3 persona), Plausible (paid self-host ~$9/mo or heavy Docker stack), GoAtBest none. Umami on ARM: verified aarch64-compatible.

## 14.6 CI/CD (GitHub Actions, free for public repos)

- **`ci.yml`** (every PR): pnpm install → `astro check` + `tsc --noEmit` → content zod validation → ESLint + Prettier + Stylelint → build → **size-limit budgets (§13.1)** → `astro preview` + Playwright (a11y smoke, form e2e, 404) → **Lighthouse CI asserts** (perf ≥ 95, a11y ≥ 100, BP ≥ 100, SEO ≥ 100 on home, work, contact) → axe-core 0 critical.
- **`deploy.yml`** (tag `v*`): build with prod env → `rsync -az --delete dist/ vishvu@vm:/var/www/` (SSH deploy key, strict host key) → `systemctl reload nginx` → API deploy: `rsync api/` + `systemctl restart contact-api` → **post-deploy smoke**: curl 200 on / + /work + /contact, form e2e against prod (test beacon), uptime robot check. Rollback: previous release retained at `/var/www/releases/<sha>` — symlink flip, documented 60-second rollback.
- Secrets: SSH key, SMTP creds — GitHub Environments, never in repo. Two-person rule N/A (solo) — instead: deploy tag requires green CI on main.

## 14.7 Ops runbook (`docs/runbook.md`)

Procedures: VM recreation from zero (scripted `oracle-setup.md` — VCN, security lists, systemd units, nginx, restore-from-backup); backup restore (rclone pull + DB file swap + verify); Oracle capacity-error retry loop; monitoring via UptimeRobot (free, 5-min checks on / + /api/health) + Cloudflare analytics; log rotation (logrotate, 14d); monthly: Ubuntu unattended-upgrades + `apt upgrade` window + cert/nginx smoke; quarterly: restore drill (backup → fresh VM → DNS switch test).
# 15. ACCESSIBILITY SPECIFICATION (WCAG 2.2 AA — full conformance target)

> v1's good instincts (landmarks, ARIA state, alt text, reduced-motion) are carried forward; every audit gap closed. Target: **WCAG 2.2 AA, verified** — and noted in the footer (judges + P3 persona reward verified a11y).

- **Contrast (fixes 4.0:1 audit fail):** body ≥ 7:1, large ≥ 4.5:1, meta ≥ 4.5:1, focus indicators ≥ 3:1 — enforced by CI token-lint (stylelint declaration checker computing ratios from tokens).
- **Focus (fixes invisible-focus fail):** `:focus-visible { outline: 2px solid var(--vf-ember); outline-offset: 3px; }` sitewide + `--vf-glow-ember` on CTAs; focus NEVER removed; skip-to-content link first tabbable element on every route (fixes the false README claim); menu overlay focus-trap + Escape + return-focus-on-close.
- **Targets (WCAG 2.2 — new in AA):** all interactive ≥ 44×44px (2.5.8), incl. link rows (full-row hit area via padding, not text-bbox — fixes v1's ~28px links); no double-tap-only affordances (2.5.7); `scroll-behavior: smooth` gated behind no-preference (fixes vestibular fail; §10.8 owns the full contract).
- **Forms:** every input has a persistent `<label>` (floating labels are *additional*, never the only label), errors `aria-describedby` + `role=alert` on submit failure, success announced `aria-live=polite`, chips are real `input[type=radio]` (fieldset + legend) — keyboard native, screen-reader native.
- **Media:** decorative glyphs/aria-hidden audit (fixes "spark symbol" announcements); every case-study image has informative alt (content pipeline *requires* alt field — zod-enforced); shader canvas `role="img"` + `aria-label="Animated night horizon"`; video previews muted + `aria-hidden` decorative.
- **Motion:** §10.8 three-tier contract; marquees pause on hover AND respect reduced-motion; no parallax > 8%.
- **Keyboard completeness:** everything operable without pointer — filters, testimonial slider (arrow keys), journey rail (native scroll-snap fallback = keyboard scrollable), custom cursor fully suppressed on Tab navigation.
- **Semantics:** heading hierarchy lint (one h1, no skips); `aria-current="page"` on nav; breadcrumbs with `aria-current`; landmarks per route; `lang` correct; live regions for availability chip.
- **Testing gates:** axe-core in CI (0 critical, 0 serious), manual NVDA + VoiceOver pass per release, keyboard-only walkthrough video (linked from About — transparency as a feature), 200% zoom reflow check, forced-colors (Windows High Contrast) visual check.
- **AC:** Lighthouse a11y = 100 on all routes; axe = clean; external audit-ready statement in `/legal/privacy`.

# 16. SEO & DISCOVERABILITY

- **Per-route meta templates:** unique `<title>` (`Case Study — Checkout Rebuild | Vishvu Tech`), meta description 120–155 chars with a number, canonical, `hreflang` N/A (single locale).
- **Structured data (JSON-LD):** `Person` + `Organization` (linked, sameAs socials) on home; `WebSite` + `SearchAction` (journal); `Service` × 6 on service pages; `CreativeWork`/`Article` on case studies + journal; `BreadcrumbList` on detail routes; `FAQPage` on service pages (Google rich results) — all validated in CI (schema validator + rich-results test).
- **Files:** `robots.txt` (allow all, sitemap ref), `sitemap.xml` (Astro integration, lastmod from git), per-route OG/Twitter cards using generated images (§12.3); favicon suite (§8.5).
- **Domain strategy (fixes split-equity flaw):** single canonical `https://vishvutech.com`; GitHub Pages retired; `www` → apex 301; HSTS preload submission post-launch stabilization.
- **Content surface:** 6 service pages + 4–6 case studies + 3 journal posts ≈ 13 indexable URLs at launch vs v1's 1 — the entire organic-growth premise.
- **Search Console + Bing Webmaster verified at launch;** basic KPI dashboard in Umami (organic weekly trend — §6.2 target ≥ 150/wk by day 90).

# 17. ANALYTICS & MEASUREMENT PLAN

**Umami event taxonomy (complete — nothing unmeasured ships):**

| Event | Trigger | Properties |
|---|---|---|
| `pageview` | route load (auto) | referrer, UTM, device |
| `cta_click` | any Start-a-project element | `location` (header/hero/work card/footer) |
| `form_start` | first field focus | `prefill` (service/project source) |
| `form_submit` | submit attempt | `valid` bool |
| `form_success` | 200 response | `ref_id` |
| `form_error` | error response | `type` (validation/turnstile/rate/server) |
| `scroll_act` | each act 50% visible | `act: I..V` |
| `case_open` | case-study detail load | `slug` |
| `case_read` | 60 s on page OR 75% scroll | `slug` |
| `outbound` | mailto/WhatsApp/calendar/social | `target` |
| `motion_pref` | save-motion toggle | `tier` |
| `vitals` | RUM beacon | LCP/CLS/INP + attribution |

**Dashboards:** conversion funnel (pageview → cta_click → form_start → form_success); content value (case reads by slug); acquisition (referrer/UTM); experience health (vitals P75 + scroll completion). Reviewed weekly in a 30-minute ritual (docs include the review template) — the "site that learns" commitment made operational.

# 18. SECURITY

- CSP as specced (§14.3) — report-only first 2 weeks, then enforce; report-uri → journald digest.
- Form: zod validation server-side (client validation is UX only), honeypot + time-trap + Turnstile + rate-limit (§14.4) — four independent layers; inbox spam < 1/quarter expected.
- Infrastructure: SSH key-only + non-standard port + admin CIDR; ufw (22 admin, 80/443 CF-only); unattended security upgrades; systemd sandboxing (`ProtectSystem=strict`, `PrivateTmp`, `NoNewPrivileges`) on both services; SQLite file 600 `vishvu:vishvu`; fail2ban on nginx 4xx.
- Data: inquiries (name/email/message only) in SQLite + email; retention 24 months then purge (privacy page states it); no third-party trackers; backup volume encrypted at rest (Object Storage).
- Dependency: `pnpm audit` + Dependabot; lockfiles committed; monthly patch window.

# 19. RELEASE PLAN — 6 PHASES, 12 WEEKS

| Phase | Weeks | Delivers | Exit gate (binary) |
|---|---|---|---|
| **0 · Discovery** | 1 | Content inventory (owner homework: 4–6 case studies' metrics/screenshots/testimonials), brand facts, this PRD signed | All case-study materials collected; numbers verified |
| **1 · Foundation** | 2–3 | Astro repo, tokens.css, Base/Paper layouts, header/footer, favicon suite, OG generation, CI (lint+build+size), Oracle VM provisioned + nginx + TLS + Cloudflare, deploy pipeline on `staging.vishvutech.com` | Staging serves HTTPS w/ grade-A headers; CI green; Lighthouse perf ≥ 90 on skeleton |
| **2 · Signature experience** | 4–6 | Preloader, MotionRoot (Lenis+ScrollTrigger), hero shader Tier A/B, split-text system, journey rail, cursor, magnetic CTAs, marquee, reveals | Motion QA pass (60 fps scroll on 4G mid-tier); JS ≤ 180 KB; reduced-motion tiers verified |
| **3 · Content & pages** | 7–8 | All routes: work index/detail × content, services × 6, about, journal × 3, legal, 404, contact form + API + email + Turnstile | Form e2e green in prod; 4–6 case studies live with metrics; content review sign-off |
| **4 · Hardening** | 9–10 | a11y audit fixes, SEO/JSON-LD/sitemap, Umami + events, RUM, security headers enforce, perf pass (budgets), QA matrix (§20) | Lighthouse 4× ≥ 95/100/100/100 all routes; axe clean; budgets green |
| **5 · Launch & awards** | 11–12 | DNS cutover, 301s, HSTS preload, monitoring, 1-week stabilization, **award submissions** (§21), retro + v2.1 backlog | Uptime ≥ 99.5% week 1; vitals P75 green; submissions entered |

**Principle:** every phase ends on a *deployable* artifact — the site is never broken for more than a day; launch-risk is diffused across six small cutovers instead of one big-bang.

# 20. QUALITY ASSURANCE & ACCEPTANCE CRITERIA

## 20.1 Global gates (all must pass before any phase exit)

1. Lighthouse (lab, throttled): Performance ≥ 95 · A11y = 100 · Best-Practices = 100 · SEO = 100 — **all routes**.
2. Field-vitals beacon wired; lab LCP ≤ 1.8 s / CLS ≤ 0.02 / TBT ≤ 150 ms.
3. Budgets (§13.1) green in `size-limit` CI.
4. axe-core: 0 critical, 0 serious; keyboard-only walkthrough video recorded.
5. Playwright e2e: form happy+failure paths, 404, route transitions, reduced-motion render, OG image existence.
6. Cross-browser: Chrome/Edge/Firefox/Safari (incl. iOS Safari 16+, Android Chrome 110+); 360 px → 1920 px reflow, 200% zoom, forced-colors.
7. Content: every metric source-verified; every image has alt; spell-check pass; microcopy.md strings match UI exactly.

## 20.2 Route-level acceptance spot-checks (excerpt — full matrix in docs)

| Route | Sample AC |
|---|---|
| `/` | Preloader ≤ 2.8 s; shader Tier B loads under reduced-motion; act sequence reveals once each; proof strip contains ≥ 3 real numbers; scroll to Act V achievable in ≤ 6 swipes mobile |
| `/work` | Filters URL-synced; 0 layout shift during image loads; card hover ≥ 2 simultaneous effects at 60 fps |
| `/work/[slug]` | Stat band ≥ 3 metrics; decision table ≥ 4 rows; next-actions row has 3 links; paper/dark contrast bands pass tokens |
| `/services/[slug]` | ≥ 350 words; 2 case links; starting-point numbers present; FAQ rendered as JSON-LD |
| `/contact` | Full form ≤ 60 s; success state has ref ID; error paths have human copy; honeypot silently absorbs bot submit |
| `/404` | Returns HTTP 404; 3 rescue links; easter egg respects motion prefs |

## 20.3 Award-readiness scorecard (internal, mirrors Awwwards)

Rubric circulated to 3 external reviewers pre-submission; each dimension scored 1–10 with written justification; gate: **all four ≥ 7.3** before spending submission fees:
- Design: identity ownership in 3 s? palette discipline? compositional variety? type system quality? depth/light discipline?
- Usability: stress-tested navigation; mobile one-hand reachability; load feel; edge states (404, form errors, offline fetch fail)
- Creativity: name the 2 "never-seen" moments (target: shader horizon + journey rail + paper-island case studies — pick strongest 2)
- Content: does the work *prove* the claims? is there a story only Vishvu can tell? honest-retro section present?

# 21. AWARD SUBMISSION PLAYBOOK (Phase 5)

1. **Order of submission (cost→value):** CSSDA (~$25–30) → Awwwards (~$50–75 standard) → FWA (~$50–90) — fees verified at submission time; set expectations: SOTD is ~1–3% acceptance — the *submissions themselves* generate backlinks, social proof, and traffic regardless of outcome.
2. **Pre-submission checklist:** case studies polished; press-kit page (`/press`: logo pack, screenshots 1440/390, palette, type, credits); 2 capture videos (60 s desktop scroll-through, 30 s mobile) hosted on the site itself; submission description written like a judge reads: problem → 2 signature moments → craft details → performance proof.
3. **Timing:** submit Tue–Thu, avoid holiday weeks; 2-week stabilization before first submission.
4. **Whatever the outcome:** judge feedback (Awwwards returns scores) → 30-day iteration list → resubmit major redesigns only (Awwwards penalizes rapid resubmits).
5. **Parallel credibility hacks:** publish the Oracle-$0-hosting journal post (guaranteed developer-audience interest — "free tier production" content outperforms); ship the Lighthouse badge; submit the site itself as the "cloud & deployment" case study #7 ("how this site runs for $0" — the site proves its own thesis).

# 22. RISK REGISTER

| # | Risk | P | Impact | Mitigation |
|---|---|---|---|---|
| R1 | A1 "out of capacity" on VM create | M | Blocks Phase 1 | Region with availability; scripted retry loop; AMD micro as interim static host |
| R2 | Idle reclamation flags VM | L | Site offline | Real traffic + Umami keep CPU > threshold; health cron; UptimeRobot alerts < 5 min |
| R3 | Case-study content slips (owner homework) | **H** | Phase 3 stalls | Phase-0 hard gate; 2-case minimum for soft launch, 4 for award submission |
| R4 | Shader perf on low-end Android | M | Jank = instant credibility loss | Tier gating (deviceMemory/WebGL2); budget wins — 2D fallback ready; 60 fps verified on Moto G class in CI device lab |
| R5 | GSAP license drift | L | Rework | v3.13+ fully free (SplitText incl.); pin exact versions in lockfile |
| R6 | Email lands in spam | M | Lost inquiries | OCI Email + SPF/DKIM/DMARC from day 1; test to Gmail/Outlook/Yahoo in Phase 3 gate; Telegram webhook backup channel |
| R7 | Oracle changes free terms again | L | Cost/infra churn | 100% static artifact — portable to any host in 1 rsync; domain on Cloudflare (DNS decoupled); quarterly limit review in runbook |
| R8 | Solo bandwidth / scope creep | **H** | Timeline slip | Non-goals §6.3 enforced; phases each shippable; Journal/CMS deferred to v2.1 |
| R9 | Cloudflare misconfig exposes origin | L | Bypass/DDoS | IP allowlist + authed origin pulls; quarterly origin-leak test |
| R10 | Accessibility regression post-launch | M | Award-eligibility + legal | a11y checks in CI (axe + token-lint) — regressions fail deploys, forever |

# 23. POST-LAUNCH ITERATION & v2.1 BACKLOG

90-day loop: weekly analytics ritual (§17) → monthly content cadence (1 journal post) → quarterly restore drill + dependency updates. Backlog candidates (explicitly out of v2): audio experience (user-toggled only), WebGL case-study transitions, CMS for journal, i18n, public mini-tools (free-quote estimator = lead magnet), LLM-powered project describer (replacing §10.6 heuristic), client portal. Each enters v2.1 only via the same PRD discipline.

# 24. APPENDICES

**A. Research sources:** Awwwards evaluation system (Design 40/Usability 30/Creativity 20/Content 10 + DEV dimensions; SOTD winners 7.3–7.6 profile — awwwards.com/sites/proof-1, /due, /create); Awwwards portfolio index (2026); Codrops: "More Than a Portfolio: Building a Scroll-Driven 3D World" (Three.js/GSAP/KTX2/instancing playbook); Oracle Cloud Free Tier docs (Always Free resources; 2026 Ampere allowance change via InfoQ); GSAP+Lenis integration pitfalls (dev.to/thebitforge); portfolio trends 2026 (Envato/globerunner/muz.li); WCAG 2.2 AA criteria.
**B. Audit evidence bundle:** `critique-evidence/` (desktop 1440 full + hero, mobile 390 full), DOM audit JSON, CSS occurrence counts, VLM judge analyses — reproduced in companion critique document.
**C. Baseline→Target scorecard:** Design 5.6→7.4 · Usability 5.8→7.4 · Creativity 4.6→7.3 · Content 4.2→7.5 · **Weighted 5.32→7.4** (nomination tier; stretch: 7.8 SOTY-profile via v2.1 audio + WebGL transitions).
**D. Open questions for owner:** real client names vs anonymized (per-case consent)? photo shoot availability? WhatsApp as primary SMB channel? budget-band comfort (transparency vs anchoring)? city/timezone for footer detail?
