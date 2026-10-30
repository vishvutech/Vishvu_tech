#!/usr/bin/env python3
"""
FIRST LIGHT journey photo re-grade (VT-PRD-004 §10.4).
+12 exposure, warm 5800K bias, lifted blacks floor at luminance >= 0.35
(no crushed darks — the photo must live in the dawn world too).
"""
from PIL import Image, ImageEnhance
import os

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "assets", "img", "vishvu-journey.webp")

img = Image.open(SRC).convert("RGB")

# 1. lift blacks to a floor of 0.35 + 2.5 stop exposure lift (~1.12x), gentle curve
def curve(v):
    x = v / 255.0
    # lifted film curve: floor 0.35, soft shoulder
    y = 0.35 + 0.65 * (x ** 0.82)
    return min(255, int(y * 255 * 1.06 + 0.5))

# 2. warm 5800K bias: R up, B down (subtle)
warm = (1.05, 1.00, 0.93)

r, g, b = img.split()
r = r.point(lambda v: curve(min(255, int(v * warm[0]))))
g = g.point(lambda v: curve(min(255, int(v * warm[1]))))
b = b.point(lambda v: curve(min(255, int(v * warm[2]))))
img = Image.merge("RGB", (r, g, b))

# 3. gentle saturation + contrast polish
img = ImageEnhance.Color(img).enhance(1.08)
img = ImageEnhance.Contrast(img).enhance(1.03)

img.save(SRC, "WEBP", quality=80, method=6)
print("journey photo re-graded to the dawn world:", SRC, os.path.getsize(SRC) // 1024, "KB")
