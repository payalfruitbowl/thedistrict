
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"/>
<title>ORYZO AI — The World's Most Sophisticated Cork Coaster</title>
<meta name="description" content="A physical product, reimagined for the AI era, proving even the smallest idea can feel extraordinary."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bl:#100904;--cr:#ffedd7;--sh:#40372e;--ck:#382416;--si:#dc5000;--gy:#6c5f51}
html{overflow-x:hidden}
body{background:var(--bl);color:var(--cr);font-family:'DM Sans',system-ui,sans-serif;font-size:14px;line-height:1.4;overflow-x:hidden;cursor:none}
img,svg{display:block}
a{color:inherit;text-decoration:none}
button{cursor:none;font-family:inherit}

/* CURSOR */
#dot{position:fixed;width:9px;height:9px;background:var(--cr);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference;transition:width .18s,height .18s;will-change:left,top}
#ring{position:fixed;width:42px;height:42px;border:1px solid rgba(255,237,215,.4);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:border-color .25s,width .2s,height .2s;will-change:left,top}
.ch #dot{width:18px;height:18px}
.ch #ring{width:62px;height:62px;border-color:rgba(220,80,0,.6)}

/* PROGRESS */
#bar{position:fixed;top:0;left:0;height:2px;background:var(--si);z-index:2000;width:0;transition:width .08s linear}

/* NAV */
#nav{position:fixed;inset:0 0 auto;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:20px 48px;transition:background .4s,border-color .4s;border-bottom:1px solid transparent}
#nav.on{background:var(--bl);border-color:var(--sh)}
.logo{display:flex}
.logo svg{width:88px;height:19px;color:var(--cr)}
.nav-r{display:flex;align-items:center;gap:30px}
.nl{font-size:10px;letter-spacing:.14em;text-transform:uppercase;position:relative;overflow:hidden;display:block;line-height:1.1}
.nl s1{display:block;transition:transform .3s cubic-bezier(.77,0,.18,1)}
.nl s2{position:absolute;top:100%;left:0;color:var(--si);display:block;transition:transform .3s cubic-bezier(.77,0,.18,1)}
.nl:hover s1{transform:translateY(-100%)}
.nl:hover s2{transform:translateY(-100%)}
.nb{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--cr);background:transparent;border:1px solid rgba(255,237,215,.45);border-radius:28px;padding:8px 22px;transition:border-color .3s,color .3s}
.nb:hover{border-color:var(--si);color:var(--si)}

/* SCROLL PROMPT */
#sp{position:fixed;bottom:36px;left:50%;transform:translateX(-50%);z-index:200;display:flex;flex-direction:column;align-items:center;gap:10px;pointer-events:none;transition:opacity .4s}
#sp.g{opacity:0}
.sp-t{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--cr);opacity:.45}
.sp-l{width:1px;height:44px;overflow:hidden;position:relative}
.sp-l::after{content:'';position:absolute;inset:0;background:linear-gradient(to bottom,transparent,var(--cr));animation:spl 1.8s ease infinite}
@keyframes spl{0%{transform:translateY(-100%)}100%{transform:translateY(100%)}}

/* CANVAS COASTER — fixed layer behind everything */
#canvas-wrap{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}
#c{width:100%;height:100%}

/* SECTIONS */
section{position:relative;z-index:2;background:transparent}
section.solid{background:var(--bl)}

/* HERO */
#hero{height:100vh;display:flex;flex-direction:column;justify-content:space-between;padding:100px 48px 52px;position:relative;z-index:2}
.h-tag{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--cr);opacity:0}
.h-tag .c{display:inline-block;opacity:0;transform:translateY(8px);transition:opacity .35s ease,transform .35s ease}
.hero-mid{display:flex;align-items:center;justify-content:center;flex:1}
#hero-svg{width:min(680px,80vw);color:var(--cr);opacity:0;transform:scale(.92);transition:opacity 1.1s ease .3s,transform 1.1s ease .3s}
#hero-svg.on{opacity:1;transform:scale(1)}
.hero-bot{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:end}
.h-copy{font-size:16px;line-height:1.55;color:var(--cr);opacity:.82}
.h-copy .ln{overflow:hidden;display:block}
.h-copy .ln i{display:block;font-style:normal;transform:translateY(105%);transition:transform .75s cubic-bezier(.16,1,.3,1)}
.h-copy.on .ln:nth-child(1) i{transform:translateY(0);transition-delay:.5s}
.h-copy.on .ln:nth-child(2) i{transform:translateY(0);transition-delay:.63s}
.h-copy.on .ln:nth-child(3) i{transform:translateY(0);transition-delay:.75s}
.h-card{border:1px solid rgba(255,237,215,.13);border-radius:12px;padding:26px;background:rgba(16,9,4,.5);backdrop-filter:blur(4px);opacity:0;transform:translateY(14px);transition:opacity .8s ease .85s,transform .8s ease .85s}
.h-card.on{opacity:1;transform:translateY(0)}
.h-card h4{font-size:19px;font-weight:500;line-height:1.2;margin-bottom:18px}
.hcd{width:100%;height:1px;background:rgba(255,237,215,.1);margin:14px 0}
.h-card p{font-size:12px;color:var(--gy);line-height:1.65}
#vchip{position:absolute;bottom:52px;right:48px;width:154px;height:96px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,237,215,.14);z-index:10;opacity:0;transform:translateY(10px);transition:opacity .7s ease 1.1s,transform .7s ease 1.1s,border-color .3s}
#vchip.on{opacity:1;transform:translateY(0)}
#vchip:hover{border-color:rgba(255,237,215,.5)}
#vchip img{width:100%;height:100%;object-fit:cover;filter:brightness(.5)}
.vp{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:30px;height:30px;border:1px solid var(--cr);border-radius:50%;display:flex;align-items:center;justify-content:center}
.vp::after{content:'';border-top:5px solid transparent;border-bottom:5px solid transparent;border-left:9px solid var(--cr);margin-left:3px}
.vl{position:absolute;bottom:8px;left:10px;font-size:9px;letter-spacing:.14em;text-transform:uppercase}

/* DASH */
.dash{width:100%;border:none;border-top:1px dashed var(--sh);position:relative;z-index:2}

