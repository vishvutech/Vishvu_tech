# Vishvu Tech — Portfolio

A single-page marketing site for **Vishvu Tech**, a product studio that turns ideas into
shipped digital products. Built with hand-written HTML, CSS and vanilla JavaScript — no build
step, no dependencies.

## Live structure

```
.
├── index.html            # Page markup
├── styles.css            # All styling, layout and animation
├── script.js             # Mobile nav, scroll reveal, footer year
└── assets/
    └── vishvu-journey-landscape.png
```

## Sections

- **Hero** — headline, calls to action and the illustrated journey artwork
- **About** — "A partner in the making"
- **Journey** — the five-stage process: Discover, Design, Code, Build, Launch
- **Services** — web products, mobile apps, AI & automation, product design,
  cloud & launch, custom software
- **Closing CTA** — contact prompt and footer

## Run locally

The site is fully static — open `index.html` in a browser, or serve the folder:

```bash
# Python
python -m http.server 8080

# Node.js
npx serve .
```

Then visit <http://localhost:8080>.

## Deploy with GitHub Pages

1. Go to **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/ (root)**, then save.

The site will be published at <https://vishvutech.github.io/Vishvu_tech/>.

## Accessibility & performance notes

- Semantic landmarks, skip-friendly anchor navigation and ARIA state on the menu button.
- Scroll-reveal respects `prefers-reduced-motion` and degrades gracefully without
  `IntersectionObserver`.
- The hero image is preloaded with `fetchpriority="high"`; fonts are preconnected.

## Contact

hello@vishvutech.com

---

© Vishvu Tech. All rights reserved.
