#!/usr/bin/env python3
"""
Vishvu Tech 2.0 — site assembler.
Partials + page bodies + generated SVGs -> static site in ./site/
Includes: per-route meta/OG/JSON-LD, sitemap, robots, manifest, link QA.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svgs

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, ".."))   # build in place — repo root is the deploy tree

GLYPH = svgs.BRAND_GLYPH

SVG_TOKENS = {
    "{{HERO_FALLBACK}}": svgs.hero_fallback_svg(),
    "{{GLYPH}}": GLYPH,
    "{{SERVICE_WEB}}": svgs.service_preview("web"),
    "{{SERVICE_MOBILE}}": svgs.service_preview("mobile"),
    "{{SERVICE_AI}}": svgs.service_preview("ai"),
    "{{SERVICE_DESIGN}}": svgs.service_preview("design"),
    "{{SERVICE_CLOUD}}": svgs.service_preview("cloud"),
    "{{SERVICE_CUSTOM}}": svgs.service_preview("custom"),
    "{{JOURNAL_ORACLE}}": svgs.journal_cover("oracle"),
    "{{JOURNAL_CWV}}": svgs.journal_cover("cwv"),
    "{{JOURNAL_AI}}": svgs.journal_cover("ai"),
}

ORG_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfessionalService","name":"Vishvu Tech",
"description":"Independent software engineering: web applications, mobile apps, UI/UX design, AI & automation, cloud deployment, and custom software.",
"url":"https://vishvutech.com","email":"hello@vishvutech.com","areaServed":"Worldwide",
"address":{"@type":"PostalAddress","addressLocality":"Bengaluru","addressCountry":"IN"},
"founder":{"@type":"Person","name":"Vishvu","jobTitle":"Software Engineer"},
"sameAs":["https://github.com/vishvutech","https://www.linkedin.com/in/vishvutech"],
"knowsAbout":["Web development","Mobile apps","UI/UX design","AI automation","Cloud deployment"]}
</script>'''

SITE_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebSite","name":"Vishvu Tech",
"url":"https://vishvutech.com","description":"Ambitious ideas, built and shipped."}
</script>'''

ARTICLE_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Article","headline":"{h}",
"description":"{d}","author":{"@type":"Person","name":"Vishvu"},
"publisher":{"@type":"Organization","name":"Vishvu Tech","url":"https://vishvutech.com"},
"datePublished":"2026-10-15","mainEntityOfPage":"https://vishvutech.com{u}"}
</script>'''

CREATIVE_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"CreativeWork","headline":"{h}",
"description":"{d}","creator":{"@type":"Person","name":"Vishvu"},
"datePublished":"{dt}","mainEntityOfPage":"https://vishvutech.com{u}"}
</script>'''

SERVICE_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Service","name":"{h}",
"description":"{d}","provider":{"@type":"ProfessionalService","name":"Vishvu Tech","url":"https://vishvutech.com"},
"areaServed":"Worldwide"}
</script>'''

PAGES = [
    # (output path, body file, root prefix, title, description, og_title, og_image, jsonld, body_class, nav active)
    ("index.html", "home.html", "",
     "Vishvu Tech — Ambitious ideas, built and shipped",
     "Web apps, mobile products, and AI automation — designed, engineered, and deployed end-to-end by one senior engineer. 14+ products shipped, zero abandoned launches.",
     "Vishvu Tech — Ambitious ideas, built and shipped", "home.jpg",
     ORG_JSONLD + SITE_JSONLD, "page-home", ""),

    ("work/index.html", "work.html", "../",
     "Work — Case studies with the full decision trail | Vishvu Tech",
     "Four case studies with problems, constraints, decisions and outcomes: +31% checkout conversion, 98.6% offline sync, booking in 41 seconds.",
     "Work that survived contact with users", "work.jpg",
     ORG_JSONLD, "page-work", "work"),

    ("work/checkout-rebuild.html", "case-checkout.html", "../",
     "The checkout rebuild — +31% conversion in 60 days | Vishvu Tech",
     "Case study: a three-step checkout that lifted D2C conversion 31%, cut LCP from 4.2s to 0.9s, and costs $0/month to host.",
     "The checkout rebuild — +31% in 60 days", "case-checkout.jpg",
     CREATIVE_JSONLD.replace("{h}", "The checkout rebuild").replace("{d}", "Three-step checkout, +31% conversion, 0.9s LCP").replace("{dt}", "2025-09-01").replace("{u}", "/work/checkout-rebuild.html"),
     "page-case", "work"),

    ("work/insightloop.html", "case-insightloop.html", "../",
     "InsightLoop — the dashboard that reads itself | Vishvu Tech",
     "Case study: an AI signal layer that replaced six weekly hours of reporting nobody read with signals a team actually argues with.",
     "InsightLoop — the dashboard that reads itself", "case-insightloop.jpg",
     CREATIVE_JSONLD.replace("{h}", "InsightLoop").replace("{d}", "AI signals that replaced reporting nobody read").replace("{dt}", "2025-06-01").replace("{u}", "/work/insightloop.html"),
     "page-case", "work"),

    ("work/clinicflow.html", "case-clinicflow.html", "../",
     "ClinicFlow — booking in 41 seconds | Vishvu Tech",
     "Case study: a healthcare booking flow redesigned until patients finish in 41 seconds and front-desk calls drop by half.",
     "ClinicFlow — booking in 41 seconds", "case-clinicflow.jpg",
     CREATIVE_JSONLD.replace("{h}", "ClinicFlow").replace("{d}", "Booking flow patients finish in 41 seconds").replace("{dt}", "2024-11-01").replace("{u}", "/work/clinicflow.html"),
     "page-case", "work"),

    ("work/fieldops.html", "case-fieldops.html", "../",
     "FieldOps — an app that works where signal doesn't | Vishvu Tech",
     "Case study: an offline-first mobile app with 98.6% sync success for field crews, and zero lost reports in six months.",
     "FieldOps — offline-first, 98.6% sync", "case-fieldops.jpg",
     CREATIVE_JSONLD.replace("{h}", "FieldOps").replace("{d}", "Offline-first field app, 98.6% sync success").replace("{dt}", "2024-05-01").replace("{u}", "/work/fieldops.html"),
     "page-case", "work"),

    ("services/index.html", "services.html", "../",
     "Services — six ways to build something that matters | Vishvu Tech",
     "Web applications, mobile apps, UI/UX design, AI & automation, cloud & launch, custom software — with honest starting points and shipped proof.",
     "Six ways to build something that matters", "services.jpg",
     ORG_JSONLD + SERVICE_JSONLD.replace("{h}", "Web development services").replace("{d}", "Web apps, mobile, design, AI, cloud — with shipped proof"),
     "page-services", "services"),

    ("about/index.html", "about.html", "../",
     "About — one senior engineer, studio-grade delivery | Vishvu Tech",
     "The story, stack, and process behind Vishvu Tech: one senior engineer accountable end-to-end, shipping since 2019.",
     "One senior engineer. Studio-grade delivery.", "about.jpg",
     ORG_JSONLD, "page-about", "about"),

    ("contact/index.html", "contact.html", "../",
     "Contact — no big deck needed, just a conversation | Vishvu Tech",
     "Sixty-second inquiry form, reply within 24 hours, discovery call, proposal in 3 days. Next opening: December.",
     "No big deck needed. Just a conversation.", "contact.jpg",
     ORG_JSONLD, "page-contact", ""),

    ("journal/index.html", "journal.html", "../",
     "Journal — notes from the forge | Vishvu Tech",
     "Field notes on shipping, hosting on Oracle's free tier, Core Web Vitals discipline, and what AI automation means for small businesses.",
     "Notes from the forge", "journal.jpg",
     ORG_JSONLD, "page-journal", "journal"),

    ("journal/oracle-free-tier.html", "essay-oracle.html", "../",
     "Hosting a production site on Oracle's free tier — the complete $0 stack | Vishvu Tech",
     "The exact playbook this site runs on: ARM compute, nginx, Cloudflare TLS, contact API, analytics, backups — $0/month, including the three ways it almost broke.",
     "The complete $0/month stack", "journal-oracle.jpg",
     ARTICLE_JSONLD.replace("{h}", "Hosting a production site on Oracle's free tier").replace("{d}", "The complete $0 stack playbook").replace("{u}", "/journal/oracle-free-tier.html"),
     "page-essay", "journal"),

    ("journal/core-web-vitals.html", "essay-cwv.html", "../",
     "Shipping Core Web Vitals green — the pre-launch checklist | Vishvu Tech",
     "Budgets before build, image pipelines, font discipline, rent-paying JavaScript, and field measurement: the boring religion behind fast sites.",
     "The pre-launch CWV checklist", "journal-cwv.jpg",
     ARTICLE_JSONLD.replace("{h}", "Shipping Core Web Vitals green").replace("{d}", "The pre-launch performance checklist").replace("{u}", "/journal/core-web-vitals.html"),
     "page-essay", "journal"),

    ("journal/ai-automation-smb.html", "essay-ai.html", "../",
     "What AI & automation actually means for a small business | Vishvu Tech",
     "Rules where they're certain, models where they pay, humans where it matters — the triage that keeps automation honest.",
     "AI for SMBs, honestly", "journal-ai.jpg",
     ARTICLE_JSONLD.replace("{h}", "What AI and automation actually means for a small business").replace("{d}", "The rules/models/humans triage").replace("{u}", "/journal/ai-automation-smb.html"),
     "page-essay", "journal"),

    ("404.html", "404.html", "",
     "404 — this page hasn't been built yet | Vishvu Tech",
     "The requested page doesn't exist. The kite knows the way back.",
     "404", "home.jpg", "", "page-404", ""),

    ("legal/privacy.html", "privacy.html", "../",
     "Privacy — in plain language | Vishvu Tech",
     "No cookies, no ad trackers, cookieless self-hosted analytics, inquiry data retained 24 months then deleted.",
     "Privacy, in plain language", "home.jpg", "", "page-legal", ""),

    ("legal/terms.html", "terms.html", "../",
     "Terms — written to be read | Vishvu Tech",
     "Engagement terms for Vishvu Tech: fixed scope, weekly demos, IP transfer on final payment, 30-day warranty.",
     "Terms of engagement", "home.jpg", "", "page-legal", ""),
]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def build():
    head = read(os.path.join(HERE, "partials", "head.tpl"))
    header = read(os.path.join(HERE, "partials", "header.tpl"))
    footer = read(os.path.join(HERE, "partials", "footer.tpl"))

    # extra scripts per page
    EXTRA = {
        "index.html": '<script src="assets/js/app/horizon.js" defer></script>',
        "contact/index.html": '<script src="assets/js/app/form.js" defer></script>',
    }

    nav_attrs = {"work": "", "services": "", "about": "", "journal": ""}
    built_files = []

    for out_path, body_file, root, title, desc, og_title, og_image, jsonld, body_class, nav_active in PAGES:
        body = read(os.path.join(HERE, "pages", body_file))

        nav = dict(nav_attrs)
        if nav_active:
            nav[nav_active] = 'aria-current="page"'

        canonical = "/" if out_path == "index.html" else "/" + out_path.replace("index.html", "")
        og_path = "/" if out_path == "index.html" else canonical

        html = head
        html = html.replace("{{title}}", title)
        html = html.replace("{{description}}", desc)
        html = html.replace("{{og_title}}", og_title)
        html = html.replace("{{og_image}}", og_image)
        html = html.replace("{{canonical}}", canonical)
        html = html.replace("{{jsonld}}", jsonld or "")
        html = html.replace("{{body_class}}", body_class)
        html = html.replace('href="{{ROOT}}assets/', 'href="' + root + 'assets/')
        html = html.replace('href="{{ROOT}}', 'href="' + root)
        # nav link rewrite needs directory-relative prefixes
        for key in ("work", "services", "about", "journal", "contact", "legal"):
            html = html.replace('href="{{ROOT}}' + key + '/', 'href="' + root + key + '/')
        html = html.replace('href="{{ROOT}}index.html"', 'href="' + root + 'index.html"')

        header_r = header
        for key, val in nav.items():
            header_r = header_r.replace("{{nav_" + key + "}}", val)
        html += header_r.replace("{{ROOT}}", root).replace("{{GLYPH}}", GLYPH)
        html += body.replace("{{ROOT}}", root)
        html += footer.replace("{{ROOT}}", root).replace("{{GLYPH}}", GLYPH)
        html = html.replace("{{extra_scripts}}", EXTRA.get(out_path, "").replace("assets/", root + "assets/"))

        for token, value in SVG_TOKENS.items():
            html = html.replace(token, value)

        out = os.path.join(SITE, out_path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        built_files.append(out_path)

    # ---------- sitemap ----------
    urls = []
    for out_path, _, _, title, desc, *_ in [(p[0], p[1], p[2], p[3], p[4]) for p in PAGES]:
        if out_path == "404.html":
            continue
        canonical = "https://vishvutech.com/" if out_path == "index.html" else "https://vishvutech.com/" + out_path.replace("index.html", "")
        urls.append(f"  <url><loc>{canonical}</loc><changefreq>monthly</changefreq><priority>{'1.0' if out_path=='index.html' else '0.8'}</priority></url>")
    with open(os.path.join(SITE, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")

    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://vishvutech.com/sitemap.xml\n")

    with open(os.path.join(SITE, "manifest.json"), "w") as f:
        f.write('''{
  "name": "Vishvu Tech",
  "short_name": "Vishvu Tech",
  "description": "Ambitious ideas, built and shipped.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0E0C09",
  "theme_color": "#0E0C09",
  "icons": [
    {"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}
  ]
}''')

    # ---------- QA: internal links & alt ----------
    problems = []
    for out_path in built_files:
        full = os.path.join(SITE, out_path)
        base = os.path.dirname(full)
        html = read(full)
        for href in re.findall(r'href="([^"#]+)"', html):
            if href.startswith(("http", "mailto:", "tel:", "wa.me", "data:")) or href.endswith(".css") or href.endswith(".js") or href == "manifest.json":
                continue
            target = os.path.normpath(os.path.join(base, href.split("?")[0]))
            if not os.path.exists(target):
                problems.append(f"BROKEN LINK: {out_path} -> {href}")
        for src in re.findall(r'src="([^"]+)"', html):
            if src.startswith("http"):
                continue
            target = os.path.normpath(os.path.join(base, src))
            if not os.path.exists(target):
                problems.append(f"BROKEN SRC: {out_path} -> {src}")
        for img_tag in re.findall(r"<img [^>]*>", html):
            if "alt=" not in img_tag:
                problems.append(f"IMG MISSING ALT: {out_path}: {img_tag[:80]}")

    print(f"Built {len(built_files)} pages + sitemap + robots + manifest")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("QA: all internal links resolve · all imgs have alt")


if __name__ == "__main__":
    build()
