/* ============================================================
   VISHVU TECH 2.0 — MOTION ENGINE
   Preloader · Lenis smooth scroll · ScrollTrigger · Split text ·
   Magnetic CTAs · Custom cursor · Journey scrub · Menu · Progress
   ============================================================ */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FINE_POINTER = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var DESKTOP = window.matchMedia('(min-width: 901px)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined';
  var hasST = hasGSAP && typeof window.ScrollTrigger !== 'undefined';

  if (hasGSAP && hasST) gsap.registerPlugin(ScrollTrigger);
  if (hasGSAP) gsap.config({ nullTargetWarn: false });

  /* ---------- Save-motion preference (persisted, defaults to OS) ---------- */
  try {
    if (localStorage.getItem('vt-save-motion') === '1') {
      document.documentElement.classList.add('save-motion');
    }
  } catch (e) {}
  var saveMotionBtn = document.querySelector('[data-toggle-motion]');
  if (saveMotionBtn) {
    saveMotionBtn.addEventListener('click', function () {
      var on = document.documentElement.classList.toggle('save-motion');
      try { localStorage.setItem('vt-save-motion', on ? '1' : '0'); } catch (e) {}
      window.location.reload();
    });
  }
  var SAVE_MOTION = document.documentElement.classList.contains('save-motion');
  var MOTION_OK = !REDUCED && !SAVE_MOTION;

  /* ---------- Lenis smooth scroll (desktop pointer only) ---------- */
  var lenis = null;
  if (typeof window.Lenis !== 'undefined' && MOTION_OK && DESKTOP && FINE_POINTER) {
    lenis = new window.Lenis({
      lerp: 0.1,
      smoothWheel: true,
      wheelMultiplier: 1,
      syncTouch: false
    });
    if (hasGSAP) {
      lenis.on('scroll', hasST ? ScrollTrigger.update : function () {});
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
    } else {
      function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
      requestAnimationFrame(raf);
    }
  }

  /* Anchor links routed through Lenis */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      closeMenu();
      if (lenis) lenis.scrollTo(target, { offset: -76, duration: 1.2 });
      else target.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth' });
    });
  });

  /* ---------- Preloader (first visit per session) ---------- */
  var preloader = document.querySelector('.preloader');
  var seen = false;
  try { seen = sessionStorage.getItem('vt-entered') === '1'; } catch (e) {}

  function lockScroll(lock) {
    document.documentElement.style.overflow = lock ? 'hidden' : '';
    if (lenis) lock ? lenis.stop() : lenis.start();
  }

  if (preloader && !seen && MOTION_OK) {
    lockScroll(true);
    var counter = preloader.querySelector('.preloader__counter b');
    var word = preloader.querySelector('.preloader__wordmark span');
    var glyphPath = preloader.querySelector('.preloader__glyph path');
    var t0 = performance.now();

    var ready = Promise.all([
      document.fonts ? document.fonts.ready : Promise.resolve(),
      new Promise(function (res) {
        if (document.readyState === 'complete') res();
        else window.addEventListener('load', res, { once: true });
        setTimeout(res, 2500);
      })
    ]);

    if (hasGSAP) {
      var tl = gsap.timeline();
      if (glyphPath) tl.fromTo(glyphPath, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: .9, ease: 'power2.out' }, 0);
      if (counter) tl.fromTo(counter, { innerText: 0 }, { innerText: 100, duration: 1.3, ease: 'power2.inOut', snap: { innerText: 1 } }, 0);
      if (word) tl.to(word, { y: 0, duration: .5, ease: 'power3.out' }, .55);
    } else if (counter) counter.textContent = '100';

    var minTime = new Promise(function (res) { setTimeout(res, 1450); });
    Promise.all([ready, minTime]).then(function () {
      preloader.classList.add('is-done');
      try { sessionStorage.setItem('vt-entered', '1'); } catch (e) {}
      setTimeout(function () { preloader.classList.add('is-hidden'); lockScroll(false); }, 650);
    });
  } else if (preloader) {
    preloader.classList.add('is-hidden');
  }

  /* ---------- Reveal system ---------- */
  function assignStagger() {
    document.querySelectorAll('[data-reveal-group]').forEach(function (group) {
      var step = parseInt(group.getAttribute('data-reveal-group'), 10) || 80;
      Array.prototype.forEach.call(group.querySelectorAll('[data-reveal]'), function (el, i) {
        if (!el.style.getPropertyValue('--reveal-delay')) {
          el.style.setProperty('--reveal-delay', (i * step) + 'ms');
        }
      });
    });
  }

  function initReveals() {
    assignStagger();
    var items = document.querySelectorAll('[data-reveal]');
    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Split text (words + chars, own implementation) ---------- */
  function splitEl(el) {
    var text = el.textContent.trim();
    var mode = el.getAttribute('data-split');
    el.setAttribute('aria-label', text);
    el.textContent = '';
    var frag = document.createDocumentFragment();
    text.split(/\s+/).forEach(function (word, wi, arr) {
      var w = document.createElement('span');
      w.className = 'split-word';
      w.style.display = 'inline-block';
      w.style.whiteSpace = 'nowrap';
      if (mode === 'chars') {
        Array.prototype.forEach.call(word, function (ch) {
          var c = document.createElement('span');
          c.className = 'split-char split-inner';
          c.style.display = 'inline-block';
          c.textContent = ch;
          c.setAttribute('aria-hidden', 'true');
          w.appendChild(c);
        });
      } else {
        var c = document.createElement('span');
        c.className = 'split-inner';
        c.style.display = 'inline-block';
        c.textContent = word;
        c.setAttribute('aria-hidden', 'true');
        w.appendChild(c);
      }
      frag.appendChild(w);
      if (wi < arr.length - 1) frag.appendChild(document.createTextNode(' '));
    });
    el.appendChild(frag);
    return el.querySelectorAll('.split-inner');
  }

  function initSplits() {
    if (!hasGSAP) return;
    document.querySelectorAll('[data-split]').forEach(function (el) {
      var chars = splitEl(el);
      if (!MOTION_OK || !hasST) return;
      gsap.set(chars, { yPercent: 110, opacity: 0 });
      ScrollTrigger.create({
        trigger: el,
        start: 'top 88%',
        once: true,
        onEnter: function () {
          gsap.to(chars, {
            yPercent: 0, opacity: 1,
            duration: .9,
            ease: 'power3.out',
            stagger: 0.018
          });
        }
      });
    });
  }

  /* ---------- Header: glass + hide/reveal ---------- */
  var header = document.querySelector('.site-header');
  var lastY = 0;
  function onScrollHeader() {
    if (!header) return;
    var y = window.scrollY || document.documentElement.scrollTop;
    header.classList.toggle('is-scrolled', y > 8);
    if (!document.querySelector('.menu-overlay.is-open')) {
      if (y > 180 && y > lastY + 4) header.classList.add('is-hidden');
      else if (y < lastY - 4 || y < 180) header.classList.remove('is-hidden');
    }
    lastY = y;
  }
  window.addEventListener('scroll', onScrollHeader, { passive: true });
  if (lenis) lenis.on('scroll', onScrollHeader);
  onScrollHeader();

  /* ---------- Progress hairline ---------- */
  var progress = document.querySelector('.progress-hairline');
  function onScrollProgress() {
    if (!progress) return;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
  }
  window.addEventListener('scroll', onScrollProgress, { passive: true });
  if (lenis) lenis.on('scroll', onScrollProgress);
  onScrollProgress();

  /* ---------- Marquee: build seamless loop ---------- */
  document.querySelectorAll('.marquee__track').forEach(function (track) {
    var set = Array.prototype.slice.call(track.children);
    if (!set.length) return;
    var setW = track.scrollWidth;
    var copies = Math.max(2, Math.ceil((window.innerWidth * 2) / setW) + 1);
    var i, clone;
    for (i = 0; i < copies - 1; i++) {
      set.forEach(function (item) {
        clone = item.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });
    }
  });

  /* ---------- Magnetic CTAs ---------- */
  if (MOTION_OK && FINE_POINTER && hasGSAP) {
    document.querySelectorAll('[data-magnetic]').forEach(function (el) {
      var xTo = gsap.quickTo(el, 'x', { duration: .4, ease: 'power3.out' });
      var yTo = gsap.quickTo(el, 'y', { duration: .4, ease: 'power3.out' });
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        xTo((e.clientX - r.left - r.width / 2) * .25);
        yTo((e.clientY - r.top - r.height / 2) * .35);
      });
      el.addEventListener('pointerleave', function () { xTo(0); yTo(0); });
    });
  }

  /* ---------- Journey rail (CSS sticky + scrubbed translate) ---------- */
  function initJourney() {
    var journey = document.querySelector('.journey');
    var track = journey && journey.querySelector('.journey__track');
    if (!journey || !track) return;
    var bar = journey.querySelector('.journey__progress .bar i');
    var steps = journey.querySelectorAll('.journey__step');

    if (!MOTION_OK || !hasST || !window.matchMedia('(min-width: 901px)').matches) {
      steps.forEach(function (s) { s.classList.add('is-active'); });
      if (bar) bar.style.transform = 'scaleX(1)';
      return;
    }
    var dist = function () { return Math.max(0, track.scrollWidth - window.innerWidth + 64); };
    gsap.set(journey, { height: function () { return window.innerHeight + dist(); } });
    gsap.to(track, {
      x: function () { return -dist(); },
      ease: 'none',
      scrollTrigger: {
        trigger: journey,
        start: 'top top',
        end: function () { return '+=' + dist(); },
        scrub: 1,
        invalidateOnRefresh: true,
        onUpdate: function (self) {
          if (bar) bar.style.transform = 'scaleX(' + self.progress + ')';
          var idx = Math.min(steps.length - 1, Math.floor(self.progress * steps.length));
          steps.forEach(function (s, i) { s.classList.toggle('is-active', i <= idx); });
        }
      }
    });
  }

  /* ---------- Custom cursor ---------- */
  function initCursor() {
    var cursor = document.querySelector('.cursor');
    if (!cursor || !MOTION_OK || !FINE_POINTER) return;
    document.documentElement.classList.add('has-cursor');
    var dot = cursor.querySelector('.cursor__dot');
    var ring = cursor.querySelector('.cursor__ring');
    var label = cursor.querySelector('.cursor__label');
    var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my, running = false;

    function tick() {
      rx += (mx - rx) * .16;
      ry += (my - ry) * .16;
      dot.style.transform = 'translate(' + mx + 'px,' + my + 'px)';
      ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px)' + (cursor.classList.contains('is-down') ? ' scale(.85)' : '');
      if (running) requestAnimationFrame(tick);
    }
    window.addEventListener('pointermove', function (e) {
      mx = e.clientX; my = e.clientY;
      if (!running) { running = true; requestAnimationFrame(tick); }
    }, { passive: true });
    window.addEventListener('pointerdown', function () { cursor.classList.add('is-down'); });
    window.addEventListener('pointerup', function () { cursor.classList.remove('is-down'); });
    document.addEventListener('visibilitychange', function () {
      running = !document.hidden;
      if (running) requestAnimationFrame(tick);
    });

    document.querySelectorAll('[data-cursor="view"]').forEach(function (el) {
      el.addEventListener('pointerenter', function () {
        cursor.classList.add('is-view');
        if (label) label.textContent = el.getAttribute('data-cursor-label') || 'VIEW';
      });
      el.addEventListener('pointerleave', function () { cursor.classList.remove('is-view'); });
    });
    document.querySelectorAll('a, button, .chip span, summary').forEach(function (el) {
      el.addEventListener('pointerenter', function () { cursor.classList.add('is-link'); });
      el.addEventListener('pointerleave', function () { cursor.classList.remove('is-link'); });
    });
  }

  /* ---------- Menu overlay ---------- */
  var menuToggle = document.querySelector('.menu-toggle');
  var menuOverlay = document.querySelector('.menu-overlay');
  function openMenu() {
    if (!menuOverlay) return;
    menuOverlay.classList.add('is-open');
    if (menuToggle) { menuToggle.setAttribute('aria-expanded', 'true'); menuToggle.setAttribute('aria-label', 'Close menu'); }
    lockScroll(true);
    var first = menuOverlay.querySelector('.menu-overlay__link');
    if (first) setTimeout(function () { first.focus(); }, 100);
  }
  function closeMenu() {
    if (!menuOverlay || !menuOverlay.classList.contains('is-open')) return;
    menuOverlay.classList.remove('is-open');
    if (menuToggle) { menuToggle.setAttribute('aria-expanded', 'false'); menuToggle.setAttribute('aria-label', 'Open menu'); }
    lockScroll(false);
    if (menuToggle) menuToggle.focus();
  }
  if (menuToggle && menuOverlay) {
    menuToggle.addEventListener('click', function () {
      menuOverlay.classList.contains('is-open') ? closeMenu() : openMenu();
    });
    menuOverlay.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
      if (e.key === 'Tab' && menuOverlay.classList.contains('is-open')) {
        var focusables = menuOverlay.querySelectorAll('a[href], button');
        if (!focusables.length) return;
        var first = focusables[0], last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* ---------- Local time (IST) ---------- */
  function updateTime() {
    document.querySelectorAll('[data-time]').forEach(function (el) {
      try {
        el.textContent = new Intl.DateTimeFormat('en-GB', {
          hour: '2-digit', minute: '2-digit', timeZone: 'Asia/Kolkata'
        }).format(new Date());
      } catch (e) {}
    });
  }
  updateTime();
  setInterval(updateTime, 30000);

  /* ---------- Hero title drift (subtle scroll exhale) ---------- */
  if (MOTION_OK && hasGSAP && hasST && document.querySelector('.hero__title')) {
    gsap.to('.hero__title', {
      yPercent: -14,
      opacity: .35,
      ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
    });
  }

  /* ---------- Boot ---------- */
  function boot() {
    initReveals();
    initSplits();
    initJourney();
    initCursor();
    if (hasST) {
      window.addEventListener('load', function () { ScrollTrigger.refresh(); });
      document.querySelectorAll('img').forEach(function (img) {
        if (!img.complete) img.addEventListener('load', function () { ScrollTrigger.refresh(); }, { once: true });
      });
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
