/* ============================================================
   VISHVU TECH — NIGHT HORIZON (WebGL hero shader) · FORGE NOIR
   The v1 ink landscape, re-rendered as a living night sky:
   stars, aurora drift, ember horizon, ridgelines, the kite.
   Re-inked per VT-PRD-002 §7.8: warm obsidian sky, bone stars,
   aurora #80D1B5, ember-500 horizon. The ground got warm.
   Tier A: WebGL · Tier B: static SVG (default, JS upgrades it)
   ============================================================ */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SAVE_MOTION = document.documentElement.classList.contains('save-motion');
  if (REDUCED || SAVE_MOTION) return; // keep SVG fallback

  var canvas = document.querySelector('.hero__canvas');
  var fallback = document.querySelector('.hero__fallback');
  if (!canvas) return;

  var gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'low-power' }) ||
           canvas.getContext('experimental-webgl');
  if (!gl) return; // keep SVG fallback

  /* Low-memory devices keep the (cheaper) SVG tier */
  if (navigator.deviceMemory && navigator.deviceMemory <= 2) return;

  var VERT = 'attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';

  var FRAG = [
    'precision highp float;',
    'uniform vec2 u_res;uniform float u_time;uniform vec2 u_mouse;',

    'vec3 mod289(vec3 x){return x-floor(x*(1.0/289.0))*289.0;}',
    'vec4 mod289(vec4 x){return x-floor(x*(1.0/289.0))*289.0;}',
    'vec4 permute(vec4 x){return mod289(((x*34.0)+1.0)*x);}',
    'vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}',
    'float snoise(vec3 v){',
    'const vec2 C=vec2(1.0/6.0,1.0/3.0);const vec4 D=vec4(0.0,0.5,1.0,2.0);',
    'vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);',
    'vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.0-g;',
    'vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);',
    'vec3 x1=x0-i1+C.xxx;vec3 x2=x0-i2+C.yyy;vec3 x3=x0-D.yyy;',
    'i=mod289(i);',
    'vec4 p=permute(permute(permute(i.z+vec4(0.0,i1.z,i2.z,1.0))+i.y+vec4(0.0,i1.y,i2.y,1.0))+i.x+vec4(0.0,i1.x,i2.x,1.0));',
    'float n_=0.142857142857;vec3 ns=n_*D.wyz-D.xzx;',
    'vec4 j=p-49.0*floor(p*ns.z*ns.z);',
    'vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.0*x_);',
    'vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;',
    'vec4 h=1.0-abs(x)-abs(y);',
    'vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);',
    'vec4 s0=floor(b0)*2.0+1.0;vec4 s1=floor(b1)*2.0+1.0;',
    'vec4 sh=-step(h,vec4(0.0));',
    'vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;',
    'vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);',
    'vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));',
    'p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;',
    'vec4 m=max(0.6-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);',
    'm=m*m;',
    'return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));',
    '}',

    'float ridge(float x,float t,float base,float amp){',
    'float v=0.0;float a=0.5;vec2 p=vec2(x*1.8,0.0);',
    'for(int i=0;i<4;i++){v+=a*snoise(vec3(p,t));p*=2.02;a*=0.5;}',
    'return base-amp*(0.5+0.5*v);',
    '}',

    'void main(){',
    'vec2 uv=gl_FragCoord.xy/u_res;',
    'vec2 p=(gl_FragCoord.xy-0.5*u_res)/u_res.y;',
    'float t=u_time*0.05;',
    'p-=(u_mouse-0.5)*0.06;',

    'vec3 col=mix(vec3(0.055,0.047,0.035),vec3(0.149,0.133,0.110),smoothstep(1.05,-0.15,p.y));',

    'vec2 grid=floor(uv*vec2(170.0,96.0));',
    'float h=fract(sin(dot(grid,vec2(12.9898,78.233)))*43758.5453);',
    'float star=step(0.9865,h)*smoothstep(0.22,0.72,uv.y);',
    'star*=0.5+0.5*sin(u_time*(0.4+h)+h*6.2831);',
    'col+=vec3(0.918,0.910,0.890)*star*0.38;',

    'float n1=snoise(vec3(p.x*1.15,p.y*1.6-t*0.75,t*0.32));',
    'float n2=snoise(vec3(p.x*2.3+5.2,p.y*3.1-t*1.05,t*0.48));',
    'float band=smoothstep(0.05,0.75,p.y)*smoothstep(1.05,0.28,p.y);',
    'float aur=band*max(0.0,0.45*n1+0.28*n2);',
    'col+=vec3(0.502,0.820,0.710)*aur*0.27;',

    'float hy=-0.22;',
    'float glow=exp(-abs(p.y-hy)*5.5);',
    'float glowN=0.62+0.38*snoise(vec3(p.x*2.8,t*0.55,0.0));',
    'col+=vec3(0.890,0.431,0.286)*glow*glowN*0.60;',
    'col+=vec3(0.996,0.561,0.357)*exp(-length(p-vec2(0.22,hy))*3.2)*0.36;',

    'float r1=ridge(p.x,t*0.22,hy+0.155,0.145);',
    'float r2=ridge(p.x+31.0,t*0.16,hy+0.045,0.105);',
    'if(p.y<r1){col=mix(col,vec3(0.086,0.075,0.063)+vec3(0.890,0.431,0.286)*exp(-abs(p.y-r1)*26.0)*0.45,0.965);}',
    'if(p.y<r2){col=mix(col,vec3(0.055,0.047,0.035),0.985);}',

    'vec2 kp=vec2(0.34,0.335+0.022*sin(u_time*0.42));',
    'vec2 kq=p-kp;',
    'float ca=0.9397;float sa=0.342;',
    'kq=vec2(kq.x*ca-kq.y*sa,kq.x*sa+kq.y*ca);',
    'float beacon=max(abs(kq.x)*1.25,abs(kq.y));',
    'float beaconGlow=smoothstep(0.034,0.004,beacon);',
    'float halo=exp(-length(kq)*7.5)*0.35;',
    'col+=vec3(0.502,0.820,0.710)*(beaconGlow*0.9+halo);',
    'float str=exp(-abs(length(p-vec2(0.28,hy+0.07))-0.30)*44.0);',
    'col+=vec3(0.502,0.820,0.710)*str*0.14;',

    'float vig=smoothstep(1.45,0.30,length(uv-vec2(0.5,0.45)));',
    'col*=mix(0.58,1.0,vig);',
    'float g=fract(sin(dot(gl_FragCoord.xy,vec2(12.9898,78.233))+mod(u_time,10.0))*43758.5453);',
    'col+=(g-0.5)*0.028;',

    'gl_FragColor=vec4(col,1.0);',
    '}'
  ].join('\n');

  function compile(type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      return null;
    }
    return s;
  }

  var vs = compile(gl.VERTEX_SHADER, VERT);
  var fs = compile(gl.FRAGMENT_SHADER, FRAG);
  if (!vs || !fs) return; // keep SVG fallback

  var prog = gl.createProgram();
  gl.attachShader(prog, vs);
  gl.attachShader(prog, fs);
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;
  gl.useProgram(prog);

  var buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(prog, 'a');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

  var uRes = gl.getUniformLocation(prog, 'u_res');
  var uTime = gl.getUniformLocation(prog, 'u_time');
  var uMouse = gl.getUniformLocation(prog, 'u_mouse');

  var isMobile = window.matchMedia('(max-width: 900px)').matches;
  var DPR = Math.min(window.devicePixelRatio || 1, isMobile ? 1.25 : 1.5);

  function resize() {
    var w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) {
      /* Layout not ready yet (defer runs before first paint). Retry on the
         next frame — bail out after ~2s so a hidden canvas can't loop. */
      if (resize._tries < 120) {
        resize._tries++;
        requestAnimationFrame(resize);
      }
      return;
    }
    resize._tries = 0;
    canvas.width = Math.max(2, Math.round(w * DPR));
    canvas.height = Math.max(2, Math.round(h * DPR));
    gl.viewport(0, 0, canvas.width, canvas.height);
  }
  resize._tries = 0;
  resize();
  window.addEventListener('resize', resize, { passive: true });
  window.addEventListener('load', resize);
  if ('ResizeObserver' in window) {
    new ResizeObserver(function () { resize(); }).observe(canvas);
  }

  /* Activate Tier A: hide SVG, show canvas */
  if (fallback) fallback.style.display = 'none';
  canvas.style.display = 'block';

  var mx = 0.5, my = 0.5, tx = 0.5, ty = 0.5;
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    window.addEventListener('pointermove', function (e) {
      tx = e.clientX / window.innerWidth;
      ty = 1 - e.clientY / window.innerHeight;
    }, { passive: true });
  }

  var running = true, visible = true, start = performance.now();

  document.addEventListener('visibilitychange', function () {
    running = !document.hidden;
    if (running) requestAnimationFrame(frame);
  });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
    }, { threshold: 0.02 }).observe(canvas);
  }
  canvas.addEventListener('webglcontextlost', function (e) {
    e.preventDefault();
    running = false;
    if (fallback) fallback.style.display = '';
    canvas.style.display = 'none';
  });

  function frame() {
    if (!running) return;
    if (visible) {
      mx += (tx - mx) * 0.04;
      my += (ty - my) * 0.04;
      gl.uniform2f(uRes, canvas.width, canvas.height);
      gl.uniform1f(uTime, (performance.now() - start) / 1000);
      gl.uniform2f(uMouse, mx, my);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
