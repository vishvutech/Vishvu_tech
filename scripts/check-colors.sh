#!/bin/bash
# ============================================================
# FORGE NOIR — pre-deploy color gates (VT-PRD-002 §10.2)
# Fails the deploy on any violation of the Ten Laws (§7.6).
# Laws enforced: L2 (aurora never in UI), L3 (no mint anywhere),
# L6 (contrast matrix), L8 (no raw hex outside tokens.css).
# ============================================================
set -e
cd "$(dirname "$0")/.."

echo "— Gate 1 · WCAG contrast matrix (law L6) —"
python3 scripts/contrast_audit.py

echo "— Gate 2 · aurora never touches UI CSS (law L2) —"
if rg -q 'var\(--vf-aurora\)' assets/css/; then
  echo "FAIL: --vf-aurora used in assets/css — the aurora is atmosphere ONLY (art + hero sky)"; exit 1
fi
echo "  clean"

echo "— Gate 3 · no mint, no retired tokens (law L3) —"
if rg -qi '7EE8C7|--vf-kite|--vf-void|--vf-gradient[^-]|--vf-glow' assets/; then
  echo "FAIL: retired Night Forge value/token found in assets/"; exit 1
fi
echo "  clean"

echo "— Gate 4 · no raw hex outside tokens.css (law L8) —"
if rg -q '#[0-9a-fA-F]{3,8}' assets/css/ -g '!tokens.css'; then
  echo "FAIL: raw hex leak in assets/css (only tokens.css may hold hex)"; exit 1
fi
echo "  clean"

echo "— Gate 5 · one palette source at the build layer (law L8, §7.8.1) —"
if rg -qi '7EE8C7|FF6B35|0B0E14|111623|F2F5FA' v2-src/svgs.py; then
  echo "FAIL: svgs.py still hardcodes Night Forge values — import palette.py"; exit 1
fi
echo "  clean"

echo ""
echo "FORGE NOIR: all color gates green"
