#!/usr/bin/env python3
"""
FIRST LIGHT Ban List scanner (VT-PRD-004 §3.3, §6.10, Appendix C).
The release gate: scans every shipped CSS/HTML/SVG/JS/JSON/TPL for
forbidden colour values. Zero whitelist by design — the Ban List has no
exceptions. Exit non-zero = no deploy.

RULE 1: forbidden hex set (§3.3) — case-insensitive, 3/4/6/8-digit forms
RULE 2: rgba(0,0,0,alpha>0.30) — dark scrims/shadows die with the dark world
RULE 3: any colour with OKLCH L<0.32 AND C<0.030 used outside --vt-ink* tokens
RULE 4: theme-color / background_color manifest values must be porcelain
"""
import fnmatch
import math
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SCAN_GLOBS = ("*.css", "*.html", "*.svg", "*.js", "*.json", "*.tpl")
SKIP_DIRS = {".git", "node_modules", "__pycache__", "work"}

FORBIDDEN_HEX = {
    # the neutral black ladder
    "000000", "050505", "0A0A0A", "111111", "141414", "1A1A1A", "1D1D1D",
    "202020", "232323", "2A2A2A", "333333", "3F3F46",
    # the old espresso ladder (Golden Hour)
    "251A11", "30241A", "3A2D23", "4A3D32", "615246",
    # neutral dark greys
    "1C1917", "292524",
    # the brown family
    "2B1B12", "3E2C1C", "4B3621", "5C4033", "6B4F3A",
    # brown-blacks
    "141210", "26201A", "332B22",
    # retired Golden Hour accents (regression guard)
    "DAC46D", "D3AB54", "E9E1B0", "E2D288", "81AFA9", "887769",
    # retired v1/v2 dark worlds (Forge Noir, Night Forge)
    "7EE8C7", "FF6B35", "E36E49", "FE8F5B", "FFAC7E", "882D16", "C65029",
    "80D1B5", "0E0C09", "161310", "1F1C18", "2B2825", "403C37", "6D6861",
    "EAE8E3", "B0ACA5", "96918B", "0C0806", "52CD86", "E7B643", "ED5350",
    "1A1712", "26221C",
}

HEX_RE = re.compile(r"#([0-9A-Fa-f]{3,8})\b")
RGBA_RE = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([0-9.]+)\s*)?\)")


def norm_hex(h):
    h = h.lower()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    elif len(h) in (4,):  # #RGBA -> expand RGB part
        h = "".join(c * 2 for c in h[:3])
    elif len(h) == 8:
        h = h[:6]
    return h[:6]


def oklch(hexstr):
    def s(c):
        c /= 255.0
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    r, g, b = (int(hexstr[i:i+2], 16) for i in (0, 2, 4))
    R, G, B = s(r), s(g), s(b)
    l = 0.4122214708*R + 0.5363325363*G + 0.0514459929*B
    m = 0.2119034982*R + 0.6806995451*G + 0.1073969566*B
    s_ = 0.0883024619*R + 0.2817188376*G + 0.6299787005*B
    if min(l, m, s_) < 0:
        return 1.0, 1.0, 0.0  # out of gamut — do not flag
    l_, m_, ss = l**(1/3), m**(1/3), s_**(1/3)
    L = 0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*ss
    a = 1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*ss
    b_ = 0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*ss
    return L, math.hypot(a, b_), math.degrees(math.atan2(b_, a)) % 360


def scan_file(path):
    violations = []
    rel = os.path.relpath(path, ROOT)
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for lineno, line in enumerate(f, 1):
                for m in HEX_RE.finditer(line):
                    h = norm_hex(m.group(1))
                    if h in FORBIDDEN_HEX:
                        violations.append((rel, lineno, "#" + h.upper(), "RULE 1: forbidden hex (§3.3 Ban List)"))
                for m in RGBA_RE.finditer(line):
                    r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
                    a = float(m.group(4)) if m.group(4) is not None else 1.0
                    if r == 0 and g == 0 and b == 0 and a > 0.30:
                        violations.append((rel, lineno, f"rgba(0,0,0,{a})", "RULE 2: black alpha > 0.30"))
                    elif r == g == b and max(r, g, b) <= 60 and a > 0.30:
                        violations.append((rel, lineno, f"rgba({r},{g},{b},{a})", "RULE 2: near-black alpha > 0.30"))
                # RULE 3: dark AND near-neutral colour used outside --vt-ink* tokens
                for m in HEX_RE.finditer(line):
                    h = norm_hex(m.group(1))
                    if len(h) != 6:
                        continue
                    try:
                        L, C, _ = oklch(h)
                    except ValueError:
                        continue
                    if L < 0.32 and C < 0.030:
                        # exemption: the definition line of an --vt-ink* token itself
                        token_def = re.search(r"--vt-ink[a-z0-9-]*\s*:\s*#", line)
                        if not token_def:
                            violations.append((rel, lineno, "#" + h.upper(),
                                               f"RULE 3: oklch({L:.3f} {C:.3f}) — dark & near-neutral (perceived black/brown)"))
                # RULE 4: theme-color must be porcelain
                if 'name="theme-color"' in line:
                    for m in HEX_RE.finditer(line):
                        if norm_hex(m.group(1)) != "f7f4ec":
                            violations.append((rel, lineno, "#" + norm_hex(m.group(1)), "RULE 4: theme-color must be porcelain #F7F4EC"))
                if '"theme_color"' in line or '"background_color"' in line:
                    for m in HEX_RE.finditer(line):
                        if norm_hex(m.group(1)) != "f7f4ec":
                            violations.append((rel, lineno, "#" + norm_hex(m.group(1)), "RULE 4: manifest colour must be porcelain #F7F4EC"))
    except (OSError, UnicodeDecodeError):
        pass
    return violations


def main():
    violations = []
    files = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not any(fnmatch.fnmatch(fn, g) for g in SCAN_GLOBS):
                continue
            files += 1
            violations.extend(scan_file(os.path.join(dirpath, fn)))

    print(f"Ban List scan: {files} files scanned (css/html/svg/js/json/tpl)")
    if violations:
        print(f"\n{len(violations)} VIOLATION(S) — the Ban List has no exceptions:")
        for rel, lineno, val, rule in violations:
            print(f"  {rel}:{lineno}  {val}  — {rule}")
        sys.exit(1)
    print("CLEAN — zero forbidden colours. The light world holds.")


if __name__ == "__main__":
    main()
