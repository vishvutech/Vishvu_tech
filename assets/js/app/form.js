/* ============================================================
   VISHVU TECH 2.0 — CONTACT FORM (60-second funnel)
   Client validation · honeypot + time-trap · POST /api/contact
   Falls back to prefilled mailto on static hosts (no API).
   ============================================================ */
(function () {
  'use strict';

  var form = document.querySelector('.contact-form');
  if (!form) return;

  var formStart = Date.now();
  var HONEYPOT = form.querySelector('input[name="website"]');
  var status = form.querySelector('.form-status');
  var success = form.querySelector('.form-success');
  var refOut = success ? success.querySelector('.ref') : null;
  var pitch = form.querySelector('textarea[name="pitch"]');
  var count = form.querySelector('.char-count');

  /* char counter */
  if (pitch && count) {
    var update = function () {
      count.textContent = pitch.value.length + ' / 500';
    };
    pitch.addEventListener('input', update);
    update();
  }

  function setErr(name, on) {
    var field = form.querySelector('[data-field="' + name + '"]');
    if (field) field.classList.toggle('has-error', on);
    return !on;
  }

  function validate() {
    var ok = true;
    var name = form.querySelector('input[name="name"]');
    var email = form.querySelector('input[name="email"]');
    ok = setErr('name', !name.value.trim()) && ok;
    ok = setErr('email', !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) && ok;
    ok = setErr('type', !form.querySelector('input[name="project_type"]:checked')) && ok;
    ok = setErr('budget', !form.querySelector('input[name="budget"]:checked')) && ok;
    ok = setErr('timeline', !form.querySelector('input[name="timeline"]:checked')) && ok;
    return ok;
  }

  function showStatus(msg, cls) {
    if (!status) return;
    status.textContent = msg;
    status.className = 'form-status ' + cls;
    status.setAttribute('role', 'alert');
  }

  function payload() {
    var data = {
      name: form.querySelector('input[name="name"]').value.trim(),
      email: form.querySelector('input[name="email"]').value.trim(),
      project_type: (form.querySelector('input[name="project_type"]:checked') || {}).value || '',
      budget: (form.querySelector('input[name="budget"]:checked') || {}).value || '',
      timeline: (form.querySelector('input[name="timeline"]:checked') || {}).value || '',
      pitch: pitch ? pitch.value.trim() : '',
      ref: document.referrer || 'direct',
      ts: new Date().toISOString()
    };
    return data;
  }

  function mailtoFallback(data) {
    var subject = 'Project inquiry — ' + data.project_type + ' (' + data.timeline + ')';
    var body = 'Name: ' + data.name + '\nEmail: ' + data.email +
      '\nProject type: ' + data.project_type +
      '\nBudget: ' + data.budget +
      '\nTimeline: ' + data.timeline +
      '\n\nIdea:\n' + (data.pitch || '—') +
      '\n\n— Sent from vishvutech.com contact form';
    window.location.href = 'mailto:hello@vishvutech.com?subject=' +
      encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    showStatus('Opening your email app — or write to hello@vishvutech.com directly', 'form-status--ok');
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (HONEYPOT && HONEYPOT.value) return; /* bot: silently drop */
    if (Date.now() - formStart < 2000) return; /* time-trap */

    if (!validate()) {
      showStatus('A few fields need attention above', 'form-status--err');
      return;
    }

    var data = payload();
    var btn = form.querySelector('button[type="submit"]');
    if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending…'; }

    var done = false;
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, 9000);

    fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
      signal: controller.signal
    }).then(function (res) {
      clearTimeout(timer);
      done = true;
      if (!res.ok) throw new Error('bad status');
      return res.json();
    }).then(function (json) {
      form.style.display = 'none';
      if (success) {
        success.classList.add('is-shown');
        if (refOut && json && json.ref) refOut.textContent = 'REF · ' + json.ref;
        success.setAttribute('tabindex', '-1');
        success.focus();
      }
    }).catch(function () {
      clearTimeout(timer);
      if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label || 'Send inquiry'; }
      if (!done) mailtoFallback(data); /* static host or network fail */
      else showStatus('Something glitched on our side — please email hello@vishvutech.com', 'form-status--err');
    });
  });

  /* live re-validation on blur */
  ['name', 'email'].forEach(function (n) {
    var el = form.querySelector('input[name="' + n + '"]');
    if (el) el.addEventListener('blur', function () {
      if (el.value.trim()) validate();
    });
  });
  form.querySelectorAll('input[name="project_type"],input[name="budget"],input[name="timeline"]').forEach(function (el) {
    el.addEventListener('change', function () {
      var field = form.querySelector('[data-field="' + el.name + '"]');
      if (field) field.classList.remove('has-error');
    });
  });
})();
