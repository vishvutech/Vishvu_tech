#!/bin/bash
# ============================================================
# STRATA — pre-deploy color gates (VT-PRD-005 §11)
# Fails the deploy on any violation of the Laws of Strata (§4/§13).
#   Gate 1 · WCAG contrast matrix over ALL legal surfaces (§6)
#   Gate 2 · THE BAN LIST — zero black/brown/dark anywhere (Law S1)
#   Gate 3 · no retired tokens — Golden Hour espresso/champagne + prior dark worlds
#   Gate 4 · one palette source at the build layer (law C6/L9, incl. strata)
#   Gate 5 · gradients in-family (law L4)
#   Gate 6 · the light-world floor + peacock ink band (laws S1/L2)
#   Gate 7 · no raw color outside tokens.css — hex OR rgba (law L9)
#   Gate 8 · zero legacy --vf- references (§14.1 gate G1)
#   Gate 9 · STRATA band rhythm — the layering itself (Law S4/S6)
# ============================================================
set -e
cd "$(dirname "$0")/.."

echo "— Gate 1 · WCAG contrast matrix, all legal surfaces (VT-PRD-005 §6) —"
python3 scripts/contrast_audit.py

echo ""
echo "— Gate 2 · THE BAN LIST — zero black/brown/dark anywhere (§3.3) —"
python3 scripts/banlist_scan.py

echo ""
echo "— Gate 3 · no retired palettes: Golden Hour + Forge Noir + Night Forge —"
if rg -qi '251A11|30241A|3A2D23|4A3D32|615246|DAC46D|D3AB54|E9E1B0|E2D288|81AFA9|7EE8C7|FF6B35|E36E49|FE8F5B|FFAC7E|882D16|C65029|80D1B5|0E0C09|161310|1F1C18|2B2825|403C37|6D6861|EAE8E3|B0ACA5|96918B|0C0806|52CD86|E7B643|ED5350|1A1712|26221C' \
     assets/css assets/js assets/img/favicon.svg assets/img/generated v2-src \
     index.html 404.html manifest.json work services about contact journal legal; then
  echo "FAIL: retired palette value found — every color must come from the current palette.py"; exit 1
fi
echo "  clean"

echo ""
echo "— Gate 4 · one palette source at the build layer (law C6/L9) —"
python3 - <<'PYEOF'
import re, sys
sys.path.insert(0, "v2-src")
import palette as P
css = open("assets/css/tokens.css", encoding="utf-8").read()
def var(name):
    m = re.search(r'--vt-' + name + r':\s*(#[0-9A-Fa-f]{6})\b', css)
    return m.group(1).upper() if m else None
pairs = [
    ("canvas", P.PORCELAIN), ("surface-1", P.MILK), ("surface-2", P.BONE),
    ("line", P.LINE), ("line-strong", P.LINE_STRONG), ("border-input", P.BORDER_IN),
    ("ink", P.INK), ("ink-2", P.INK2), ("ink-3", P.INK3),
    ("accent", P.PEACOCK_500), ("accent-soft", P.PEACOCK_300), ("accent-deep", P.PEACOCK_600),
    ("on-accent", P.ON_PEACOCK),
    ("coral", P.CORAL), ("saffron", P.SAFFRON), ("sky", P.SKY),
    ("ok", P.SIGNAL_OK), ("warn", P.SIGNAL_WARN), ("err", P.SIGNAL_ERR),
    ("wash-saffron", P.WASH_SAFFRON), ("wash-sky", P.WASH_SKY), ("wash-peacock", P.WASH_PEACOCK),
    # STRATA tokens (VT-PRD-005 §5)
    ("stratum-dawn", P.STRATUM_DAWN), ("stratum-gold", P.STRATUM_GOLD),
    ("stratum-sage", P.STRATUM_SAGE), ("stratum-powder", P.STRATUM_POWDER),
    ("stratum-blush", P.STRATUM_BLUSH), ("stratum-gold-deep", P.STRATUM_GOLD_DEEP),
    ("well-sage", P.WELL_SAGE), ("well-powder", P.WELL_POWDER),
    ("well-blush", P.WELL_BLUSH), ("well-gold", P.WELL_GOLD),
    ("line-sage", P.LINE_SAGE), ("line-powder", P.LINE_POWDER),
    ("line-blush", P.LINE_BLUSH), ("line-gold", P.LINE_GOLD),
]
bad = [(n, v, var(n)) for n, v in pairs if var(n) != v.upper()]
if bad:
    for n, v, c in bad:
        print(f"  FAIL: --vt-{n} = {c} in tokens.css vs {v.upper()} in palette.py")
    sys.exit(1)
