
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ORYZO AI — Material Intelligence</title>
  <meta name="description" content="ORYZO AI — Where material intelligence meets precision engineering. The ORYZO-1 model redefines how objects understand their environment." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,400&display=swap" rel="stylesheet" />
  <style>
    /* =========================================================
       DESIGN TOKENS
    ========================================================= */
    :root {
      --c-black:   #100904;
      --c-cream:   #ffedd7;
      --c-shadow:  #40372e;
      --c-cork:    #382416;
      --c-sienna:  #dc5000;
      --c-grey:    #6c5f51;
      --c-forest:  #445231;

      --f-main: 'DM Sans', ui-sans-serif, system-ui, sans-serif;

      --sz-10: 10px; --sz-12: 12px; --sz-14: 14px; --sz-15: 15px;
      --sz-18: 18px; --sz-24: 24px; --sz-29: 29px; --sz-41: 41px; --sz-51: 51px;

      --lh-tight: 0.90; --lh-snap: 1.0; --lh-hd: 1.09; --lh-sub: 1.2; --lh-body: 1.33;

      --sp-6:6px; --sp-8:8px; --sp-9:9px; --sp-10:10px; --sp-12:12px;
      --sp-14:14px; --sp-18:18px; --sp-24:24px; --sp-31:31px;
      --sp-41:41px; --sp-45:45px; --sp-68:68px; --sp-204:204px;

      --r-card: 12px; --r-pill: 36px; --r-round: 22.5px;
    }

    /* =========================================================
       RESET
    ========================================================= */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--c-black);
      color: var(--c-cream);
      font-family: var(--f-main);
      font-size: var(--sz-14);
      line-height: var(--lh-body);
      overflow-x: hidden;
      cursor: none;
    }
    img { display: block; max-width: 100%; }
    a { color: inherit; text-decoration: none; }
    button { font-family: inherit; cursor: none; }

    /* =========================================================
       CUSTOM CURSOR
    ========================================================= */
    #cur-dot {
      position: fixed; width: 8px; height: 8px;
      background: var(--c-cream); border-radius: 50%;
      pointer-events: none; z-index: 9999;
      left: 0; top: 0;
      transform: translate(-50%,-50%);
      mix-blend-mode: difference;
      transition: width .2s ease, height .2s ease;
      will-change: left, top;
    }
    #cur-ring {
      position: fixed; width: 38px; height: 38px;
      border: 1px solid rgba(255,237,215,.45); border-radius: 50%;
      pointer-events: none; z-index: 9998;
      left: 0; top: 0;
      transform: translate(-50%,-50%);
      transition: width .25s ease, height .25s ease, border-color .25s ease;
      will-change: left, top;
    }
    body.hovering #cur-dot { width: 14px; height: 14px; }
    body.hovering #cur-ring { width: 54px; height: 54px; border-color: rgba(220,80,0,.6); }

    /* =========================================================
       EDGE LABEL (fixed right)
    ========================================================= */
    #edge-label {
      position: fixed; right: 14px; top: 50%;
      transform: translateY(-50%) rotate(90deg);
      transform-origin: center center;
      font-size: var(--sz-10); letter-spacing: .18em;
      text-transform: uppercase; color: var(--c-cream);
      opacity: .4; z-index: 200; white-space: nowrap;
      pointer-events: none;
    }

    /* =========================================================
       SCROLL PROMPT
    ========================================================= */
    #scroll-prompt {
      position: fixed; bottom: var(--sp-31); left: 50%;
      transform: translateX(-50%);
      display: flex; flex-direction: column; align-items: center; gap: var(--sp-8);
      z-index: 200; pointer-events: none;
      opacity: 1; transition: opacity .3s ease;
    }
    #scroll-prompt.gone { opacity: 0; }
    #scroll-prompt span {
      font-size: var(--sz-10); letter-spacing: .18em;
      text-transform: uppercase; color: var(--c-cream);
    }
    .chevron {
      width: 12px; height: 12px;
      border-right: 1px solid var(--c-cream);
      border-bottom: 1px solid var(--c-cream);
      transform: rotate(45deg);
      animation: chev 1.6s ease infinite;
    }
    @keyframes chev {
      0%,100% { opacity: .35; transform: rotate(45deg) translate(0,0); }
      50%      { opacity: 1;   transform: rotate(45deg) translate(2px,2px); }
    }

    /* =========================================================
       NAVIGATION
    ========================================================= */
    nav#nav {
      position: fixed; inset: 0 0 auto 0;
      z-index: 1000;
      display: flex; align-items: center; justify-content: space-between;
      padding: var(--sp-18) var(--sp-41);
      border-bottom: 1px solid var(--c-shadow);
      background: transparent;
      transition: background .4s ease;
    }
    nav#nav.scrolled { background: var(--c-black); }

    .nav-logo {
      font-size: var(--sz-18); font-weight: 500;
      letter-spacing: .08em;
      display: flex; gap: 1px;
    }
    .nav-logo .cl {
      display: inline-block;
      opacity: 0; transform: translateY(10px);
      animation: clIn .4s ease forwards;
    }
    @keyframes clIn { to { opacity:1; transform:translateY(0); } }

    .nav-links {
      display: flex; gap: var(--sp-24); list-style: none;
    }
    .nav-links li a {
      position: relative; overflow: hidden;
      display: block;
      font-size: var(--sz-10); letter-spacing: .14em; text-transform: uppercase;
      line-height: 1;
    }
    .nav-links li a .t1,
    .nav-links li a .t2 {
      display: block;
      transition: transform .3s ease;
    }
    .nav-links li a .t2 {
      position: absolute; top: 100%; left: 0;
      color: var(--c-sienna);
    }
    .nav-links li a:hover .t1 { transform: translateY(-100%); }
    .nav-links li a:hover .t2 { transform: translateY(-100%); }

    .nav-btn {
      font-size: var(--sz-12); letter-spacing: .08em; text-transform: uppercase;
      color: var(--c-cream); background: transparent;
      border: 1px solid var(--c-cream); border-radius: var(--r-round);
      padding: var(--sp-8) var(--sp-18);
      transition: border-color .3s ease, color .3s ease;
    }
    .nav-btn:hover { border-color: var(--c-sienna); color: var(--c-sienna); }

    /* =========================================================
       DASHED RULE
    ========================================================= */
    .dash { width: 100%; border: none; border-top: 1px dashed var(--c-shadow); }

    /* =========================================================
       SECTION: HERO
    ========================================================= */
    #intro {
      position: relative; width: 100vw; height: 100vh; overflow: hidden;
    }
    #hero-img {
      position: absolute; inset: 0;
      width: 100%; height: 100%;
      object-fit: cover; object-position: center;
      filter: brightness(.72) contrast(1.06) saturate(.88);
      transform: scale(1.06);
      transition: transform 12s ease;
    }
    #hero-img.loaded { transform: scale(1); }
    .hero-vignette {
      position: absolute; inset: 0;
      background:
        linear-gradient(to bottom,  rgba(16,9,4,.6) 0%, transparent 35%),
        linear-gradient(to top,     rgba(16,9,4,.75) 0%, transparent 45%),
        linear-gradient(to right,   rgba(16,9,4,.4) 0%, transparent 55%);
    }
    .hero-content {
      position: absolute; inset: 0;
      display: flex; flex-direction: column; justify-content: space-between;
      padding: 116px var(--sp-41) var(--sp-68);
    }
    /* HEADLINE — char split */
    #hero-h1 {
      font-size: var(--sz-51); font-weight: 500;
      line-height: var(--lh-tight); max-width: 520px;
      letter-spacing: -.01em;
    }
    #hero-h1 .w { display: block; overflow: hidden; }
    #hero-h1 .w .wi {
      display: block; transform: translateY(110%);
      transition: transform .8s cubic-bezier(.16,1,.3,1);
    }
    #hero-h1.revealed .w:nth-child(1) .wi { transform:translateY(0); transition-delay: .05s; }
    #hero-h1.revealed .w:nth-child(2) .wi { transform:translateY(0); transition-delay: .18s; }
    #hero-h1.revealed .w:nth-child(3) .wi { transform:translateY(0); transition-delay: .29s; }
    #hero-h1.revealed .w:nth-child(4) .wi { transform:translateY(0); transition-delay: .40s; }

    .hero-foot {
      display: flex; align-items: flex-end; justify-content: space-between;
      gap: var(--sp-24);
    }
    .hero-tagline {
      font-size: var(--sz-18); line-height: var(--lh-sub);
      max-width: 360px; opacity: 0;
      transform: translateY(18px);
      transition: opacity .9s ease .6s, transform .9s ease .6s;
    }
    .hero-tagline.vis { opacity: .85; transform: translateY(0); }

    .hero-right {
      display: flex; flex-direction: column; align-items: flex-end; gap: var(--sp-12);
      opacity: 0; transform: translateY(18px);
      transition: opacity .9s ease .75s, transform .9s ease .75s;
    }
    .hero-right.vis { opacity: 1; transform: translateY(0); }

    .live-badge {
      display: flex; align-items: center; gap: var(--sp-8);
      font-size: var(--sz-10); letter-spacing: .14em; text-transform: uppercase;
      color: var(--c-cream); opacity: .55;
    }
    .live-dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--c-sienna);
      animation: livepulse 2s ease infinite;
    }
    @keyframes livepulse {
      0%,100% { opacity:1; transform:scale(1); }
      50%      { opacity:.4; transform:scale(.65); }
    }

    /* VIDEO CHIP */
    #video-chip {
      position: absolute; bottom: var(--sp-68); right: var(--sp-41);
      width: 148px; height: 92px;
      border-radius: var(--r-card);
      overflow: hidden;
      border: 1px solid rgba(255,237,215,.18);
      transition: border-color .3s ease, transform .3s ease;
      opacity: 0; transform: translateY(12px) scale(.96);
      transition: opacity .7s ease 1.1s, transform .7s ease 1.1s, border-color .3s ease;
    }
    #video-chip.vis { opacity: 1; transform: translateY(0) scale(1); }
    #video-chip:hover { border-color: var(--c-cream); transform: scale(1.04) !important; }
    #video-chip img {
      width: 100%; height: 100%; object-fit: cover;
      filter: brightness(.55) saturate(.7);
    }
    .chip-label {
      position: absolute; bottom: var(--sp-8); left: var(--sp-8);
      font-size: var(--sz-10); letter-spacing: .13em; text-transform: uppercase;
    }
    .chip-play {
      position: absolute; top: 50%; left: 50%;
      transform: translate(-50%,-50%);
      width: 30px; height: 30px;
      border: 1px solid var(--c-cream); border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
    }
    .chip-play::after {
      content:''; display:block;
      width:0; height:0;
      border-top: 5px solid transparent;
      border-bottom: 5px solid transparent;
      border-left: 9px solid var(--c-cream);
      margin-left: 3px;
    }

    /* =========================================================
       MARQUEE STRIP
    ========================================================= */
    .marquee-wrap {
      overflow: hidden;
      padding: var(--sp-31) 0;
      border-top: 1px dashed var(--c-shadow);
      border-bottom: 1px dashed var(--c-shadow);
    }
    .marquee-track {
      display: flex; gap: var(--sp-68);
      width: max-content;
      animation: mq 22s linear infinite;
    }
    .marquee-track:hover { animation-play-state: paused; }
    .marquee-item {
      font-size: var(--sz-10); letter-spacing: .18em; text-transform: uppercase;
      color: var(--c-grey); white-space: nowrap;
      display: flex; align-items: center; gap: var(--sp-24);
    }
    .marquee-item::after { content: '·'; color: var(--c-sienna); }
    @keyframes mq {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }

    /* =========================================================
       STATS
    ========================================================= */
    .stats {
      display: grid; grid-template-columns: repeat(3,1fr);
      gap: var(--sp-41);
      padding: var(--sp-68) var(--sp-41);
      background: var(--c-black);
    }
    .stat {
      padding-top: var(--sp-31);
      border-top: 1px solid rgba(255,237,215,.1);
    }
    .stat-num {
      font-size: var(--sz-41); font-weight: 500;
      line-height: var(--lh-snap); margin-bottom: var(--sp-8);
    }
    .stat-num sup { font-size: var(--sz-18); color: var(--c-sienna); }
    .stat-lbl {
      font-size: var(--sz-10); letter-spacing: .14em;
      text-transform: uppercase; color: var(--c-grey);
    }
    .stat-desc {
      font-size: var(--sz-12); color: var(--c-grey);
      line-height: 1.5; margin-top: var(--sp-8); max-width: 210px;
    }

    /* =========================================================
       FEATURES SECTION
    ========================================================= */
    #features {
      background: var(--c-black);
    }
    .feat-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      min-height: 100vh; align-items: center;
    }
    .feat-left {
      padding: var(--sp-68) var(--sp-68) var(--sp-68) var(--sp-41);
      display: flex; flex-direction: column; gap: var(--sp-41);
    }
    .section-tag {
      font-size: var(--sz-10); letter-spacing: .18em; text-transform: uppercase;
      color: var(--c-grey);
    }
    #feat-h2 {
      font-size: var(--sz-41); font-weight: 500;
      line-height: var(--lh-snap); max-width: 440px;
    }
    #feat-h2 .w { display: block; overflow: hidden; }
    #feat-h2 .w .wi {
      display: block; transform: translateY(110%);
      transition: transform .75s cubic-bezier(.16,1,.3,1);
    }
    #feat-h2.revealed .w:nth-child(1) .wi { transform:translateY(0); transition-delay:.04s; }
    #feat-h2.revealed .w:nth-child(2) .wi { transform:translateY(0); transition-delay:.15s; }
    #feat-h2.revealed .w:nth-child(3) .wi { transform:translateY(0); transition-delay:.25s; }

    .feat-body {
      font-size: var(--sz-14); color: var(--c-grey);
      line-height: var(--lh-body); max-width: 340px;
    }
    .feat-list { display: flex; flex-direction: column; }
    .feat-row {
      display: flex; gap: var(--sp-18); align-items: flex-start;
      padding: var(--sp-18) 0;
      border-top: 1px dashed var(--c-shadow);
      opacity: 0; transform: translateX(-22px);
      transition: opacity .55s ease, transform .55s ease;
    }
    .feat-row:last-child { border-bottom: 1px dashed var(--c-shadow); }
    .feat-row.vis { opacity: 1; transform: translateX(0); }
    .feat-num { font-size: var(--sz-10); color: var(--c-grey); letter-spacing: .1em; min-width: 22px; margin-top: 2px; }
    .feat-title { font-size: var(--sz-14); font-weight: 500; margin-bottom: var(--sp-6); }
    .feat-desc  { font-size: var(--sz-12); color: var(--c-grey); line-height: 1.5; }

    /* right: product orbit */
    .feat-right {
      position: relative; height: 100vh;
      display: flex; align-items: center; justify-content: center;
    }
    .orbit-wrap {
      position: relative; width: 68%; aspect-ratio: 1;
    }
    .orbit-ring {
      position: absolute;
      border-radius: 50%;
      border: 1px solid rgba(255,237,215,.055);
      animation: orb 20s linear infinite;
    }
    .orbit-ring:nth-child(1) { inset: -16%; animation-duration: 20s; }
    .orbit-ring:nth-child(2) { inset: -29%; animation-duration: 30s; animation-direction: reverse; border-color: rgba(64,55,46,.5); }
    @keyframes orb { to { transform: rotate(360deg); } }
    #spin-img {
      width: 100%; height: 100%; object-fit: contain;
      filter: drop-shadow(0 0 50px rgba(220,80,0,.07));
      will-change: transform;
    }

    /* =========================================================
       INTERACTIVE TILT
    ========================================================= */
    .tilt-section {
      background: var(--c-black);
      min-height: 100vh;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      padding: var(--sp-68) var(--sp-41);
    }
    #tilt-wrap {
      position: relative; width: 420px; height: 420px;
      perspective: 900px;
    }
    #tilt-inner {
      width: 100%; height: 100%;
      transform-style: preserve-3d;
      transition: transform .18s ease;
      border-radius: 50%;
    }
    #tilt-inner img {
      width: 100%; height: 100%; object-fit: contain; border-radius: 50%;
      filter: drop-shadow(0 28px 72px rgba(220,80,0,.14));
    }
    .tilt-hint {
      position: absolute; bottom: -48px; left: 50%;
      transform: translateX(-50%);
      font-size: var(--sz-10); color: var(--c-grey);
      letter-spacing: .12em; white-space: nowrap; opacity: .65;
    }
    .tilt-caption { margin-top: var(--sp-68); text-align: center; }
    .tilt-title { font-size: var(--sz-24); font-weight: 500; margin-bottom: var(--sp-8); }
    .tilt-sub { font-size: var(--sz-14); color: var(--c-grey); max-width: 400px; text-align: center; }

    /* =========================================================
       HAIRLINE
    ========================================================= */
    .sienna-line { height: 1px; background: var(--c-sienna); }

    /* =========================================================
       PRODUCT SPEC SECTION
    ========================================================= */
    #product {
      background: var(--c-black); position: relative; min-height: 100vh;
    }
    .prod-layout {
      position: relative; min-height: 100vh;
      display: flex; align-items: center; justify-content: center;
    }
    #prod-bg {
      position: absolute; inset: 0;
      width: 100%; height: 100%; object-fit: contain; object-position: center;
      opacity: .28; filter: saturate(.5) brightness(.55);
      will-change: transform;
    }
    .prod-content {
      position: relative; z-index: 2;
      width: 100%; padding: var(--sp-68) var(--sp-41);
      min-height: 100vh;
      display: flex; flex-direction: column; justify-content: flex-end;
    }
    .prod-tag {
      position: absolute; top: var(--sp-68); left: var(--sp-41);
      font-size: var(--sz-10); letter-spacing: .18em; text-transform: uppercase; color: var(--c-grey);
    }
    .prod-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: var(--sp-41); align-items: flex-end;
    }
    #prod-h2 {
      font-size: var(--sz-51); font-weight: 500;
      line-height: var(--lh-tight);
    }
    #prod-h2 .w { display: block; overflow: hidden; }
    #prod-h2 .w .wi {
      display: block; transform: translateY(110%);
      transition: transform .75s cubic-bezier(.16,1,.3,1);
    }
    #prod-h2.revealed .w:nth-child(1) .wi { transform:translateY(0); transition-delay:.04s; }
    #prod-h2.revealed .w:nth-child(2) .wi { transform:translateY(0); transition-delay:.16s; }
    #prod-h2.revealed .w:nth-child(3) .wi { transform:translateY(0); transition-delay:.27s; }

    .prod-specs { display: flex; flex-direction: column; gap: var(--sp-18); }
    .spec-row {
      display: flex; flex-direction: column; gap: var(--sp-6);
      padding-bottom: var(--sp-14);
      border-bottom: 1px dashed var(--c-shadow);
    }
    .spec-lbl { font-size: var(--sz-10); letter-spacing: .14em; text-transform: uppercase; color: var(--c-grey); }
    .spec-val { font-size: var(--sz-24); font-weight: 500; line-height: 1.1; }

    /* =========================================================
       BUTTONS
    ========================================================= */
    .btn-cork {
      display: inline-flex; align-items: center;
      background: var(--c-cork); color: var(--c-cream);
      border: none; border-radius: var(--r-pill);
      padding: 14px var(--sp-24);
      font-family: var(--f-main); font-size: var(--sz-14); font-weight: 400;
      letter-spacing: .06em;
      transition: opacity .3s ease, transform .25s ease;
    }
    .btn-cork:hover { opacity: .8; transform: translateY(-2px); }

    .btn-ghost {
      display: inline-flex; align-items: center;
      background: transparent; color: var(--c-cream);
      border: 1px solid var(--c-cream); border-radius: var(--r-round);
      padding: var(--sp-9) var(--sp-18);
      font-family: var(--f-main); font-size: var(--sz-12); font-weight: 400;
      letter-spacing: .08em; text-transform: uppercase;
      transition: border-color .3s ease, color .3s ease;
    }
    .btn-ghost:hover { border-color: var(--c-sienna); color: var(--c-sienna); }

    /* =========================================================
       CONTACT
    ========================================================= */
    #contact { background: var(--c-black); }
    .contact-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: var(--sp-68); align-items: center;
      padding: var(--sp-68) var(--sp-41);
      min-height: 75vh;
    }
    .contact-tag { font-size: var(--sz-10); letter-spacing: .18em; text-transform: uppercase; color: var(--c-grey); margin-bottom: var(--sp-24); }
    .contact-h2 {
      font-size: var(--sz-29); font-weight: 500;
      line-height: var(--lh-hd); margin-bottom: var(--sp-18);
    }
    .contact-body { font-size: var(--sz-14); color: var(--c-grey); line-height: var(--lh-body); }
    .form-col { display: flex; flex-direction: column; gap: var(--sp-24); }
    .f-input {
      background: transparent; color: var(--c-cream);
      border: none; border-bottom: 1px solid var(--c-cream);
      padding: var(--sp-9) 2px;
      font-family: var(--f-main); font-size: var(--sz-15); font-weight: 400;
      outline: none; width: 100%;
      transition: border-color .3s ease;
    }
    .f-input::placeholder { color: rgba(255,237,215,.38); }
    .f-input:focus { border-color: var(--c-sienna); }

    /* =========================================================
       FOOTER
    ========================================================= */
    footer {
      background: var(--c-black);
      padding: var(--sp-41) var(--sp-41) var(--sp-24);
      border-top: 1px dashed var(--c-shadow);
    }
    .foot-top {
      display: flex; justify-content: space-between; align-items: center;
      margin-bottom: var(--sp-24);
    }
    .foot-logo { font-size: var(--sz-24); font-weight: 500; letter-spacing: .06em; }
    .foot-nav { display: flex; gap: var(--sp-24); list-style: none; }
    .foot-nav a { font-size: var(--sz-10); color: var(--c-grey); letter-spacing: .12em; text-transform: uppercase; transition: color .3s ease; }
    .foot-nav a:hover { color: var(--c-cream); }
    .foot-bot {
      display: flex; justify-content: space-between; align-items: center;
      padding-top: var(--sp-18); border-top: 1px dashed var(--c-shadow);
    }
    .foot-copy { font-size: var(--sz-10); color: var(--c-grey); letter-spacing: .08em; }
    .foot-model { font-size: var(--sz-10); color: var(--c-grey); letter-spacing: .14em; text-transform: uppercase; }
    .foot-model em { color: var(--c-sienna); font-style: normal; }

    /* =========================================================
       SCROLL-DRIVEN REVEAL CLASSES
    ========================================================= */
    .sr {
      opacity: 0; transform: translateY(28px);
      transition: opacity .75s ease, transform .75s ease;
    }
    .sr.vis { opacity: 1; transform: translateY(0); }
    .sr-l {
      opacity: 0; transform: translateX(-26px);
      transition: opacity .7s ease, transform .7s ease;
    }
    .sr-l.vis { opacity: 1; transform: translateX(0); }
    .sr-r {
      opacity: 0; transform: translateX(26px);
      transition: opacity .7s ease, transform .7s ease;
    }
    .sr-r.vis { opacity: 1; transform: translateX(0); }

    /* =========================================================
       RESPONSIVE
    ========================================================= */
    @media (max-width: 900px) {
      nav#nav { padding: var(--sp-18) var(--sp-24); }
      .feat-grid { grid-template-columns: 1fr; }
      .feat-right { height: 55vw; }
      .prod-grid { grid-template-columns: 1fr; }
      .contact-grid { grid-template-columns: 1fr; }
      .stats { grid-template-columns: 1fr 1fr; }
      #tilt-wrap { width: 280px; height: 280px; }
      #hero-h1 { font-size: 36px; }
      #prod-h2 { font-size: 36px; }
      #edge-label { display: none; }
    }
    @media (max-width: 600px) {
      #hero-h1 { font-size: 26px; }
      .hero-foot { flex-direction: column; align-items: flex-start; }
      .nav-links { display: none; }
      .stats { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

<!-- CURSOR -->
<div id="cur-dot"></div>
<div id="cur-ring"></div>

<!-- EDGE LABEL -->
<div id="edge-label">ORYZO&#8209;1 MODEL</div>

<!-- SCROLL PROMPT -->
<div id="scroll-prompt">
  <span>Scroll to continue</span>
  <div class="chevron"></div>
</div>

<!-- ==============  NAV  ============== -->
<nav id="nav">
  <a href="#intro" class="nav-logo">
    <span class="cl" style="animation-delay:.06s">O</span><span class="cl" style="animation-delay:.12s">R</span><span class="cl" style="animation-delay:.18s">Y</span><span class="cl" style="animation-delay:.24s">Z</span><span class="cl" style="animation-delay:.30s">O</span>
  </a>
  <ul class="nav-links">
    <li><a href="#intro"><span class="t1">INTRO</span><span class="t2">INTRO</span></a></li>
    <li><a href="#features"><span class="t1">FEATURES</span><span class="t2">FEATURES</span></a></li>
    <li><a href="#product"><span class="t1">PRODUCT</span><span class="t2">PRODUCT</span></a></li>
    <li><a href="#contact"><span class="t1">CONTACT</span><span class="t2">CONTACT</span></a></li>
  </ul>
  <button class="nav-btn">Request Access</button>
</nav>

<!-- ==============  HERO  ============== -->
<section id="intro">
  <img id="hero-img" src="hero.png" alt="Cork coaster on warm wooden worktop with forest green cutting mat" />
  <div class="hero-vignette"></div>
  <div class="hero-content">
    <h1 id="hero-h1">
      <span class="w"><span class="wi">Material</span></span>
      <span class="w"><span class="wi">intelligence,</span></span>
      <span class="w"><span class="wi">precisely</span></span>
      <span class="w"><span class="wi">engineered.</span></span>
    </h1>
    <div class="hero-foot">
      <p class="hero-tagline" id="hero-tag">
        ORYZO&#8209;1 reads its environment at a molecular level —
        temperature, humidity, pressure — and responds in milliseconds.
      </p>
      <div class="hero-right" id="hero-right">
        <div class="live-badge">
          <div class="live-dot"></div>
          ORYZO&#8209;1 MODEL — AVAILABLE NOW
        </div>
        <button class="btn-cork">Explore the model</button>
      </div>
    </div>
  </div>
  <!-- video chip -->
  <div id="video-chip">
    <img src="coaster.png" alt="ORYZO product preview" />
    <div class="chip-play"></div>
    <span class="chip-label">PLAY ORYZO</span>
  </div>
</section>

<hr class="dash" />

<!-- ==============  MARQUEE  ============== -->
<div class="marquee-wrap">
  <div class="marquee-track">
    <span class="marquee-item">Material Intelligence</span>
    <span class="marquee-item">ORYZO&#8209;1 Model</span>
    <span class="marquee-item">Thermal Sensing</span>
    <span class="marquee-item">Cork Technology</span>
    <span class="marquee-item">Precision Engineering</span>
    <span class="marquee-item">Zero Latency</span>
    <span class="marquee-item">Ambient Response</span>
    <span class="marquee-item">Studio Dark</span>
    <!-- dupe for seamless loop -->
    <span class="marquee-item">Material Intelligence</span>
    <span class="marquee-item">ORYZO&#8209;1 Model</span>
    <span class="marquee-item">Thermal Sensing</span>
    <span class="marquee-item">Cork Technology</span>
    <span class="marquee-item">Precision Engineering</span>
    <span class="marquee-item">Zero Latency</span>
    <span class="marquee-item">Ambient Response</span>
    <span class="marquee-item">Studio Dark</span>
  </div>
</div>

<!-- ==============  STATS  ============== -->
<div class="stats">
  <div class="stat sr">
    <div class="stat-num">0.3<sup>ms</sup></div>
    <div class="stat-lbl">Response latency</div>
    <div class="stat-desc">From environmental input to adaptive output — 0.3 ms, measured under ISO 8124.</div>
  </div>
  <div class="stat sr" style="transition-delay:.14s">
    <div class="stat-num">14<sup>+</sup></div>
    <div class="stat-lbl">Sensor modalities</div>
    <div class="stat-desc">Temperature, humidity, pressure, vibration, UV — embedded in natural cork.</div>
  </div>
  <div class="stat sr" style="transition-delay:.28s">
    <div class="stat-num">99.7<sup>%</sup></div>
    <div class="stat-lbl">Accuracy rate</div>
    <div class="stat-desc">Environmental classification accuracy across 2.4 million controlled test cycles.</div>
  </div>
</div>

<hr class="dash" />

<!-- ==============  FEATURES  ============== -->
<section id="features">
  <div class="feat-grid">
    <!-- left -->
    <div class="feat-left">
      <p class="section-tag sr">— System capabilities</p>
      <h2 id="feat-h2">
        <span class="w"><span class="wi">One object.</span></span>
        <span class="w"><span class="wi">Infinite</span></span>
        <span class="w"><span class="wi">awareness.</span></span>
      </h2>
      <p class="feat-body sr" style="transition-delay:.18s">
        ORYZO&#8209;1 transforms an ordinary cork surface into a precision sensor array.
        Fourteen embedded modalities work in concert — each feeding the central model
        with environmental data at sub-millisecond intervals.
      </p>
      <div class="feat-list">
        <div class="feat-row" data-feat>
          <span class="feat-num">01</span>
          <div>
            <div class="feat-title">Thermal Mapping</div>
            <div class="feat-desc">Full-surface gradient at 0.01&deg;C resolution across 280 sensor nodes.</div>
          </div>
        </div>
        <div class="feat-row" data-feat>
          <span class="feat-num">02</span>
          <div>
            <div class="feat-title">Pressure Intelligence</div>
            <div class="feat-desc">Weight, distribution, and placement angle detected in three-dimensional space.</div>
          </div>
        </div>
        <div class="feat-row" data-feat>
          <span class="feat-num">03</span>
          <div>
            <div class="feat-title">Ambient Humidity</div>
            <div class="feat-desc">Condensation predicted 4.2 s before surface moisture forms — zero slip.</div>
          </div>
        </div>
        <div class="feat-row" data-feat>
          <span class="feat-num">04</span>
          <div>
            <div class="feat-title">UV Exposure Logging</div>
            <div class="feat-desc">Cumulative UV tracked across material lifetime with 12-hour health reports.</div>
          </div>
        </div>
      </div>
    </div>
    <!-- right -->
    <div class="feat-right">
      <div class="orbit-wrap">
        <div class="orbit-ring"></div>
        <div class="orbit-ring"></div>
        <img id="spin-img" src="coaster.png" alt="ORYZO-1 coaster rotating product view" />
      </div>
    </div>
  </div>
</section>

<hr class="dash" />

<!-- ==============  3D TILT  ============== -->
<section class="tilt-section">
  <p class="section-tag sr" style="margin-bottom: var(--sp-68);">— Interactive model preview</p>
  <div id="tilt-wrap">
    <div id="tilt-inner">
      <img src="coaster.png" alt="ORYZO-1 interactive 3D view" />
    </div>
    <div class="tilt-hint">Move cursor to rotate</div>
  </div>
  <div class="tilt-caption sr" style="transition-delay:.25s">
    <div class="tilt-title">ORYZO&#8209;1 Cork Intelligence Array</div>
    <div class="tilt-sub">
      Natural cork substrate, 108 mm diameter, 6 mm depth.
      Fourteen embedded sensor nodes. Zero external power at rest.
    </div>
  </div>
</section>

<div class="sienna-line"></div>

<!-- ==============  PRODUCT SPEC  ============== -->
<section id="product">
  <div class="prod-layout">
    <img id="prod-bg" src="coaster.png" alt="ORYZO coaster floating in void" />
    <div class="prod-content">
      <span class="prod-tag">— Technical specification</span>
      <div class="prod-grid">
        <h2 id="prod-h2">
          <span class="w"><span class="wi">Engineered</span></span>
          <span class="w"><span class="wi">from</span></span>
          <span class="w"><span class="wi">nothing.</span></span>
        </h2>
        <div class="prod-specs">
          <div class="spec-row sr" style="transition-delay:.08s">
            <span class="spec-lbl">Material</span>
            <span class="spec-val">Natural Cork + Ceramic Nano-layer</span>
          </div>
          <div class="spec-row sr" style="transition-delay:.18s">
            <span class="spec-lbl">Diameter</span>
            <span class="spec-val">108 mm — ISO 4784</span>
          </div>
          <div class="spec-row sr" style="transition-delay:.27s">
            <span class="spec-lbl">Model</span>
            <span class="spec-val">ORYZO&#8209;1 Rev. C</span>
          </div>
          <div class="spec-row sr" style="transition-delay:.36s">
            <span class="spec-lbl">Sensor Nodes</span>
            <span class="spec-val">280 embedded &middot; 14 modalities</span>
          </div>
          <div class="spec-row sr" style="transition-delay:.44s">
            <span class="spec-lbl">Power</span>
            <span class="spec-val">Kinetic harvest &middot; no external source</span>
          </div>
          <div class="sr" style="transition-delay:.52s; margin-top: var(--sp-18);">
            <button class="btn-ghost">View full specification &rarr;</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="dash" />

<!-- ==============  CONTACT  ============== -->
<section id="contact">
  <div class="contact-grid">
    <div>
      <p class="contact-tag sr">— Get in touch</p>
      <h2 class="contact-h2 sr" style="transition-delay:.12s">
        Early access.<br/>Limited allocation.
      </h2>
      <p class="contact-body sr" style="transition-delay:.24s">
        ORYZO&#8209;1 is in limited pre-release. We accept applications from design studios,
        research institutions, and material scientists. Allocation reviewed quarterly.
      </p>
    </div>
    <div class="form-col sr-r" style="transition-delay:.16s">
      <input class="f-input" type="text"  placeholder="Your name"             autocomplete="off" />
      <input class="f-input" type="email" placeholder="Email address"         autocomplete="off" />
      <input class="f-input" type="text"  placeholder="Organisation / Studio" autocomplete="off" />
      <input class="f-input" type="text"  placeholder="Intended use"          autocomplete="off" />
      <button class="btn-cork" id="submit-btn">Submit application</button>
    </div>
  </div>
</section>

<!-- ==============  FOOTER  ============== -->
<footer>
  <div class="foot-top">
    <div class="foot-logo">ORYZO</div>
    <ul class="foot-nav">
      <li><a href="#intro">Intro</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#product">Product</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#">Privacy</a></li>
    </ul>
  </div>
  <div class="foot-bot">
    <span class="foot-copy">&copy; 2026 ORYZO AI. All rights reserved.</span>
    <span class="foot-model">Running <em>ORYZO&#8209;1</em> &middot; Rev. C</span>
  </div>
</footer>

<!-- ==============  SCRIPTS  ============== -->
<script>
/* ─ CURSOR ─────────────────────────────────────── */
const dot  = document.getElementById('cur-dot');
const ring = document.getElementById('cur-ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove', e=>{ mx=e.clientX; my=e.clientY; dot.style.left=mx+'px'; dot.style.top=my+'px'; });
(function tick(){
  rx+=(mx-rx)*0.1; ry+=(my-ry)*0.1;
  ring.style.left=rx+'px'; ring.style.top=ry+'px';
  requestAnimationFrame(tick);
})();
document.querySelectorAll('a,button,input').forEach(el=>{
  el.addEventListener('mouseenter',()=>document.body.classList.add('hovering'));
  el.addEventListener('mouseleave',()=>document.body.classList.remove('hovering'));
});

/* ─ NAV + SCROLL PROMPT ─────────────────────────── */
const nav    = document.getElementById('nav');
const prompt = document.getElementById('scroll-prompt');
window.addEventListener('scroll',()=>{
  const sy = window.scrollY;
  nav.classList.toggle('scrolled', sy>60);
  prompt.classList.toggle('gone',   sy>window.innerHeight*.45);
}, {passive:true});

/* ─ HERO LOAD ANIMATION ─────────────────────────── */
window.addEventListener('DOMContentLoaded',()=>{
  const heroImg = document.getElementById('hero-img');
  setTimeout(()=>{ document.getElementById('hero-h1').classList.add('revealed'); }, 200);
  setTimeout(()=>{ document.getElementById('hero-tag').classList.add('vis'); }, 600);
  setTimeout(()=>{ document.getElementById('hero-right').classList.add('vis'); }, 750);
  setTimeout(()=>{ document.getElementById('video-chip').classList.add('vis'); }, 1000);
  heroImg.classList.add('loaded');
});

/* ─ INTERSECTION OBSERVER ───────────────────────── */
function makeIO(threshold=0.12){
  return new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('vis','revealed');
        e.target.observer?.disconnect();
      }
    });
  },{threshold});
}