/* MARQUEE */
.mq{overflow:hidden;padding:26px 0;border-top:1px dashed var(--sh);border-bottom:1px dashed var(--sh);position:relative;z-index:2;background:var(--bl)}
.mqt{display:flex;gap:56px;width:max-content;animation:mqr 18s linear infinite}
.mqt:hover{animation-play-state:paused}
.mi{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--gy);white-space:nowrap;display:inline-flex;align-items:center;gap:24px}
.mi::after{content:'·';color:var(--si);font-size:18px}
@keyframes mqr{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ─── WORD-WRAP HEADLINE BASE ─── */
.wh .w{display:block;overflow:hidden}
.wh .w i{display:block;font-style:normal;transform:translateY(106%);transition:transform .85s cubic-bezier(.16,1,.3,1)}
.wh.on .w:nth-child(1) i{transform:translateY(0);transition-delay:.04s}
.wh.on .w:nth-child(2) i{transform:translateY(0);transition-delay:.17s}
.wh.on .w:nth-child(3) i{transform:translateY(0);transition-delay:.29s}
.wh.on .w:nth-child(4) i{transform:translateY(0);transition-delay:.40s}

/* BODY LINES BASE */
.bl span{display:block;overflow:hidden}
.bl span i{display:block;font-style:normal;transform:translateY(106%);transition:transform .7s cubic-bezier(.16,1,.3,1)}
.bl.on span:nth-child(1) i{transform:translateY(0);transition-delay:.1s}
.bl.on span:nth-child(2) i{transform:translateY(0);transition-delay:.22s}
.bl.on span:nth-child(3) i{transform:translateY(0);transition-delay:.33s}
.bl.on span:nth-child(4) i{transform:translateY(0);transition-delay:.44s}

/* SR utility */
.sr{opacity:0;transform:translateY(26px);transition:opacity .8s ease,transform .8s ease}
.sr.on{opacity:1;transform:translateY(0)}
.sl{opacity:0;transform:translateX(-26px);transition:opacity .75s ease,transform .75s ease}
.sl.on{opacity:1;transform:translateX(0)}
.sx{opacity:0;transform:translateX(26px);transition:opacity .75s ease,transform .75s ease}
.sx.on{opacity:1;transform:translateX(0)}

/* SECTIONS COMMON */
.sec{padding:100px 48px;background:var(--bl)}

/* AI */
#ai .sec{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;min-height:100vh}
.ai-l h2{font-size:clamp(36px,5.5vw,72px);font-weight:500;line-height:.92;margin-bottom:28px}
.ai-l .body{font-size:15px;line-height:1.65;color:var(--gy)}
.ai-r{}
#ai-big{font-size:clamp(50px,8vw,108px);font-weight:500;line-height:.88;margin-bottom:16px}
#ai-tag{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--si);overflow:hidden}
#ai-tag i{display:block;font-style:normal;transform:translateY(105%);transition:transform .6s ease .5s}
#ai-tag.on i{transform:translateY(0)}
.ai-desc{font-size:20px;font-weight:500;line-height:1.15;margin-top:28px}
.ai-foot{margin-top:32px;padding-top:20px;border-top:1px solid var(--sh)}
.ai-foot-txt{font-size:11px;color:var(--gy);letter-spacing:.1em;text-transform:uppercase;overflow:hidden}
.ai-foot-txt i{display:block;font-style:normal;transform:translateY(105%);transition:transform .6s ease .6s}
.ai-foot-txt.on i{transform:translateY(0)}

/* FEATURES */
#feats .sec{min-height:100vh}
.ft-hd{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:end;margin-bottom:80px}
.ft-lbl{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gy);margin-bottom:20px;overflow:hidden}
.ft-lbl i{display:block;font-style:normal;transform:translateY(105%);transition:transform .6s ease}
.ft-lbl.on i{transform:translateY(0)}
.ft-h2{font-size:clamp(32px,5vw,64px);font-weight:500;line-height:.92}
.ft-body{font-size:14px;line-height:1.7;color:var(--gy);padding-top:60px}
.ft-cards{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px dashed var(--sh)}
.fc{padding:32px;border-right:1px dashed var(--sh);opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease}
.fc:first-child{padding-left:0}
.fc:last-child{border-right:none;padding-right:0}
.fc.on{opacity:1;transform:translateY(0)}
.fc-icon{width:54px;height:54px;border-radius:50%;background:rgba(255,237,215,.07);display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.fc-icon svg{width:28px;height:28px;color:var(--cr)}
.fc-tag{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--gy);margin-bottom:12px}
.fc-desc{font-size:12px;line-height:1.65;color:rgba(255,237,215,.55);margin-bottom:18px}
.fc-d{width:100%;height:1px;background:var(--sh);margin:14px 0}
.fc-title{font-size:17px;font-weight:500;line-height:1.2}

/* GRIP / ZOOM */
#grip .sec{min-height:80vh;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.grip-h{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gy);margin-bottom:18px}
.grip-h2{font-size:clamp(28px,4vw,52px);font-weight:500;line-height:.95;margin-bottom:20px}
.grip-desc{font-size:14px;line-height:1.7;color:var(--gy)}
.grip-zoom{border:1px dashed var(--sh);border-radius:12px;overflow:hidden;aspect-ratio:4/3;position:relative;cursor:crosshair}
.gz-img{width:100%;height:100%;object-fit:cover;filter:brightness(.55) saturate(.7);transform:scale(1);transition:transform .1s ease;transform-origin:center center}
.gz-lens{position:absolute;width:100px;height:100px;border-radius:50%;border:1px solid rgba(255,237,215,.3);background:radial-gradient(circle,rgba(255,237,215,.06) 0%,transparent 70%);pointer-events:none;opacity:0;transition:opacity .2s;transform:translate(-50%,-50%)}
.grip-zoom:hover .gz-lens{opacity:1}
.gz-coeff{position:absolute;bottom:16px;right:16px;font-size:11px;letter-spacing:.1em;color:var(--cr);background:rgba(16,9,4,.7);padding:6px 12px;border-radius:6px;border:1px solid rgba(255,237,215,.12)}

