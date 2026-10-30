#!/usr/bin/env python3
"""
Vishvu Tech — STRATA · LAYERED LIGHT palette (VT-PRD-005 §5)
Single source of truth for every color the build touches.
tokens.css mirrors these values; svgs.py, the OG generator and the
favicon/icons are all derived from HERE. Law L9: no raw color anywhere else.

OKLCH primitives — the LAYERED world (each layer chosen against the
composite below it, per the owner's mandate):
  L1 GROUND    porcelain                       (hue 90)
  L2 STRATA    dawn/gold/sage/powder/blush     (hues 15–250, visible bands)
  L3 PLANE     milk                             (raised paper)
  L4 WELLS     tinted by host stratum            (sunken insets)
  L5 LINES     per-stratum hairlines
  L6 INK       peacock ladder (typographic only)

THE MANDATE (unchanged): zero black, zero brown, zero dark shades anywhere —
the canvas is porcelain ivory, ink is a chromatic peacock jewel, and depth
is lightness + cast shadows, never darkness. Strata add VISIBLE layered
colour combinations — many colours behaving as one dawn world.
"""

# ---- L1 · Porcelain ground (hue 88–95°, Law L0/L1) ----
PORCELAIN    = "#F7F4EC"  # page canvas — porcelain ivory      (oklch .967 .011 90)
MILK         = "#FDFCF8"  # L3 plane — raised cards            (oklch .991 .005 95)
BONE         = "#F0EBDF"  # L4 well on porcelain — darkest neutral (oklch .941 .017 88)
LINE         = "#E2DBC8"  # decorative hairlines               (oklch .892 .027 90)
LINE_STRONG = "#CFC6AE"  # structural hairlines               (oklch .827 .034 90)
BORDER_IN    = "#857A5F"  # border-input — WCAG 1.4.11 · 3.86:1 (oklch .582 .041 88)

# ---- L2 · STRATA — section bands (VT-PRD-005 §5.2, Law S2/S4/S6) ----
STRATUM_DAWN      = "#FFEBE6"  # hero mid-sky + contact peach  (oklch .958 .026 35)
STRATUM_GOLD      = "#FDECCF"  # journal ground                (oklch .950 .042 82)
STRATUM_SAGE      = "#E7F5E7"  # services — the green of making (oklch .956 .024 145)
STRATUM_POWDER    = "#E3F3FF"  # about/journey — the wide sky  (oklch .956 .026 248)
STRATUM_BLUSH     = "#FFE9EA"  # contact/404 — the warm invitation (oklch .957 .030 15)
STRATUM_GOLD_DEEP = "#FEEFD7"  # essay pull-quote wash         (oklch .958 .036 80)

# ---- L4 · WELLS — sunken insets tinted by host (Law S5 chroma escalation) ----
WELL_SAGE   = "#DCEEDC"  # in sage bands      (oklch .930 .030 145)
WELL_POWDER = "#D8EAFD"  # in powder bands    (oklch .930 .032 248)
WELL_BLUSH  = "#FCE1E0"  # in blush bands     (oklch .931 .030 20)
WELL_GOLD   = "#F7E6CA"  # in gold bands      (oklch .932 .042 82)

# ---- L5 · LINES — per-stratum hairlines ----
LINE_SAGE   = "#D1E2D0"  # (oklch .895 .030 145)
LINE_POWDER = "#CCDFF1"  # (oklch .895 .032 248)
LINE_BLUSH  = "#F0D6D3"  # (oklch .896 .030 24)
LINE_GOLD   = "#EADBC0"  # (oklch .897 .040 84)

# Washes — tinted porcelain (Law L4 atmosphere / bands)
WASH_SAFFRON  = "#FDF3E3"  # kicker bands
WASH_SKY      = "#EEF3F9"  # atmosphere bands
WASH_PEACOCK  = "#EAF2EF"  # availability / success

# ---- L6 · Ink · Peacock ladder (typographic only, Law L2 — never fills) ----
INK   = "#123F3B"     # 8.9–11.4:1 on every layer — AAA       (oklch .336 .049 187)
INK2  = "#3E5C58"     # 5.6–7.1:1 — AA+                        (oklch .450 .036 186)
INK3  = "#506561"     # 4.6:1 on the deepest well — AA        (oklch .488 .026 183)