// generic sr/sr-l/sr-r elements
const ioGeneral = makeIO(0.1);
document.querySelectorAll('.sr,.sr-l,.sr-r').forEach(el=>{ el.observer=ioGeneral; ioGeneral.observe(el); });

// word-line headings
const ioHeads = makeIO(0.15);
['feat-h2','prod-h2'].forEach(id=>{
  const el=document.getElementById(id);
  if(el){ el.observer=ioHeads; ioHeads.observe(el); }
});

// feature rows stagger
const featRows = document.querySelectorAll('[data-feat]');
const ioFeat = new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      featRows.forEach((r,i)=>setTimeout(()=>r.classList.add('vis'),i*100));
      ioFeat.disconnect();
    }
  });
},{threshold:0.12});
if(featRows[0]) ioFeat.observe(featRows[0]);

/* ─ SCROLL PARALLAX ─────────────────────────────── */
const spinImg = document.getElementById('spin-img');
const prodBg  = document.getElementById('prod-bg');

window.addEventListener('scroll',()=>{
  const sy = window.scrollY;

  // features coaster spin on scroll
  const featSec = document.getElementById('features');
  if(featSec && spinImg){
    const r = featSec.getBoundingClientRect();
    const p = -r.top / r.height;
    if(p>-0.3 && p<1.3) spinImg.style.transform=`rotate(${p*35}deg)`;
  }

  // product bg parallax
  const prodSec = document.getElementById('product');
  if(prodSec && prodBg){
    const r = prodSec.getBoundingClientRect();
    const p = -r.top / r.height;
    if(p>-0.6 && p<1.4){
      const ty = p*48;
      const op = Math.max(0.1, Math.min(0.42, 0.15 + p*0.28));
      prodBg.style.transform = `translateY(${ty}px)`;
      prodBg.style.opacity   = op;
    }
  }
},{passive:true});

/* ─ 3D TILT ─────────────────────────────────────── */
const tiltWrap  = document.getElementById('tilt-wrap');
const tiltInner = document.getElementById('tilt-inner');
if(tiltWrap){
  tiltWrap.addEventListener('mousemove',e=>{
    const r=tiltWrap.getBoundingClientRect();
    const dx=(e.clientX-r.left-r.width/2)/(r.width/2);
    const dy=(e.clientY-r.top-r.height/2)/(r.height/2);
    tiltInner.style.transform=`rotateY(${dx*26}deg) rotateX(${-dy*26}deg)`;
  });
  tiltWrap.addEventListener('mouseleave',()=>{
    tiltInner.style.transform='rotateY(0deg) rotateX(0deg)';
  });
}

/* ─ SUBMIT FEEDBACK ─────────────────────────────── */
const submitBtn = document.getElementById('submit-btn');
if(submitBtn){
  submitBtn.addEventListener('click',()=>{
    submitBtn.textContent='Application received —';
    submitBtn.style.opacity='.65';
    setTimeout(()=>{ submitBtn.textContent='Submit application'; submitBtn.style.opacity=''; },3200);
  });
}
</script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html written:", len(html), "bytes")
