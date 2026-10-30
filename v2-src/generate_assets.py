#!/usr/bin/env python3
"""
GOLDEN HOUR asset generator (VT-PRD-003 §12.10)
Regenerates: favicon.ico, icon-32/192/512, apple-touch-icon (from favicon.svg)
and the 13 OG share cards — all from v2-src/palette.py (single source, law L9).
Run after any palette change:  python3 v2-src/generate_assets.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import palette as P

import cairosvg
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
IMG = os.path.join(ROOT, "assets", "img")
TMP = os.path.join(ROOT, "..", "work", "fonts-ttf")
os.makedirs(TMP, exist_ok=True)

W, H = 1200, 630


def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def decompress_fonts():
    """woff2 -> ttf so PIL/FreeType can load the brand fonts."""
    from fontTools.ttLib import TTFont
    pairs = {
        "clash-display-600.woff2": "clash.ttf",
        "instrument-serif-italic.woff2": "serif-it.ttf",
        "jetbrains-mono.woff2": "mono.ttf",
        "satoshi-500.woff2": "satoshi.ttf",
    }
    out = {}
    for woff, ttf in pairs.items():
        src = os.path.join(IMG, "..", "fonts", woff)
        dst = os.path.join(TMP, ttf)
        if not os.path.exists(dst):
            f = TTFont(src)
            f.flavor = None          # strip woff2 container -> plain ttf
            f.save(dst)
        out[ttf.replace('.ttf', '')] = dst
    return out


def star_path(cx, cy, r, draw, fill_top, fill_bot):
    """Four-point brand star with an in-family vertical ramp (ember-300→600)."""
    import math
    # star outline: 4 outer points at N/E/S/W, concave curves between
    pts = []
    N = 160
    # parametric four-point star (same silhouette as the SVG path)
    def radius(a):
        # diamond star: r / (|cos|^k + |sin|^k)^(1/k) approximates the glyph
        k = 0.42
        ca, sa = abs(math.cos(a)), abs(math.sin(a))
        return r / ((ca ** (1 / k) + sa ** (1 / k)) ** k)
    for i in range(N):
        a = i / N * 2 * math.pi - math.pi / 2
        rr = radius(a)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    # vertical gradient fill via mask
    grad = Image.new('L', (int(2 * r) + 4, int(2 * r) + 4), 0)
    gd = ImageDraw.Draw(grad)
    for y in range(grad.height):
        t = y / max(1, grad.height - 1)
        gd.line([(0, y), (grad.width, y)], fill=int(255 * t))
    solid = Image.new('RGBA', (int(2 * r) + 4, int(2 * r) + 4), (0, 0, 0, 0))
    sd = ImageDraw.Draw(solid)
    sd.polygon([(px - (cx - r - 2), py - (cy - r - 2)) for px, py in pts], fill=(255, 255, 255, 255))
    top, bot = hex2rgb(fill_top), hex2rgb(fill_bot)
    layer = Image.new('RGBA', solid.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for y in range(layer.height):
        t = y / max(1, layer.height - 1)
        c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)) + (255,)
        ld.line([(0, y), (layer.width, y)], fill=c)
    star = Image.composite(layer, Image.new('RGBA', layer.size, (0, 0, 0, 0)), grad)
    star.putalpha(solid.split()[3])
    return star


def og_canvas():
    """Espresso sky ramp + champagne horizon glow + dusk-ribbon whisper + grain."""
    img = Image.new('RGB', (W, H), hex2rgb(P.SKY_TOP))
    d = ImageDraw.Draw(img)
    top, mid, bot = hex2rgb(P.SKY_TOP), hex2rgb(P.SKY_MID), hex2rgb(P.SKY_BOTTOM)
    for y in range(H):
        t = y / (H - 1)
        if t < .62:
            c = tuple(int(top[i] + (mid[i] - top[i]) * (t / .62)) for i in range(3))
        else:
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * ((t - .62) / .38)) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # ember horizon glow, bottom-left (the forge's fire keeps its seat)
    glow = Image.new('L', (W, H), 0)
    gd = ImageDraw.Draw(glow)
    for i in range(140):
        a = int(60 * (1 - i / 140) ** 2)
        gd.ellipse([40 - i * 2.1, H - 30 - i * 1.5, 340 + i * 2.6, H + 40 + i * 1.2], fill=a)
    glow = glow.filter(ImageFilter.GaussianBlur(60))
    ember = Image.new('RGB', (W, H), hex2rgb(P.EMBER_500))
    img = Image.composite(ember, img, glow)
    # aurora whisper, top-right (the cool light above the forge)
    aur = Image.new('L', (W, H), 0)
    ad = ImageDraw.Draw(aur)
    for i in range(110):
        a = int(26 * (1 - i / 110) ** 2)
        ad.ellipse([W - 360 - i * 2.0, -60 - i * 1.1, W + 80 + i * 2.0, 240 + i * 1.0], fill=a)
    aur = aur.filter(ImageFilter.GaussianBlur(70))
    aurora = Image.new('RGB', (W, H), hex2rgb(P.AURORA))
    img = Image.composite(aurora, img, aur)
    return img


def add_grain(img, strength=7):
    import random
    rnd = random.Random(42)
    noise = Image.new('L', (W // 2, H // 2))
    noise.putdata([rnd.randint(128 - strength * 6, 128 + strength * 6) for _ in range((W // 2) * (H // 2))])
    noise = noise.resize((W, H), Image.BILINEAR)
    return Image.blend(img, Image.merge('RGB', (noise, noise, noise)), 0.035)


def wrap(text, font, maxw, draw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make_og(name, kicker, line1, line2, meta, fonts):
    img = og_canvas()
    d = ImageDraw.Draw(img)
    f_kick = ImageFont.truetype(fonts['mono'], 26)
    f_head = ImageFont.truetype(fonts['clash'], 84)
    f_serif = ImageFont.truetype(fonts['serif-it'], 88)
    f_meta = ImageFont.truetype(fonts['mono'], 24)

    x, y = 84, 74
    # brand star
    star = star_path(x + 30, y + 30, 27, d, P.EMBER_300, P.EMBER_600)
    img.paste(star, (x - 2, y - 2), star)
    # kicker + ember mark rule
    d.text((x + 78, y - 4), kicker.upper(), font=f_kick, fill=hex2rgb(P.EMBER_500))
    kw = d.textlength(kicker.upper(), font=f_kick)
    d.line([(x + 78, y + 38), (x + 78 + kw, y + 38)], fill=hex2rgb(P.EMBER_600), width=3)

    # headline: line1 bone Clash, line2 serif italic ember
    y = 208
    maxw = W - 2 * 84
    for ln in wrap(line1, f_head, maxw, d):
        d.text((x, y), ln, font=f_head, fill=hex2rgb(P.INK))
        y += 96
    d.text((x, y + 6), line2, font=f_serif, fill=hex2rgb(P.EMBER))
    y += 118

    # meta row with ember dot marks
    my = H - 96
    d.ellipse([x, my + 11, x + 10, my + 21], fill=hex2rgb(P.EMBER_600))
    d.text((x + 26, my), meta.upper(), font=f_meta, fill=hex2rgb(P.INK3))
    # domain, right-aligned
    dom = "VISHVUTECH.COM"
    dw = d.textlength(dom, font=f_meta)
    d.text((W - 84 - dw, my), dom, font=f_meta, fill=hex2rgb(P.INK2))

    img = add_grain(img)
    out = os.path.join(IMG, "og", name)
    img.save(out, "JPEG", quality=84, optimize=True)
    return out


OGS = [
    ("home.jpg", "Vishvu Tech — software, end to end", "Ambitious ideas,", "built and shipped.", "14+ products shipped · zero abandoned launches"),
    ("work.jpg", "Selected work", "Work that survived", "contact with users.", "4 case studies · full decision trail"),
    ("case-checkout.jpg", "Case study", "The checkout rebuild —", "+31% in 60 days.", "+31% conversion · 0.9s LCP · $0/month"),
    ("case-insightloop.jpg", "Case study", "InsightLoop — the dashboard", "that reads itself.", "6 weekly hours of reporting → signals"),
    ("case-clinicflow.jpg", "Case study", "ClinicFlow — booking", "in 41 seconds.", "front-desk calls cut by half"),
    ("case-fieldops.jpg", "Case study", "FieldOps — an app that works", "where signal doesn't.", "98.6% sync success · zero lost reports"),
    ("services.jpg", "Services", "Six ways to build", "something that matters.", "web · mobile · ui · cloud · ai · custom"),
    ("about.jpg", "About", "One senior engineer.", "Studio-grade delivery.", "shipping since 2019 · Bengaluru"),
    ("contact.jpg", "Contact", "No big deck needed.", "Just a conversation.", "reply within 24h · proposal in 3 days"),
    ("journal.jpg", "Journal", "Notes", "from the forge.", "shipping · hosting · performance · ai"),
    ("journal-oracle.jpg", "Journal — hosting", "Oracle's free tier —", "the complete $0 stack.", "ARM · nginx · TLS · $0/month"),
    ("journal-cwv.jpg", "Journal — performance", "Shipping Core Web Vitals", "green.", "the pre-launch checklist"),
    ("journal-ai.jpg", "Journal — AI & automation", "What AI actually means", "for a small business.", "rules · models · humans"),
]


def gen_icons():
    svg = os.path.join(IMG, "favicon.svg")
    for size, name in [(512, "icon-512.png"), (192, "icon-192.png"), (32, "icon-32.png"), (180, "apple-touch-icon.png")]:
        png = os.path.join(TMP, f"icon-{size}.png")
        cairosvg.svg2png(url=svg, write_to=png, output_width=size, output_height=size)
        im = Image.open(png).convert("RGBA")
        im.save(os.path.join(IMG, name))
    # favicon.ico: 16/32/48
    base = Image.open(os.path.join(TMP, "icon-512.png")).convert("RGBA")
    base.save(os.path.join(IMG, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    print("icons regenerated: 32/180/192/512 + favicon.ico")


if __name__ == "__main__":
    fonts = decompress_fonts()
    gen_icons()
    for name, k, l1, l2, m in OGS:
        out = make_og(name, k, l1, l2, m, fonts)
        print("og:", os.path.basename(out), os.path.getsize(out) // 1024, "KB")
    print("GOLDEN HOUR assets regenerated")
