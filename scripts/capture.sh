#!/bin/bash
# Capture rendered screenshots of Vishvu Tech static site for the color audit
set -e
SITE=/home/z/my-project/vishvu-tech
OUT=/home/z/my-project/download/current-site-screenshots
URL=http://127.0.0.1:8080

mkdir -p "$OUT"
cd "$SITE"
python3 -m http.server 8080 >/home/z/my-project/work/server.log 2>&1 &
SRV=$!
sleep 1.5

FORCE='document.querySelectorAll("[data-reveal]").forEach(el=>el.classList.add("is-visible")); document.querySelector(".preloader")?.classList.add("is-hidden"); const c=document.querySelector(".cursor"); if(c) c.style.display="none"; "ok"'

shot() {
  agent-browser open "$URL$1" >/dev/null
  agent-browser wait --load networkidle >/dev/null
  agent-browser wait 4000 >/dev/null
  agent-browser eval "$FORCE" >/dev/null
  agent-browser screenshot "$OUT/$2" --full
  echo "captured: $2"
}

agent-browser set viewport 1920 1080

# Home: full page + hero viewport (same load)
agent-browser open "$URL/" >/dev/null
agent-browser wait --load networkidle >/dev/null
agent-browser wait 5000 >/dev/null
agent-browser eval "$FORCE" >/dev/null
agent-browser screenshot "$OUT/01-home-desktop-full.png" --full
echo "captured: 01-home-desktop-full.png"
agent-browser screenshot "$OUT/02-home-desktop-hero.png"
echo "captured: 02-home-desktop-hero.png"

shot "/work/index.html" 03-work-desktop-full.png
shot "/work/fieldops.html" 04-case-fieldops-desktop-full.png
shot "/services/index.html" 05-services-desktop-full.png
shot "/contact/index.html" 06-contact-desktop-full.png

agent-browser set viewport 390 844
shot "/" 07-home-mobile-full.png

kill $SRV 2>/dev/null || true
echo "ALL DONE"
