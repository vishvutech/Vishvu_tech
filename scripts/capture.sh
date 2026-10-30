#!/bin/bash
# Capture rendered screenshots of the Vishvu Tech static site for the
# colour pixel audit (VT-PRD-004 §15.2) and OG card regeneration (§10.3).
# Usage: bash scripts/capture.sh [port]
set -e
PORT="${1:-8080}"
SITE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${SITE}/../fl-shots"
URL="http://127.0.0.1:${PORT}"

mkdir -p "$OUT"
cd "$SITE"
python3 -m http.server "$PORT" >/tmp/vishvu-server.log 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 1.5

FORCE='document.querySelectorAll("[data-reveal]").forEach(el=>el.classList.add("is-visible")); document.querySelector(".preloader")?.classList.add("is-hidden"); const c=document.querySelector(".cursor"); if(c) c.style.display="none"; "ok"'

shot() {
  agent-browser open "$URL$1" >/dev/null
  agent-browser wait --load networkidle >/dev/null 2>&1 || true
  agent-browser wait 3500 >/dev/null 2>&1 || true
  agent-browser eval "$FORCE" >/dev/null 2>&1 || true
  agent-browser wait 600 >/dev/null 2>&1 || true
  agent-browser screenshot --full "$OUT/$2" >/dev/null 2>&1
  echo "shot: $2"
}

agent-browser set viewport 1600 1000 >/dev/null 2>&1 || true

shot "/"             home.png
shot "/work/"        work.png
shot "/services/"    services.png
shot "/about/"       about.png
shot "/contact/"     contact.png
shot "/journal/"     journal.png
shot "/work/checkout-rebuild.html" case-checkout.png
shot "/journal/oracle-free-tier.html" essay-oracle.png
shot "/nope-404-check" 404.png

echo "done -> $OUT (now run: python3 scripts/pixel_audit.py)"
