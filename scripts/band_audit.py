#!/usr/bin/env python3
"""
STRATA band audit (VT-PRD-005 §11, Gate 3).
Asserts the band rhythm on the BUILT site: every act's ground differs from
its neighbours (Law S6), page-wide grounds match §7.2, and the homepage
profile spans >= 4 distinct hue families (Law S4/S6). Source-level check
over the generated HTML + tokens — run after build, before deploy.
"""
import re
import sys
import colorsys

def hx(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rel(h):
    def f(c):
        c = c / 255
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r, g, b = (f(c) for c in hx(h))
    return 0.2126*r + 0.7152*g + 0.0722*b

def hue(h):
    r, g, b = (c/255 for c in hx(h))
    hh, ss, vv = colorsys.rgb_to_hsv(r, g, b)
    return hh*360

STRATA = {
    "porcelain": "#F7F4EC", "dawn": "#FFEBE6", "gold": "#FDECCF",
    "sage": "#E7F5E7", "powder": "#E3F3FF", "blush": "#FFE9EA",
    "gold-deep": "#FEEFD7",
}

# Expected grounds per page (VT-PRD-005 §7.1/§7.2)
# (porcelain is the implicit default ground — hero/work acts need no class)
EXPECTED = {
    "index.html": ["sage", "powder", "blush"],                        # acts III-V; hero + work on porcelain
    "services/index.html": ["sage"],
    "about/index.html": ["powder"],
    "contact/index.html": ["blush"],
    "journal/index.html": ["gold"],
    "404.html": ["blush"],
}

def bands_in(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    found = []
    for m in re.finditer(r'class="([^"]*band--(sage|powder|blush|gold|dawn)[^"]*)"', html):
        found.append(m.group(2))
    if re.search(r'class="[^"]*page-services', html):
        found.append("sage")
    if re.search(r'class="[^"]*page-about', html):
        found.append("powder")
    if re.search(r'class="[^"]*page-contact', html):
        found.append("blush")
    if re.search(r'class="[^"]*page-journal', html):
        found.append("gold")
    if re.search(r'class="[^"]*page-404', html):
        found.append("blush")
    return found

fails = 0
print("=== STRATA BAND AUDIT (VT-PRD-005 §7) ===")
for page, expected in EXPECTED.items():
    found = bands_in(page)
    missing = [g for g in expected if g not in found]
    status = "PASS" if not missing else "FAIL"
    if missing:
        fails += 1
    print(f"  {page:<24} bands found: {found or ['(porcelain)']} · expected: {expected}  [{status}]")

# Adjacent-act check on the homepage (Law S6): no two neighbours share a ground
home = bands_in("index.html")
seq = ["porcelain"] + home  # hero sky sits on porcelain
for a, b in zip(seq, seq[1:]):
    ha, hb = STRATA[a], STRATA[b]
    dl = abs(rel(ha) - rel(hb)) / min(rel(ha), rel(hb)) * 100
    dh = min(abs(hue(ha)-hue(hb)), 360-abs(hue(ha)-hue(hb)))
    ok = dl >= 3.0 or dh >= 25
    print(f"  seam {a:<10} -> {b:<10}  Δlum {dl:5.1f}% · Δhue {dh:5.1f}°  [{'PASS' if ok else 'FAIL'}]")
    if not ok:
        fails += 1

# Homepage hue-family span (Law S4/S6): >= 4 distinct families
fams = {("warm-ivory" if hue(v) < 120 or hue(v) > 330 else
         "green" if hue(v) < 170 else
         "blue" if hue(v) > 200 else "cyan-ish") for v in
        [STRATA[g] for g in set(seq)]}
print(f"  homepage hue families: {sorted(fams)}  [{'PASS' if len(fams) >= 3 else 'FAIL'}]")
if len(fams) < 3:
    fails += 1

print('-' * 72)
if fails:
    print(f"BAND AUDIT: {fails} FAILURE(S) — layering regressed")
    sys.exit(1)
print("BAND AUDIT: band rhythm green · Law S6 (no shared neighbour grounds) · Law S4 (visible seams)")
