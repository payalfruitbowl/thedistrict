
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no"/>
<title>ORYZO AI — The World's Most Sophisticated Cork Coaster</title>
<meta name="description" content="A physical product, reimagined for the AI era, proving even the smallest idea can feel extraordinary."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --black:#100904;--cream:#ffedd7;--shadow:#40372e;--cork:#382416;
  --sienna:#dc5000;--grey:#6c5f51;--f:'DM Sans',system-ui,sans-serif;
}
html{scroll-behavior:auto;overflow-x:hidden}
body{background:var(--black);color:var(--cream);font-family:var(--f);font-size:14px;line-height:1.4;overflow-x:hidden;cursor:none}
img{display:block}
a{color:inherit;text-decoration:none}
button{cursor:none;font-family:var(--f)}

/* ── CURSOR ─────────────────────────────── */
#dot{position:fixed;width:8px;height:8px;background:var(--cream);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference;transition:width .15s,height .15s;will-change:transform}
#ring{position:fixed;width:40px;height:40px;border:1px solid rgba(255,237,215,.4);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:border-color .25s,width .2s,height .2s;will-change:transform}
.hov #dot{width:16px;height:16px}
.hov #ring{width:58px;height:58px;border-color:rgba(220,80,0,.55)}

/* ── NAV ────────────────────────────────── */
#nav{position:fixed;top:0;left:0;right:0;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:22px 48px;border-bottom:1px solid rgba(64,55,46,0);transition:border-color .4s,background .4s}
#nav.on{border-color:var(--shadow);background:var(--black)}
.nav-logo{display:flex;align-items:center;gap:0}
.nav-logo svg{width:80px;height:17px;color:var(--cream);overflow:visible}
.nav-r{display:flex;align-items:center;gap:28px}
.nav-link{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--cream);opacity:.6;position:relative;overflow:hidden;display:block;line-height:1}
.nav-link span{display:block;transition:transform .3s cubic-bezier(.77,0,.18,1)}
.nav-link .clone{position:absolute;top:100%;left:0;color:var(--sienna);opacity:1}
.nav-link:hover span{transform:translateY(-100%)}
.nav-link:hover .clone{transform:translateY(-100%)}
.btn-nav{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--cream);background:transparent;border:1px solid rgba(255,237,215,.5);border-radius:30px;padding:8px 20px;transition:border-color .3s,color .3s}
.btn-nav:hover{border-color:var(--sienna);color:var(--sienna)}

/* ── HERO ───────────────────────────────── */
#hero{position:relative;width:100vw;height:100vh;display:flex;flex-direction:column;justify-content:space-between;padding:100px 48px 52px;overflow:hidden}
/* Coaster canvas sits behind */
#coaster-canvas{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}

.hero-tagline{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--cream);opacity:.5;position:relative;z-index:2}
.hero-tagline .char{display:inline-block;opacity:0;transform:translateY(10px);transition:opacity .4s ease,transform .4s ease}
.hero-tagline.revealed .char{opacity:1;transform:translateY(0)}

#hero-logo-area{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;flex:1}
#hero-logo-svg{width:min(600px,80vw);color:var(--cream);opacity:0;transform:scale(.94);transition:opacity 1s ease .4s,transform 1s ease .4s}
#hero-logo-svg.revealed{opacity:1;transform:scale(1)}

.hero-bottom{position:relative;z-index:2;display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:end}
.hero-copy{font-size:15px;line-height:1.5;color:var(--cream);opacity:.8;max-width:380px}
.hero-copy .line{overflow:hidden}
.hero-copy .line .li{display:block;transform:translateY(100%);transition:transform .7s cubic-bezier(.16,1,.3,1)}
.hero-copy.revealed .line:nth-child(1) .li{transform:translateY(0);transition-delay:.55s}
.hero-copy.revealed .line:nth-child(2) .li{transform:translateY(0);transition-delay:.68s}
.hero-copy.revealed .line:nth-child(3) .li{transform:translateY(0);transition-delay:.80s}

.hero-card{border:1px solid rgba(255,237,215,.15);border-radius:12px;padding:24px;backdrop-filter:blur(2px);background:rgba(16,9,4,.4);opacity:0;transform:translateY(16px);transition:opacity .8s ease .9s,transform .8s ease .9s}
.hero-card.revealed{opacity:1;transform:translateY(0)}
.hero-card h4{font-size:18px;font-weight:500;line-height:1.2;margin-bottom:16px}
.hero-card-dash{width:100%;height:1px;background:rgba(255,237,215,.12);margin:16px 0}
.hero-card-desc{font-size:12px;color:var(--grey);line-height:1.6}
.hero-card-desc span{display:block}

/* Video thumbnail */
#vid-thumb{position:absolute;bottom:52px;right:48px;width:160px;height:100px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,237,215,.15);z-index:10;opacity:0;transform:translateY(10px);transition:opacity .7s ease 1.2s,transform .7s ease 1.2s,border-color .3s,box-shadow .3s}
#vid-thumb.revealed{opacity:1;transform:translateY(0)}
#vid-thumb:hover{border-color:rgba(255,237,215,.5);box-shadow:0 0 30px rgba(220,80,0,.15)}
#vid-thumb img{width:100%;height:100%;object-fit:cover;filter:brightness(.55)}
#vid-play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:32px;height:32px;border:1px solid var(--cream);border-radius:50%;display:flex;align-items:center;justify-content:center;transition:background .3s}
#vid-play::after{content:'';border-top:6px solid transparent;border-bottom:6px solid transparent;border-left:10px solid var(--cream);margin-left:3px}
#vid-thumb:hover #vid-play{background:rgba(255,237,215,.1)}
.vid-lbl{position:absolute;bottom:8px;left:10px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--cream)}