/* ENCRYPTION */
#enc .sec{min-height:80vh;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.enc-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gy);margin-bottom:18px}
.enc-h2{font-size:clamp(28px,4vw,52px);font-weight:500;line-height:.95;margin-bottom:20px}
.enc-desc{font-size:14px;line-height:1.7;color:var(--gy)}
.enc-r{display:flex;flex-direction:column;gap:24px}
.enc-field{position:relative;border-bottom:1px solid rgba(255,237,215,.28)}
.enc-field input{width:100%;background:transparent;border:none;outline:none;font-family:inherit;font-size:36px;font-weight:500;color:var(--cr);padding:14px 0;letter-spacing:.04em}
.enc-btn{background:var(--si);color:var(--cr);border:none;border-radius:30px;padding:15px 32px;font-size:13px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;position:relative;overflow:hidden}
.enc-btn:hover{opacity:.85}
.flipper{display:flex;flex-direction:column;height:1.3em;overflow:hidden;transition:transform .4s cubic-bezier(.77,0,.18,1)}
.flipper span{display:block;line-height:1.3}
.enc-btn.flipped .flipper{transform:translateY(-50%)}

/* SUSTAINABILITY */
#sust .sec{min-height:100vh}
.st-hero{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:end;margin-bottom:80px}
.st-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--gy);margin-bottom:20px}
.st-pre{font-size:20px;font-weight:500;color:rgba(255,237,215,.45);margin-bottom:4px;overflow:hidden}
.st-pre i{display:block;font-style:normal;transform:translateY(105%);transition:transform .7s ease}
.st-pre.on i{transform:translateY(0)}
.st-h2{font-size:clamp(40px,6.5vw,88px);font-weight:500;line-height:.88}
.st-desc{font-size:14px;line-height:1.7;color:var(--gy);padding-top:60px}
.st-grid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px dashed var(--sh)}
.si{padding:40px 32px;border-right:1px dashed var(--sh);opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}
.si:first-child{padding-left:0}
.si:last-child{border-right:none;padding-right:0}
.si.on{opacity:1;transform:translateY(0)}
.si-num{font-size:80px;font-weight:500;line-height:1;color:var(--cr);margin-bottom:12px}
.si-title{font-size:15px;font-weight:500;line-height:1.25;margin-bottom:14px}
.si-desc{font-size:12px;line-height:1.65;color:var(--gy)}

/* TESTIMONIALS */
#test{padding:100px 48px;background:var(--bl)}
.ts-hero{margin-bottom:56px}
.ts-h2{font-size:clamp(26px,4vw,54px);font-weight:500;line-height:1.05;max-width:580px;margin-bottom:18px}
.ts-sub{font-size:14px;color:var(--gy);line-height:1.6}
.ts-hd{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;padding:14px 0;border-top:1px dashed var(--sh);border-bottom:1px dashed var(--sh);font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--gy)}
.tr{display:grid;grid-template-columns:1fr auto 96px;gap:20px;padding:28px 0;border-bottom:1px dashed var(--sh);align-items:center;opacity:0;transform:translateY(16px);transition:opacity .65s ease,transform .65s ease}
.tr.on{opacity:1;transform:translateY(0)}
.stars{display:flex;gap:3px;margin-bottom:10px}
.star{width:11px;height:11px;background:var(--cr);clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.star.h{opacity:.35}
.tq{font-size:15px;line-height:1.5;font-style:italic;margin-bottom:10px}
.tq strong{color:var(--cr);font-style:normal}
.ta-n{font-size:12px;font-weight:500}
.ta-r{font-size:11px;color:var(--gy)}
.tr-rt{font-size:11px;color:var(--gy);letter-spacing:.1em;align-self:start;padding-top:4px}
.tr-img{width:96px;height:64px;border-radius:8px;overflow:hidden;border:1px solid rgba(255,237,215,.09)}
.tr-img img{width:100%;height:100%;object-fit:cover;filter:brightness(.55) saturate(.5)}

/* CTA + FOOTER */
#cta{padding:100px 48px;border-top:1px dashed var(--sh);text-align:center;background:var(--bl);display:flex;flex-direction:column;align-items:center;gap:32px;min-height:60vh;justify-content:center}
.cta-tag{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--gy)}
.cta-h2{font-size:clamp(44px,8vw,108px);font-weight:500;line-height:.88}
.cta-btns{display:flex;gap:16px;flex-wrap:wrap;justify-content:center}
.btf{background:var(--ck);color:var(--cr);border:none;border-radius:36px;padding:14px 32px;font-size:14px;letter-spacing:.06em;transition:opacity .3s,transform .2s}
.btf:hover{opacity:.8;transform:translateY(-2px)}
.bto{background:transparent;color:var(--cr);border:1px solid rgba(255,237,215,.38);border-radius:22px;padding:10px 24px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;transition:border-color .3s,color .3s}
.bto:hover{border-color:var(--si);color:var(--si)}
footer{padding:40px 48px 32px;border-top:1px dashed var(--sh);background:var(--bl)}
.ft{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}
.fl{font-size:22px;font-weight:500;letter-spacing:.04em}
.fn{display:flex;gap:24px;list-style:none}
.fn a{font-size:10px;color:var(--gy);letter-spacing:.12em;text-transform:uppercase;transition:color .3s}
.fn a:hover{color:var(--cr)}
.fb{display:flex;justify-content:space-between;align-items:center;padding-top:18px;border-top:1px dashed var(--sh);font-size:10px;color:var(--gy);letter-spacing:.07em}
.fb em{color:var(--si);font-style:normal}

@media(max-width:900px){
  #nav{padding:18px 22px}
  #hero,.sec,#test,#cta,footer{padding-left:22px;padding-right:22px}
  .hero-bot,#ai .sec,#feats .ft-hd,#grip .sec,#enc .sec,#sust .st-hero{grid-template-columns:1fr}
  .ft-cards,.st-grid{grid-template-columns:1fr}
  .fc,.si{border-right:none;padding:24px 0;border-bottom:1px dashed var(--sh)}
  .ts-hd,.tr{grid-template-columns:1fr}
  .tr-img,.tr-rt{display:none}
}
</style>
</head>
<body>

<div id="dot"></div>
<div id="ring"></div>
<div id="bar"></div>

<!-- CANVAS — 3D spinning coaster behind everything -->
<div id="canvas-wrap"><canvas id="c"></canvas></div>

