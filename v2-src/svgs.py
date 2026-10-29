#!/usr/bin/env python3
"""
Vishvu Tech 2.0 — SVG visual library (build-time generated)
Abstract product mockups in Night Forge palette. Vector-crisp, ~3KB each.
No fake screenshots — intentional, branded UI compositions.
"""

VOID = "#0B0E14"; SURFACE = "#111623"; SURFACE2 = "#1A2133"; LINE = "#232B40"
INK = "#F2F5FA"; INK2 = "#A8B3C7"; INK3 = "#6B7690"
EMBER = "#FF6B35"; KITE = "#7EE8C7"
PAPER = "#F5EFE4"; PAPER_INK = "#1C2433"; PAPER_LINE = "#D9CFBD"


def browser_frame(inner: str, title: str = "app.vishvutech.com", w=800, h=500, bg=SURFACE) -> str:
    """Dark browser window chrome wrapping arbitrary inner SVG content."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Product preview">
  <defs>
    <linearGradient id="g-emb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{EMBER}"/><stop offset="1" stop-color="{KITE}"/></linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="{VOID}"/>
  <rect x="40" y="36" width="{w-80}" height="{h-72}" rx="14" fill="{bg}" stroke="{LINE}"/>
  <rect x="40" y="36" width="{w-80}" height="44" rx="14" fill="{SURFACE2}"/>
  <rect x="40" y="66" width="{w-80}" height="14" fill="{SURFACE2}"/>
  <circle cx="68" cy="58" r="5" fill="{EMBER}"/><circle cx="88" cy="58" r="5" fill="{PAPER_LINE}"/><circle cx="108" cy="58" r="5" fill="{KITE}"/>
  <rect x="132" y="48" width="300" height="20" rx="10" fill="{VOID}"/>
  <text x="146" y="62" font-family="monospace" font-size="11" fill="{INK3}">{title}</text>
  {inner}
</svg>'''


def el(x, y, w, h, fill, rx=6, opacity=1.0) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{opacity}"/>'


def txt(x, y, s, size=11, fill=INK2, family="monospace", weight="normal", anchor="start") -> str:
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>'


# ---------------------------------------------------------------- CASE 1: Checkout rebuild
def case_checkout() -> str:
    bars_nav = el(60, 100, 120, 14, SURFACE2) + txt(200, 112, "store", 10, INK3)
    hero = f'''
    {el(60, 140, 680, 120, SURFACE2, 10)}
    {txt(84, 182, "Cart — 3 items", 16, INK, "monospace", "bold")}
    {txt(84, 206, "Express checkout rebuilt", 11, INK3)}
    {txt(84, 244, "+31%", 34, EMBER, "monospace", "bold")}
    {txt(160, 244, "conversion · 60 days", 11, INK3)}
    <rect x="560" y="150" width="160" height="100" rx="10" fill="none" stroke="{EMBER}" stroke-dasharray="4 4" opacity=".7"/>
    {txt(640, 196, "0.9s", 22, KITE, "monospace", "bold", "middle")}
    {txt(640, 218, "LCP · was 4.2s", 9, INK3, "monospace", "normal", "middle")}
    '''
    cards = "".join([
        el(60 + i * 175, 290, 150, 90, SURFACE2, 10) for i in range(4)
    ]) + "".join([
        el(74 + i * 175, 304, 60, 34, VOID, 4) for i in range(4)
    ]) + "".join([
        txt(74 + i * 175, 360, ["USB-C Hub", "Desk Mat", "Lamp Pro", "Stand"][i], 10, INK2) for i in range(4)
    ]) + "".join([
        txt(74 + i * 175, 374, ["$59 · 2", "$39 · 1", "$89 · 3", "$45 · 1"][i], 9, INK3) for i in range(4)
    ])
    pay = f'''
    {el(60, 400, 680, 56, SURFACE2, 10)}
    {txt(84, 434, "PAY", 14, VOID, "monospace", "bold")}
    <rect x="60" y="400" width="120" height="56" rx="10" fill="url(#g-emb)"/>
    {txt(120, 434, "PAY", 14, VOID, "monospace", "bold", "middle")}
    {txt(200, 434, "Apple Pay · UPI · Cards — one screen, no redirects", 10, INK3)}
    '''
    return browser_frame(bars_nav + hero + cards + pay, "shop.example.com/checkout")


# ---------------------------------------------------------------- CASE 2: FieldOps mobile
def case_fieldops() -> str:
    phone = f'''
    <rect x="300" y="92" width="200" height="400" rx="26" fill="{VOID}" stroke="{LINE}" stroke-width="2"/>
    <rect x="316" y="128" width="168" height="346" rx="14" fill="{SURFACE}"/>
    <rect x="368" y="104" width="64" height="10" rx="5" fill="{SURFACE2}"/>
    {txt(400, 152, "Today", 15, INK, "monospace", "bold", "middle")}
    {txt(400, 168, "6 jobs · 2 routes", 9, INK3, "monospace", "normal", "middle")}
    <path d="M330 300 C 360 250, 440 260, 470 210" fill="none" stroke="{KITE}" stroke-width="3" stroke-dasharray="1 7" stroke-linecap="round"/>
    <path d="M330 340 C 380 320, 420 360, 470 330" fill="none" stroke="{EMBER}" stroke-width="3" stroke-dasharray="1 7" stroke-linecap="round"/>
    <circle cx="330" cy="300" r="6" fill="{KITE}"/><circle cx="470" cy="210" r="6" fill="{KITE}"/>
    <circle cx="330" cy="340" r="6" fill="{EMBER}"/><circle cx="470" cy="330" r="6" fill="{EMBER}"/>
    {[el(330, 200 + i * 26, 140, 18, SURFACE2, 5) for i in range(3)][0]}
    {el(330, 226, 90, 18, SURFACE2, 5)}{el(330, 252, 120, 18, SURFACE2, 5)}
    {[el(330, 396 + i * 22, 150, 14, SURFACE2, 4) for i in range(3)][0]}
    {el(330, 418, 110, 14, SURFACE2, 4)}{el(330, 440, 130, 14, SURFACE2, 4)}
    <circle cx="446" cy="440" r="18" fill="url(#g-emb)"/>
    {txt(446, 446, "✓", 16, VOID, "monospace", "bold", "middle")}
    '''
    side = f'''
    {txt(120, 130, "Offline-first", 13, INK, "monospace", "bold")}
    {txt(120, 150, "sync engine", 9, INK3, "monospace")}
    {el(80, 170, 8, 220, LINE, 4)}
    <circle cx="84" cy="190" r="5" fill="{EMBER}"/><circle cx="84" cy="240" r="5" fill="{KITE}"/>
    <circle cx="84" cy="290" r="5" fill="{KITE}"/><circle cx="84" cy="340" r="5" fill="{INK3}"/>
    {txt(100, 194, "GPS → job card", 10, INK2)}
    {txt(100, 244, "photos → S3", 10, INK2)}
    {txt(100, 294, "queue → retry", 10, INK2)}
    {txt(100, 344, "master data", 10, INK2)}
    '''
    side_r = f'''
    {txt(688, 130, "98.6%", 22, EMBER, "monospace", "bold", "end")}
    {txt(688, 148, "sync success", 9, INK3, "monospace", "normal", "end")}
    {txt(688, 196, "-38%", 22, KITE, "monospace", "bold", "end")}
    {txt(688, 214, "job admin time", 9, INK3, "monospace", "normal", "end")}
    {txt(688, 262, "4.8★", 22, INK, "monospace", "bold", "end")}
    {txt(688, 280, "field rating", 9, INK3, "monospace", "normal", "end")}
    '''
    return browser_frame(phone + side + side_r, "fieldops — route today")


# ---------------------------------------------------------------- CASE 3: ClinicFlow design
def case_clinicflow() -> str:
    cal = f'''
    {el(60, 100, 440, 370, SURFACE2, 10)}
    {txt(84, 132, "October", 14, INK, "monospace", "bold")}
    {txt(476, 132, "◄  ►", 11, INK3, "monospace", "normal", "end")}
    {[txt(84 + i * 62, 162, ["M", "T", "W", "T", "F"][i], 10, INK3, "monospace", "normal", "middle") for i in range(5)][0]}
    {txt(146, 162, "T", 10, INK3, "monospace", "normal", "middle")}{txt(208, 162, "W", 10, INK3, "monospace", "normal", "middle")}
    {txt(270, 162, "T", 10, INK3, "monospace", "normal", "middle")}{txt(332, 162, "F", 10, INK3, "monospace", "normal", "middle")}
    {[el(66 + (i % 5) * 62, 176 + (i // 5) * 52, 50, 44, SURFACE, 8) for i in range(15)][0]}
    {el(128, 176, 50, 44, SURFACE, 8)}{el(190, 176, 50, 44, SURFACE, 8)}{el(252, 176, 50, 44, SURFACE, 8)}{el(314, 176, 50, 44, SURFACE, 8)}
    <rect x="66" y="228" width="50" height="44" rx="8" fill="{SURFACE}"/><rect x="128" y="228" width="50" height="44" rx="8" fill="none" stroke="{EMBER}"/>
    <rect x="190" y="228" width="50" height="44" rx="8" fill="{SURFACE}"/><rect x="252" y="228" width="50" height="44" rx="8" fill="{SURFACE}"/>
    <rect x="314" y="228" width="50" height="44" rx="8" fill="{SURFACE}"/>
    <rect x="128" y="228" width="50" height="44" rx="8" fill="{EMBER}" opacity=".18"/>
    {txt(153, 254, "14", 13, INK, "monospace", "bold", "middle")}
    {txt(153, 266, "6 slots", 7, EMBER, "monospace", "normal", "middle")}
    {[el(66 + (i % 5) * 62, 280 + (i // 5) * 52, 50, 44, SURFACE, 8) for i in range(10)][0]}
    {el(128, 280, 50, 44, SURFACE, 8)}{el(190, 280, 50, 44, SURFACE, 8)}{el(252, 280, 50, 44, SURFACE, 8)}{el(314, 280, 50, 44, SURFACE, 8)}
    {[el(66 + (i % 5) * 62, 332 + (i // 5) * 52, 50, 44, SURFACE, 8) for i in range(5)][0]}
    {el(128, 332, 50, 44, SURFACE, 8)}{el(190, 332, 50, 44, SURFACE, 8)}{el(252, 332, 50, 44, SURFACE, 8)}{el(314, 332, 50, 44, SURFACE, 8)}
    '''
    flow = f'''
    {el(530, 100, 210, 370, SURFACE2, 10)}
    {txt(554, 132, "New booking flow", 12, INK, "monospace", "bold")}
    {[el(554, 152 + i * 58, 162, 42, SURFACE, 8) for i in range(5)][0]}
    {el(554, 210, 162, 42, SURFACE, 8)}{el(554, 268, 162, 42, SURFACE, 8)}{el(554, 326, 162, 42, SURFACE, 8)}{el(554, 384, 162, 42, SURFACE, 8)}
    {txt(574, 178, "1 · pick service", 10, INK2)}
    {txt(574, 236, "2 · pick slot", 10, INK2)}
    {txt(574, 294, "3 · details", 10, INK2)}
    {txt(574, 352, "4 · confirm", 10, INK2)}
    <rect x="554" y="384" width="162" height="42" rx="8" fill="url(#g-emb)"/>
    {txt(635, 410, "Booked in 41s", 11, VOID, "monospace", "bold", "middle")}
    {[el(554, 456, 162, 4, LINE, 2) for i in range(1)][0]}
    {txt(554, 458, "", 8, INK3)}
    '''
    return browser_frame(cal + flow, "clinic.example.com/schedule")


# ---------------------------------------------------------------- CASE 4: InsightLoop AI
def case_insightloop() -> str:
    chart = f'''
    {el(60, 100, 680, 200, SURFACE2, 10)}
    {txt(84, 130, "Revenue signals — last 30 days", 12, INK, "monospace", "bold")}
    <path d="M84 250 L 144 236 L 204 244 L 264 216 L 324 224 L 384 196 L 444 178 L 504 188 L 564 158 L 624 140 L 684 128"
      fill="none" stroke="{KITE}" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M84 250 L 144 236 L 204 244 L 264 216 L 324 224 L 384 196 L 444 178 L 504 188 L 564 158 L 624 140 L 684 128 L 684 286 L 84 286 Z"
      fill="{KITE}" opacity=".08"/>
    <path d="M84 262 L 144 260 L 204 256 L 264 258 L 324 250 L 384 252 L 444 246 L 504 248 L 564 240 L 624 238 L 684 236"
      fill="none" stroke="{INK3}" stroke-width="1.5" stroke-dasharray="3 5"/>
    <circle cx="684" cy="128" r="5" fill="{EMBER}"/>
    <circle cx="684" cy="128" r="10" fill="none" stroke="{EMBER}" opacity=".5"/>
    {txt(560, 116, "forecast ↑", 10, EMBER)}
    '''
    insights = f'''
    {[el(60 + i * 232, 320, 216, 120, SURFACE2, 10) for i in range(3)][0]}
    {el(292, 320, 216, 120, SURFACE2, 10)}{el(524, 320, 216, 120, SURFACE2, 10)}
    {txt(84, 348, "⚠ churn risk", 11, EMBER, "monospace", "bold")}
    {el(84, 362, 168, 8, LINE, 4)}{el(84, 378, 120, 8, LINE, 4)}
    {txt(84, 408, "3 accounts · draft email ready", 9, INK3)}
    {txt(316, 348, "✳ pattern found", 11, KITE, "monospace", "bold")}
    {el(316, 362, 168, 8, LINE, 4)}{el(316, 378, 140, 8, LINE, 4)}
    {txt(316, 408, "Tuesday spikes · +22% orders", 9, INK3)}
    {txt(548, 348, "→ auto-report", 11, INK, "monospace", "bold")}
    {el(548, 362, 168, 8, LINE, 4)}{el(548, 378, 96, 8, LINE, 4)}
    {txt(548, 408, "sent Mon 9:00 · whatsapp + mail", 9, INK3)}
    '''
    return browser_frame(chart + insights, "insightloop — signals")


# ---------------------------------------------------------------- Service preview panels (220x138)
def service_preview(kind: str) -> str:
    common = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 138" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">
  <defs><linearGradient id="sp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{EMBER}"/><stop offset="1" stop-color="{KITE}"/></linearGradient></defs>
  <rect width="220" height="138" fill="{SURFACE}"/>'''
    if kind == "web":
        body = f'''{el(24, 22, 172, 96, SURFACE2, 8)}
      {el(24, 22, 172, 16, VOID, 8)}{el(24, 30, 172, 8, VOID)}
      <circle cx="36" cy="30" r="2.5" fill="{EMBER}"/><circle cx="46" cy="30" r="2.5" fill="{INK3}"/><circle cx="56" cy="30" r="2.5" fill="{KITE}"/>
      {el(34, 48, 70, 30, VOID, 4)}{el(34, 84, 46, 6, LINE, 3)}{el(34, 96, 60, 6, LINE, 3)}
      <rect x="112" y="48" width="72" height="52" rx="6" fill="none" stroke="{EMBER}" stroke-dasharray="3 3"/>
      {txt(148, 78, "&lt;/&gt;", 16, EMBER, "monospace", "bold", "middle")}'''
    elif kind == "mobile":
        body = f'''<rect x="88" y="12" width="46" height="114" rx="10" fill="{VOID}" stroke="{LINE}"/>
      <rect x="94" y="24" width="34" height="90" rx="6" fill="{SURFACE2}"/>
      <rect x="100" y="18" width="22" height="4" rx="2" fill="{SURFACE2}"/>
      {el(98, 32, 26, 18, VOID, 3)}{el(98, 56, 26, 6, LINE, 3)}{el(98, 66, 18, 6, LINE, 3)}
      {el(98, 80, 26, 24, VOID, 3)}
      <rect x="98" y="80" width="26" height="24" rx="3" fill="url(#sp)" opacity=".25"/>
      {txt(111, 96, "✳", 12, KITE, "monospace", "bold", "middle")}'''
    elif kind == "ai":
        body = f'''<circle cx="110" cy="69" r="34" fill="none" stroke="{LINE}"/>
      <circle cx="110" cy="69" r="22" fill="none" stroke="{KITE}" stroke-dasharray="2 4"/>
      <circle cx="110" cy="69" r="10" fill="url(#sp)"/>
      <circle cx="110" cy="35" r="4" fill="{EMBER}"/><circle cx="144" cy="69" r="4" fill="{KITE}"/>
      <circle cx="110" cy="103" r="4" fill="{INK3}"/><circle cx="76" cy="69" r="4" fill="{INK3}"/>
      <path d="M110 39 L110 59" stroke="{EMBER}" stroke-width="1.5"/><path d="M138 69 L120 69" stroke="{KITE}" stroke-width="1.5"/>
      {txt(110, 128, "idea → insight", 9, INK3, "monospace", "normal", "middle")}'''
    elif kind == "design":
        body = f'''{el(30, 26, 78, 88, SURFACE2, 8)}
      {el(42, 38, 54, 34, VOID, 4)}{el(42, 80, 34, 5, LINE, 3)}{el(42, 90, 46, 5, LINE, 3)}
      {el(120, 26, 70, 40, SURFACE2, 8)}
      <rect x="120" y="26" width="70" height="40" rx="8" fill="url(#sp)" opacity=".3"/>
      {el(120, 76, 70, 38, SURFACE2, 8)}{el(132, 88, 46, 5, LINE, 3)}{el(132, 99, 30, 5, LINE, 3)}
      <path d="M112 128 l 8 -10 l 8 10 z" fill="{EMBER}"/>'''
    elif kind == "cloud":
        body = f'''{el(56, 76, 108, 40, SURFACE2, 8)}
      {el(70, 88, 14, 6, KITE, 3)}{el(92, 88, 14, 6, EMBER, 3)}{el(114, 88, 14, 6, INK3, 3)}
      {txt(110, 116, "▲ live · 99.9%", 8, KITE, "monospace", "normal", "middle")}
      <circle cx="110" cy="46" r="18" fill="none" stroke="{KITE}" stroke-dasharray="3 4"/>
      {txt(110, 50, "☁", 14, INK2, "monospace", "bold", "middle")}
      <path d="M110 64 L110 76" stroke="{KITE}" stroke-width="1.5"/>
      <path d="M96 34 a 14 14 0 0 1 28 0" fill="none" stroke="{EMBER}" stroke-width="1.5"/>'''
    else:  # custom
        body = f'''{el(34, 30, 68, 78, SURFACE2, 8)}{el(46, 44, 44, 8, VOID, 3)}{el(46, 58, 30, 8, VOID, 3)}{el(46, 72, 44, 8, VOID, 3)}
      <rect x="116" y="30" width="70" height="78" rx="8" fill="{VOID}" stroke="{LINE}"/>
      {txt(151, 50, "$", 12, INK3, "monospace", "bold", "middle")}
      {txt(151, 74, "run", 9, EMBER, "monospace", "normal", "middle")}
      {txt(151, 96, "your.js", 8, KITE, "monospace", "normal", "middle")}
      <path d="M102 69 l 14 0" stroke="{EMBER}" stroke-width="1.5" stroke-dasharray="2 3"/>'''
    return common + body + "</svg>"


# ---------------------------------------------------------------- Journal covers
def journal_cover(kind: str) -> str:
    if kind == "oracle":
        inner = f'''{txt(40, 60, "$ ssh ubuntu@vm", 13, KITE, "monospace")}
      {txt(40, 84, "✓ nginx · tls · brotli", 11, INK2, "monospace")}
      {txt(40, 104, "✓ systemd · api · umami", 11, INK2, "monospace")}
      {txt(40, 124, "TOTAL: $0.00 / month", 13, EMBER, "monospace", "bold")}
      {el(320, 48, 120, 90, SURFACE2, 8)}{txt(380, 88, "☁", 22, INK2, "monospace", "bold", "middle")}
      {txt(380, 112, "ARM · A1", 9, INK3, "monospace", "normal", "middle")}'''
    elif kind == "cwv":
        inner = f'''{el(40, 40, 120, 96, SURFACE2, 8)}
      {txt(100, 74, "1.4s", 22, EMBER, "monospace", "bold", "middle")}
      {txt(100, 96, "LCP", 10, INK3, "monospace", "normal", "middle")}
      {el(180, 52, 96, 6, KITE, 3)}{el(180, 66, 96, 6, KITE, 3)}{el(180, 80, 96, 6, INK3, 3)}
      {el(180, 94, 70, 6, INK3, 3)}
      {txt(180, 126, "CLS 0.01 · INP 90ms", 10, INK2, "monospace")}
      {txt(320, 60, "budget", 11, INK3, "monospace")}
      {el(320, 70, 8, 60, EMBER, 4)}{el(340, 88, 8, 42, KITE, 4)}{el(360, 80, 8, 50, KITE, 4)}'''
    else:  # ai
        inner = f'''{txt(40, 60, "INPUT:", 11, INK3, "monospace")}
      {el(110, 48, 240, 20, SURFACE2, 6)}
      {txt(40, 100, "OUTPUT:", 11, INK3, "monospace")}
      {el(110, 88, 180, 20, SURFACE2, 6)}{el(300, 88, 60, 20, VOID, 6)}
      {txt(330, 102, "auto", 10, EMBER, "monospace", "bold", "middle")}
      {txt(40, 140, "boring tasks → gone", 11, KITE, "monospace")}'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 180" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">
  <defs><linearGradient id="jc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{EMBER}" stop-opacity=".12"/><stop offset="1" stop-color="{KITE}" stop-opacity=".08"/></linearGradient></defs>
  <rect width="480" height="180" fill="{SURFACE}"/>
  <rect width="480" height="180" fill="url(#jc)"/>
  {inner}
</svg>'''


# ---------------------------------------------------------------- Journey landscape fallback (hero Tier B)
def hero_fallback_svg() -> str:
    """Static night horizon — same composition as the shader, 2 tones + grain."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Illustrated night horizon with aurora, ridgelines and a glowing kite">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0A0D13"/><stop offset=".55" stop-color="#101828"/><stop offset="1" stop-color="#1A2438"/>
    </linearGradient>
    <radialGradient id="ember" cx=".28" cy=".86" r=".5">
      <stop offset="0" stop-color="{EMBER}" stop-opacity=".5"/><stop offset="1" stop-color="{EMBER}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="aur" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{KITE}" stop-opacity="0"/><stop offset=".5" stop-color="{KITE}" stop-opacity=".16"/><stop offset="1" stop-color="{KITE}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="kiteglow" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{KITE}" stop-opacity=".9"/><stop offset="1" stop-color="{KITE}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#sky)"/>
  <g fill="#F2F5FA">
    <circle cx="90" cy="80" r="1.4" opacity=".8"/><circle cx="220" cy="140" r="1" opacity=".6"/><circle cx="340" cy="60" r="1.6" opacity=".9"/>
    <circle cx="500" cy="110" r="1" opacity=".5"/><circle cx="650" cy="70" r="1.3" opacity=".8"/><circle cx="810" cy="150" r="1" opacity=".6"/>
    <circle cx="960" cy="90" r="1.5" opacity=".85"/><circle cx="1090" cy="130" r="1" opacity=".55"/><circle cx="420" cy="200" r="1" opacity=".4"/>
    <circle cx="740" cy="210" r="1.1" opacity=".5"/><circle cx="1030" cy="230" r="1" opacity=".4"/><circle cx="160" cy="240" r="1.2" opacity=".5"/>
  </g>
  <path d="M0 180 Q 300 120 600 190 T 1200 160 V 420 H 0 Z" fill="url(#aur)"/>
  <path d="M0 260 Q 200 210 420 270 T 900 250 T 1200 300 V 560 H 0 Z" fill="url(#aur)" opacity=".6"/>
  <rect width="1200" height="800" fill="url(#ember)"/>
  <path d="M0 560 L 120 540 L 260 585 L 400 545 L 560 590 L 700 550 L 860 595 L 1000 555 L 1200 590 L 1200 800 L 0 800 Z" fill="#0C101A"/>
  <path d="M0 640 L 180 615 L 340 660 L 520 620 L 680 665 L 880 625 L 1060 670 L 1200 640 L 1200 800 L 0 800 Z" fill="#080B12"/>
  <g transform="translate(842 300) rotate(20)">
    <path d="M0 -26 C 6 -9 13 -3 30 0 C 13 3 6 9 0 26 C -6 9 -13 3 -30 0 C -13 -3 -6 -9 0 -26 Z" fill="{KITE}" opacity=".95"/>
    <circle r="60" fill="url(#kiteglow)" opacity=".35"/>
  </g>
  <path d="M830 330 Q 700 480 560 570" fill="none" stroke="{KITE}" stroke-width="1.5" opacity=".35"/>
  <rect width="1200" height="800" fill="#0B0E14" opacity=".12"/>
</svg>'''


KITE_GLYPH = '''<svg class="brand__glyph" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" aria-hidden="true">
  <defs><linearGradient id="kg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF6B35"/><stop offset="1" stop-color="#7EE8C7"/></linearGradient></defs>
  <path d="M32 6 C35.2 21.5 42.5 28.8 58 32 C42.5 35.2 35.2 42.5 32 58 C28.8 42.5 21.5 35.2 6 32 C21.5 28.8 28.8 21.5 32 6 Z" fill="url(#kg)"/>
</svg>'''

KITE_GLYPH_DARK = KITE_GLYPH.replace('fill="url(#kg)"', 'fill="#1C2433"')


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), "..", "assets", "img", "generated")
    os.makedirs(out, exist_ok=True)
    for name, fn in [("case-checkout", case_checkout), ("case-fieldops", case_fieldops),
                     ("case-clinicflow", case_clinicflow), ("case-insightloop", case_insightloop)]:
        with open(os.path.join(out, name + ".svg"), "w") as f:
            f.write(fn())
    with open(os.path.join(out, "hero-fallback.svg"), "w") as f:
        f.write(hero_fallback_svg())
    print("SVGs generated:", os.listdir(out))
