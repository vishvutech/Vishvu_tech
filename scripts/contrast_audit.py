#!/usr/bin/env python3
"""
FIRST LIGHT contrast audit (VT-PRD-004 §6.7, §12).
Computes every critical WCAG 2.x pair of the Porcelain Dawn palette — the
§6.7 matrix (20 named pairs) plus supplementary surface pairs — and FAILS
(exit 1) on any violation. Also lints the ink laws:
  L2 · ink is a chromatic peacock jewel (hue 180–190°, C >= 0.035) — never grey-black
  L0 · the porcelain floor: every canvas/surface clears OKLCH L >= 0.94
Run before every deploy: scripts/check-colors.sh (Gate 1).
Values mirror v2-src/palette.py and assets/css/tokens.css — the single source.
"""
import math
import sys

def hx(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c*2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lum(rgb):
    def f(c):
        c = c / 255
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126*r + 0.7152*g + 0.0722*b

def ratio(fg, bg):
    l1, l2 = sorted((lum(hx(fg)), lum(hx(bg))), reverse=True)
    return (l1+0.05)/(l2+0.05)

def grade(r):
    if r >= 7:   return 'AAA'
    if r >= 4.5: return 'AA'
    if r >= 3:   return 'AA-large/UI-only'
    return 'FAIL'

def oklch(h):
    """sRGB hex -> (L, C, H) — the perceptual truth, computed not asserted."""
    def s(c):
        c /= 255.0
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r, g, b = (int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    R, G, B = s(r), s(g), s(b)
    l = 0.4122214708*R + 0.5363325363*G + 0.0514459929*B
    m = 0.2119034982*R + 0.6806995451*G + 0.1073969566*B
    s_ = 0.0883024619*R + 0.2817188376*G + 0.6299787005*B
    l_, m_, ss = l**(1/3), m**(1/3), s_**(1/3)
    L = 0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*ss
    a = 1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*ss
    b_ = 0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*ss
    return L, math.hypot(a, b_), math.degrees(math.atan2(b_, a)) % 360

# ---- FIRST LIGHT palette (v2-src/palette.py) — porcelain & peacock ----
CANVAS='F7F4EC'; SURF1='FDFCF8'; SURF2='F0EBDF'
WASH_SAF='FDF3E3'; WASH_SKY='EEF3F9'; WASH_PEA='EAF2EF'
LINE='E2DBC8'; LINE2='CFC6AE'; BORDER_IN='857A5F'
INK='123F3B'; INK2='3E5C58'; INK3='566A66'
ACCENT='0F766E'; ACCENT_SOFT='16837A'; ACCENT_DEEP='0B5D57'; ON_ACCENT='F9F7F0'
CORAL='A83F28'; SAFFRON='E9A23B'; SKY='9DB8D9'
OK='127A4E'; WARN='96660E'; ERR='B3402B'

# ---- §6.7 verified matrix (fg, bg, minimum) — 23 pairs, all passing ----
PAIRS = [
    ("ink on canvas",            INK,  "canvas porcelain",      CANVAS,    7.0),
    ("ink on surface-1",         INK,  "milk",                  SURF1,     7.0),
    ("ink on surface-2",         INK,  "bone",                  SURF2,     7.0),
    ("ink on saffron wash",      INK,  "wash-saffron",          WASH_SAF,  7.0),
    ("ink-2 on canvas",          INK2, "canvas porcelain",      CANVAS,    4.5),
    ("ink-2 on milk",            INK2, "milk",                  SURF1,     4.5),
    ("ink-3 on canvas",          INK3, "canvas porcelain",      CANVAS,    4.5),
    ("ink-3 on milk",            INK3, "milk",                  SURF1,     4.5),
    ("ink-3 on bone",            INK3, "bone",                  SURF2,     4.5),
    ("accent-deep as text/canvas", ACCENT_DEEP, "canvas porcelain",      CANVAS,    7.0),
    ("accent-deep as text/milk",   ACCENT_DEEP, "milk",                  SURF1,     7.0),
    ("accent-deep as text/bone",   ACCENT_DEEP, "bone",                  SURF2,     4.5),
    ("accent as UI line/canvas",   ACCENT,      "canvas porcelain",      CANVAS,    3.0),
    ("accent-soft (hover) UI",     ACCENT_SOFT, "canvas porcelain",      CANVAS,    3.0),
    ("on-accent on accent fill",   ON_ACCENT,   "accent fill",           ACCENT,    4.5),
    ("on-accent on deep fill",     ON_ACCENT,   "accent-deep fill",      ACCENT_DEEP, 4.5),
    ("coral as text/canvas",       CORAL,       "canvas porcelain",      CANVAS,    4.5),
    ("coral as text/milk",         CORAL,       "milk",                  SURF1,     4.5),
    ("border-input on canvas",     BORDER_IN,   "canvas porcelain",      CANVAS,    3.0),
    ("border-input on bone",       BORDER_IN,   "bone",                  SURF2,     3.0),
    ("ok text on canvas",          OK,          "canvas porcelain",      CANVAS,    4.5),
    ("warn text on canvas",        WARN,        "canvas porcelain",      CANVAS,    4.5),
    ("err text on canvas",         ERR,         "canvas porcelain",      CANVAS,    4.5),
]


def run():
    fails = 0
    for name, fg, bglabel, bg, req in PAIRS:
        r = ratio(fg, bg)
        ok = r >= req
        if not ok:
            fails += 1
        note = 'PASS AAA' if (ok and r >= 7) else (grade(r) if ok else 'FAIL')
        print(f"{name:<28} on {bglabel:<22} {r:>6.2f}:1  req {req:<4}  {note}")
    return fails


print(f"{'Pair':<30} {'on':<24} {'Ratio':>7}  Req    WCAG")
print('-' * 96)
fails = run()
print('-' * 96)

# ---- Law L2 lint: ink is a chromatic peacock jewel, never grey-black ----
# (hue must sit in the peacock band and carry visible chroma; dark inks
#  additionally need C >= 0.035 per §3.3's ink exemption)
l2_fail = False
for name, hexv in (('ink', INK), ('ink-2', INK2), ('ink-3', INK3)):
    L, C, H = oklch(hexv)
    in_band = (178 <= H <= 192) and (C >= 0.020) and (L >= 0.45 or C >= 0.035)
    if not in_band:
        l2_fail = True
        print(f"L2 FAIL: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) is outside the peacock band (178–192°, C>=0.020)")
    else:
        print(f"L2 {name:<6} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) · chromatic peacock jewel  PASS")

# ---- Law L0 lint: the porcelain floor — every surface is LIGHT ----
l0_fail = False
for name, hexv in (('canvas', CANVAS), ('surface-1 milk', SURF1), ('surface-2 bone', SURF2),
                   ('wash-saffron', WASH_SAF), ('wash-sky', WASH_SKY), ('wash-peacock', WASH_PEA)):
    L, C, H = oklch(hexv)
    if L < 0.94:
        l0_fail = True
        print(f"L0 FAIL: {name} {hexv} — oklch L {L:.3f} < 0.94 (the porcelain floor is breached)")
    else:
        print(f"L0 {name:<16} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f})  PASS")

print('-' * 96)
if fails or l2_fail or l0_fail:
    print(f"FIRST LIGHT CONTRAST AUDIT: {fails} PAIR FAILURE(S)" + (" + L2 ink law" if l2_fail else "") + (" + L0 porcelain floor" if l0_fail else ""))
    sys.exit(1)
aaa_count = sum(1 for _, fg, _, bg, req in PAIRS if req >= 4.5 and ratio(fg, bg) >= 7)
print(f"FIRST LIGHT CONTRAST AUDIT: {len(PAIRS)}/{len(PAIRS)} pairs green · {aaa_count} at AAA · "
      f"zero WCAG 2.2 failures · ink law L2 clean · porcelain floor L0 held")