/* scroll prompt */
#scroll-prompt{position:fixed;bottom:36px;left:50%;transform:translateX(-50%);z-index:200;display:flex;flex-direction:column;align-items:center;gap:10px;pointer-events:none;transition:opacity .4s}
#scroll-prompt.gone{opacity:0}
.sp-txt{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--cream);opacity:.5}
.sp-arr{display:flex;flex-direction:column;gap:4px;align-items:center}
.sp-line{width:1px;height:40px;background:linear-gradient(to bottom,rgba(255,237,215,.4),transparent);animation:spline 1.8s ease infinite}
@keyframes spline{0%{transform:scaleY(0);transform-origin:top}50%{transform:scaleY(1);transform-origin:top}51%{transform:scaleY(1);transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}

/* ── DASHED RULE ─────────────────────────── */
.dash{width:100%;border:none;border-top:1px dashed var(--shadow);position:relative;z-index:2}

/* ── SECTION BASE ────────────────────────── */
section{position:relative;z-index:2;background:var(--black)}
.container{padding:0 48px}
.sec-inner{padding:100px 48px}

/* ── SECTION: AI ─────────────────────────── */
#ai{min-height:100vh;display:flex;align-items:stretch}
.ai-inner{width:100%;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;padding:100px 48px}
.ai-pre{}
.ai-pre h2{font-size:clamp(36px,5vw,64px);font-weight:500;line-height:.95;margin-bottom:24px}
.ai-pre h2 .w{display:block;overflow:hidden}
.ai-pre h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.ai-pre h2.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.05s}
.ai-pre h2.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.18s}
.ai-pre .body{font-size:15px;line-height:1.6;color:var(--grey);overflow:hidden}
.ai-pre .body span{display:block;transform:translateY(105%);transition:transform .7s cubic-bezier(.16,1,.3,1)}
.ai-pre .body.revealed span:nth-child(1){transform:translateY(0);transition-delay:.2s}
.ai-pre .body.revealed span:nth-child(2){transform:translateY(0);transition-delay:.32s}
.ai-pre .body.revealed span:nth-child(3){transform:translateY(0);transition-delay:.44s}
.ai-pre .body.revealed span:nth-child(4){transform:translateY(0);transition-delay:.56s}

.ai-right{display:flex;flex-direction:column;gap:32px}
.ai-title-block{}
#ai-title{font-size:clamp(48px,7vw,96px);font-weight:500;line-height:.88;overflow:hidden}
#ai-title .w{display:block;overflow:hidden}
#ai-title .w .wi{display:block;transform:translateY(105%);transition:transform .9s cubic-bezier(.16,1,.3,1)}
#ai-title.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.1s}
#ai-title.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.22s}
.ai-tag{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--sienna);margin-top:12px;opacity:0;transition:opacity .6s ease .5s}
.ai-tag.revealed{opacity:1}
.ai-desc{font-size:18px;font-weight:500;line-height:1.15;overflow:hidden}
.ai-desc span{display:block;overflow:hidden}
.ai-desc span .wi{display:block;transform:translateY(105%);transition:transform .7s cubic-bezier(.16,1,.3,1)}
.ai-desc.revealed span:nth-child(1) .wi{transform:translateY(0);transition-delay:.15s}
.ai-desc.revealed span:nth-child(2) .wi{transform:translateY(0);transition-delay:.28s}
.ai-desc.revealed span:nth-child(3) .wi{transform:translateY(0);transition-delay:.40s}
.ai-disclaimer{display:flex;flex-direction:column;gap:8px}
.ai-disc-line{width:100%;height:1px;background:var(--shadow)}
.ai-disc-txt{font-size:11px;color:var(--grey);letter-spacing:.1em;text-transform:uppercase;overflow:hidden}
.ai-disc-txt span{display:block}
.ai-disc-txt .wi{display:block;transform:translateY(105%);transition:transform .6s cubic-bezier(.16,1,.3,1)}
.ai-disc-txt.revealed .wi{transform:translateY(0);transition-delay:.6s}

/* ── FEATURES SECTION ────────────────────── */
#features{padding:0}
.feat-inner{padding:100px 48px}
.feat-header{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;margin-bottom:80px}
.feat-header-left{}
.feat-header-left .sub{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:20px;overflow:hidden}
.feat-header-left .sub .wi{display:block;transform:translateY(105%);transition:transform .6s ease}
.feat-header-left .sub.revealed .wi{transform:translateY(0)}
.feat-h2{font-size:clamp(32px,4.5vw,58px);font-weight:500;line-height:.95}
.feat-h2 .w{display:block;overflow:hidden}
.feat-h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.feat-h2.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.05s}
.feat-h2.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.18s}
.feat-h2.revealed .w:nth-child(3) .wi{transform:translateY(0);transition-delay:.3s}
.feat-header-right{padding-top:60px}
.feat-body{font-size:14px;line-height:1.7;color:var(--grey)}

/* Feature cards */
.feat-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px dashed var(--shadow)}
.feat-card{padding:32px 0 32px;border-right:1px dashed var(--shadow);padding-right:32px;padding-left:32px;opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease}
.feat-card:first-child{padding-left:0}
.feat-card:last-child{border-right:none;padding-right:0}
.feat-card.vis{opacity:1;transform:translateY(0)}
.feat-card-icon{width:56px;height:56px;border-radius:50%;background:rgba(255,237,215,.08);display:flex;align-items:center;justify-content:center;margin-bottom:20px}
.feat-card-icon svg{width:32px;height:32px;color:var(--cream)}
.feat-card-tag{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--grey);margin-bottom:12px}
.feat-card-desc{font-size:12px;line-height:1.6;color:rgba(255,237,215,.6);margin-bottom:20px}
.feat-card-dash{width:100%;height:1px;background:var(--shadow);margin:16px 0}
.feat-card-title{font-size:18px;font-weight:500;line-height:1.2}

