#!/usr/bin/env python3
"""
FORGE NOIR contrast audit (VT-PRD-002 §7.5, §10.2).
Computes every critical WCAG 2.x pair of the Forge Noir palette and
FAILS (exit 1) on any violation. Run before every deploy: scripts/check-colors.sh
Values mirror v2-src/palette.py and assets/css/tokens.css — the single source.
"""
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

# ---- Forge Noir palette (v2-src/palette.py) ----
CANVAS='0E0C09'; SURF1='161310'; SURF2='1F1C18'; LINE='2B2825'; LINE2='403C37'; BORDER_IN='6D6861'
INK='EAE8E3'; INK2='B0ACA5'; INK3='96918B'
EMBER300='FFAC7E'; EMBER400='FE8F5B'; EMBER='E36E49'; EMBER600='C65029'; EMBER700='882D16'; ON_EMBER='0C0806'
AURORA='80D1B5'
OK='52CD86'; WARN='E7B643'; ERR='ED5350'
PAPER='EFEBDF'; PAPER2='E6E1D3'; PAPER_SURF='F7F4EA'; PINK='28231E'; PINK2='615951'; PLINE='D7D2C7'
PAPER_INK3='6B6359'   # .paper context meta grade — 4.96:1 on paper (PRD draft 756D64 measured 4.27 and was corrected)

# (name, fg, on-label, bg, requirement)  requirement: 'text' 4.5 / 'aaa' 7 / 'ui' 3 / 'deco' none
pairs = [
    # --- dark world: text on surfaces ---
    ('ink (primary text)',            INK,  'canvas',              CANVAS,  'aaa'),
    ('ink (primary text)',            INK,  'surface-1 (cards)',   SURF1,   'aaa'),
    ('ink (primary text)',            INK,  'surface-2 (hover)',   SURF2,   'aaa'),
    ('ink-2 (secondary text)',        INK2, 'canvas',              CANVAS,  'text'),
    ('ink-2 (secondary text)',        INK2, 'surface-1 (cards)',   SURF1,   'text'),
    ('ink-2 (secondary text)',        INK2, 'surface-2',           SURF2,   'text'),
    ('ink-3 (tertiary/meta text)',    INK3, 'canvas',              CANVAS,  'text'),
    ('ink-3 (tertiary/meta text)',    INK3, 'surface-1 (cards)',   SURF1,   'text'),
    ('ink-3 (tertiary/meta text)',    INK3, 'surface-2 (hover)',   SURF2,   'text'),
    # --- accents as text on dark ---
    ('ember-500 as text (kicker/links)', EMBER, 'canvas',          CANVAS,  'text'),
    ('ember-500 as text',             EMBER, 'surface-1 (cards)',  SURF1,   'text'),
    # --- accent fills ---
    ('on-ember text on ember-500 (btn/checked chip/selection/skip)', ON_EMBER, 'ember-500 fill', EMBER, 'text'),
    ('on-ember text on ember-400 (btn hover)', ON_EMBER, 'ember-400 fill', EMBER400, 'text'),
    # --- feedback ---
    ('signal-ok text',   OK,   'canvas', CANVAS, 'text'),
    ('signal-warn text', WARN, 'canvas', CANVAS, 'text'),
    ('signal-err text',  ERR,  'canvas', CANVAS, 'text'),
    ('signal-err text',  ERR,  'surface-1', SURF1, 'text'),
    # --- paper world (Ledger) ---
    ('paper-ink (primary) on paper',      PINK,  'paper',           PAPER,   'aaa'),
    ('paper-ink (primary) on paper-2',    PINK,  'paper-2',         PAPER2,  'aaa'),
    ('paper-ink (primary) on paper-surface', PINK, 'paper-surface', PAPER_SURF, 'aaa'),
    ('paper-ink-2 (secondary) on paper',  PINK2, 'paper',           PAPER,   'text'),
    ('paper-ink-2 (secondary) on paper-2', PINK2, 'paper-2',        PAPER2,  'text'),
    ('paper ink-3 (meta) on paper',       PAPER_INK3, 'paper',      PAPER,   'text'),
    ('paper ink-3 (meta) on paper-2',     PAPER_INK3, 'paper-2',    PAPER2,  'text'),
    ('ember-700 kicker text on paper',    EMBER700, 'paper',        PAPER,   'text'),
    ('ember-700 kicker text on paper-2',  EMBER700, 'paper-2',      PAPER2,  'text'),
    ('ember-700 kicker text on paper-surface', EMBER700, 'paper-surface', PAPER_SURF, 'text'),
    # --- marks & non-text ---
    ('ember-600 marks (rules/dots/units) on paper', EMBER600, 'paper', PAPER, 'ui'),
    ('ember-600 marks on paper-surface', EMBER600, 'paper-surface', PAPER_SURF, 'ui'),
    ('aurora on canvas (atmosphere only)', AURORA, 'canvas', CANVAS, 'text'),
    # --- component boundaries (WCAG 1.4.11) ---
    ('border-input on surface-1 (form fields)', BORDER_IN, 'surface-1', SURF1, 'ui'),
    ('border-input on canvas',                  BORDER_IN, 'canvas',    CANVAS, 'ui'),
    ('ember-500 focus ring on canvas',          EMBER, 'canvas',        CANVAS, 'ui'),
    ('ember-500 focus ring on surface-1',       EMBER, 'surface-1',     SURF1,  'ui'),
    # --- decorative (documented exemptions) ---
    ('line (hairline) vs canvas',   LINE,  'canvas',  CANVAS, 'deco'),
    ('line-strong vs canvas',       LINE2, 'canvas',  CANVAS, 'deco'),
    ('paper-line vs paper',         PLINE, 'paper',   PAPER,  'deco'),
]

REQ = {'text': 4.5, 'aaa': 7.0, 'ui': 3.0, 'deco': 0.0}
fails = 0
print(f"{'Foreground':<52} {'on':<20} {'Ratio':>7}  Req    WCAG")
print('-' * 100)
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
    print(f"{name:<52} {bglabel:<20} {r:>6.2f}:1  {req:<5}  {note}")

print('-' * 100)
if fails:
    print(f"FORGE NOIR CONTRAST AUDIT: {fails} FAILURE(S)")
    sys.exit(1)
print("FORGE NOIR CONTRAST AUDIT: all pairs green — zero WCAG 2.2 AA failures")
