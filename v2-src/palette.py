#!/usr/bin/env python3
"""
Vishvu Tech — FIRST LIGHT palette (VT-PRD-004 §6, "Porcelain Dawn")
Single source of truth for every color the build touches.
tokens.css mirrors these values; svgs.py, the OG generator and the
favicon/icons are all derived from HERE. Law L9: no raw color anywhere else.

OKLCH primitives (hue 88–95 porcelain / hue 186 peacock — the light world)
→ computed sRGB hex. Every pairing verified by scripts/contrast_audit.py.

THE MANDATE: zero black, zero brown, zero dark shades anywhere — the
canvas is porcelain ivory, ink is a chromatic peacock jewel, and depth
is lightness + cast shadows, never darkness.
"""

# ---- Porcelain Ladder — neutrals (hue 88–95°, Law L0/L1) ----
PORCELAIN    = "#F7F4EC"  # page canvas — porcelain ivory      (oklch .967 .011 90)
MILK         = "#FDFCF8"  # surface-1 — raised cards           (oklch .991 .005 95)
BONE         = "#F0EBDF"  # surface-2 — inset wells, darkest neutral (oklch .941 .017 88)
LINE         = "#E2DBC8"  # decorative hairlines               (oklch .892 .027 90)
LINE_STRONG = "#CFC6AE"  # structural hairlines               (oklch .827 .034 90)
BORDER_IN    = "#857A5F"  # border-input — WCAG 1.4.11 · 3.86:1 (oklch .582 .041 88)

# Washes — tinted porcelain (Law L4 atmosphere / bands)
WASH_SAFFRON  = "#FDF3E3"  # kicker bands
WASH_SKY      = "#EEF3F9"  # atmosphere bands
WASH_PEACOCK  = "#EAF2EF"  # availability / success

# ---- Ink · Peacock ladder (typographic only, Law L2 — never fills) ----
INK   = "#123F3B"     # 10.62:1 on canvas — AAA                 (oklch .336 .049 187)
INK2  = "#3E5C58"     # 6.64:1 — AA+                            (oklch .450 .036 186)
INK3  = "#566A66"     # 5.24:1 — AA · min meta grade            (oklch .507 .025 182)

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

# ---- Signal — feedback (light-world tuned) ----
SIGNAL_OK   = "#127A4E"   # oklch .528 .106 158 · 4.87:1
SIGNAL_WARN = "#96660E"   # oklch .548 .111 75  · 4.55:1
SIGNAL_ERR  = "#B3402B"   # oklch .529 .154 33  · 5.18:1

# ---- Dawn sky ramp (hero sky art only — light, not void) ----
SKY_TOP    = MILK          # #FDFCF8 — the zenith, first light
SKY_MID    = PORCELAIN     # #F7F4EC — the middle sky
SKY_BOTTOM = "#F0E9D8"     # the horizon, warm bone (light with hue temperature)

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