/* ── COASTER FLOAT SECTION ───────────────── */
#coaster-section{min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.coaster-wrap{position:relative;width:min(500px,70vw);aspect-ratio:1;perspective:1000px}
#float-coaster{width:100%;height:100%;transform-style:preserve-3d;transition:transform .1s linear;will-change:transform}
#float-coaster img{width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 40px 100px rgba(220,80,0,.18))}
.coaster-orbit{position:absolute;inset:-20%;border-radius:50%;border:1px solid rgba(255,237,215,.04);animation:orb 24s linear infinite}
.coaster-orbit.o2{inset:-38%;animation-duration:36s;animation-direction:reverse;border-color:rgba(64,55,46,.35)}
@keyframes orb{to{transform:rotate(360deg)}}
.coaster-label{position:absolute;bottom:-60px;left:50%;transform:translateX(-50%);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--grey);white-space:nowrap}
.coaster-scroll-text{position:absolute;top:50%;right:-140px;transform:rotate(90deg) translateX(-50%);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,237,215,.3);white-space:nowrap}

/* ── ENCRYPTION SECTION ──────────────────── */
#encryption{min-height:70vh;display:flex;align-items:center}
.enc-inner{width:100%;padding:100px 48px;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.enc-header{}
.enc-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:20px}
.enc-h2{font-size:clamp(32px,4.5vw,58px);font-weight:500;line-height:.95;margin-bottom:20px}
.enc-h2 .w{display:block;overflow:hidden}
.enc-h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.enc-h2.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.05s}
.enc-h2.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.18s}
.enc-desc{font-size:14px;line-height:1.7;color:var(--grey)}
.enc-right{display:flex;flex-direction:column;gap:24px;opacity:0;transform:translateX(24px);transition:opacity .8s ease,transform .8s ease}
.enc-right.vis{opacity:1;transform:translateX(0)}
.enc-field{position:relative;border-bottom:1px solid rgba(255,237,215,.3)}
.enc-field input{width:100%;background:transparent;border:none;outline:none;font-family:var(--f);font-size:32px;font-weight:500;color:var(--cream);padding:12px 0;letter-spacing:.06em}
.enc-field-lines{position:absolute;inset:0;pointer-events:none;display:grid;grid-template-rows:repeat(4,1fr)}
.enc-field-lines span{border-bottom:1px solid rgba(255,237,215,.06)}
.enc-btn{display:flex;align-items:center;justify-content:center;background:var(--sienna);color:var(--cream);border:none;border-radius:30px;padding:14px 32px;font-size:13px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;transition:opacity .3s,transform .2s;overflow:hidden;position:relative}
.enc-btn:hover{opacity:.85;transform:translateY(-2px)}
.enc-btn .flip-wrap{display:flex;flex-direction:column;height:1.2em;overflow:hidden;transition:transform .35s cubic-bezier(.77,0,.18,1)}
.enc-btn.flipped .flip-wrap{transform:translateY(-50%)}
.enc-btn .flip-wrap span{display:block;line-height:1.2}

/* ── SUSTAINABILITY ───────────────────────── */
#sustain{min-height:100vh;display:flex;align-items:center}
.sust-inner{width:100%;padding:100px 48px}
.sust-hero{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:end;margin-bottom:80px}
.sust-left{}
.sust-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:24px}
.sust-pre{font-size:18px;font-weight:500;color:rgba(255,237,215,.5);margin-bottom:4px;overflow:hidden}
.sust-pre .wi{display:block;transform:translateY(105%);transition:transform .7s ease}
.sust-pre.revealed .wi{transform:translateY(0)}
.sust-h2{font-size:clamp(40px,6vw,80px);font-weight:500;line-height:.9}
.sust-h2 .w{display:block;overflow:hidden}
.sust-h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.sust-h2.revealed .w .wi{transform:translateY(0)}
.sust-h2.revealed .w:nth-child(1) .wi{transition-delay:.05s}
.sust-h2.revealed .w:nth-child(2) .wi{transition-delay:.16s}
.sust-desc{font-size:14px;line-height:1.7;color:var(--grey)}
.sust-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px dashed var(--shadow)}
.sust-item{padding:40px 32px;border-right:1px dashed var(--shadow);opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease}
.sust-item:first-child{padding-left:0}
.sust-item:last-child{border-right:none;padding-right:0}
.sust-item.vis{opacity:1;transform:translateY(0)}
.sust-num{font-size:72px;font-weight:500;line-height:1;color:var(--cream);margin-bottom:12px}
.sust-item-title{font-size:16px;font-weight:500;line-height:1.2;margin-bottom:16px}
.sust-item-desc{font-size:12px;line-height:1.6;color:var(--grey)}

/* ── TESTIMONIALS ────────────────────────── */
#testimonies{min-height:100vh;padding:100px 48px}
.test-hero{margin-bottom:60px}
.test-h2{font-size:clamp(28px,4vw,52px);font-weight:500;line-height:1.05;max-width:600px;margin-bottom:20px;overflow:hidden}
.test-h2 .w{display:block;overflow:hidden}
.test-h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.test-h2.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.05s}
.test-h2.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.15s}
.test-h2.revealed .w:nth-child(3) .wi{transform:translateY(0);transition-delay:.24s}
.test-desc{font-size:15px;color:var(--grey);line-height:1.6}
.test-table{}
.test-header{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;padding:16px 0;border-top:1px dashed var(--shadow);border-bottom:1px dashed var(--shadow);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--grey);margin-bottom:0}
.test-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;padding:28px 0;border-bottom:1px dashed var(--shadow);align-items:center;opacity:0;transform:translateY(16px);transition:opacity .6s ease,transform .6s ease}
.test-row.vis{opacity:1;transform:translateY(0)}
.test-stars{display:flex;gap:4px;margin-bottom:8px}
.star{width:12px;height:12px;background:var(--cream);clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)}
.star.half{opacity:.4}
.test-quote{font-size:15px;line-height:1.5;font-style:italic}
.test-quote strong{color:var(--cream);font-style:normal}
.test-author-name{font-size:12px;font-weight:500;margin-top:8px}
.test-author-role{font-size:11px;color:var(--grey)}
.test-rating{font-size:11px;color:var(--grey);letter-spacing:.1em}
.test-img-wrap{width:80px;height:80px;border-radius:8px;overflow:hidden;border:1px solid rgba(255,237,215,.1)}
.test-img-wrap img{width:100%;height:100%;object-fit:cover;filter:brightness(.7) saturate(.6)}

