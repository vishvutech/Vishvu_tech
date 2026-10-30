#!/usr/bin/env python3
"""
Vishvu Tech — FORGE NOIR palette (VT-PRD-002 §7.3)
Single source of truth for every color the build touches.
tokens.css mirrors these values; svgs.py, the OG generator and the
favicon/icons are all derived from HERE. Law L8: no raw hex anywhere else.

OKLCH primitives (hue 75 = committed warmth) → computed sRGB hex.
Every text/marks pairing is verified by scripts/contrast_audit.py.
"""

# ---- Obsidian & Ash — neutrals (warm smoked iron, hue 75) ----
ASH_950 = "#0E0C09"   # page canvas — warm obsidian          (oklch .155 .006 75)
ASH_900 = "#161310"   # surface-1 — raised panels            (oklch .190 .007 75)
ASH_850 = "#1F1C18"   # surface-2 — hover/active raised      (oklch .228 .008 75)
ASH_800 = "#2B2825"   # line — decorative hairlines          (oklch .280 .008 75)
ASH_700 = "#403C37"   # line-strong — interaction hairlines  (oklch .360 .010 75)
ASH_600 = "#6D6861"   # border-input — WCAG 1.4.11 · 3.35:1  (oklch .520 .012 75)

# ---- Bone & Ash — text ladder (warm-tinted, never pure white) ----
INK   = "#EAE8E3"     # 15.95:1 on canvas — AAA              (oklch .930 .006 85)
INK2  = "#B0ACA5"     # 8.64:1 — AAA                         (oklch .745 .011 80)
INK3  = "#96918B"     # 6.25:1 — AA+ · min meta grade        (oklch .645 .012 80)
                      # VT-CTA-003: raised from #8D8881 (5.55:1) after three of four
                      # blind reviews flagged perceived dimness / mobile daylight washout

# ---- Molten — the ember ramp (the only interactive hue, 35–48°) ----
EMBER_300 = "#FFAC7E"  # highlight tints · gradient top      (oklch .820 .120 48)
EMBER_400 = "#FE8F5B"  # hover state                          (oklch .760 .150 45)
EMBER_500 = "#E36E49"  # THE accent — CTAs, focus, markers   (oklch .670 .155 38)
                      # VT-CTA-003: trimmed from #EE6E3F (oklch .685 .170 40) after
                      # two of four blind reviews pattern-matched "traffic-cone";
                      # chroma .170→.155 + hue 40→38 reads burnt, not safety
EMBER_600 = "#C65029"  # marks-grade on paper · 3.85:1        (oklch .580 .160 38)
EMBER_700 = "#882D16"  # text-grade on paper · 7.24:1         (oklch .430 .130 35)
ON_EMBER  = "#0C0806"  # text on ember fills · 6.26:1         (oklch .140 .010 60)

# ---- Aurora — atmosphere (LAW L2: illustrations & hero sky ONLY) ----
AURORA = "#80D1B5"     # the cool light above the forge       (oklch .800 .090 170)

# ---- Signal — feedback ----
SIGNAL_OK   = "#52CD86"
SIGNAL_WARN = "#E7B643"
SIGNAL_ERR  = "#ED5350"

# ---- Ledger — the paper world (case-study islands) ----
LEDGER_50      = "#EFEBDF"  # paper canvas
LEDGER_100     = "#E6E1D3"  # paper alt surface
LEDGER_200     = "#D7D2C7"  # paper hairlines
LEDGER_SURFACE = "#F7F4EA"  # raised paper cards
LEDGER_INK     = "#28231E"  # warm ink · 13.06:1 on paper
LEDGER_INK2    = "#615951"  # paper secondary · 5.77:1

# ---- Hero night sky ramp (warm obsidian — the ground got warm) ----
SKY_TOP    = ASH_950       # #0E0C09
SKY_MID    = "#1A1712"
SKY_BOTTOM = "#26221C"

# Convenience aliases used by the SVG library
VOID = ASH_950        # legacy name kept so generated art reads the same
SURFACE = ASH_900
SURFACE2 = ASH_850
LINE = ASH_800
EMBER = EMBER_500
PAPER = LEDGER_50
PAPER_INK = LEDGER_INK
PAPER_LINE = LEDGER_200
