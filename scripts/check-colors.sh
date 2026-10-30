#!/bin/bash
# ============================================================
# GOLDEN HOUR — pre-deploy color gates (VT-PRD-003 §15.2)
# Fails the deploy on any violation of the Thirteen Laws (§12.7).
#   Gate 1 · WCAG contrast matrix, 30 critical pairs (law L7)
#   Gate 2 · dusk ribbon never touches UI CSS (law L3)
#   Gate 3 · no retired tokens — v1 Night Forge + Forge Noir (law L2)
#   Gate 4 · one palette source at the build layer (law L9)
#   Gate 5 · gradients in-family (law L4)
#   Gate 6 · THE BLACK FLOOR + HUE FLOOR (laws L0 + L1)
#   Gate 7 · no raw color outside tokens.css — hex OR rgba (law L9)
# ============================================================
set -e
cd "$(dirname "$0")/.."

echo "— Gate 1 · WCAG contrast matrix, 30 critical pairs (law L7) —"
python3 scripts/contrast_audit.py

echo "— Gate 2 · dusk ribbon never touches UI CSS (law L3) —"
if rg -q 'var\(--vf-aurora\)' assets/css/; then
  echo "FAIL: --vf-aurora used in assets/css — the dusk ribbon is hero sky art ONLY"; exit 1
fi
echo "  clean"

echo "— Gate 3 · no retired tokens: v1 Night Forge + Forge Noir (law L2) —"
if rg -qi '7EE8C7|FF6B35|E36E49|FE8F5B|FFAC7E|882D16|C65029|80D1B5|0E0C09|161310|1F1C18|2B2825|403C37|6D6861|EAE8E3|B0ACA5|96918B|0C0806|52CD86|E7B643|ED5350|1A1712|26221C' \
     assets/css assets/js assets/img/favicon.svg assets/img/generated v2-src \
     index.html 404.html manifest.json work services about contact journal legal; then
  echo "FAIL: retired palette value found — every color must come from the current palette.py"; exit 1
fi
echo "  clean"

echo "— Gate 4 · one palette source at the build layer (law L9) —"
python3 - <<'PYEOF'
import re, sys
sys.path.insert(0, "v2-src")
import palette as P
css = open("assets/css/tokens.css", encoding="utf-8").read()
def var(name):
    m = re.search(r'--vf-' + name + r':\s*(#[0-9A-Fa-f]{6})\b', css)
    return m.group(1).upper() if m else None
pairs = [
    ("canvas", P.ROAST_950), ("surface-1", P.ROAST_900), ("surface-2", P.ROAST_850),
    ("line", P.ROAST_800), ("line-strong", P.ROAST_700), ("border-input", P.ROAST_600),
    ("ink", P.INK), ("ink-2", P.INK2), ("ink-3", P.INK3),
    ("ember", P.CHAMP_500), ("ember-soft", P.CHAMP_400),
    ("ember-text-paper", P.CHAMP_700), ("ember-mark-paper", P.CHAMP_600),
    ("on-ember", P.ON_CHAMP), ("aurora", P.DUSK_RIBBON),
    ("ok", P.SIGNAL_OK), ("warn", P.SIGNAL_WARN), ("err", P.SIGNAL_ERR),
    ("paper", P.LEDGER_50), ("paper-2", P.LEDGER_100), ("paper-line", P.LEDGER_200),
    ("paper-ink", P.LEDGER_INK), ("paper-ink-2", P.LEDGER_INK2),
]
bad = [(n, v, var(n)) for n, v in pairs if var(n) != v.upper()]
if bad:
    for n, v, c in bad:
        print(f"  FAIL: --vf-{n} = {c} in tokens.css vs {v.upper()} in palette.py")
    sys.exit(1)
print(f"  {len(pairs)} tokens in sync: palette.py == tokens.css")
PYEOF

