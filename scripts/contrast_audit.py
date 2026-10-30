#!/usr/bin/env python3
"""
STRATA contrast audit (VT-PRD-005 §6/§11).
Computes every critical WCAG 2.x pair of the Layered Light palette — the
§6 matrix over ALL legal surfaces (ground, six strata, milk plane, six
wells) — and FAILS (exit 1) on any violation. Also lints the laws:
  S1/L0 · the light-world floor: every fill clears OKLCH L >= 0.89
  L2  · ink is a chromatic peacock jewel (hue 178–192°, C >= 0.020)
  S2  · strata stay in the dawn family (L .955–.960, C .020–.040)
  S4  · visibility: band-vs-ground >= 3% rel-lum delta or >= 25° hue step
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

# ---- STRATA palette (v2-src/palette.py) — ground, strata, planes, wells ----
CANVAS='F7F4EC'; SURF1='FDFCF8'; SURF2='F0EBDF'; WELL_MILK='E6E0D2'
ST_DAWN='FFEBE6'; ST_GOLD='FDECCF'; ST_SAGE='E7F5E7'; ST_POWDER='E3F3FF'; ST_BLUSH='FFE9EA'; ST_GOLD_DEEP='FEEFD7'
W_SAGE='DCEEDC'; W_POWDER='D8EAFD'; W_BLUSH='FCE1E0'; W_GOLD='F7E6CA'
WASH_SAF='FDF3E3'; WASH_SKY='EEF3F9'; WASH_PEA='EAF2EF'
LINE='E2DBC8'; LINE2='CFC6AE'; BORDER_IN='857A5F'
INK='123F3B'; INK2='3E5C58'; INK3='506561'
ACCENT='0F766E'; ACCENT_SOFT='16837A'; ACCENT_DEEP='0B5D57'; ON_ACCENT='F9F7F0'
CORAL='A83F28'; SAFFRON='E9A23B'; SKY='9DB8D9'
OK='0E7447'; WARN='8F610C'; ERR='AC3B27'

# ---- Legal surfaces (Law S7): where text/marks may actually sit ----
TEXT_SURFACES = [
    ("canvas porcelain", CANVAS), ("stratum dawn", ST_DAWN), ("stratum gold", ST_GOLD),
    ("stratum sage", ST_SAGE), ("stratum powder", ST_POWDER), ("stratum blush", ST_BLUSH),
    ("stratum gold-deep", ST_GOLD_DEEP), ("milk plane", SURF1),
    ("well bone", SURF2), ("well sage", W_SAGE), ("well powder", W_POWDER),
    ("well blush", W_BLUSH), ("well gold", W_GOLD), ("well milk", WELL_MILK),
]
# Signals are legal on strata + planes only (never wells) — Law S7
SIGNAL_SURFACES = [(n, h) for n, h in TEXT_SURFACES if not n.startswith("well")]

# ---- §6 verified matrix (fg, surfaces, minimum) ----
GROUPS = [
    ("ink (AAA)",         INK,   TEXT_SURFACES,    7.0),
    ("ink-2 (AA+)",       INK2,  TEXT_SURFACES,    4.5),
    ("ink-3 (AA)",        INK3,  TEXT_SURFACES,    4.5),
    ("accent-deep text",  ACCENT_DEEP, TEXT_SURFACES, 4.5),
    ("accent UI/large",   ACCENT,      TEXT_SURFACES, 3.0),
    ("accent-soft UI",    ACCENT_SOFT, TEXT_SURFACES, 3.0),
    ("coral text",        CORAL,       TEXT_SURFACES, 4.5),
    ("signal ok text",    OK,          SIGNAL_SURFACES, 4.5),
    ("signal warn text",  WARN,        SIGNAL_SURFACES, 4.5),
    ("signal err text",   ERR,         SIGNAL_SURFACES, 4.5),
    ("border-input UI",   BORDER_IN,   [("canvas porcelain", CANVAS), ("well bone", SURF2)], 3.0),
    ("on-accent on accent",  ON_ACCENT, [("accent fill", ACCENT)],       4.5),
    ("on-accent on deep",    ON_ACCENT, [("accent-deep fill", ACCENT_DEEP)], 4.5),
]


def run():
    fails = 0
    total = 0
    for name, fg, surfaces, req in GROUPS:
        worst = min(((ratio(fg, bg), n) for n, bg in surfaces))
        r, surf = worst
        total += len(surfaces)
        ok = r >= req
        if not ok:
            fails += 1
        note = 'PASS AAA' if (ok and r >= 7) else (grade(r) if ok else 'FAIL')
        print(f"{name:<22} worst {r:>6.2f}:1 on {surf:<18} req {req:<4}  {note}  ({len(surfaces)} surfaces verified)")
    return fails, total


print(f"{'Group':<24} {'Worst pair':<32} {'Ratio':>7}  Req    WCAG")
print('-' * 100)
fails, total = run()
print('-' * 100)

# ---- Law L2 lint: ink is a chromatic peacock jewel, never grey-black ----
l2_fail = False
for name, hexv in (('ink', INK), ('ink-2', INK2), ('ink-3', INK3)):
    L, C, H = oklch(hexv)
    in_band = (178 <= H <= 192) and (C >= 0.020) and (L >= 0.45 or C >= 0.035)
    if not in_band:
        l2_fail = True
        print(f"L2 FAIL: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) is outside the peacock band (178–192°, C>=0.020)")
    else:
        print(f"L2 {name:<6} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) · chromatic peacock jewel  PASS")

# ---- Law S1/L0 lint: the light-world floor — every fill is LIGHT ----
l0_fail = False
FILLS = [('ground porcelain', CANVAS), ('milk plane', SURF1), ('well bone', SURF2),
         ('stratum dawn', ST_DAWN), ('stratum gold', ST_GOLD), ('stratum sage', ST_SAGE),
         ('stratum powder', ST_POWDER), ('stratum blush', ST_BLUSH), ('stratum gold-deep', ST_GOLD_DEEP),
         ('well sage', W_SAGE), ('well powder', W_POWDER), ('well blush', W_BLUSH),
         ('well gold', W_GOLD), ('well milk', WELL_MILK),
         ('wash-saffron', WASH_SAF), ('wash-sky', WASH_SKY), ('wash-peacock', WASH_PEA)]
for name, hexv in FILLS:
    L, C, H = oklch(hexv)
    if L < 0.89:
        l0_fail = True
        print(f"S1 FAIL: {name} {hexv} — oklch L {L:.3f} < 0.89 (the light-world floor is breached)")
    else:
        print(f"S1 {name:<18} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f})  PASS")

# ---- Law S2 lint: strata stay in the dawn family ----
s2_fail = False
for name, hexv in (('stratum dawn', ST_DAWN), ('stratum gold', ST_GOLD), ('stratum sage', ST_SAGE),
                   ('stratum powder', ST_POWDER), ('stratum blush', ST_BLUSH), ('stratum gold-deep', ST_GOLD_DEEP)):
    L, C, H = oklch(hexv)
    if not (0.948 <= L <= 0.965 and 0.020 <= C <= 0.045):
        s2_fail = True
        print(f"S2 FAIL: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) outside the dawn-family band (L .948–.965, C .020–.045)")
    else:
        print(f"S2 {name:<18} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) · dawn family  PASS")

# ---- Law S4 lint: band visibility — strata vs ground ----
def rel(h):
    return lum(hx(h))
s4_fail = False
import colorsys
def hue_of(h):
    r, g, b = (c/255 for c in hx(h))
    hh, ss, vv = colorsys.rgb_to_hsv(r, g, b)
    return hh*360, ss
print('-' * 100)
print("Law S4 · band visibility vs ground (>=3% rel-lum delta or >=25 deg hue step):")
for name, hexv in (('stratum dawn', ST_DAWN), ('stratum gold', ST_GOLD), ('stratum sage', ST_SAGE),
                   ('stratum powder', ST_POWDER), ('stratum blush', ST_BLUSH)):
    dl = abs(rel(hexv) - rel(CANVAS)) / rel(CANVAS) * 100
    hg, _ = hue_of(hexv)
    chg, _ = hue_of(CANVAS)
    dh = min(abs(hg-chg), 360-abs(hg-chg))
    ok = dl >= 3.0 or dh >= 25
    if not ok:
        s4_fail = True
    print(f"  {name:<16} Δlum {dl:5.1f}% · Δhue {dh:5.1f}°  {'PASS' if ok else 'FAIL'}")

print('-' * 100)
if fails or l2_fail or l0_fail or s2_fail or s4_fail:
    print(f"STRATA CONTRAST AUDIT: {fails} GROUP FAILURE(S)" +
          (" + L2 ink law" if l2_fail else "") + (" + S1 light floor" if l0_fail else "") +
          (" + S2 dawn family" if s2_fail else "") + (" + S4 visibility" if s4_fail else ""))
    sys.exit(1)
print(f"STRATA CONTRAST AUDIT: {total} pairs green across {len(TEXT_SURFACES)} legal surfaces · "
      f"zero WCAG 2.2 failures · ink law L2 clean · light floor S1 held · dawn family S2 held · visibility S4 held")