/* ── CTA / FOOTER ────────────────────────── */
#cta-section{min-height:60vh;display:flex;align-items:center;justify-content:center;padding:80px 48px;text-align:center;flex-direction:column;gap:32px;border-top:1px dashed var(--shadow)}
.cta-tag{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--grey)}
.cta-h2{font-size:clamp(40px,7vw,96px);font-weight:500;line-height:.9}
.cta-h2 .w{display:block;overflow:hidden}
.cta-h2 .w .wi{display:block;transform:translateY(105%);transition:transform .8s cubic-bezier(.16,1,.3,1)}
.cta-h2.revealed .w:nth-child(1) .wi{transform:translateY(0);transition-delay:.05s}
.cta-h2.revealed .w:nth-child(2) .wi{transform:translateY(0);transition-delay:.18s}
.cta-h2.revealed .w:nth-child(3) .wi{transform:translateY(0);transition-delay:.30s}
.cta-buttons{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.btn-fill{background:var(--cork);color:var(--cream);border:none;border-radius:36px;padding:14px 32px;font-size:14px;font-weight:400;letter-spacing:.06em;transition:opacity .3s,transform .2s}
.btn-fill:hover{opacity:.8;transform:translateY(-2px)}
.btn-out{background:transparent;color:var(--cream);border:1px solid rgba(255,237,215,.4);border-radius:22.5px;padding:10px 24px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;transition:border-color .3s,color .3s}
.btn-out:hover{border-color:var(--sienna);color:var(--sienna)}

footer{padding:40px 48px 32px;border-top:1px dashed var(--shadow)}
.foot-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.foot-logo{font-size:22px;font-weight:500;letter-spacing:.04em}
.foot-links{display:flex;gap:24px;list-style:none}
.foot-links a{font-size:10px;color:var(--grey);letter-spacing:.12em;text-transform:uppercase;transition:color .3s}
.foot-links a:hover{color:var(--cream)}
.foot-bot{display:flex;justify-content:space-between;align-items:center;padding-top:20px;border-top:1px dashed var(--shadow)}
.foot-copy,.foot-model{font-size:10px;color:var(--grey);letter-spacing:.08em}
.foot-model em{color:var(--sienna);font-style:normal}

/* ── MARQUEE STRIP ───────────────────────── */
.marquee{overflow:hidden;padding:24px 0;border-top:1px dashed var(--shadow);border-bottom:1px dashed var(--shadow)}
.marquee-track{display:flex;gap:60px;width:max-content;animation:mq 20s linear infinite}
.marquee-track:hover{animation-play-state:paused}
.mi{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--grey);white-space:nowrap;display:flex;align-items:center;gap:28px}
.mi::after{content:'·';color:var(--sienna);font-size:16px}
@keyframes mq{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ── SCROLL ANIMATIONS ───────────────────── */
.sr{opacity:0;transform:translateY(28px);transition:opacity .8s ease,transform .8s ease}
.sr.vis{opacity:1;transform:translateY(0)}
.sr-l{opacity:0;transform:translateX(-28px);transition:opacity .75s ease,transform .75s ease}
.sr-l.vis{opacity:1;transform:translateX(0)}

/* ── PROGRESS BAR ────────────────────────── */
#progress{position:fixed;top:0;left:0;height:2px;background:var(--sienna);z-index:1000;width:0%;transition:width .1s linear}

/* RESPONSIVE */
@media(max-width:900px){
  #nav{padding:18px 24px}
  #hero{padding:80px 24px 40px}
  .hero-bottom,.ai-inner,.feat-header,.enc-inner,.sust-hero,.sust-grid,.feat-cards,.test-header,.test-row{grid-template-columns:1fr}
  .sec-inner,.feat-inner,.enc-inner > *,.sust-inner,.sust-inner > *{padding-left:24px;padding-right:24px}
  .container{padding:0 24px}
  #cta-section,#testimonies,#sustain,#encryption,#features{padding:60px 24px}
  .sust-item,.feat-card{padding-left:0;padding-right:0}
  #vid-thumb{bottom:24px;right:24px;width:120px;height:76px}
  .coaster-scroll-text{display:none}
}
</style>
</head>
<body>

<!-- CURSOR -->
<div id="dot"></div>
<div id="ring"></div>

<!-- PROGRESS BAR -->
<div id="progress"></div>

<!-- SCROLL PROMPT -->
<div id="scroll-prompt">
  <span class="sp-txt">Scroll</span>
  <div class="sp-arr"><div class="sp-line"></div></div>
</div>

<!-- NAV -->
<nav id="nav">
  <a href="#hero" class="nav-logo">
    <svg viewBox="0 0 809 174" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M87 174C36 174 0 132 0 87C0 42 36 0 87 0C138 0 174 42 174 87C174 132 138 174 87 174ZM87 135C112 135 135 115 135 87C135 59 112 39 87 39C62 39 39 59 39 87C39 115 62 135 87 135Z" fill="currentColor"/>
      <path d="M196 170V4H263C307 4 327 28 327 61C327 84 317 103 296 112L333 170H284L255 118H237V170H196ZM237 80H264C280 80 285 72 285 61C285 50 280 42 264 42H237V80Z" fill="currentColor"/>
      <path d="M385 170V101L325 4H373L406 62L439 4H487L427 100V170H385Z" fill="currentColor"/>
      <path d="M490 170V133L568 42H494V4H620V41L543 132H622V170H490Z" fill="currentColor"/>
      <path d="M722 174C671 174 635 132 635 87C635 42 671 0 722 0C773 0 809 42 809 87C809 132 773 174 722 174ZM722 135C747 135 770 115 770 87C770 59 747 39 722 39C697 39 674 59 674 87C674 115 697 135 722 135Z" fill="currentColor"/>
    </svg>
  </a>
  <div class="nav-r">
    <a href="#ai" class="nav-link"><span>AI</span><span class="clone">AI</span></a>
    <a href="#features" class="nav-link"><span>Features</span><span class="clone">Features</span></a>
    <a href="#sustain" class="nav-link"><span>Sustainability</span><span class="clone">Sustainability</span></a>
    <button class="btn-nav">Order Now</button>
  </div>
</nav>

<!-- ═══════════════ HERO ═══════════════ -->
<section id="hero">
  <!-- Canvas for 3D coaster (CSS-driven) -->
  <div id="coaster-scene">
    <div id="coaster-canvas-wrap">
      <div id="scene-coaster"></div>
    </div>
  </div>

  <div class="hero-tagline" id="hero-tag">
    <span class="char">M</span><span class="char">a</span><span class="char">d</span><span class="char">e</span>
    <span class="char">&nbsp;</span>
    <span class="char">f</span><span class="char">o</span><span class="char">r</span>
    <span class="char">&nbsp;</span>
    <span class="char">m</span><span class="char">u</span><span class="char">g</span><span class="char">s</span><span class="char">.</span>
    <span class="char">&nbsp;</span>
    <span class="char">B</span><span class="char">u</span><span class="char">i</span><span class="char">l</span><span class="char">t</span>
    <span class="char">&nbsp;</span>
    <span class="char">f</span><span class="char">o</span><span class="char">r</span>
    <span class="char">&nbsp;</span>
    <span class="char">t</span><span class="char">a</span><span class="char">b</span><span class="char">l</span><span class="char">e</span><span class="char">s</span><span class="char">.</span>
  </div>

  <!-- Big logo in center -->
  <div id="hero-logo-area">
    <svg id="hero-logo-svg" viewBox="0 0 809 174" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M87 174C36 174 0 132 0 87C0 42 36 0 87 0C138 0 174 42 174 87C174 132 138 174 87 174ZM87 135C112 135 135 115 135 87C135 59 112 39 87 39C62 39 39 59 39 87C39 115 62 135 87 135Z" fill="currentColor"/>
      <path d="M196 170V4H263C307 4 327 28 327 61C327 84 317 103 296 112L333 170H284L255 118H237V170H196ZM237 80H264C280 80 285 72 285 61C285 50 280 42 264 42H237V80Z" fill="currentColor"/>
      <path d="M385 170V101L325 4H373L406 62L439 4H487L427 100V170H385Z" fill="currentColor"/>
      <path d="M490 170V133L568 42H494V4H620V41L543 132H622V170H490Z" fill="currentColor"/>
      <path d="M722 174C671 174 635 132 635 87C635 42 671 0 722 0C773 0 809 42 809 87C809 132 773 174 722 174ZM722 135C747 135 770 115 770 87C770 59 747 39 722 39C697 39 674 59 674 87C674 115 697 135 722 135Z" fill="currentColor"/>
    </svg>
  </div>

  <div class="hero-bottom">
    <p class="hero-copy" id="hero-copy">
      <span class="line"><span class="li">Designed to lift, insulate, and grip in all</span></span>
      <span class="line"><span class="li">the right ways. Oryzo makes the simplest</span></span>
      <span class="line"><span class="li">moment feel considered.</span></span>
    </p>
    <div class="hero-card" id="hero-card">
      <h4>Designed<br>by Lusion,<br>the award-winning<br>design studio.</h4>
      <div class="hero-card-dash"></div>
      <div class="hero-card-desc">
        <span>The world's most</span>
        <span>unnecessarily</span>
        <span>sophisticated cork coaster.</span>
      </div>
    </div>
  </div>

  <!-- Video thumbnail -->
  <div id="vid-thumb">
    <img src="coaster1.png" alt="ORYZO product"/>
    <div id="vid-play"></div>
    <span class="vid-lbl">PLAY</span>
  </div>
</section>

<!-- ═══════════════ COASTER 3D INTERACTIVE ═════════════ -->
<section id="coaster-section">
  <div class="coaster-wrap" id="coaster-tilt-wrap">
    <div class="coaster-orbit"></div>
    <div class="coaster-orbit o2"></div>
    <div id="float-coaster">
      <img src="coaster2.png" alt="ORYZO coaster 3D view"/>
    </div>
    <div class="coaster-label">ORYZO&#8209;1 · Hover to rotate</div>
    <div class="coaster-scroll-text">SCROLL TO EXPLORE MODEL</div>
  </div>
</section>

<hr class="dash"/>

<!-- ═══════════════ MARQUEE ═══════════════ -->
<div class="marquee">
  <div class="marquee-track">
    <span class="mi">Made for mugs</span><span class="mi">Built for tables</span>
    <span class="mi">Cork intelligence</span><span class="mi">Unnecessarily sophisticated</span>
    <span class="mi">Award winning</span><span class="mi">Designed by Lusion</span>
    <span class="mi">Thermodynamic stability</span><span class="mi">Zero drama</span>
    <span class="mi">Made for mugs</span><span class="mi">Built for tables</span>
    <span class="mi">Cork intelligence</span><span class="mi">Unnecessarily sophisticated</span>
    <span class="mi">Award winning</span><span class="mi">Designed by Lusion</span>
    <span class="mi">Thermodynamic stability</span><span class="mi">Zero drama</span>
  </div>
</div>

<!-- ═══════════════ AI SECTION ═══════════════ -->
<section id="ai">
  <div class="ai-inner">
    <div class="ai-pre">
      <h2 id="ai-pre-h2">
        <span class="w"><span class="wi">isn't just</span></span>
        <span class="w"><span class="wi">a coaster.</span></span>
      </h2>
      <div class="body" id="ai-pre-body">
        <span>Oryzo isn't just a </span>
        <span>coaster. It's the result </span>
        <span>of unprecedented AI* </span>
        <span>breakthroughs.</span>
      </div>
    </div>
    <div class="ai-right">
      <div class="ai-title-block">
        <div id="ai-title">
          <span class="w"><span class="wi">Powered</span></span>
          <span class="w"><span class="wi">by AI<sup style="font-size:.5em;color:var(--sienna)">*</sup></span></span>
        </div>
        <div class="ai-tag" id="ai-tag">Oryzo&#8209;1</div>
      </div>
      <div class="ai-desc" id="ai-desc">
        <span><span class="wi">AI fills in the gaps.</span></span>
        <span><span class="wi">We said high five.</span></span>
        <span><span class="wi">It heard six.</span></span>
      </div>
      <div class="ai-disclaimer sr">
        <div class="ai-disc-line"></div>
        <div class="ai-disc-txt" id="ai-disc">
          <span class="wi">* Adobe Illustrator</span>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="dash"/>

<!-- ═══════════════ FEATURES ═══════════════ -->
<section id="features">
  <div class="feat-inner">
    <div class="feat-header">
      <div class="feat-header-left">
        <div class="sub" id="feat-sub"><span class="wi">— What it does</span></div>
        <h2 class="feat-h2" id="feat-h2">
          <span class="w"><span class="wi">Elevate</span></span>
          <span class="w"><span class="wi">everything.</span></span>
          <span class="w"><span class="wi">Literally.</span></span>
        </h2>
      </div>
      <div class="feat-header-right">
        <p class="feat-body sr">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable while your coffee table already tapped out three sips ago. Precision engineered for the unnecessarily sophisticated.</p>
      </div>
    </div>
    <div class="feat-cards">
      <div class="feat-card" data-fc>
        <div class="feat-card-icon">
          <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width=".8" opacity=".3"/><path d="M16 8l5 6h-3v8h-4v-8H11z" fill="currentColor"/><path stroke="currentColor" stroke-width=".8" d="M12 23h8M12 25h8M12 27h8" opacity=".6"/></svg>
        </div>
        <div class="feat-card-tag">Rise above mediocrity</div>
        <div class="feat-card-desc">With a precision-engineered lift (exactly one coaster thick), Oryzo doesn't just hold your mug — it elevates it. Literally. Above every boring surface you've ever known.</div>
        <div class="feat-card-dash"></div>
        <div class="feat-card-title">Elevate your coffee experience</div>
      </div>
      <div class="feat-card" data-fc>
        <div class="feat-card-icon">
          <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width=".8" opacity=".3"/><path d="M13 10a3 3 0 016 0v12a3 3 0 01-6 0V10z" stroke="currentColor" stroke-width=".8" fill="none"/><path d="M13 20h6" stroke="currentColor" stroke-width=".8"/></svg>
        </div>
        <div class="feat-card-tag">Handles Extremes with Ease</div>
        <div class="feat-card-desc">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable. Your coffee table already tapped out three sips ago.</div>
        <div class="feat-card-dash"></div>
        <div class="feat-card-title">Thermodynamic stability</div>
      </div>
      <div class="feat-card" data-fc>
        <div class="feat-card-icon">
          <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="currentColor" stroke-width=".8" opacity=".3"/><circle cx="16" cy="16" r="8" stroke="currentColor" stroke-width=".8"/><circle cx="16" cy="16" r="2" fill="currentColor"/><path d="M16 8v2M16 22v2M8 16h2M22 16h2" stroke="currentColor" stroke-width=".8"/></svg>
        </div>
        <div class="feat-card-tag">Perfectly Round, Seriously</div>
        <div class="feat-card-desc">Our engineers recalibrated its circumference with disturbing levels of attention to detail — just because we could.</div>
        <div class="feat-card-dash"></div>
        <div class="feat-card-title">Now 37.9% More Circular</div>
      </div>
    </div>
  </div>
</section>

<hr class="dash"/>

<!-- ═══════════════ ENCRYPTION ═══════════════ -->
<section id="encryption">
  <div class="enc-inner">
    <div class="enc-header sr-l">
      <div class="enc-tag">Secure communications simplified</div>
      <h2 class="enc-h2" id="enc-h2">
        <span class="w"><span class="wi">Smart flip</span></span>
        <span class="w"><span class="wi">encryption</span></span>
      </h2>
      <p class="enc-desc">Write a message. Flip. Instantly secure — until someone flips it back. Genius.</p>
    </div>
    <div class="enc-right" id="enc-right">
      <div class="enc-field">
        <div class="enc-field-lines"><span></span><span></span><span></span><span></span></div>
        <input type="text" id="enc-input" value="ORYZO" maxlength="10" autocomplete="off"/>
      </div>
      <button class="enc-btn" id="enc-btn">
        <span class="flip-wrap" id="enc-flip">
          <span>Encode Message</span>
          <span>Decode Message</span>
        </span>
      </button>
    </div>
  </div>
</section>

<hr class="dash"/>

<!-- ═══════════════ SUSTAINABILITY ═══════════════ -->
<section id="sustain">
  <div class="sust-inner">
    <div class="sust-hero">
      <div class="sust-left">
        <div class="sust-tag sr">100% Plant-based</div>
        <div class="sust-pre" id="sust-pre"><span class="wi">Vegan-friendly</span></div>
        <h2 class="sust-h2" id="sust-h2">
          <span class="w"><span class="wi">sustainability</span></span>
        </h2>
      </div>
      <div class="sust-desc sr" style="transition-delay:.2s">Pure cork sourced sustainably. Completely vegan — no cows were harmed, but it might be full of "bull"sh*t.</div>
    </div>
    <div class="sust-grid">
      <div class="sust-item" data-si>
        <div class="sust-num">25</div>
        <div class="sust-item-title">Average age of first harvest</div>
        <div class="sust-item-desc">Cork oaks are typically first harvested at around 25 years, once the bark is thick enough to remove safely.</div>
      </div>
      <div class="sust-item" data-si>
        <div class="sust-num">9</div>
        <div class="sust-item-title">Harvesting interval (years)</div>
        <div class="sust-item-desc">After each harvest, the bark takes about 9 years to regrow, making cork a renewable material.</div>
      </div>
      <div class="sust-item" data-si>
        <div class="sust-num">0W</div>
        <div class="sust-item-title">Power draw while in use</div>
        <div class="sust-item-desc">No compute. No tokens. So you can say "please" and "thank you" as much as you want, guilt free.</div>
      </div>
    </div>
  </div>
</section>

<hr class="dash"/>

<!-- ═══════════════ TESTIMONIALS ═══════════════ -->
<section id="testimonies">
  <div class="test-hero">
    <h2 class="test-h2" id="test-h2">
      <span class="w"><span class="wi">People all around</span></span>
      <span class="w"><span class="wi">the world love</span></span>
      <span class="w"><span class="wi">Oryzo</span></span>
    </h2>
    <p class="test-desc sr">Do not take our word for it, see what people say after living with Oryzo.</p>
  </div>
  <div class="test-table">
    <div class="test-header">
      <div>Rating &amp; Reviews</div>
      <div>Custom reviews [ 364 ] &nbsp;★ 4.9/5</div>
      <div>ORYZO in use</div>
    </div>
    <div class="test-row" data-tr>
      <div>
        <div class="test-stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div>
        <div class="test-quote">"This is the <strong>best coaster</strong> that I've ever used. I can't go to space without it"</div>
        <div class="test-author-name">Edan K.</div>
        <div class="test-author-role">NASA astronaut wannabe</div>
      </div>
      <div class="test-rating">[ 5/5 ]</div>
      <div class="test-img-wrap"><img src="coaster2.png" alt=""/></div>
    </div>
    <div class="test-row" data-tr>
      <div>
        <div class="test-stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star half"></div></div>
        <div class="test-quote">"My coaster? If you want it, I'll let you have it. Look for it — I left everything in <strong>one place!</strong>"</div>
        <div class="test-author-name">Gol D. Roger</div>
        <div class="test-author-role">Old-school Pirate</div>
      </div>
      <div class="test-rating">[ 4.5/5 ]</div>
      <div class="test-img-wrap"><img src="coaster1.png" alt=""/></div>
    </div>
    <div class="test-row" data-tr>
      <div>
        <div class="test-stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div>
        <div class="test-quote">"<strong>We are so cooked.</strong> Hollywood is not ready for a coaster this cinematic."</div>
        <div class="test-author-name">Jamie R.</div>
        <div class="test-author-role">AI influencer, Ex-Web3 influencer</div>
      </div>
      <div class="test-rating">[ 5/5 ]</div>
      <div class="test-img-wrap"><img src="coaster2.png" alt=""/></div>
    </div>
    <div class="test-row" data-tr>
      <div>
        <div class="test-stars"><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div><div class="star"></div></div>
        <div class="test-quote">"My table hasn't been this protected since I stopped trusting <strong>gravity</strong>."</div>
        <div class="test-author-name">Priya K.</div>
        <div class="test-author-role">Flat Earth believer</div>
      </div>
      <div class="test-rating">[ 5/5 ]</div>
      <div class="test-img-wrap"><img src="coaster1.png" alt=""/></div>
    </div>
  </div>
</section>

<!-- ═══════════════ CTA ═══════════════ -->
<section id="cta-section">
  <div class="cta-tag sr">Ready to elevate?</div>
  <h2 class="cta-h2" id="cta-h2">
    <span class="w"><span class="wi">Order</span></span>
    <span class="w"><span class="wi">yours</span></span>
    <span class="w"><span class="wi">today.</span></span>
  </h2>
  <div class="cta-buttons sr" style="transition-delay:.4s">
    <button class="btn-fill">Get ORYZO&#8209;1</button>
    <button class="btn-out">Learn more</button>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="foot-top">
    <div class="foot-logo">ORYZO</div>
    <ul class="foot-links">
      <li><a href="#ai">AI</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#sustain">Sustainability</a></li>
      <li><a href="#testimonies">Reviews</a></li>
      <li><a href="#">Privacy</a></li>
    </ul>
  </div>
  <div class="foot-bot">
    <span class="foot-copy">&copy; 2026 ORYZO AI. Designed by Lusion. All rights reserved.</span>
    <span class="foot-model">Powered by <em>ORYZO&#8209;1</em></span>
  </div>
</footer>

<script>
/* ═══════════════════════════════════════════
   CURSOR
═══════════════════════════════════════════ */
const dot=document.getElementById('dot'),ring=document.getElementById('ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{
  mx=e.clientX;my=e.clientY;
  dot.style.left=mx+'px';dot.style.top=my+'px';
},{passive:true});
(function loop(){rx+=(mx-rx)*.1;ry+=(my-ry)*.1;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(loop)})();
document.querySelectorAll('a,button,input').forEach(el=>{
  el.addEventListener('mouseenter',()=>document.body.classList.add('hov'));
  el.addEventListener('mouseleave',()=>document.body.classList.remove('hov'));
});

