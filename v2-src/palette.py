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
                      # Golden Hour: re-tuned from the v2 meta grade (6.25:1) — the
                      # espresso floor is lighter than obsidian, so the meta grade rose with it

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

# Convenience aliases used by the SVG library and the asset generator
# (legacy names kept so generated art reads the same — re-inks automatically)
VOID = ROAST_950           # legacy name kept so generated art reads the same
SURFACE = ROAST_900
SURFACE2 = ROAST_850
LINE = ROAST_800
EMBER = CHAMP_500          # legacy alias — champagne now owns interaction
EMBER_300 = CHAMP_300
EMBER_400 = CHAMP_400
EMBER_500 = CHAMP_500
EMBER_600 = CHAMP_600
EMBER_700 = CHAMP_700
ON_EMBER = ON_CHAMP
PAPER = LEDGER_50
PAPER_INK = LEDGER_INK
PAPER_LINE = LEDGER_200
AURORA = DUSK_RIBBON       # legacy alias — the dusk ribbon replaces the mint
