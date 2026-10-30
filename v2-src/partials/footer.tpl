  <footer class="site-footer">
    <div class="container">
      <div class="site-footer__watermark" aria-hidden="true">VISHVU TECH</div>
      <div class="site-footer__grid">
        <div class="site-footer__brand">
          <a class="brand" href="{{ROOT}}index.html" style="margin-bottom:18px">
            {{GLYPH}}
            <span class="brand__name">Vishvu&nbsp;Tech<em>®</em></span>
          </a>
          <p class="site-footer__tag">Ambitious ideas, built and shipped — by one senior engineer you actually talk to.</p>
        </div>
        <div class="footer-col">
          <h4>Sitemap</h4>
          <ul>
            <li><a href="{{ROOT}}index.html">Home</a></li>
            <li><a href="{{ROOT}}work/index.html">Work</a></li>
            <li><a href="{{ROOT}}services/index.html">Services</a></li>
            <li><a href="{{ROOT}}about/index.html">About</a></li>
            <li><a href="{{ROOT}}journal/index.html">Journal</a></li>
            <li><a href="{{ROOT}}contact/index.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="{{ROOT}}services/index.html#web">Web apps</a></li>
            <li><a href="{{ROOT}}services/index.html#mobile">Mobile apps</a></li>
            <li><a href="{{ROOT}}services/index.html#ai">AI &amp; automation</a></li>
            <li><a href="{{ROOT}}services/index.html#design">UI/UX design</a></li>
            <li><a href="{{ROOT}}services/index.html#cloud">Cloud &amp; launch</a></li>
            <li><a href="{{ROOT}}services/index.html#custom">Custom software</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Direct</h4>
          <ul>
            <li><a href="mailto:hello@vishvutech.com">hello@vishvutech.com ↗</a></li>
            <li><a href="https://wa.me/919999999999">WhatsApp ↗</a></li>
            <li><a href="https://github.com/vishvutech" rel="me noopener">GitHub ↗</a></li>
            <li><a href="https://www.linkedin.com/in/vishvutech" rel="me noopener">LinkedIn ↗</a></li>
            <li><a href="{{ROOT}}legal/privacy.html">Privacy</a></li>
            <li><a href="{{ROOT}}legal/terms.html">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="site-footer__meta">
        <span>© 2026 Vishvu Tech · Bengaluru · <b data-time>--:--</b> IST</span>
        <span class="made">Built &amp; deployed by <b>the same pair of hands</b> you'd hire.</span>
        <button data-toggle-motion style="font:inherit;color:inherit;letter-spacing:inherit;text-transform:inherit;min-height:44px;padding:0 4px">Motion: on/off</button>
      </div>
    </div>
  </footer>

  <div class="cursor" data-cursor aria-hidden="true">
    <div class="cursor__dot"></div>
    <div class="cursor__ring"><span class="cursor__label">VIEW</span></div>
  </div>

  <div class="preloader" aria-hidden="true">
    <svg class="preloader__glyph" viewBox="0 0 64 64" fill="none">
      <path d="M32 6 C35.2 21.5 42.5 28.8 58 32 C42.5 35.2 35.2 42.5 32 58 C28.8 42.5 21.5 35.2 6 32 C21.5 28.8 28.8 21.5 32 6 Z"
        stroke="{{PRELOADER_STROKE}}" stroke-width="1.5" pathLength="1"/>
    </svg>
    <div class="preloader__wordmark"><span>Vishvu Tech</span></div>
    <div class="preloader__counter">FORGING — <b>0</b>%</div>
  </div>

  <script src="{{ROOT}}assets/js/vendor/gsap.min.js" defer></script>
  <script src="{{ROOT}}assets/js/vendor/ScrollTrigger.min.js" defer></script>
  <script src="{{ROOT}}assets/js/vendor/lenis.min.js" defer></script>
  <script src="{{ROOT}}assets/js/app/motion.js" defer></script>
  {{extra_scripts}}
</body>
</html>