<!-- SCROLL PROMPT -->
<div id="sp"><span class="sp-t">Scroll</span><div class="sp-l"></div></div>

<!-- NAV -->
<nav id="nav">
  <a href="#hero" class="logo">
    <svg viewBox="0 0 809 174" fill="none"><path d="M87 174C36 174 0 132 0 87C0 42 36 0 87 0C138 0 174 42 174 87C174 132 138 174 87 174ZM87 135C112 135 135 115 135 87C135 59 112 39 87 39C62 39 39 59 39 87C39 115 62 135 87 135Z" fill="currentColor"/><path d="M196 170V4H263C307 4 327 28 327 61C327 84 317 103 296 112L333 170H284L255 118H237V170H196ZM237 80H264C280 80 285 72 285 61C285 50 280 42 264 42H237V80Z" fill="currentColor"/><path d="M385 170V101L325 4H373L406 62L439 4H487L427 100V170H385Z" fill="currentColor"/><path d="M490 170V133L568 42H494V4H620V41L543 132H622V170H490Z" fill="currentColor"/><path d="M722 174C671 174 635 132 635 87C635 42 671 0 722 0C773 0 809 42 809 87C809 132 773 174 722 174ZM722 135C747 135 770 115 770 87C770 59 747 39 722 39C697 39 674 59 674 87C674 115 697 135 722 135Z" fill="currentColor"/></svg>
  </a>
  <div class="nav-r">
    <a href="#ai" class="nl"><s1>AI</s1><s2>AI</s2></a>
    <a href="#feats" class="nl"><s1>Features</s1><s2>Features</s2></a>
    <a href="#sust" class="nl"><s1>Sustainability</s1><s2>Sustainability</s2></a>
    <button class="nb">Order Now</button>
  </div>
</nav>

<!-- ══ HERO ══ -->
<section id="hero">
  <div class="h-tag" id="htag">
    <span class="c">M</span><span class="c">a</span><span class="c">d</span><span class="c">e</span><span class="c">&nbsp;</span><span class="c">f</span><span class="c">o</span><span class="c">r</span><span class="c">&nbsp;</span><span class="c">m</span><span class="c">u</span><span class="c">g</span><span class="c">s</span><span class="c">.</span><span class="c">&nbsp;</span><span class="c">B</span><span class="c">u</span><span class="c">i</span><span class="c">l</span><span class="c">t</span><span class="c">&nbsp;</span><span class="c">f</span><span class="c">o</span><span class="c">r</span><span class="c">&nbsp;</span><span class="c">t</span><span class="c">a</span><span class="c">b</span><span class="c">l</span><span class="c">e</span><span class="c">s</span><span class="c">.</span>
  </div>
  <div class="hero-mid">
    <svg id="hero-svg" viewBox="0 0 809 174" fill="none"><path d="M87 174C36 174 0 132 0 87C0 42 36 0 87 0C138 0 174 42 174 87C174 132 138 174 87 174ZM87 135C112 135 135 115 135 87C135 59 112 39 87 39C62 39 39 59 39 87C39 115 62 135 87 135Z" fill="currentColor"/><path d="M196 170V4H263C307 4 327 28 327 61C327 84 317 103 296 112L333 170H284L255 118H237V170H196ZM237 80H264C280 80 285 72 285 61C285 50 280 42 264 42H237V80Z" fill="currentColor"/><path d="M385 170V101L325 4H373L406 62L439 4H487L427 100V170H385Z" fill="currentColor"/><path d="M490 170V133L568 42H494V4H620V41L543 132H622V170H490Z" fill="currentColor"/><path d="M722 174C671 174 635 132 635 87C635 42 671 0 722 0C773 0 809 42 809 87C809 132 773 174 722 174ZM722 135C747 135 770 115 770 87C770 59 747 39 722 39C697 39 674 59 674 87C674 115 697 135 722 135Z" fill="currentColor"/></svg>
  </div>
  <div class="hero-bot">
    <p class="h-copy" id="hcopy">
      <span class="ln"><i>Designed to lift, insulate, and grip in all</i></span>
      <span class="ln"><i>the right ways. Oryzo makes the simplest</i></span>
      <span class="ln"><i>moment feel considered.</i></span>
    </p>
    <div class="h-card" id="hcard">
      <h4>Designed<br>by Lusion,<br>the award-winning<br>design studio.</h4>
      <div class="hcd"></div>
      <p>The world's most<br>unnecessarily<br>sophisticated cork coaster.</p>
    </div>
  </div>
  <div id="vchip">
    <img src="coaster1.png" alt="ORYZO"/>
    <div class="vp"></div><span class="vl">PLAY</span>
  </div>
</section>

<!-- MARQUEE -->
<div class="mq"><div class="mqt">
  <span class="mi">Made for mugs</span><span class="mi">Built for tables</span><span class="mi">Cork intelligence</span><span class="mi">Unnecessarily sophisticated</span><span class="mi">Award winning</span><span class="mi">Designed by Lusion</span><span class="mi">Thermodynamic stability</span><span class="mi">Zero drama</span>
  <span class="mi">Made for mugs</span><span class="mi">Built for tables</span><span class="mi">Cork intelligence</span><span class="mi">Unnecessarily sophisticated</span><span class="mi">Award winning</span><span class="mi">Designed by Lusion</span><span class="mi">Thermodynamic stability</span><span class="mi">Zero drama</span>
</div></div>

<!-- ══ AI ══ -->
<section id="ai"><div class="sec">
  <div class="ai-l">
    <h2 class="wh" id="ai-pre">
      <span class="w"><i>isn't just</i></span>
      <span class="w"><i>a coaster.</i></span>
    </h2>
    <div class="bl sr" id="ai-body" style="font-size:15px;line-height:1.65;color:var(--gy)">
      <span><i>Oryzo isn't just a coaster.</i></span>
      <span><i>It's the result of unprecedented</i></span>
      <span><i>AI* breakthroughs.</i></span>
    </div>
  </div>
  <div class="ai-r">
    <div id="ai-big" class="wh">
      <span class="w"><i>Powered</i></span>
      <span class="w"><i>by AI<sup style="font-size:.5em;vertical-align:super;color:var(--si)">*</sup></i></span>
    </div>
    <div id="ai-tag"><i>Oryzo&#8209;1</i></div>
    <div class="ai-desc wh" id="ai-desc" style="margin-top:32px">
      <span class="w"><i>AI fills in the gaps.</i></span>
      <span class="w"><i>We said high five.</i></span>
      <span class="w"><i>It heard six.</i></span>
    </div>
    <div class="ai-foot sr" style="transition-delay:.4s">
      <div class="ai-foot-txt" id="ai-disc"><i>* Adobe Illustrator</i></div>
    </div>
  </div>