print(f"  {len(pairs)} tokens in sync: palette.py == tokens.css")
PYEOF

echo ""
echo "— Gate 5 · gradients in-family (law L4) —"
GRAD_HITS=$(rg -n 'gradient\(' assets/css/ -g '!tokens.css' | rg '#[0-9A-Fa-f]{3,8}|rgba?\(' || true)
if [ -n "$GRAD_HITS" ]; then
  echo "FAIL: gradient with a raw color outside tokens.css — gradients are built from tokens:"; echo "$GRAD_HITS"; exit 1
fi
if ! rg -q 'linear-gradient\(90deg, #16837A 0%, #0F766E 100%\)' assets/css/tokens.css; then
  echo "FAIL: the one sanctioned ramp --vt-gradient-accent must be peacock-300 -> 500 (#16837A -> #0F766E)"; exit 1
fi
echo "  the one ramp is peacock-300->500 · every other gradient is token-built"

echo ""
echo "— Gate 6 · THE PORCELAIN FLOOR + PEACOCK INK BAND (laws L0/L1/L2) —"
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
    ("canvas porcelain", P.PORCELAIN), ("surface-1 milk", P.MILK), ("surface-2 bone", P.BONE),
    ("wash-saffron", P.WASH_SAFFRON), ("wash-sky", P.WASH_SKY), ("wash-peacock", P.WASH_PEACOCK),
    # STRATA fills (VT-PRD-005) — every band and well clears the floor
    ("stratum dawn", P.STRATUM_DAWN), ("stratum gold", P.STRATUM_GOLD),
    ("stratum sage", P.STRATUM_SAGE), ("stratum powder", P.STRATUM_POWDER),
    ("stratum blush", P.STRATUM_BLUSH), ("stratum gold-deep", P.STRATUM_GOLD_DEEP),
    ("well sage", P.WELL_SAGE), ("well powder", P.WELL_POWDER),
    ("well blush", P.WELL_BLUSH), ("well gold", P.WELL_GOLD),
    ("sky-blush", P.SKY_BLUSH), ("sky-gold", P.SKY_GOLD), ("sky-bottom", P.SKY_BOTTOM),
]
fails = 0
print("  S1/L0 · The Light-World Floor — every fill clears OKLCH L >= 0.89:")
for name, hexv in surfaces:
    L, C, H = oklch(hexv)
    ok = L >= 0.89
    if not ok:
        print(f"    FAIL: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f}) is too dark for the light world")
        fails += 1
print("  (hairlines and border-input are 1px lines/interactive")
print("   borders at verified ratios — not fills; the floor governs surfaces only)")
print("  L2 · ink is a chromatic peacock jewel (hue 178–192°, C >= 0.020; dark inks C >= 0.035):")
for name, hexv in (("ink", P.INK), ("ink-2", P.INK2), ("ink-3", P.INK3)):
    L, C, H = oklch(hexv)
    if not ((178 <= H <= 192) and (C >= 0.020) and (L >= 0.45 or C >= 0.035)):
        print(f"    FAIL INK LAW: {name} {hexv} — oklch({L:.3f} {C:.3f} {H:.0f})")
        fails += 1
if fails:
    sys.exit(1)
print("    all floors held — light-world floor at L 0.89+, ink in the peacock band")
PYEOF

echo ""
echo "— Gate 7 · NO RAW COLOR outside tokens.css — hex OR rgb()/rgba() (law L9) —"
RAW=$(rg -n '#[0-9A-Fa-f]{3,8}|rgba?\(\s*[0-9]' assets/css/ -g '!tokens.css' || true)
if [ -n "$RAW" ]; then
  echo "FAIL: raw color outside tokens.css — a color written anywhere else is a bug:"; echo "$RAW"; exit 1
fi
echo "  clean — zero hex, zero rgb()/rgba() literals outside tokens.css"

echo ""
echo "— Gate 8 · zero legacy --vf- references (§14.1 gate G1) —"
VF=$(rg -n 'var\(--vf-|case-band--paper|case-band--dark|class="paper|\.paper\s*\{|--vf-[a-z-]+:' assets/css assets/js v2-src index.html 404.html work services about contact journal legal 2>/dev/null || true)
if [ -n "$VF" ]; then
  echo "FAIL: legacy --vf-/paper references remain:"; echo "$VF"; exit 1
fi
echo "  clean — the migration is grep-clean"

echo ""
echo "— Gate 9 · STRATA band rhythm — the layering itself (Law S4/S6) —"
python3 scripts/band_audit.py

echo ""
echo "STRATA: all 9 color gates green — deploy is lawful"