/* ═══════════════════════════════════════════
   SCROLL PROGRESS + NAV
═══════════════════════════════════════════ */
const nav=document.getElementById('nav');
const prompt=document.getElementById('scroll-prompt');
const prog=document.getElementById('progress');
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const tot=document.body.scrollHeight-window.innerHeight;
  prog.style.width=(sy/tot*100)+'%';
  nav.classList.toggle('on',sy>60);
  prompt.classList.toggle('gone',sy>window.innerHeight*.5);
},{passive:true});

/* ═══════════════════════════════════════════
   HERO ANIMATIONS — on load
═══════════════════════════════════════════ */
window.addEventListener('DOMContentLoaded',()=>{
  // Tagline chars stagger
  const chars=document.querySelectorAll('#hero-tag .char');
  chars.forEach((c,i)=>{
    setTimeout(()=>{c.style.opacity='1';c.style.transform='translateY(0)';},200+i*40);
  });
  // Logo fade in
  setTimeout(()=>document.getElementById('hero-logo-svg').classList.add('revealed'),400);
  // Copy lines
  setTimeout(()=>document.getElementById('hero-copy').classList.add('revealed'),500);
  // Card
  setTimeout(()=>document.getElementById('hero-card').classList.add('revealed'),700);
  // Video chip
  setTimeout(()=>document.getElementById('vid-thumb').classList.add('revealed'),900);
});