echo "— Gate 5 · gradients in-family (law L4) —"
GRAD_HITS=$(rg -n 'gradient\(' assets/css/ -g '!tokens.css' | rg '#[0-9A-Fa-f]{3,8}|rgba?\(' || true)
if [ -n "$GRAD_HITS" ]; then
  echo "FAIL: gradient with a raw color outside tokens.css — gradients are built from tokens:"; echo "$GRAD_HITS"; exit 1
fi
if ! rg -q 'linear-gradient\(90deg, #E9E1B0 0%, #DAC46D 100%\)' assets/css/tokens.css; then
  echo "FAIL: the one sanctioned ramp --vf-gradient-ember must be champagne-300 -> 500 (#E9E1B0 -> #DAC46D)"; exit 1
fi
echo "  the one ramp is champagne-300->500 · every other gradient is token-built"

echo "— Gate 6 · THE BLACK FLOOR + HUE FLOOR (laws L0 + L1) —"
python3 - <<'PYEOF'
import math, sys
sys.path.insert(0, "v2-src")
import palette as P

def oklch(hexstr):
    """sRGB hex -> (L, C, H): the perceptual truth, computed not asserted."""
    def s(c):
        c /= 255.0
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r, g, b = (int(hexstr.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    R, G, B = s(r), s(g), s(b)
    l = 0.4122214708*R + 0.5363325363*G + 0.0514459929*B
    m = 0.2119034982*R + 0.6806995451*G + 0.1073969566*B
    s_ = 0.0883024619*R + 0.2817188376*G + 0.6299787005*B
    l_, m_, ss = l**(1/3), m**(1/3), s_**(1/3)
    L = 0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*ss
    a = 1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*ss
    b_ = 0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*ss
    return L, math.hypot(a, b_), math.degrees(math.atan2(b_, a)) % 360

surfaces = [
    ("roast-950 canvas",        P.ROAST_950), ("roast-900 surface-1", P.ROAST_900),
    ("roast-850 surface-2",     P.ROAST_850), ("roast-800 line",     P.ROAST_800),
    ("roast-700 line-strong",   P.ROAST_700), ("roast-600 border-input", P.ROAST_600),
    ("on-champagne",            P.ON_CHAMP),  ("champagne-700 paper text", P.CHAMP_700),
    ("champagne-600 paper marks", P.CHAMP_600), ("paper-ink", P.LEDGER_INK),
    ("paper-ink-2",             P.LEDGER_INK2),
]
fails = 0
print("  L0 · the Black Floor — every surface clears OKLCH L >= 0.22 or C >= 0.035:")
for name, hexv in surfaces:
    L, C, H = oklch(hexv)
    ok = L >= 0.22 or C >= 0.035
    if not ok:
        print(f"    FAIL BLACK ZONE: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f})")
        fails += 1
print("  L1 · the Hue Floor — canvas-family chroma >= 0.018 (warmth must be a perception):")
for name, hexv in [("roast-950 canvas", P.ROAST_950), ("roast-900 surface-1", P.ROAST_900),
                   ("roast-850 surface-2", P.ROAST_850)]:
    L, C, H = oklch(hexv)
    if C < 0.018:
        print(f"    FAIL HUE FLOOR: {name} {hexv} chroma {C:.3f} < 0.018")
        fails += 1
if fails:
    sys.exit(1)
print("    all floors held")
PYEOF

echo "— Gate 7 · NO RAW COLOR outside tokens.css — hex OR rgb()/rgba() (law L9) —"
RAW=$(rg -n '#[0-9A-Fa-f]{3,8}|rgba?\(\s*[0-9]' assets/css/ -g '!tokens.css' || true)
if [ -n "$RAW" ]; then
  echo "FAIL: raw color outside tokens.css — a color written anywhere else is a bug:"; echo "$RAW"; exit 1
fi
echo "  clean — zero hex, zero rgb()/rgba() literals outside tokens.css"

echo ""
echo "GOLDEN HOUR: all 7 color gates green"