</div></section>

<hr class="dash"/>

<!-- ══ FEATURES ══ -->
<section id="feats"><div class="sec">
  <div class="ft-hd">
    <div>
      <div class="ft-lbl" id="ftlbl"><i>— What it does</i></div>
      <h2 class="ft-h2 wh" id="fth2">
        <span class="w"><i>Elevate</i></span>
        <span class="w"><i>everything.</i></span>
        <span class="w"><i>Literally.</i></span>
      </h2>
    </div>
    <p class="ft-body sr">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable while your coffee table tapped out three sips ago. Precision engineered for the unnecessarily sophisticated.</p>
  </div>
  <div class="ft-cards">
    <div class="fc" data-fc>
      <div class="fc-icon"><svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="12" stroke="currentColor" stroke-width=".7" opacity=".3"/><path d="M14 7l4.5 5.5h-3v7.5h-3V12.5H9z" fill="currentColor"/><path d="M10.5 20.5h7M10.5 22.5h7" stroke="currentColor" stroke-width=".7" opacity=".5"/></svg></div>
      <div class="fc-tag">Rise above mediocrity</div>
      <div class="fc-desc">With a precision-engineered lift (exactly one coaster thick), Oryzo doesn't just hold your mug — it elevates it. Literally.</div>
      <div class="fc-d"></div>
      <div class="fc-title">Elevate your coffee experience</div>
    </div>
    <div class="fc" data-fc>
      <div class="fc-icon"><svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="12" stroke="currentColor" stroke-width=".7" opacity=".3"/><rect x="11" y="8" width="6" height="14" rx="3" stroke="currentColor" stroke-width=".7" fill="none"/><path d="M11 18h6" stroke="currentColor" stroke-width=".7"/></svg></div>
      <div class="fc-tag">Handles Extremes with Ease</div>
      <div class="fc-desc">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable. Your coffee table tapped out three sips ago.</div>
      <div class="fc-d"></div>
      <div class="fc-title">Thermodynamic stability</div>
    </div>
    <div class="fc" data-fc>
      <div class="fc-icon"><svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="12" stroke="currentColor" stroke-width=".7" opacity=".3"/><circle cx="14" cy="14" r="7" stroke="currentColor" stroke-width=".7"/><circle cx="14" cy="14" r="2" fill="currentColor"/></svg></div>
      <div class="fc-tag">Perfectly Round, Seriously</div>
      <div class="fc-desc">Our engineers recalibrated its circumference with disturbing levels of attention to detail — just because we could.</div>
      <div class="fc-d"></div>
      <div class="fc-title">Now 37.9% More Circular</div>
    </div>
  </div>
</div></section>

<hr class="dash"/>

<!-- ══ GRIP ══ -->
<section id="grip"><div class="sec">
  <div class="sl">
    <div class="grip-h sr">Precision Grip, Zero Drama</div>
    <h2 class="grip-h2 wh" id="grph2">
      <span class="w"><i>Grip-locked</i></span>
      <span class="w"><i>Antislip tech</i></span>
    </h2>
    <p class="grip-desc sr" style="transition-delay:.2s">Micro-textured cork so grippy your drink files a restraining order against gravity. Spills? Consider them politely discouraged.</p>
  </div>
  <div class="grip-zoom sx" id="gzoom">
    <img class="gz-img" id="gzimg" src="coaster2.png" alt="cork texture zoom"/>
    <div class="gz-lens" id="gzlens"></div>
    <div class="gz-coeff">Friction coefficient: <strong>0.80</strong></div>
  </div>
</div></section>

<hr class="dash"/>

<!-- ══ ENCRYPTION ══ -->
<section id="enc"><div class="sec">
  <div class="sl">
    <div class="enc-tag">Secure communications simplified</div>
    <h2 class="enc-h2 wh" id="ench2">
      <span class="w"><i>Smart flip</i></span>
      <span class="w"><i>encryption</i></span>
    </h2>
    <p class="enc-desc sr" style="transition-delay:.2s">Write a message. Flip. Instantly secure — until someone flips it back. Genius.</p>
  </div>
  <div class="enc-r sx" style="transition-delay:.15s">
    <div class="enc-field">
      <input type="text" id="einput" value="ORYZO" maxlength="10" autocomplete="off" spellcheck="false"/>
    </div>
    <button class="enc-btn" id="ebtn">
      <div class="flipper" id="eflip">
        <span>Encode Message</span>
        <span>Decode Message</span>
      </div>
    </button>
  </div>
</div></section>

<hr class="dash"/>

<!-- ══ SUSTAINABILITY ══ -->
<section id="sust"><div class="sec">
  <div class="st-hero">
    <div>
      <div class="st-tag sr">100% Plant-based</div>
      <div class="st-pre" id="stpre"><i>Vegan-friendly</i></div>
      <h2 class="st-h2 wh" id="sth2">
        <span class="w"><i>sustain</i></span>
        <span class="w"><i>ability</i></span>
      </h2>
    </div>
    <p class="st-desc sr" style="transition-delay:.25s">Pure cork sourced sustainably. Completely vegan — no cows were harmed, but it might be full of "bull"sh*t.</p>
  </div>
  <div class="st-grid">
    <div class="si" data-si><div class="si-num">25</div><div class="si-title">Average age of first harvest</div><div class="si-desc">Cork oaks are typically first harvested at 25 years, once bark is thick enough to remove safely.</div></div>
    <div class="si" data-si><div class="si-num">9</div><div class="si-title">Harvesting interval (years)</div><div class="si-desc">After each harvest the bark takes about 9 years to regrow, making cork a perfectly renewable material.</div></div>
    <div class="si" data-si><div class="si-num">0W</div><div class="si-title">Power draw while in use</div><div class="si-desc">No compute. No tokens. Say "please" and "thank you" as much as you want — guilt free.</div></div>
  </div>