/* ═══════════════════════════════════════════
   INTERSECTION OBSERVER — word reveals + sr
═══════════════════════════════════════════ */
const ioOpts={threshold:.12};
const io=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(!e.isIntersecting)return;
    e.target.classList.add('vis','revealed');
    io.unobserve(e.target);
  });
},ioOpts);

// word-wrap headlines
['ai-pre-h2','ai-title','ai-desc','ai-disc','feat-sub','feat-h2','enc-h2','sust-pre','sust-h2','test-h2','cta-h2'].forEach(id=>{
  const el=document.getElementById(id);
  if(el)io.observe(el);
});
// ai-pre body, ai-tag
['ai-pre-body','ai-tag'].forEach(id=>{
  const el=document.getElementById(id);
  if(el)io.observe(el);
});
// generic sr/sr-l
document.querySelectorAll('.sr,.sr-l').forEach(el=>io.observe(el));
// enc-right
const encRight=document.getElementById('enc-right');
if(encRight){
  new IntersectionObserver(([e])=>{if(e.isIntersecting){encRight.classList.add('vis');} },{threshold:.15}).observe(encRight);
}

// feature cards stagger
const fcards=document.querySelectorAll('[data-fc]');
const fcIO=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      fcards.forEach((c,i)=>setTimeout(()=>c.classList.add('vis'),i*120));
      fcIO.disconnect();
    }
  });
},{threshold:.12});
if(fcards[0])fcIO.observe(fcards[0]);

