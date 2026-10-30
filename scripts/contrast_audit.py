#!/usr/bin/env python3
"""
GOLDEN HOUR contrast audit (VT-PRD-003 §12.6, §14).
Computes every critical WCAG 2.x pair of the Golden Hour palette — the
30-pair matrix of §12.6 plus the supplementary paper/meta/decorative
pairs — and FAILS (exit 1) on any violation. Also lints law L12
(signal hues >= 30 degrees from champagne on the OKLCH wheel).
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

# ---- GOLDEN HOUR palette (v2-src/palette.py) — espresso & champagne ----
CANVAS='251A11'; SURF1='30241A'; SURF2='3A2D23'; LINE='4A3D32'; LINE2='615246'; BORDER_IN='887769'
INK='EDEAE2'; INK2='C2BCB1'; INK3='A8A196'
CHAMP300='E9E1B0'; CHAMP400='E2D288'; CHAMP500='DAC46D'; CHAMP600='72560F'; CHAMP700='5A3E00'; ON_CHAMP='2A1C10'
DUSK='81AFA9'; BRASS='D3AB54'
OK='57CC88'; WARN='F49752'; ERR='FC6E68'
PAPER='EFEBDF'; PAPER2='E6E1D3'; PAPER_SURF='F7F4EA'; PINK='28231E'; PINK2='615951'; PLINE='D7D2C7'
PAPER_INK3='6B6359'   # .paper context meta grade — 4.96:1 on paper (kept verbatim from v2)

# (name, fg, on-label, bg, requirement)  requirement: 'text' 4.5 / 'aaa' 7 / 'ui' 3 / 'deco' none
# ---- THE 30-PAIR MATRIX (VT-PRD-003 §12.6) ----
critical = [
    # --- 1-7 · the dark world: text on surfaces ---
    ('1  ink (primary text)',                 INK,   'canvas',              CANVAS,   'aaa'),
    ('2  ink (primary text)',                 INK,   'surface-1 (cards)',   SURF1,    'aaa'),
    ('3  ink (primary text)',                 INK,   'surface-2 (hover)',   SURF2,    'aaa'),
    ('4  ink-2 (secondary text)',             INK2,  'canvas',              CANVAS,   'aaa'),
    ('5  ink-2 (secondary text)',             INK2,  'surface-1 (cards)',   SURF1,    'aaa'),
    ('6  ink-3 (tertiary/meta text)',         INK3,  'canvas',              CANVAS,   'text'),
    ('7  ink-3 (tertiary/meta text)',         INK3,  'surface-1 (cards)',   SURF1,    'text'),
    # --- 8-11 · champagne as text & fills ---
    ('8  champagne-500 kicker text',          CHAMP500, 'canvas',           CANVAS,   'text'),
    ('9  champagne-500 kicker text',          CHAMP500, 'surface-1 (cards)', SURF1,   'text'),
    ('10 on-champagne text on champagne-500', ON_CHAMP, 'champagne-500 fill (btn/chip/selection/skip)', CHAMP500, 'text'),
    ('11 on-champagne text on champagne-400', ON_CHAMP, 'champagne-400 fill (btn hover)', CHAMP400,    'text'),
    # --- 12-14 · focus rings & component boundaries (WCAG 1.4.11) ---
    ('12 focus ring champagne-500',           CHAMP500, 'canvas',           CANVAS,   'ui'),
    ('13 focus ring champagne-500',           CHAMP500, 'surface-1',        SURF1,    'ui'),
    ('14 border-input (form fields)',         BORDER_IN, 'canvas',          CANVAS,   'ui'),
    # --- 15-19 · the paper world: champagne grades ---
    ('15 champagne-700 kicker text on paper', CHAMP700, 'paper',            PAPER,    'text'),
    ('16 champagne-700 kicker text on paper-2', CHAMP700, 'paper-2',        PAPER2,   'text'),
    ('17 champagne-700 kicker text on paper-surface', CHAMP700, 'paper-surface', PAPER_SURF, 'text'),
    ('18 champagne-600 marks (rules/dots) on paper',  CHAMP600, 'paper',    PAPER,    'ui'),
    ('19 champagne-600 marks on paper-2',     CHAMP600, 'paper-2',          PAPER2,   'ui'),
    # --- 20-24 · ledger text ---
    ('20 paper-ink (primary) on paper',       PINK,  'paper',              PAPER,    'aaa'),
    ('21 paper-ink (primary) on paper-2',     PINK,  'paper-2',            PAPER2,   'aaa'),
    ('22 paper-ink (primary) on paper-surface', PINK, 'paper-surface',     PAPER_SURF, 'aaa'),
    ('23 paper-ink-2 (secondary) on paper',   PINK2, 'paper',              PAPER,    'text'),
    ('24 paper-ink-2 (secondary) on paper-2', PINK2, 'paper-2',            PAPER2,   'text'),
    # --- 25-28 · signal feedback ---
    ('25 signal-ok text',                     OK,    'canvas',             CANVAS,   'text'),
    ('26 signal-warn text (copper)',          WARN,  'canvas',             CANVAS,   'text'),
    ('27 signal-err text',                    ERR,   'canvas',             CANVAS,   'text'),
    ('28 signal-err text',                    ERR,   'surface-1',          SURF1,    'text'),
    # --- 29-30 · the one gradient (progress hairline ends) ---
    ('29 gradient end champagne-300',         CHAMP300, 'canvas',           CANVAS,   'ui'),
    ('30 gradient end champagne-500',         CHAMP500, 'canvas',           CANVAS,   'ui'),
]

# ---- supplementary pairs (kept from the v2 audit; all green, all documented) ----
supplementary = [
    ('S1 ink-2 (secondary text)',             INK2,  'surface-2',          SURF2,    'text'),
    ('S2 ink-3 (tertiary/meta text)',         INK3,  'surface-2',          SURF2,    'text'),
    ('S3 paper ink-3 (meta) on paper',        PAPER_INK3, 'paper',         PAPER,    'text'),
    ('S4 paper ink-3 (meta) on paper-2',      PAPER_INK3, 'paper-2',       PAPER2,   'text'),
    ('S5 champagne-600 marks on paper-surface', CHAMP600, 'paper-surface', PAPER_SURF, 'ui'),
    ('S6 dusk ribbon on canvas (atmosphere only)', DUSK, 'canvas',         CANVAS,   'text'),
    ('S7 brass kite on canvas (hero art only)', BRASS, 'canvas',           CANVAS,   'text'),
    ('S8 border-input on surface-1',          BORDER_IN, 'surface-1',      SURF1,    'ui'),
    # --- decorative (documented exemptions — hairlines are not information) ---
    ('D1 line (hairline) vs canvas',          LINE,  'canvas',             CANVAS,   'deco'),
    ('D2 line-strong vs canvas',              LINE2, 'canvas',             CANVAS,   'deco'),
    ('D3 paper-line vs paper',                PLINE, 'paper',              PAPER,    'deco'),
]

REQ = {'text': 4.5, 'aaa': 7.0, 'ui': 3.0, 'deco': 0.0}

def run(pairs, title):
    fails = 0
    for name, fg, bglabel, bg, req in pairs:
        r = ratio(fg, bg)
        need = REQ[req]
        ok = r >= need
        if not ok:
            fails += 1
        if req == 'deco':
            note = 'decorative (exempt)'
        elif req == 'ui':
            note = 'PASS (>=3)' if ok else 'FAIL (needs 3.0)'
        elif req == 'aaa':
            note = 'PASS AAA' if ok else 'FAIL (needs 7.0)'
        else:
            note = grade(r) if ok else 'FAIL (needs 4.5)'
        print(f"{name:<46} {bglabel:<46} {r:>6.2f}:1  {req:<5}  {note}")
    return fails

print(f"{'Foreground':<46} {'on':<46} {'Ratio':>7}  Req    WCAG")
print('-' * 118)
fails = run(critical, 'critical')
print('-' * 118)
sup_fails = run(supplementary, 'supplementary')
fails += sup_fails
print('-' * 118)

# ---- law L12 lint: signal hues >= 30 degrees from champagne on the OKLCH wheel ----
_, _, champ_hue = oklch(CHAMP500)
l12_fail = False
for name, sig in (('signal-ok', OK), ('signal-warn (copper)', WARN), ('signal-err', ERR)):
    _, _, hue = oklch(sig)
    dist = min(abs(hue - champ_hue), 360 - abs(hue - champ_hue))
    flag = 'PASS' if dist >= 30 else 'FAIL'
    if dist < 30: l12_fail = True
    print(f"L12 {name:<24} hue {hue:>3.0f} vs champagne {champ_hue:.0f} — {dist:>2.0f} degrees apart  {flag}")

print('-' * 118)
if fails or l12_fail:
    print(f"GOLDEN HOUR CONTRAST AUDIT: {fails} FAILURE(S)" + (" + L12 hue-collision" if l12_fail else ""))
    sys.exit(1)
aaa_count = 0
for name, fg, bglabel, bg, req in critical:
    if req in ('text', 'aaa') and ratio(fg, bg) >= 7:
        aaa_count += 1
print(f"GOLDEN HOUR CONTRAST AUDIT: 30/30 critical pairs green · {aaa_count} at AAA · "
      f"{len(supplementary)} supplementary green · zero WCAG 2.2 failures · L12 clean")