</div></section>

<hr class="dash"/>

<!-- ══ TESTIMONIALS ══ -->
<section id="test">
  <div class="ts-hero">
    <h2 class="ts-h2 wh" id="tsh2">
      <span class="w"><i>People all around</i></span>
      <span class="w"><i>the world love</i></span>
      <span class="w"><i>Oryzo</i></span>
    </h2>
    <p class="ts-sub sr">Do not take our word for it, see what people say after living with Oryzo.</p>
  </div>
  <div class="ts-hd"><div>Rating &amp; Reviews</div><div>Custom reviews [364] ★ 4.9/5</div><div>ORYZO in use</div></div>
  <div class="tr" data-tr><div><div class="stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div><div class="tq">"This is the <strong>best coaster</strong> I've ever used. I can't go to space without it."</div><div class="ta-n">Edan K.</div><div class="ta-r">NASA astronaut wannabe</div></div><div class="tr-rt">[ 5/5 ]</div><div class="tr-img"><img src="coaster2.png" alt=""/></div></div>
  <div class="tr" data-tr><div><div class="stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star h"></div></div><div class="tq">"My coaster? If you want it, I'll let you have it. I left everything in <strong>one place!</strong>"</div><div class="ta-n">Gol D. Roger</div><div class="ta-r">Old-school Pirate</div></div><div class="tr-rt">[ 4.5/5 ]</div><div class="tr-img"><img src="coaster1.png" alt=""/></div></div>
  <div class="tr" data-tr><div><div class="stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div><div class="tq">"<strong>We are so cooked.</strong> Hollywood is not ready for a coaster this cinematic."</div><div class="ta-n">Jamie R.</div><div class="ta-r">AI influencer, Ex-Web3 influencer</div></div><div class="tr-rt">[ 5/5 ]</div><div class="tr-img"><img src="coaster2.png" alt=""/></div></div>
  <div class="tr" data-tr><div><div class="stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div><div class="tq">"My table hasn't been this protected since I stopped trusting <strong>gravity</strong>."</div><div class="ta-n">Priya K.</div><div class="ta-r">Flat Earth believer</div></div><div class="tr-rt">[ 5/5 ]</div><div class="tr-img"><img src="coaster1.png" alt=""/></div></div>
</section>

<!-- ══ CTA ══ -->
<section id="cta">
  <div class="cta-tag sr">Ready to elevate?</div>
  <h2 class="cta-h2 wh" id="ctah2">
    <span class="w"><i>Order yours</i></span>
    <span class="w"><i>today.</i></span>
  </h2>
  <div class="cta-btns sr" style="transition-delay:.35s">
    <button class="btf">Get ORYZO&#8209;1</button>
    <button class="bto">Learn more</button>
  </div>
</section>

<footer>
  <div class="ft"><div class="fl">ORYZO</div><ul class="fn"><li><a href="#ai">AI</a></li><li><a href="#feats">Features</a></li><li><a href="#sust">Sustainability</a></li><li><a href="#test">Reviews</a></li><li><a href="#">Privacy</a></li></ul></div>
  <div class="fb"><span>&copy; 2026 ORYZO AI. Designed by Lusion.</span><span>Powered by <em>ORYZO&#8209;1</em></span></div>
</footer>

<script>
/* ══════════════════════════════════════════════════
   CURSOR
══════════════════════════════════════════════════ */
const dot=document.getElementById('dot'),ring=document.getElementById('ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px';},{passive:true});
(function l(){rx+=(mx-rx)*.1;ry+=(my-ry)*.1;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(l)})();
document.querySelectorAll('a,button,input').forEach(el=>{el.addEventListener('mouseenter',()=>document.body.classList.add('ch'));el.addEventListener('mouseleave',()=>document.body.classList.remove('ch'));});

/* ══════════════════════════════════════════════════
   CANVAS 3D CORK COASTER
══════════════════════════════════════════════════ */
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');
let W,H,cx,cy,R;
let rotY=0;        // current Y rotation (radians) — 0=top, PI/2=edge
let rotX=0;        // current X tilt
let tRotY=0;       // target Y rotation driven by scroll
let tRotX=0;       // target X tilt driven by mouse
let tRotXmouse=0;
let tRotYmouse=0;
let scrollRotY=0;  // accumulated from scroll
let t=0;           // time for float animation
let mousePx=0,mousePy=0; // normalized -1..1 mouse position

function resize(){
  W=canvas.width=window.innerWidth;
  H=canvas.height=window.innerHeight;
  cx=W/2; cy=H/2;
  R=Math.min(W,H)*0.26;
}
resize();
window.addEventListener('resize',resize);

document.addEventListener('mousemove',e=>{
  mousePx=(e.clientX/window.innerWidth-.5)*2;
  mousePy=(e.clientY/window.innerHeight-.5)*2;
},{passive:true});

/* Scroll drives rotation */
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const docH=document.body.scrollHeight-window.innerHeight;
  const p=sy/docH; // 0..1 full page scroll
  // Rotate coaster based on scroll: full page = 4 full rotations
  scrollRotY=p*Math.PI*8;
},{passive:true});

/* Draw a single grain ring on the cork face */
function corkGrain(ctx,cx,cy,a,b,angle,alpha){
  ctx.save();
  ctx.globalAlpha=alpha;
  ctx.strokeStyle='rgba(80,40,10,0.35)';
  ctx.lineWidth=0.7;
  ctx.beginPath();
  ctx.ellipse(cx+Math.random()*4-2,cy+Math.random()*4-2,a,b,angle,0,Math.PI*2);
  ctx.stroke();
  ctx.restore();
}