// sustain items stagger
const sitems=document.querySelectorAll('[data-si]');
const siIO=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      sitems.forEach((c,i)=>setTimeout(()=>c.classList.add('vis'),i*130));
      siIO.disconnect();
    }
  });
},{threshold:.12});
if(sitems[0])siIO.observe(sitems[0]);

// test rows stagger
const trows=document.querySelectorAll('[data-tr]');
const trIO=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      trows.forEach((r,i)=>setTimeout(()=>r.classList.add('vis'),i*100));
      trIO.disconnect();
    }
  });
},{threshold:.08});
if(trows[0])trIO.observe(trows[0]);

/* ═══════════════════════════════════════════
   3D COASTER TILT  (features-right style)
═══════════════════════════════════════════ */
const tiltWrap=document.getElementById('coaster-tilt-wrap');
const floatC=document.getElementById('float-coaster');
let targetRX=0,targetRY=0,currentRX=0,currentRY=0;
let floatTime=0;
// auto-float animation
function animateCoaster(){
  floatTime+=0.008;
  // gentle float
  const autoY=Math.sin(floatTime)*4;
  const autoX=Math.cos(floatTime*.7)*2;
  // lerp toward target
  currentRX+=(targetRX-currentRX)*.08;
  currentRY+=(targetRY-currentRY)*.08;
  floatC.style.transform=`rotateX(${currentRX+autoX}deg) rotateY(${currentRY+autoY}deg) translateZ(0)`;
  requestAnimationFrame(animateCoaster);
}
animateCoaster();