# ---- Peacock — the accent ramp (the only interactive hue, 186°, Law L3) ----
PEACOCK_300 = "#16837A"  # hover state / ramp top               (oklch .551 .092 186)
PEACOCK_400 = "#16837A"  # hover ramp target
PEACOCK_500 = "#0F766E"  # THE accent — CTAs, focus, markers     (oklch .511 .086 186)
PEACOCK_600 = "#0B5D57"  # accent as TEXT · 7.03:1 AAA          (oklch .432 .072 187)
ON_PEACOCK  = "#F9F7F0"  # text on peacock fills · 5.11:1        (oklch .976 .009 94)

# ---- Reserve accents · Law L4 (sacred, rationed) ----
CORAL   = "#A83F28"  # one italic word per page · 5.61:1         (oklch .510 .143 34)
SAFFRON = "#E9A23B"  # marks/charts only — NEVER text            (oklch .764 .142 72)
SKY     = "#9DB8D9"  # atmosphere only                           (oklch .774 .056 254)

# ---- Signal — feedback (light-world tuned; legal on strata + planes, Law S7) ----
SIGNAL_OK   = "#0E7447"   # oklch .515 .104 158 · ≥4.55:1 on legal surfaces
SIGNAL_WARN = "#8F610C"   # oklch .535 .108 75  · ≥4.55:1
SIGNAL_ERR  = "#AC3B27"   # oklch .515 .152 33  · ≥4.55:1

# ---- Dawn sky ramp — the hero as strata composition (VT-PRD-005 §5.8/§9) ----
SKY_TOP    = MILK          # #FDFCF8 — the zenith, first light
SKY_MID    = PORCELAIN     # #F7F4EC — the middle sky
SKY_BLUSH  = STRATUM_DAWN  # #FFEBE6 — the blush band (teaches the layer grammar)
SKY_GOLD   = "#FFEBD2"    # the gold-mid glow (oklch .950 .040 75)
SKY_BOTTOM = "#EFE3C2"    # the warm horizon (oklch .938 .042 85)

# ---- Legacy aliases kept so generated art reads the same — re-inks automatically ----
VOID = PORCELAIN           # the art canvas is now porcelain
SURFACE = MILK             # raised panels are milk
SURFACE2 = BONE            # wells are bone
EMBER = PEACOCK_500        # peacock now owns interaction
EMBER_300 = PEACOCK_300
EMBER_400 = PEACOCK_400
EMBER_500 = PEACOCK_500
EMBER_600 = PEACOCK_600
EMBER_700 = PEACOCK_600
ON_EMBER = ON_PEACOCK
AURORA = SKY               # the dawn ribbon replaces the dusk ribbon
BRASS_KITE = PEACOCK_500   # the kite is now peacock, the first star of morning
PAPER = MILK               # the paper world folded into milk
PAPER_INK = INK
PAPER_LINE = LINE

# ---- Named exports for the mirror check (tokens.css ↔ palette.py, Law C6) ----
CANVAS = PORCELAIN
SURFACE_1 = MILK
SURFACE_2 = BONE
LINE_STRONG_ = LINE_STRONG
ACCENT = PEACOCK_500
ACCENT_SOFT = PEACOCK_300
ACCENT_DEEP = PEACOCK_600
OK = SIGNAL_OK
WARN = SIGNAL_WARN
ERR = SIGNAL_ERR

# ---- STRATA named exports (VT-PRD-005 mirror check) ----
STRATUM = {"dawn": STRATUM_DAWN, "gold": STRATUM_GOLD, "sage": STRATUM_SAGE,
           "powder": STRATUM_POWDER, "blush": STRATUM_BLUSH, "gold-deep": STRATUM_GOLD_DEEP}
WELLS = {"porcelain": BONE, "sage": WELL_SAGE, "powder": WELL_POWDER,
         "blush": WELL_BLUSH, "gold": WELL_GOLD, "milk": "#E6E0D2"}
BAND_LINES = {"sage": LINE_SAGE, "powder": LINE_POWDER, "blush": LINE_BLUSH, "gold": LINE_GOLD}