function drawCoaster(){
  ctx.clearRect(0,0,W,H);
  t+=0.012;

  // Smooth lerp rotations
  rotY+=(scrollRotY-rotY)*0.06;
  rotX+=(tRotX-rotX)*0.06;

  // Mouse tilt
  tRotX=mousePy*0.3;
  tRotYmouse=mousePx*0.2;

  // Gentle idle float
  const floatY=Math.sin(t)*6;
  const floatX=Math.cos(t*0.7)*3;

  // Coaster center with float
  const ox=cx+floatX;
  const oy=cy+floatY;

  // Y rotation determines how flat/edge the ellipse looks
  const cosY=Math.cos(rotY+tRotYmouse);
  const sinY=Math.sin(rotY+tRotYmouse);
  const cosX=Math.cos(rotX);

  // Horizontal radius = R (constant)
  const ra=R;
  // Vertical radius = R * |cos(rotY)| (squishes as it rotates)
  const rb=R*Math.abs(cosY)*cosX;
  const thick=Math.max(4,22*Math.abs(sinY)*Math.abs(cosX));
  const edgeUp=cosY>=0; // which side the edge is visible

  /* --- SHADOW --- */
  const sg=ctx.createRadialGradient(ox+10,oy+rb+thick+10,0,ox+10,oy+rb+thick+10,R*0.9);
  sg.addColorStop(0,'rgba(0,0,0,0.35)');
  sg.addColorStop(1,'rgba(0,0,0,0)');
  ctx.fillStyle=sg;
  ctx.beginPath();
  ctx.ellipse(ox+10,oy+rb+thick+10,ra*0.8,R*0.18,0,0,Math.PI*2);
  ctx.fill();

  /* --- EDGE (side of disc) --- */
  if(thick>2){
    const edgeOffY=edgeUp?rb:-rb;
    // Edge gradient
    const eg=ctx.createLinearGradient(ox-ra,oy+edgeOffY,ox+ra,oy+edgeOffY+thick);
    eg.addColorStop(0,'#3a2010');
    eg.addColorStop(0.3,'#6b3d1a');
    eg.addColorStop(0.7,'#8b5225');
    eg.addColorStop(1,'#3a2010');
    ctx.fillStyle=eg;
    ctx.beginPath();
    ctx.ellipse(ox,oy+edgeOffY+(edgeUp?thick/2:-thick/2),ra,Math.max(1,thick/2),0,0,Math.PI*2);
    ctx.fill();
    // Edge top arc
    ctx.beginPath();
    ctx.ellipse(ox,oy+edgeOffY,ra,Math.max(1,thick*0.15),0,0,Math.PI*2);
    ctx.fillStyle='#4a2a10';
    ctx.fill();
  }

  /* --- CORK FACE --- */
  if(Math.abs(rb)>1){
    // Base cork gradient — warm tan
    const angle=Math.atan2(rb,ra);
    const lightX=ox-ra*0.35;
    const lightY=oy-Math.abs(rb)*0.35;
    const cg=ctx.createRadialGradient(lightX,lightY,0,ox,oy,ra*1.1);
    cg.addColorStop(0,'#d4a06a');
    cg.addColorStop(0.35,'#c0905a');
    cg.addColorStop(0.65,'#a87840');
    cg.addColorStop(0.85,'#8a5f30');
    cg.addColorStop(1,'#6e4520');

    ctx.save();
    ctx.beginPath();
    ctx.ellipse(ox,oy,ra,Math.abs(rb),0,0,Math.PI*2);
    ctx.fillStyle=cg;
    ctx.fill();

    /* Cork grain rings */
    ctx.beginPath();
    ctx.ellipse(ox,oy,ra,Math.abs(rb),0,0,Math.PI*2);
    ctx.clip();
    // Draw concentric grain rings
    const rings=12;
    for(let i=1;i<=rings;i++){
      const rf=i/rings;
      const gra=ra*rf+(Math.random()*3-1.5);
      const grb=Math.abs(rb)*rf+(Math.random()*2-1);
      ctx.beginPath();
      ctx.ellipse(ox+(Math.random()*6-3),oy+(Math.random()*4-2),gra,grb,Math.random()*0.1,0,Math.PI*2);
      ctx.strokeStyle=`rgba(${60+Math.random()*30},${25+Math.random()*15},${5+Math.random()*8},${0.2+Math.random()*0.25})`;
      ctx.lineWidth=0.6+Math.random()*0.8;
      ctx.stroke();
    }
    // Irregular radial lines (cork grain direction)
    for(let i=0;i<18;i++){
      const ga=Math.random()*Math.PI*2;
      const gr1=ra*0.05;
      const gr2=ra*(0.3+Math.random()*0.65);
      ctx.beginPath();
      const gx1=ox+Math.cos(ga)*gr1;
      const gy1=oy+Math.sin(ga)*gr1*(Math.abs(rb)/ra);
      const gx2=ox+Math.cos(ga)*gr2;
      const gy2=oy+Math.sin(ga)*gr2*(Math.abs(rb)/ra);
      ctx.moveTo(gx1,gy1);
      ctx.lineTo(gx2+Math.random()*4-2,gy2+Math.random()*3-1.5);
      ctx.strokeStyle=`rgba(60,25,5,${0.08+Math.random()*0.12})`;
      ctx.lineWidth=0.5;
      ctx.stroke();
    }
    ctx.restore();

    /* Rim highlight */
    ctx.save();
    ctx.beginPath();
    ctx.ellipse(ox,oy,ra,Math.abs(rb),0,0,Math.PI*2);
    ctx.clip();
    const rimG=ctx.createRadialGradient(lightX,lightY,ra*0.6,lightX,lightY,ra*1.1);
    rimG.addColorStop(0,'rgba(255,220,160,0)');
    rimG.addColorStop(0.7,'rgba(255,220,160,0)');
    rimG.addColorStop(0.88,'rgba(255,220,160,0.12)');
    rimG.addColorStop(1,'rgba(255,200,120,0.25)');
    ctx.fillStyle=rimG;
    ctx.fillRect(ox-ra,oy-Math.abs(rb),ra*2,Math.abs(rb)*2);

    /* Top sheen */
    const shG=ctx.createRadialGradient(lightX,lightY,0,lightX,lightY,ra*0.7);
    shG.addColorStop(0,'rgba(255,240,200,0.14)');
    shG.addColorStop(0.4,'rgba(255,230,180,0.06)');
    shG.addColorStop(1,'rgba(255,210,160,0)');
    ctx.fillStyle=shG;
    ctx.fillRect(ox-ra,oy-Math.abs(rb),ra*2,Math.abs(rb)*2);
    ctx.restore();

    /* ORYZO text on face */
    if(Math.abs(rb)>R*0.18){
      ctx.save();
      ctx.beginPath();
      ctx.ellipse(ox,oy,ra,Math.abs(rb),0,0,Math.PI*2);
      ctx.clip();
      const textScale=Math.abs(rb)/ra;
      ctx.transform(1,0,0,textScale,0,oy*(1-textScale));
      ctx.font=`500 ${Math.floor(ra*0.14)}px 'DM Sans',sans-serif`;
      ctx.fillStyle='rgba(255,237,215,0.2)';
      ctx.textAlign='center';
      ctx.letterSpacing='0.2em';
      ctx.fillText('ORYZO',ox,oy+ra*0.04);
      ctx.restore();
    }
  }

  requestAnimationFrame(drawCoaster);
}
drawCoaster();