if(tiltWrap){
  tiltWrap.addEventListener('mousemove',e=>{
    const r=tiltWrap.getBoundingClientRect();
    const dx=(e.clientX-r.left-r.width/2)/(r.width/2);
    const dy=(e.clientY-r.top-r.height/2)/(r.height/2);
    targetRY=dx*28;targetRX=-dy*28;
  });
  tiltWrap.addEventListener('mouseleave',()=>{targetRX=0;targetRY=0;});
}

/* ═══════════════════════════════════════════
   SCROLL-DRIVEN COASTER ROTATION (hero area)
═══════════════════════════════════════════ */
// We use a CSS animated coaster in the hero bg
// using scroll-driven transform on product images
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const vh=window.innerHeight;
  // Rotate float coaster based on scroll (in features section)
  const cs=document.getElementById('coaster-section');
  if(cs){
    const r=cs.getBoundingClientRect();
    const p=-r.top/r.height;
    if(p>-0.5&&p<1.5){
      // extra rotation from scroll
      targetRY+=0.3;
    }
  }
},{passive:true});

/* ═══════════════════════════════════════════
   ENCRYPTION FLIP
═══════════════════════════════════════════ */
const encInput=document.getElementById('enc-input');
const encBtn=document.getElementById('enc-btn');
const encFlip=document.getElementById('enc-flip');
let encoded=false;
function rotateText(str){
  return str.split('').map(c=>{
    if(c>='A'&&c<='Z')return String.fromCharCode((c.charCodeAt(0)-65+13)%26+65);
    if(c>='a'&&c<='z')return String.fromCharCode((c.charCodeAt(0)-97+13)%26+97);
    return c;
  }).join('');
}
if(encBtn){
  encBtn.addEventListener('click',()=>{
    encoded=!encoded;
    encFlip.style.transform=encoded?'translateY(-50%)':'translateY(0)';
    // animate the text scramble
    const orig=encInput.value;
    const target=rotateText(orig);
    let frame=0;
    const chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const interval=setInterval(()=>{
      frame++;
      if(frame>12){clearInterval(interval);encInput.value=target;return;}
      encInput.value=orig.split('').map((c,i)=>{
        if(i<frame/12*orig.length)return target[i];
        return chars[Math.floor(Math.random()*chars.length)];
      }).join('');
    },40);
  });
}

/* ═══════════════════════════════════════════
   SMOOTH SCROLL PARALLAX — hero logo scale
═══════════════════════════════════════════ */
const heroLogoSvg=document.getElementById('hero-logo-svg');
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const vh=window.innerHeight;
  if(sy<vh){
    const p=sy/vh;
    if(heroLogoSvg){
      heroLogoSvg.style.transform=`scale(${1+p*.06}) translateY(${p*-30}px)`;
      heroLogoSvg.style.opacity=`${1-p*.8}`;
    }
    // hero tagline parallax
    const tag=document.getElementById('hero-tag');
    if(tag) tag.style.transform=`translateY(${p*-20}px)`;
    // hero copy
    const cp=document.getElementById('hero-copy');
    if(cp) cp.style.transform=`translateY(${p*-15}px)`;
  }
},{passive:true});
</script>
</body>
</html>"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("Written:",len(html),"bytes")
