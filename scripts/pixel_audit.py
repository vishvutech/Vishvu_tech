#!/usr/bin/env python3
"""
FIRST LIGHT pixel audit (VT-PRD-004 §15.2).
The tribunal's own instrument, run against captured screenshots:
  - dark-pixel share (< 60/255 luminance) must be < 8% per page
  - dominant background colour must be porcelain-family (#F7F4EC ± quantisation)
Usage: bash scripts/capture.sh 8080 && python3 scripts/pixel_audit.py
"""
from PIL import Image
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "fl-shots"))
PAGES = ["home.png", "work.png", "services.png", "about.png", "contact.png",
         "journal.png", "case-checkout.png", "essay-oracle.png", "404.png"]

fails = 0
print(f"{'page':<22} {'dark%':>7}  dominant colour   verdict")
print('-' * 64)
for name in PAGES:
    path = os.path.join(OUT, name)
    if not os.path.exists(path):
        print(f"{name:<22} MISSING — run scripts/capture.sh first")
        fails += 1
        continue
    img = Image.open(path).convert('RGB')
    w, h = img.size
    px = img.load()
    total = 0
    dark = 0
    colors = Counter()
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            r, g, b = px[x, y]
            total += 1
            lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
            if lum < 60:
                dark += 1
            colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
    dark_share = 100.0 * dark / total
    (dr, dg, db), _ = colors.most_common(1)[0]
    dom = f"#{dr:02X}{dg:02X}{db:02X}"
    porcelain = dr >= 0xE0 and dg >= 0xDC and db >= 0xD0 and dr >= dg >= db
    ok = dark_share < 8.0
    if not (ok and porcelain):
        fails += 1
    print(f"{name:<22} {dark_share:>6.1f}%  {dom:<17} {'PASS (porcelain-family)' if ok and porcelain else 'FAIL'}")

print('-' * 64)
if fails:
    print(f"PIXEL AUDIT: {fails} page(s) failed")
    sys.exit(1)
print("PIXEL AUDIT: dark-pixel share < 8% on every page · dominant colour porcelain-family · the light world holds")