/* ══════════════════════════════════════════════════
   NAV + PROGRESS + SCROLL PROMPT
══════════════════════════════════════════════════ */
const nav=document.getElementById('nav');
const sp=document.getElementById('sp');
const bar=document.getElementById('bar');
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const tot=document.body.scrollHeight-window.innerHeight;
  bar.style.width=(sy/tot*100)+'%';
  nav.classList.toggle('on',sy>70);
  sp.classList.toggle('g',sy>window.innerHeight*.45);
},{passive:true});

/* ══════════════════════════════════════════════════
   HERO LOAD ANIMATIONS
══════════════════════════════════════════════════ */
window.addEventListener('DOMContentLoaded',()=>{
  // Tagline char stagger
  document.querySelectorAll('#htag .c').forEach((c,i)=>{
    setTimeout(()=>{c.style.opacity='1';c.style.transform='translateY(0)';},180+i*42);
  });
  setTimeout(()=>document.getElementById('hero-svg').classList.add('on'),300);
  setTimeout(()=>document.getElementById('hcopy').classList.add('on'),450);
  setTimeout(()=>document.getElementById('hcard').classList.add('on'),650);
  setTimeout(()=>document.getElementById('vchip').classList.add('on'),900);
});

/* ══════════════════════════════════════════════════
   INTERSECTION OBSERVER
══════════════════════════════════════════════════ */
const io=new IntersectionObserver(e=>{
  e.forEach(x=>{if(!x.isIntersecting)return;x.target.classList.add('on');io.unobserve(x.target);});
},{threshold:.12});

// Word-wrap headlines
['ai-pre','ai-big','ai-desc','fth2','grph2','ench2','sth2','tsh2','ctah2'].forEach(id=>{
  const el=document.getElementById(id);if(el)io.observe(el);
});
// Single elements
['ai-body','ai-tag','ai-disc','ftlbl','stpre'].forEach(id=>{
  const el=document.getElementById(id);if(el)io.observe(el);
});
// SR/SL/SX
document.querySelectorAll('.sr,.sl,.sx').forEach(el=>io.observe(el));

// Feature cards stagger
const fcs=document.querySelectorAll('[data-fc]');
new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  fcs.forEach((f,i)=>setTimeout(()=>f.classList.add('on'),i*130));
},{threshold:.1}).observe(fcs[0]||document.body);

// Sustain items stagger
const sis=document.querySelectorAll('[data-si]');
new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  sis.forEach((s,i)=>setTimeout(()=>s.classList.add('on'),i*140));
},{threshold:.1}).observe(sis[0]||document.body);

// Test rows stagger
const trs=document.querySelectorAll('[data-tr]');
new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  trs.forEach((r,i)=>setTimeout(()=>r.classList.add('on'),i*110));
},{threshold:.08}).observe(trs[0]||document.body);

/* ══════════════════════════════════════════════════
   HERO PARALLAX — logo + copy scroll out
══════════════════════════════════════════════════ */
const heroSvg=document.getElementById('hero-svg');
const hcopy=document.getElementById('hcopy');
window.addEventListener('scroll',()=>{
  const sy=window.scrollY,vh=window.innerHeight;
  if(sy<vh){
    const p=sy/vh;
    if(heroSvg){heroSvg.style.transform=`scale(${1+p*.07}) translateY(${-p*40}px)`;heroSvg.style.opacity=`${1-p*.9}`;}
    if(hcopy)hcopy.style.transform=`translateY(${-p*24}px)`;
    const htag=document.getElementById('htag');
    if(htag)htag.style.transform=`translateY(${-p*18}px)`;
  }
},{passive:true});

/* ══════════════════════════════════════════════════
   GRIP ZOOM LENS
══════════════════════════════════════════════════ */
const gz=document.getElementById('gzoom');
const gzlens=document.getElementById('gzlens');
const gzimg=document.getElementById('gzimg');
if(gz){
  gz.addEventListener('mousemove',e=>{
    const r=gz.getBoundingClientRect();
    const px=(e.clientX-r.left)/r.width;
    const py=(e.clientY-r.top)/r.height;
    gzlens.style.left=`${e.clientX-r.left}px`;
    gzlens.style.top=`${e.clientY-r.top}px`;
    gzimg.style.transformOrigin=`${px*100}% ${py*100}%`;
    gzimg.style.transform='scale(2.2)';
  });
  gz.addEventListener('mouseleave',()=>{
    gzimg.style.transform='scale(1)';
    gzimg.style.transformOrigin='center center';
  });
}

/* ══════════════════════════════════════════════════
   ENCRYPTION FLIP
══════════════════════════════════════════════════ */
const einput=document.getElementById('einput');
const ebtn=document.getElementById('ebtn');
const eflip=document.getElementById('eflip');
let enc=false;
function rot13(s){return s.split('').map(c=>{if(c>='A'&&c<='Z')return String.fromCharCode((c.charCodeAt(0)-65+13)%26+65);if(c>='a'&&c<='z')return String.fromCharCode((c.charCodeAt(0)-97+13)%26+97);return c;}).join('');}
if(ebtn){
  ebtn.addEventListener('click',()=>{
    enc=!enc;
    eflip.style.transform=enc?'translateY(-50%)':'translateY(0)';
    const orig=einput.value;
    const tgt=rot13(orig);
    const chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let f=0;
    const iv=setInterval(()=>{
      f++;
      if(f>14){clearInterval(iv);einput.value=tgt;return;}
      einput.value=orig.split('').map((c,i)=>i<f/14*orig.length?tgt[i]:chars[Math.floor(Math.random()*26)]).join('');
    },38);
  });
}
</script>
</body>
</html>"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("Written:",len(html),"bytes")
