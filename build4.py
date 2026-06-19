
html = r"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<title>ORYZO AI</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="description" content="A physical product, reimagined for the AI era, proving even the smallest idea can feel extraordinary.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --black:#100904;
  --cream:#ffedd7;
  --shadow:#40372e;
  --cork-dark:#382416;
  --sienna:#dc5000;
  --grey:#6c5f51;
  --font-display:'Syne',system-ui,sans-serif;
  --font-body:'DM Sans',system-ui,sans-serif;
}

html{scroll-behavior:auto;overflow-x:hidden}
body{
  background:var(--black);
  color:var(--cream);
  font-family:var(--font-body);
  font-size:14px;
  line-height:1.4;
  overflow-x:hidden;
  cursor:none;
}
img,canvas,svg{display:block}
a{color:inherit;text-decoration:none}
button{cursor:none;font-family:inherit}
sup{font-size:.55em;vertical-align:super;color:var(--sienna)}

/* ─── CURSOR ─────────────────────── */
#cursor-dot{
  position:fixed;width:8px;height:8px;background:var(--cream);border-radius:50%;
  pointer-events:none;z-index:9999;transform:translate(-50%,-50%);
  mix-blend-mode:difference;transition:width .15s,height .15s;will-change:transform;
}
#cursor-ring{
  position:fixed;width:40px;height:40px;border:1px solid rgba(255,237,215,.38);
  border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);
  transition:border-color .25s,width .2s,height .2s;will-change:transform;
}
body.hovered #cursor-dot{width:16px;height:16px}
body.hovered #cursor-ring{width:56px;height:56px;border-color:rgba(220,80,0,.5)}

/* ─── PROGRESS ───────────────────── */
#progress-bar{
  position:fixed;top:0;left:0;height:2px;background:var(--sienna);
  z-index:3000;width:0%;transition:width .08s linear;pointer-events:none;
}

/* ─── THREE.JS CANVAS ────────────── */
#canvas{
  position:fixed;top:0;left:0;width:100%;height:100%;
  z-index:1;pointer-events:none;
}

/* ─── UI LAYER ───────────────────── */
#ui{position:relative;z-index:2}

/* ─── NAV ────────────────────────── */
#nav{
  position:fixed;top:0;left:0;right:0;z-index:500;
  display:flex;align-items:center;justify-content:space-between;
  padding:22px 56px;
  border-bottom:1px solid transparent;
  transition:background .4s ease,border-color .4s ease;
}
#nav.scrolled{
  background:rgba(16,9,4,.96);
  border-color:var(--shadow);
  backdrop-filter:blur(8px);
}
.nav-logo svg{width:90px;height:20px;color:var(--cream)}
.nav-links{display:flex;align-items:center;gap:32px}
.nav-link{
  font-size:10px;letter-spacing:.16em;text-transform:uppercase;
  position:relative;overflow:hidden;display:block;line-height:1.1;
  color:rgba(255,237,215,.65);
}
.nav-link .t1{display:block;transition:transform .3s cubic-bezier(.77,0,.18,1)}
.nav-link .t2{
  position:absolute;top:100%;left:0;
  color:var(--sienna);display:block;
  transition:transform .3s cubic-bezier(.77,0,.18,1);
}
.nav-link:hover .t1{transform:translateY(-100%)}
.nav-link:hover .t2{transform:translateY(-100%)}
.nav-btn{
  font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--cream);background:transparent;
  border:1px solid rgba(255,237,215,.45);
  border-radius:28px;padding:9px 22px;
  transition:border-color .3s,color .3s;
}
.nav-btn:hover{border-color:var(--sienna);color:var(--sienna)}

/* ─── SCROLL INDICATOR ───────────── */
#scroll-ind{
  position:fixed;bottom:36px;left:50%;transform:translateX(-50%);
  z-index:300;display:flex;flex-direction:column;align-items:center;gap:10px;
  pointer-events:none;transition:opacity .4s;
}
#scroll-ind.hidden{opacity:0}
.si-text{font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,237,215,.45)}
.si-line{width:1px;height:44px;overflow:hidden;position:relative;background:transparent}
.si-line::after{
  content:'';position:absolute;top:0;left:0;right:0;bottom:0;
  background:linear-gradient(to bottom,transparent 0%,var(--cream) 100%);
  animation:linefall 1.9s cubic-bezier(.4,0,.2,1) infinite;
}
@keyframes linefall{
  0%{transform:translateY(-100%);opacity:0}
  30%{opacity:.5}
  100%{transform:translateY(100%);opacity:0}
}

/* ─── SECTIONS ───────────────────── */
.section{background:var(--black);position:relative;z-index:2}
.o-container{padding:0 56px}
.section__inner{padding:100px 56px}
.o-dashline{width:100%;height:1px;background:transparent;border-top:1px dashed var(--shadow)}

/* ─── HERO ───────────────────────── */
#hero{
  height:100vh;display:flex;flex-direction:column;
  justify-content:space-between;
  padding:120px 56px 56px;
  position:relative;z-index:2;
}
/* hero transparent bg — canvas shows through */

/* Sub1 class — small label text */
.sub1{font-size:11px;letter-spacing:.15em;text-transform:uppercase;font-family:var(--font-body)}

/* Hero top tagline — word by word animation */
#hero-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:auto}
#hero-top-tagline{font-family:var(--font-body);font-size:11px;letter-spacing:.15em;text-transform:uppercase;display:flex;flex-wrap:wrap;gap:0.35em}
/* Each word wrapped in overflow clip */
.word-clip{position:relative;display:inline-block;overflow:clip}
.word-clip .word-inner{
  position:relative;display:inline-block;
  transform:translate3d(0px,1em,0px);opacity:0;
  transition:transform .6s cubic-bezier(.16,1,.3,1),opacity .01s ease .6s;
}
.word-clip .word-inner.revealed{
  transform:translate3d(0px,0em,0px);opacity:1;
  transition:transform .6s cubic-bezier(.16,1,.3,1),opacity .01s ease 0s;
}

/* Hero copy — character by character */
#hero-copy{
  font-family:var(--font-body);font-size:16px;line-height:1.6;
  color:rgba(255,237,215,.82);
}
#hero-copy .copy-line{
  display:block;position:relative;overflow:clip;
}
#hero-copy .copy-line .line-inner{
  display:block;
  transform:translate3d(0px,105%,0px);
  transition:transform .75s cubic-bezier(.16,1,.3,1);
}
#hero-copy .copy-line .line-inner.revealed{transform:translate3d(0px,0px,0px)}

/* Hero card */
#hero-card{
  border:1px solid rgba(255,237,215,.12);border-radius:14px;
  padding:28px;background:rgba(16,9,4,.45);backdrop-filter:blur(6px);
  max-width:280px;
  opacity:0;transform:translate3d(8px,0px,0px);
  transition:opacity .8s ease,transform .8s ease;
}
#hero-card.revealed{opacity:1;transform:translate3d(0px,0px,0px)}
#hero-card-header{
  font-family:var(--font-display);font-size:20px;font-weight:700;line-height:1.15;
  margin-bottom:0;
}
#hero-card-header .line-wrap{display:block;overflow:clip}
#hero-card-header .line-wrap .li{
  display:block;transform:translate3d(0px,1em,0px);
  transition:transform .7s cubic-bezier(.16,1,.3,1);
}
#hero-card-header .line-wrap .li.revealed{transform:translate3d(0px,0px,0px)}
.card-dash{width:0%;height:1px;background:rgba(255,237,215,.15);margin:18px 0;transition:width 1s ease .9s}
.card-dash.revealed{width:100%}
#hero-card-desc{font-size:12px;color:var(--grey);line-height:1.65}
#hero-card-desc span{display:block}

/* Hero video chip */
#hero-video-wrapper{
  position:absolute;bottom:56px;right:56px;
  width:160px;
  opacity:0;transform:translate3d(8px,0px,0px);
  transition:opacity .6s ease 1.1s,transform .6s ease 1.1s,box-shadow .3s;
  border-radius:14px;overflow:hidden;
  border:1px solid rgba(255,237,215,.18);
}
#hero-video-wrapper.revealed{opacity:1;transform:translate3d(0px,0px,0px)}
#hero-video-wrapper:hover{box-shadow:0 0 30px rgba(220,80,0,.15)}
.hero-video__glow{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(circle at 50% 100%,rgba(220,80,0,.15),transparent 70%);
}
.hero-video__border{
  position:absolute;inset:0;z-index:2;pointer-events:none;
  border-radius:14px;border:1px solid rgba(255,237,215,.18);
}
#hero-video-thumbnail-wrapper{width:100%;aspect-ratio:16/9;overflow:hidden}
#hero-video-thumbnail{width:100%;height:100%;object-fit:cover;filter:brightness(.55)}
#hero-video-play{
  position:absolute;bottom:10px;left:14px;z-index:3;
  font-size:9px;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(255,237,215,.8);
}

/* ─── MARQUEE ────────────────────── */
#marquee{
  overflow:hidden;
  border-top:1px dashed var(--shadow);
  border-bottom:1px dashed var(--shadow);
  padding:20px 0;
  background:var(--black);
  position:relative;z-index:2;
}
.marquee-track{
  display:flex;gap:0;width:max-content;
  animation:marquee 24s linear infinite;
}
.marquee-track:hover{animation-play-state:paused}
.marquee-item{
  font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--grey);white-space:nowrap;
  display:inline-flex;align-items:center;
  padding:0 28px;
}
.marquee-item::after{content:'·';color:var(--sienna);font-size:16px;margin-left:28px}
@keyframes marquee{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ─── COMMON TEXT ANIMATIONS ─────── */
/* For wipe-up line reveals triggered by IntersectionObserver */
.reveal-line{display:block;overflow:clip}
.reveal-line .rl-inner{
  display:block;
  transform:translate3d(0px,105%,0px);
  transition:transform .85s cubic-bezier(.16,1,.3,1);
}
.reveal-line .rl-inner.on{transform:translate3d(0px,0px,0px)}

.fade-up{opacity:0;transform:translate3d(0px,24px,0px);transition:opacity .8s ease,transform .8s ease}
.fade-up.on{opacity:1;transform:translate3d(0px,0px,0px)}
.fade-in{opacity:0;transition:opacity .8s ease}
.fade-in.on{opacity:1}

/* ─── AI SECTION ─────────────────── */
#ai{min-height:100vh}
#ai .section__inner{
  display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;
}
#ai-pre{}
#ai-pre h2{
  font-family:var(--font-display);font-size:clamp(36px,6vw,80px);
  font-weight:800;line-height:.9;margin-bottom:28px;
}
.body1{font-size:16px;line-height:1.65;color:var(--grey)}
#ai-header{}
#ai-title{
  font-family:var(--font-display);
  font-size:clamp(52px,9vw,120px);font-weight:800;line-height:.86;
  margin-bottom:16px;
}
#ai-tagline{
  font-size:11px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--sienna);
}
.ai-desc-area{margin-top:32px}
#ai-desc{font-family:var(--font-display);font-size:22px;font-weight:600;line-height:1.15}
#ai-instruction{
  display:flex;align-items:center;gap:16px;margin-top:20px;
  font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--grey);
}
#ai-instruction svg{width:22px;height:28px;color:var(--grey)}
#ai-disclaimer-wrapper{margin-top:28px;border-top:1px dashed var(--shadow);padding-top:18px}
#ai-disclaimer{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--grey)}

/* ─── WEARABLE (So portable) ─────── */
#wearable{min-height:80vh}
#wearable .section__inner{display:flex;flex-direction:column;gap:40px}
#wearable-title{
  font-family:var(--font-display);
  font-size:clamp(32px,5vw,64px);font-weight:800;line-height:.92;
}
#wearable-main{
  border:1px dashed var(--shadow);border-radius:16px;overflow:hidden;
  aspect-ratio:16/8;display:flex;align-items:center;justify-content:center;
  background:rgba(255,237,215,.02);position:relative;
}
.wearable-placeholder{
  display:flex;flex-direction:column;align-items:center;gap:16px;
  color:var(--grey);font-size:12px;letter-spacing:.1em;text-transform:uppercase;
}
.wearable-items-strip{
  display:flex;gap:16px;overflow-x:auto;padding:24px 0;scrollbar-width:none;
}
.wearable-items-strip::-webkit-scrollbar{display:none}
.wear-item{
  flex-shrink:0;border:1px dashed var(--shadow);border-radius:10px;
  padding:18px 24px;font-size:12px;color:var(--grey);
  white-space:nowrap;transition:border-color .3s,color .3s;cursor:none;
}
.wear-item:hover{border-color:rgba(255,237,215,.4);color:var(--cream)}

/* ─── FEATURES ───────────────────── */
#features{min-height:100vh}
#features-items{
  display:grid;grid-template-columns:repeat(3,1fr);
  border-top:1px dashed var(--shadow);
}
.features-item{
  padding:36px 32px;border-right:1px dashed var(--shadow);
  opacity:0;transform:translate3d(0px,20px,0px);
  transition:opacity .7s ease,transform .7s ease;
}
.features-item:first-child{padding-left:0}
.features-item:last-child{border-right:none;padding-right:0}
.features-item.on{opacity:1;transform:translate3d(0px,0px,0px)}
.features-item-top{display:flex;align-items:center;gap:14px;margin-bottom:20px}
.features-item-icon{
  width:52px;height:52px;border-radius:50%;
  background:rgba(255,237,215,.07);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.features-item-icon svg{width:30px;height:30px}
.features-item-tagline{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--grey)}
.features-item-desc{font-size:12px;line-height:1.65;color:rgba(255,237,215,.55);margin-bottom:20px}
.features-item .o-dashline{margin:16px 0}
.features-item-title{font-family:var(--font-display);font-size:18px;font-weight:700;line-height:1.2}
.feat-header{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:end;margin-bottom:72px}
.feat-h2{font-family:var(--font-display);font-size:clamp(36px,5.5vw,72px);font-weight:800;line-height:.9}
.feat-sub{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:18px}
.feat-body{font-size:14px;line-height:1.7;color:var(--grey);padding-top:56px}

/* ─── ENCRYPTION ─────────────────── */
#encryption{min-height:70vh}
#encryption .section__inner{
  display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;
}
.enc-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:18px}
.enc-h2{font-family:var(--font-display);font-size:clamp(28px,4.5vw,58px);font-weight:800;line-height:.92;margin-bottom:20px}
.enc-desc{font-size:14px;line-height:1.7;color:var(--grey)}
.enc-field-wrapper{border-bottom:1px solid rgba(255,237,215,.25);position:relative;margin-bottom:24px}
.enc-field-input{
  width:100%;background:transparent;border:none;outline:none;
  font-family:var(--font-display);font-size:40px;font-weight:700;
  color:var(--cream);padding:14px 0;letter-spacing:.04em;cursor:none;
}
.enc-btn{
  display:inline-flex;align-items:center;justify-content:center;
  background:var(--sienna);color:var(--cream);border:none;
  border-radius:28px;padding:14px 32px;
  font-size:12px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;
  overflow:hidden;position:relative;height:48px;
  transition:opacity .3s,transform .2s;
}
.enc-btn:hover{opacity:.85;transform:translateY(-2px)}
.enc-btn-flipper{
  display:flex;flex-direction:column;height:1.4em;overflow:hidden;
  transition:transform .4s cubic-bezier(.77,0,.18,1);
}
.enc-btn-flipper span{display:block;line-height:1.4;white-space:nowrap}
.enc-btn.flipped .enc-btn-flipper{transform:translateY(-50%)}

/* ─── GRIP ───────────────────────── */
#grip{min-height:70vh}
#grip .section__inner{
  display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;
}
.grip-tag{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:18px}
.grip-h2{font-family:var(--font-display);font-size:clamp(28px,4.5vw,58px);font-weight:800;line-height:.92;margin-bottom:20px}
.grip-desc{font-size:14px;line-height:1.7;color:var(--grey)}
.grip-zoom-box{
  border:1px dashed var(--shadow);border-radius:14px;overflow:hidden;
  aspect-ratio:4/3;position:relative;cursor:crosshair;
}
.grip-zoom-box img{width:100%;height:100%;object-fit:cover;filter:brightness(.6);
  transform:scale(1);transform-origin:center;transition:transform .12s ease}
.grip-zoom-box:hover img{transform:scale(2.5)}
.gz-overlay{
  position:absolute;bottom:14px;right:14px;
  font-size:11px;letter-spacing:.1em;color:var(--cream);
  background:rgba(16,9,4,.75);padding:6px 12px;border-radius:6px;
  border:1px solid rgba(255,237,215,.12);
}

/* ─── SUSTAINABILITY ─────────────── */
#sustainability{min-height:100vh}
#sustainability-hero{
  display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:end;margin-bottom:80px;
}
#sustainability-tagline{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);margin-bottom:20px}
#sustainability-title{margin-bottom:0}
#sustainability-title-pre{font-family:var(--font-display);font-size:20px;font-weight:700;color:rgba(255,237,215,.45);margin-bottom:4px}
#sustainability-title-main{font-family:var(--font-display);font-size:clamp(44px,7vw,96px);font-weight:800;line-height:.88}
#sustainability-desc{font-size:14px;line-height:1.7;color:var(--grey);padding-top:56px}
#sustainability-items{
  display:grid;grid-template-columns:repeat(3,1fr);
  border-top:1px dashed var(--shadow);
}
.sustainability-item{
  padding:40px 32px;border-right:1px dashed var(--shadow);
  opacity:0;transform:translate3d(0px,20px,0px);
  transition:opacity .7s ease,transform .7s ease;
}
.sustainability-item:first-child{padding-left:0}
.sustainability-item:last-child{border-right:none;padding-right:0}
.sustainability-item.on{opacity:1;transform:translate3d(0px,0px,0px)}
.sustainability-item-num{font-family:var(--font-display);font-size:80px;font-weight:800;line-height:1;color:var(--cream);margin-bottom:14px}
.sustainability-item-title{font-family:var(--font-display);font-size:16px;font-weight:700;line-height:1.2;margin-bottom:16px}
.sustainability-item-desc{font-size:12px;line-height:1.65;color:var(--grey)}

/* ─── TESTIMONIALS ───────────────── */
#testimonies{min-height:100vh}
#testimonies-hero{margin-bottom:52px}
#testimonies-hero-title{
  font-family:var(--font-display);
  font-size:clamp(28px,4.5vw,58px);font-weight:800;line-height:1;max-width:620px;margin-bottom:18px;
}
#testimonies-hero-desc{font-size:15px;color:var(--grey);line-height:1.6}
#testimonies-table-header{
  display:grid;grid-template-columns:2fr 1fr 160px;gap:20px;
  padding:14px 0;border-top:1px dashed var(--shadow);border-bottom:1px dashed var(--shadow);
  font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--grey);
}
.testimonies-table-item{
  display:grid;grid-template-columns:2fr 1fr 160px;gap:20px;
  padding:28px 0;border-bottom:1px dashed var(--shadow);align-items:start;
  opacity:0;transform:translate3d(0px,16px,0px);
  transition:opacity .65s ease,transform .65s ease;
}
.testimonies-table-item.on{opacity:1;transform:translate3d(0px,0px,0px)}
.testimonies-table-rating{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.testimonies-table-rating svg{width:80px;height:13px}
.testimonies-table-rating-text{font-size:11px;color:var(--grey);letter-spacing:.1em}
.testimonies-table-item-content-title{font-size:15px;line-height:1.5;font-style:italic;margin-bottom:10px}
.testimonies-table-item-content-title span{color:var(--cream);font-style:normal;font-weight:600}
.testimonies-table-item-content-author-name{font-size:12px;font-weight:500}
.testimonies-table-item-content-author-desc{font-size:11px;color:var(--grey)}
.testimonies-table-item-image-wrapper{
  width:140px;height:95px;border-radius:8px;overflow:hidden;
  border:1px solid rgba(255,237,215,.1);
}
.testimonies-table-item-image-wrapper img{
  width:100%;height:100%;object-fit:cover;filter:brightness(.55) saturate(.5);
}

/* ─── SOCIAL CONTENT (CTA) ───────── */
#cta-section{
  min-height:60vh;display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:100px 56px;text-align:center;gap:32px;
  border-top:1px dashed var(--shadow);
}
.cta-label{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--grey)}
.cta-h2{
  font-family:var(--font-display);
  font-size:clamp(48px,9vw,120px);font-weight:800;line-height:.86;
}
.cta-buttons{display:flex;gap:14px;flex-wrap:wrap;justify-content:center}
.btn-primary{
  background:var(--cork-dark);color:var(--cream);border:none;
  border-radius:36px;padding:14px 32px;font-size:14px;letter-spacing:.06em;
  transition:opacity .3s,transform .2s;
}
.btn-primary:hover{opacity:.82;transform:translateY(-2px)}
.btn-secondary{
  background:transparent;color:var(--cream);
  border:1px solid rgba(255,237,215,.38);border-radius:22px;
  padding:10px 24px;font-size:12px;letter-spacing:.09em;text-transform:uppercase;
  transition:border-color .3s,color .3s;
}
.btn-secondary:hover{border-color:var(--sienna);color:var(--sienna)}

/* ─── FOOTER ─────────────────────── */
footer{
  padding:40px 56px 32px;
  border-top:1px dashed var(--shadow);
  background:var(--black);position:relative;z-index:2;
}
.footer-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.footer-logo{font-family:var(--font-display);font-size:24px;font-weight:800;letter-spacing:.04em}
.footer-links{display:flex;gap:28px;list-style:none}
.footer-links a{
  font-size:10px;color:var(--grey);letter-spacing:.13em;text-transform:uppercase;
  transition:color .3s;
}
.footer-links a:hover{color:var(--cream)}
.footer-bottom{
  display:flex;justify-content:space-between;align-items:center;
  padding-top:18px;border-top:1px dashed var(--shadow);
  font-size:10px;color:var(--grey);letter-spacing:.08em;
}
.footer-bottom em{color:var(--sienna);font-style:normal}

/* ─── RESPONSIVE ─────────────────── */
@media(max-width:900px){
  #nav{padding:18px 24px}
  #hero{padding:90px 24px 40px}
  .section__inner{padding-left:24px;padding-right:24px}
  #ai .section__inner,#features .feat-header,#encryption .section__inner,
  #grip .section__inner,#sustainability-hero{grid-template-columns:1fr}
  #features-items,#sustainability-items{grid-template-columns:1fr}
  .features-item,.sustainability-item{border-right:none;padding-left:0;padding-right:0;border-bottom:1px dashed var(--shadow)}
  .testimonies-table-item,#testimonies-table-header{grid-template-columns:1fr}
  .testimonies-table-item-image-wrapper,.testimonies-table-header > div:last-child{display:none}
  #hero-video-wrapper{right:24px;bottom:40px;width:130px}
  footer,#cta-section{padding-left:24px;padding-right:24px}
}
</style>
</head>
<body>

<!-- CURSOR -->
<div id="cursor-dot"></div>
<div id="cursor-ring"></div>

<!-- PROGRESS -->
<div id="progress-bar"></div>

<!-- THREE.JS CANVAS -->
<canvas id="canvas"></canvas>

<!-- SCROLL INDICATOR -->
<div id="scroll-ind">
  <span class="si-text">Scroll</span>
  <div class="si-line"></div>
</div>

<!-- SVG SYMBOLS -->
<svg style="display:none">
  <symbol id="logo-tmpl" viewBox="0 0 809 174">
    <path d="M87 174C36 174 0 132 0 87C0 42 36 0 87 0C138 0 174 42 174 87C174 132 138 174 87 174ZM87 135C112 135 135 115 135 87C135 59 112 39 87 39C62 39 39 59 39 87C39 115 62 135 87 135Z" fill="currentColor"/>
    <path d="M196 170V4H263C307 4 327 28 327 61C327 84 317 103 296 112L333 170H284L255 118H237V170H196ZM237 80H264C280 80 285 72 285 61C285 50 280 42 264 42H237V80Z" fill="currentColor"/>
    <path d="M385 170V101L325 4H373L406 62L439 4H487L427 100V170H385Z" fill="currentColor"/>
    <path d="M490 170V133L568 42H494V4H620V41L543 132H622V170H490Z" fill="currentColor"/>
    <path d="M722 174C671 174 635 132 635 87C635 42 671 0 722 0C773 0 809 42 809 87C809 132 773 174 722 174ZM722 135C747 135 770 115 770 87C770 59 747 39 722 39C697 39 674 59 674 87C674 115 697 135 722 135Z" fill="currentColor"/>
  </symbol>
  <symbol id="hand-tmpl" viewBox="0 0 32 40">
    <path fill="currentColor" d="M6.718 22.615V17.36c-.325.341-.659.696-.986 1.058-1.276 1.407-2.352 2.76-2.775 3.622-.293.602-.263 1.344.017 2.186.271.816.721 1.549 1.03 2.016l5.182 6.817a5.1 5.1 0 0 1 1.04 3.085v2.231a1.375 1.375 0 0 1-2.75 0v-2.231c0-.515-.169-1.012-.48-1.421v-.001l-5.214-6.859-.028-.036-.025-.038c-.34-.513-.97-1.506-1.365-2.696-.393-1.182-.616-2.748.124-4.262v-.002c.616-1.254 1.946-2.867 3.207-4.258a64 64 0 0 1 3.023-3.103V6.902a4.156 4.156 0 0 1 5.711-3.851 4.155 4.155 0 0 1 8.153.86c.466-.175.966-.27 1.483-.27A4.167 4.167 0 0 1 26.23 7.68a4.133 4.133 0 0 1 5.52 3.893v15.933c0 2.3-.866 4.735-3.162 7.469h.001c-.444.53-.681 1.14-.681 1.727v1.673a1.375 1.375 0 1 1-2.75 0v-1.673c0-1.332.533-2.55 1.324-3.493v-.001C28.46 30.854 29 29.024 29 27.506V11.572a1.383 1.383 0 1 0-2.767.008v8.293a1.375 1.375 0 1 1-2.75 0V7.808c0-.782-.635-1.417-1.418-1.417-.82 0-1.474.67-1.474 1.415v10.23a1.375 1.375 0 0 1-2.75 0V4.153a1.406 1.406 0 0 0-2.81 0v11.974a1.375 1.375 0 0 1-2.75 0V6.902l-.007-.142a1.406 1.406 0 0 0-2.806.142v15.713a1.375 1.375 0 0 1-2.75 0"/>
  </symbol>
</svg>

<!-- UI -->
<div id="ui">

<!-- NAV -->
<nav id="nav">
  <a href="#hero" class="nav-logo">
    <svg viewBox="0 0 809 174" fill="none" color="#ffedd7"><use href="#logo-tmpl"/></svg>
  </a>
  <div class="nav-links">
    <a href="#ai" class="nav-link"><span class="t1">AI</span><span class="t2">AI</span></a>
    <a href="#features" class="nav-link"><span class="t1">Features</span><span class="t2">Features</span></a>
    <a href="#sustainability" class="nav-link"><span class="t1">Sustainability</span><span class="t2">Sustainability</span></a>
    <button class="nav-btn">Order Now</button>
  </div>
</nav>

<!-- ════════════ HERO ════════════ -->
<section id="hero" class="section">
  <div id="hero-top" class="sub1">
    <div id="hero-top-tagline">
      <span class="word-clip"><span class="word-inner">Made</span></span>
      <span class="word-clip"><span class="word-inner">for</span></span>
      <span class="word-clip"><span class="word-inner">mugs.</span></span>
      <span class="word-clip"><span class="word-inner">Built</span></span>
      <span class="word-clip"><span class="word-inner">for</span></span>
      <span class="word-clip"><span class="word-inner">tables.</span></span>
    </div>
    <div id="hero-logo-ref">
      <svg viewBox="0 0 809 174" fill="none" style="width:clamp(200px,30vw,400px);color:var(--cream);opacity:0;transition:opacity 1.2s ease .6s" id="hero-center-logo">
        <use href="#logo-tmpl"/>
      </svg>
    </div>
  </div>

  <div id="hero-copy" class="body1">
    <span class="copy-line"><span class="line-inner">Designed to lift, insulate, and grip in all the right ways.</span></span>
    <span class="copy-line"><span class="line-inner">Oryzo makes the simplest moment feel considered.</span></span>
  </div>

  <div id="hero-card">
    <h4 id="hero-card-header">
      <span class="line-wrap"><span class="li">Designed</span></span>
      <span class="line-wrap"><span class="li">by Lusion,</span></span>
      <span class="line-wrap"><span class="li">the award-winning</span></span>
      <span class="line-wrap"><span class="li">design studio.</span></span>
    </h4>
    <div class="card-dash" id="hero-card-dash"></div>
    <div id="hero-card-desc" class="body2">
      <span>The world's most</span>
      <span>unnecessarily</span>
      <span>sophisticated cork coaster.</span>
    </div>
  </div>

  <div id="hero-video-wrapper">
    <span class="hero-video__glow"></span>
    <span class="hero-video__border"></span>
    <div id="hero-video-thumbnail-wrapper">
      <img id="hero-video-thumbnail" src="coaster1.png" alt="Video thumbnail">
    </div>
    <div id="hero-video-play">PLAY</div>
  </div>
</section>

<!-- ════════════ MARQUEE ════════════ -->
<div id="marquee">
  <div class="marquee-track">
    <span class="marquee-item">Made for mugs</span>
    <span class="marquee-item">Built for tables</span>
    <span class="marquee-item">Cork intelligence</span>
    <span class="marquee-item">Unnecessarily sophisticated</span>
    <span class="marquee-item">Award winning</span>
    <span class="marquee-item">Designed by Lusion</span>
    <span class="marquee-item">Thermodynamic stability</span>
    <span class="marquee-item">Zero drama</span>
    <span class="marquee-item">Made for mugs</span>
    <span class="marquee-item">Built for tables</span>
    <span class="marquee-item">Cork intelligence</span>
    <span class="marquee-item">Unnecessarily sophisticated</span>
    <span class="marquee-item">Award winning</span>
    <span class="marquee-item">Designed by Lusion</span>
    <span class="marquee-item">Thermodynamic stability</span>
    <span class="marquee-item">Zero drama</span>
  </div>
</div>

<!-- ════════════ AI ════════════ -->
<section id="ai" class="section">
  <div class="section__inner">
    <div id="ai-pre">
      <h2>
        <span class="reveal-line" data-delay="0"><span class="rl-inner">isn't just</span></span>
        <span class="reveal-line" data-delay="120"><span class="rl-inner">a coaster.</span></span>
      </h2>
      <div class="body1 fade-up" data-delay="200" style="margin-top:24px">
        Oryzo isn't just a coaster. It's the result of unprecedented AI* breakthroughs.
      </div>
    </div>
    <div id="ai-header">
      <h1 id="ai-title">
        <span class="reveal-line" data-delay="0"><span class="rl-inner">Powered</span></span>
        <span class="reveal-line" data-delay="140"><span class="rl-inner">by AI<sup>*</sup></span></span>
      </h1>
      <h4 id="ai-tagline" class="fade-in" data-delay="400">Oryzo&#8209;1</h4>
      <div class="ai-desc-area">
        <div id="ai-instruction" class="fade-up" data-delay="350">
          <svg><use href="#hand-tmpl"/></svg>
          <span>Try to hover hand</span>
        </div>
        <div id="ai-desc">
          <span class="reveal-line" data-delay="250"><span class="rl-inner">AI fills in the gaps.</span></span>
          <span class="reveal-line" data-delay="360"><span class="rl-inner">We said high five.</span></span>
          <span class="reveal-line" data-delay="460"><span class="rl-inner">It heard six.</span></span>
        </div>
      </div>
      <div id="ai-disclaimer-wrapper" class="fade-up" data-delay="550">
        <div id="ai-disclaimer">* Adobe Illustrator</div>
      </div>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ WEARABLE ════════════ -->
<section id="wearable" class="section">
  <div class="section__inner">
    <h4 id="wearable-title">
      <span class="reveal-line" data-delay="0"><span class="rl-inner">So portable,</span></span>
      <span class="reveal-line" data-delay="140"><span class="rl-inner">it's wearable</span></span>
    </h4>
    <div id="wearable-main" class="fade-up" data-delay="200">
      <div class="wearable-placeholder">
        <svg width="48" height="48" viewBox="0 0 32 40" fill="none" color="var(--shadow)"><use href="#hand-tmpl"/></svg>
        <span>Interactive wearable gallery</span>
      </div>
    </div>
    <div class="wearable-items-strip">
      <div class="wear-item">Yoga mat</div>
      <div class="wear-item">On shoulder</div>
      <div class="wear-item">As a hat</div>
      <div class="wear-item">Glasses</div>
      <div class="wear-item">In pocket</div>
      <div class="wear-item">Issue No. 00124</div>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ FEATURES ════════════ -->
<section id="features" class="section">
  <div class="section__inner">
    <div class="feat-header">
      <div>
        <div class="feat-sub fade-in" data-delay="0">— What it does</div>
        <h2 class="feat-h2">
          <span class="reveal-line" data-delay="50"><span class="rl-inner">Elevate</span></span>
          <span class="reveal-line" data-delay="170"><span class="rl-inner">everything.</span></span>
          <span class="reveal-line" data-delay="280"><span class="rl-inner">Literally.</span></span>
        </h2>
      </div>
      <p class="feat-body fade-up" data-delay="150">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable while your coffee table tapped out three sips ago. Precision engineered for the unnecessarily sophisticated.</p>
    </div>
    <div id="features-items">
      <div class="features-item" data-fi>
        <div class="features-item-top">
          <div class="features-item-icon">
            <svg viewBox="0 0 64 64" fill="none" color="var(--cream)">
              <circle cx="32" cy="32" r="32" fill="currentColor" opacity=".12"/>
              <path fill="currentColor" stroke="currentColor" stroke-width="1" d="m24 27 7.9-10.1a.09.09 0 0 1 .14 0L39.9 27h-4.7v12.7h-6.6z"/>
              <path stroke="currentColor" stroke-linecap="square" stroke-width="1.1" d="M28.8 42.1h6.4M28.8 44.8h6.4M28.8 47.4h6.4" opacity=".7"/>
            </svg>
          </div>
          <div class="features-item-tagline">Rise above mediocrity</div>
        </div>
        <div class="features-item-desc">With a precision-engineered lift (exactly one coaster thick), Oryzo doesn't just hold your mug — it elevates it. Literally. Above every boring surface.</div>
        <div class="o-dashline"></div>
        <h3 class="features-item-title">Elevate your coffee experience</h3>
      </div>
      <div class="features-item" data-fi>
        <div class="features-item-top">
          <div class="features-item-icon">
            <svg viewBox="0 0 54 54" fill="none" color="var(--cream)">
              <circle cx="27" cy="27" r="27" fill="currentColor" opacity=".12"/>
              <path fill="currentColor" d="M20.5 21.7a.47.47 0 0 1 .77.36v13.7a5.69 5.69 0 0 0 11.37 0v-2h.8v2a6.49 6.49 0 0 1-12.97 0V23l-.3.36-.3-.26-.3-.26zm6.45-6.84a3.37 3.37 0 0 1 3.37 3.37v17.55a3.37 3.37 0 0 1-6.75 0V18.23a3.37 3.37 0 0 1 3.38-3.37"/>
            </svg>
          </div>
          <div class="features-item-tagline">Handles Extremes with Ease</div>
        </div>
        <div class="features-item-desc">From piping-hot mugs to ice-cold drinks — Oryzo stays perfectly stable. Your coffee table already tapped out three sips ago.</div>
        <div class="o-dashline"></div>
        <h3 class="features-item-title">Thermodynamic stability</h3>
      </div>
      <div class="features-item" data-fi>
        <div class="features-item-top">
          <div class="features-item-icon">
            <svg viewBox="0 0 54 54" fill="none" color="var(--cream)">
              <circle cx="27" cy="27" r="27" fill="currentColor" opacity=".12"/>
              <circle cx="27" cy="27" r="13.8" stroke="currentColor" stroke-width=".8"/>
              <path fill="currentColor" d="M42 25.7v2.3h-2.3v-2.3zM14.3 25.7v2.3H12v-2.3zM27 17.75a9.25 9.25 0 1 1 0 18.5 9.25 9.25 0 0 1 0-18.5m.53 10.34 1.63 1.63.56-.56-1.63-1.63zm-3.24 1.06.56.56 1.63-1.63-.56-.56zm.02-4.28 1.63 1.63.56-.56-1.63-1.63zm3.2 1.06.56.56 1.63-1.63-.56-.56z"/>
            </svg>
          </div>
          <div class="features-item-tagline">Perfectly Round, Seriously</div>
        </div>
        <div class="features-item-desc">Our engineers recalibrated its circumference with disturbing levels of attention to detail — just because we could.</div>
        <div class="o-dashline"></div>
        <h3 class="features-item-title">Now 37.9% More Circular</h3>
      </div>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ ENCRYPTION ════════════ -->
<section id="encryption" class="section">
  <div class="section__inner">
    <div class="fade-up">
      <div class="enc-tag">Secure communications simplified</div>
      <h2 class="enc-h2">
        <span class="reveal-line" data-delay="0"><span class="rl-inner">Smart flip</span></span>
        <span class="reveal-line" data-delay="130"><span class="rl-inner">encryption</span></span>
      </h2>
      <p class="enc-desc">Write a message. Flip. Instantly secure — until someone flips it back. Genius.</p>
    </div>
    <div class="fade-up" data-delay="150">
      <div class="enc-field-wrapper">
        <input class="enc-field-input" type="text" id="encryption-field-input" value="ORYZO" maxlength="10" autocomplete="off" spellcheck="false"/>
      </div>
      <button class="enc-btn" id="encryption-field-flip-btn">
        <span class="enc-btn-flipper" id="enc-flipper">
          <span>Encode Message</span>
          <span>Decode Message</span>
        </span>
      </button>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ GRIP ════════════ -->
<section id="grip" class="section">
  <div class="section__inner">
    <div class="fade-up">
      <div class="grip-tag">Precision Grip, Zero Drama</div>
      <h2 class="grip-h2">
        <span class="reveal-line" data-delay="0"><span class="rl-inner">Grip-locked Antislip</span></span>
        <span class="reveal-line" data-delay="140"><span class="rl-inner">technology</span></span>
      </h2>
      <p class="grip-desc" style="margin-top:20px">Micro-textured cork so grippy your drink files a restraining order against gravity. Spills? Consider them politely discouraged.</p>
    </div>
    <div class="grip-zoom-box fade-up" data-delay="200">
      <img src="coaster2.png" alt="Cork texture closeup"/>
      <div class="gz-overlay">Friction coefficient (est): <strong>0.80</strong></div>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ SUSTAINABILITY ════════════ -->
<section id="sustainability" class="section">
  <div class="section__inner">
    <div id="sustainability-hero">
      <div>
        <div id="sustainability-tagline" class="fade-in">100% Plant-based</div>
        <div id="sustainability-title">
          <h4 id="sustainability-title-pre" class="fade-up" data-delay="50">Vegan-friendly</h4>
          <h2 id="sustainability-title-main">
            <span class="reveal-line" data-delay="0"><span class="rl-inner">sustain</span></span>
            <span class="reveal-line" data-delay="130"><span class="rl-inner">ability</span></span>
          </h2>
        </div>
      </div>
      <div id="sustainability-desc" class="fade-up" data-delay="200">
        Pure cork sourced sustainably. Completely vegan — no cows were harmed, but it might be full of "bull"sh*t.
      </div>
    </div>
    <div id="sustainability-items">
      <div class="sustainability-item" data-si>
        <div class="sustainability-item-num">25</div>
        <h3 class="sustainability-item-title">Average<br>age of first<br>harvest</h3>
        <div class="sustainability-item-desc">Cork oaks are typically first harvested at around 25 years, once the bark is thick enough to remove safely.</div>
      </div>
      <div class="sustainability-item" data-si>
        <div class="sustainability-item-num">9</div>
        <h4 class="sustainability-item-title">Harvesting<br>interval</h4>
        <div class="sustainability-item-desc">After each harvest, the bark takes about 9 years to regrow, making cork a renewable material.</div>
      </div>
      <div class="sustainability-item" data-si>
        <div class="sustainability-item-num">0W</div>
        <h4 class="sustainability-item-title">Power draw<br>while in use</h4>
        <div class="sustainability-item-desc">No compute. No tokens. So you can say "please" and "thank you" as much as you want, guilt free.</div>
      </div>
    </div>
  </div>
</section>

<hr class="o-dashline" style="position:relative;z-index:2;background:var(--black)"/>

<!-- ════════════ TESTIMONIALS ════════════ -->
<section id="testimonies" class="section">
  <div class="section__inner">
    <div id="testimonies-hero">
      <h2 id="testimonies-hero-title">
        <span class="reveal-line" data-delay="0"><span class="rl-inner">People all around the world</span></span>
        <span class="reveal-line" data-delay="120"><span class="rl-inner">love Oryzo</span></span>
      </h2>
      <div id="testimonies-hero-desc" class="fade-up" data-delay="200">Do not take our word for it, see what people say after living with Oryzo.</div>
    </div>
    <div id="testimonies-table-header">
      <div>Rating &amp; Reviews</div>
      <div>Custom reviews [ 364 ] ★ 4.9/5</div>
      <div>ORYZO in use</div>
    </div>
    <div class="testimonies-table-item" data-ti>
      <div class="testimonies-table-item-content">
        <div class="testimonies-table-rating">
          <svg viewBox="0 0 96 15" fill="var(--cream)"><use href="#star" x="0"/><use href="#star" x="19"/><use href="#star" x="38"/><use href="#star" x="57"/><use href="#star" x="76"/></svg>
          <div class="testimonies-table-rating-text">[ 5/5 ]</div>
        </div>
        <div class="testimonies-table-item-content-title">"This is the <span>best coaster</span> that I've ever used. I can't go to space without it"</div>
        <div class="testimonies-table-item-content-author-name">Edan K.</div>
        <div class="testimonies-table-item-content-author-desc">NASA astronaut wannabe</div>
      </div>
      <div class="testimonies-table-rating-text" style="padding-top:4px">[ 5/5 ]</div>
      <div class="testimonies-table-item-image-wrapper"><img src="coaster2.png" alt=""/></div>
    </div>
    <div class="testimonies-table-item" data-ti>
      <div class="testimonies-table-item-content">
        <div class="testimonies-table-rating">
          <svg viewBox="0 0 96 15" fill="var(--cream)"><use href="#star" x="0"/><use href="#star" x="19"/><use href="#star" x="38"/><use href="#star" x="57"/><use href="#star-half" x="76"/></svg>
          <div class="testimonies-table-rating-text">[ 4.5/5 ]</div>
        </div>
        <div class="testimonies-table-item-content-title">"My coaster? If you want it, I'll let you have it. Look for it! I left everything in <span>one place!</span>"</div>
        <div class="testimonies-table-item-content-author-name">Gol D. Roger</div>
        <div class="testimonies-table-item-content-author-desc">Old-school Pirate</div>
      </div>
      <div class="testimonies-table-rating-text" style="padding-top:4px">[ 4.5/5 ]</div>
      <div class="testimonies-table-item-image-wrapper"><img src="coaster1.png" alt=""/></div>
    </div>
    <div class="testimonies-table-item" data-ti>
      <div class="testimonies-table-item-content">
        <div class="testimonies-table-rating">
          <svg viewBox="0 0 96 15" fill="var(--cream)"><use href="#star" x="0"/><use href="#star" x="19"/><use href="#star" x="38"/><use href="#star" x="57"/><use href="#star" x="76"/></svg>
          <div class="testimonies-table-rating-text">[ 5/5 ]</div>
        </div>
        <div class="testimonies-table-item-content-title">"<span>We are so cooked</span>. Hollywood is not ready for a coaster this cinematic."</div>
        <div class="testimonies-table-item-content-author-name">Jamie R.</div>
        <div class="testimonies-table-item-content-author-desc">AI influencer, Ex-Web3 influencer</div>
      </div>
      <div class="testimonies-table-rating-text" style="padding-top:4px">[ 5/5 ]</div>
      <div class="testimonies-table-item-image-wrapper"><img src="coaster2.png" alt=""/></div>
    </div>
    <div class="testimonies-table-item" data-ti>
      <div class="testimonies-table-item-content">
        <div class="testimonies-table-rating">
          <svg viewBox="0 0 96 15" fill="var(--cream)"><use href="#star" x="0"/><use href="#star" x="19"/><use href="#star" x="38"/><use href="#star" x="57"/><use href="#star" x="76"/></svg>
          <div class="testimonies-table-rating-text">[ 5/5 ]</div>
        </div>
        <div class="testimonies-table-item-content-title">"My table hasn't been this protected since I stopped trusting <span>gravity</span>."</div>
        <div class="testimonies-table-item-content-author-name">Priya K.</div>
        <div class="testimonies-table-item-content-author-desc">Flat Earth believer</div>
      </div>
      <div class="testimonies-table-rating-text" style="padding-top:4px">[ 5/5 ]</div>
      <div class="testimonies-table-item-image-wrapper"><img src="coaster1.png" alt=""/></div>
    </div>
  </div>
</section>

<!-- ════════════ CTA ════════════ -->
<section id="cta-section" class="section">
  <div class="cta-label fade-in">Ready to elevate?</div>
  <h2 class="cta-h2">
    <span class="reveal-line" data-delay="0"><span class="rl-inner">Order yours</span></span>
    <span class="reveal-line" data-delay="140"><span class="rl-inner">today.</span></span>
  </h2>
  <div class="cta-buttons fade-up" data-delay="300">
    <button class="btn-primary">Get ORYZO&#8209;1</button>
    <button class="btn-secondary">Learn more</button>
  </div>
</section>

<footer>
  <div class="footer-top">
    <div class="footer-logo">ORYZO</div>
    <ul class="footer-links">
      <li><a href="#ai">AI</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#sustainability">Sustainability</a></li>
      <li><a href="#testimonies">Reviews</a></li>
      <li><a href="#">Privacy</a></li>
    </ul>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2026 ORYZO AI. Designed by Lusion. All rights reserved.</span>
    <span>Powered by <em>ORYZO&#8209;1</em></span>
  </div>
</footer>

</div><!-- #ui -->

<!-- SVG star symbols for ratings -->
<svg style="display:none">
  <symbol id="star" viewBox="0 0 15 15">
    <path d="M6.96.95c.18-.46.84-.46 1.02 0l1.51 3.88c.08.2.26.33.48.35l4.16.24c.5.03.7.65.31.97L11.2 8.79c-.17.14-.24.35-.18.56l1.06 4.03c.13.48-.41.87-.82.6L7.7 11.74c-.18-.12-.41-.12-.59 0l-3.51 2.24c-.42.27-.95-.12-.82-.6l1.06-4.03c.05-.21-.02-.43-.18-.56L.49 6.39c-.39-.32-.18-.94.31-.97l4.16-.24c.21-.01.4-.15.48-.35z"/>
  </symbol>
  <symbol id="star-half" viewBox="0 0 15 15">
    <path d="M6.96.95c.18-.46.84-.46 1.02 0l1.51 3.88c.08.2.26.33.48.35l4.16.24c.5.03.7.65.31.97L11.2 8.79c-.17.14-.24.35-.18.56l1.06 4.03c.13.48-.41.87-.82.6L7.7 11.74c-.18-.12-.41-.12-.59 0l-3.51 2.24c-.42.27-.95-.12-.82-.6l1.06-4.03c.05-.21-.02-.43-.18-.56L.49 6.39c-.39-.32-.18-.94.31-.97l4.16-.24c.21-.01.4-.15.48-.35z" fill="currentColor" opacity=".3"/>
    <path d="M7.47.62c-.2.01-.39.12-.48.34l-1.51 3.88c-.08.2-.26.33-.48.35l-4.16.24c-.5.03-.7.65-.31.97l3.22 2.64c.17.14.24.35.18.56l-1.06 4.03c-.13.48.41.87.82.6l3.51-2.25c.08-.05.17-.07.27-.08V.62z"/>
  </symbol>
</svg>

<script>
/* ══════════════════════════════════════
   THREE.JS — 3D Cork Coaster
══════════════════════════════════════ */
(function(){
  const canvas = document.getElementById('canvas');
  const renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  renderer.setClearColor(0x000000,0);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 100);
  camera.position.set(0, 0, 5);

  // Resize
  function resize(){
    renderer.setSize(window.innerWidth,window.innerHeight);
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  /* ── LIGHTING ── */
  const ambientLight = new THREE.AmbientLight(0xffedd7, 0.4);
  scene.add(ambientLight);

  const keyLight = new THREE.DirectionalLight(0xffd4a0, 2.2);
  keyLight.position.set(-3, 4, 5);
  scene.add(keyLight);

  const rimLight = new THREE.DirectionalLight(0xff8040, 0.8);
  rimLight.position.set(4, -2, -3);
  scene.add(rimLight);

  const fillLight = new THREE.DirectionalLight(0xffedd7, 0.3);
  fillLight.position.set(2, 3, 2);
  scene.add(fillLight);

  /* ── CORK COASTER GEOMETRY ── */
  // Main disc
  const discGeo = new THREE.CylinderGeometry(1.8, 1.8, 0.14, 80, 4);

  // Cork texture canvas
  const texCanvas = document.createElement('canvas');
  texCanvas.width = 512; texCanvas.height = 512;
  const tc = texCanvas.getContext('2d');

  // Base cork gradient
  const cg = tc.createRadialGradient(230,220,0, 256,256,260);
  cg.addColorStop(0,'#d4a870');
  cg.addColorStop(0.3,'#c09050');
  cg.addColorStop(0.65,'#a87838');
  cg.addColorStop(0.85,'#8a6028');
  cg.addColorStop(1,'#6a4218');
  tc.fillStyle = cg;
  tc.fillRect(0,0,512,512);

  // Cork grain rings
  for(let i=0;i<20;i++){
    const r = 20 + i*13 + Math.random()*6;
    const ox = 256 + (Math.random()-0.5)*18;
    const oy = 256 + (Math.random()-0.5)*18;
    tc.beginPath();
    tc.ellipse(ox,oy,r,r*(0.88+Math.random()*0.1),Math.random()*0.2,0,Math.PI*2);
    tc.strokeStyle=`rgba(${50+Math.floor(Math.random()*30)},${20+Math.floor(Math.random()*15)},${5+Math.floor(Math.random()*8)},${0.18+Math.random()*0.22})`;
    tc.lineWidth = 0.8+Math.random()*1.2;
    tc.stroke();
  }
  // Radial grain lines
  for(let i=0;i<28;i++){
    const a = Math.random()*Math.PI*2;
    const r1 = 8+Math.random()*20;
    const r2 = 80+Math.random()*160;
    tc.beginPath();
    tc.moveTo(256+Math.cos(a)*r1, 256+Math.sin(a)*r1);
    const curve = (Math.random()-0.5)*12;
    tc.quadraticCurveTo(256+Math.cos(a+0.1)*r2*0.5+curve,256+Math.sin(a+0.1)*r2*0.5+curve, 256+Math.cos(a+Math.random()*0.15)*r2, 256+Math.sin(a+Math.random()*0.15)*r2);
    tc.strokeStyle=`rgba(60,24,4,${0.06+Math.random()*0.1})`;
    tc.lineWidth=0.6;
    tc.stroke();
  }
  // Subtle spots
  for(let i=0;i<40;i++){
    const a=Math.random()*Math.PI*2, r=Math.random()*230;
    tc.beginPath();
    tc.arc(256+Math.cos(a)*r,256+Math.sin(a)*r,Math.random()*2.5,0,Math.PI*2);
    tc.fillStyle=`rgba(50,20,4,${0.08+Math.random()*0.12})`;
    tc.fill();
  }

  const texture = new THREE.CanvasTexture(texCanvas);

  // Edge texture (darker cork)
  const edgeCanvas = document.createElement('canvas');
  edgeCanvas.width = 128; edgeCanvas.height = 32;
  const ec = edgeCanvas.getContext('2d');
  const eg = ec.createLinearGradient(0,0,128,0);
  eg.addColorStop(0,'#3a2010');
  eg.addColorStop(0.2,'#6b3d1a');
  eg.addColorStop(0.5,'#8a5228');
  eg.addColorStop(0.8,'#6b3d1a');
  eg.addColorStop(1,'#3a2010');
  ec.fillStyle=eg; ec.fillRect(0,0,128,32);
  // Edge grain
  for(let i=0;i<16;i++){
    ec.fillStyle=`rgba(30,10,2,${0.1+Math.random()*0.15})`;
    ec.fillRect(Math.random()*128,Math.random()*32,1,Math.random()*32);
  }
  const edgeTex = new THREE.CanvasTexture(edgeCanvas);

  const discMat = new THREE.MeshStandardMaterial({
    map: texture,
    roughness: 0.88,
    metalness: 0.02,
    color: 0xffffff,
  });

  // Custom edge material
  const edgeMat = new THREE.MeshStandardMaterial({
    map: edgeTex,
    roughness: 0.95,
    metalness: 0.0,
    color: 0xffffff,
  });

  // Build multi-material mesh
  const disc = new THREE.Mesh(discGeo, [discMat, edgeMat, discMat]);
  scene.add(disc);

  // Subtle ORYZO text ring (canvas texture overlay)
  const ringCanvas = document.createElement('canvas');
  ringCanvas.width=512;ringCanvas.height=512;
  const rc=ringCanvas.getContext('2d');
  rc.clearRect(0,0,512,512);
  rc.save();
  rc.font='bold 18px Syne, sans-serif';
  rc.fillStyle='rgba(255,237,215,0.18)';
  rc.textAlign='center';
  rc.letterSpacing='0.3em';
  // Draw text in a circle
  const txt='· ORYZO AI · ORYZO AI · ORYZO AI · ';
  const radius=190;
  for(let i=0;i<txt.length;i++){
    const angle=(i/txt.length)*Math.PI*2-Math.PI/2;
    rc.save();
    rc.translate(256+Math.cos(angle)*radius,256+Math.sin(angle)*radius);
    rc.rotate(angle+Math.PI/2);
    rc.fillText(txt[i],0,0);
    rc.restore();
  }
  rc.restore();
  const ringTex=new THREE.CanvasTexture(ringCanvas);
  // Overlay plane on top of disc
  const ringGeo=new THREE.CircleGeometry(1.78,80);
  const ringMat=new THREE.MeshBasicMaterial({map:ringTex,transparent:true,opacity:1,depthWrite:false});
  const ringMesh=new THREE.Mesh(ringGeo,ringMat);
  ringMesh.rotation.x=-Math.PI/2;
  ringMesh.position.y=0.071;
  disc.add(ringMesh);

  /* ── ANIMATION STATE ── */
  let scrollY = 0;
  let mouseX = 0, mouseY = 0;
  let targetRotX = 0, targetRotY = 0;
  let currentRotX = 0, currentRotY = 0;
  let time = 0;

  window.addEventListener('scroll',()=>{scrollY=window.scrollY;},{passive:true});
  document.addEventListener('mousemove',e=>{
    mouseX=(e.clientX/window.innerWidth-.5)*2;
    mouseY=(e.clientY/window.innerHeight-.5)*2;
  },{passive:true});

  /* ── RENDER LOOP ── */
  function animate(){
    requestAnimationFrame(animate);
    time += 0.008;

    // Scroll drives continuous Y rotation
    const scrollRotY = scrollY * 0.003;
    // Mouse adds gentle tilt
    targetRotX = mouseY * 0.35;
    targetRotY = scrollRotY + mouseX * 0.2;

    // Smooth lerp
    currentRotX += (targetRotX - currentRotX) * 0.06;
    currentRotY += (targetRotY - currentRotY) * 0.06;

    // Gentle idle float
    const floatY = Math.sin(time) * 0.08;
    const floatX = Math.cos(time * 0.7) * 0.04;

    disc.rotation.x = currentRotX + floatX;
    disc.rotation.y = currentRotY;
    disc.position.y = floatY;

    // Position based on scroll — move disc through sections
    const docH = document.body.scrollHeight - window.innerHeight;
    const progress = Math.min(scrollY / (docH||1), 1);

    // Parallax camera-like movement (disc drifts right then left)
    disc.position.x = Math.sin(progress * Math.PI * 2) * 0.6;

    renderer.render(scene, camera);
  }
  animate();
})();

/* ══════════════════════════════════════
   CURSOR
══════════════════════════════════════ */
const cursorDot = document.getElementById('cursor-dot');
const cursorRing = document.getElementById('cursor-ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{
  mx=e.clientX;my=e.clientY;
  cursorDot.style.left=mx+'px';cursorDot.style.top=my+'px';
},{passive:true});
(function loop(){
  rx+=(mx-rx)*.1;ry+=(my-ry)*.1;
  cursorRing.style.left=rx+'px';cursorRing.style.top=ry+'px';
  requestAnimationFrame(loop);
})();
document.querySelectorAll('a,button,input').forEach(el=>{
  el.addEventListener('mouseenter',()=>document.body.classList.add('hovered'));
  el.addEventListener('mouseleave',()=>document.body.classList.remove('hovered'));
});

/* ══════════════════════════════════════
   PROGRESS + NAV + SCROLL INDICATOR
══════════════════════════════════════ */
const navEl = document.getElementById('nav');
const scrollInd = document.getElementById('scroll-ind');
const progressBar = document.getElementById('progress-bar');
window.addEventListener('scroll',()=>{
  const sy=window.scrollY;
  const tot=document.body.scrollHeight-window.innerHeight;
  progressBar.style.width=(sy/tot*100)+'%';
  navEl.classList.toggle('scrolled',sy>60);
  scrollInd.classList.toggle('hidden',sy>window.innerHeight*.4);
},{passive:true});

/* ══════════════════════════════════════
   HERO LOAD ANIMATIONS
══════════════════════════════════════ */
window.addEventListener('DOMContentLoaded',()=>{
  // Word clips stagger
  const wc = document.querySelectorAll('#hero-top-tagline .word-inner');
  wc.forEach((w,i)=>{
    setTimeout(()=>w.classList.add('revealed'), 200+i*80);
  });
  // Center logo
  setTimeout(()=>{
    const logo=document.getElementById('hero-center-logo');
    if(logo)logo.style.opacity='1';
  },400);
  // Copy lines
  const lines=document.querySelectorAll('#hero-copy .line-inner');
  lines.forEach((l,i)=>setTimeout(()=>l.classList.add('revealed'),480+i*120));
  // Card
  setTimeout(()=>{
    document.getElementById('hero-card').classList.add('revealed');
    document.getElementById('hero-card-dash').classList.add('revealed');
    const cardLines=document.querySelectorAll('#hero-card-header .li');
    cardLines.forEach((l,i)=>setTimeout(()=>l.classList.add('revealed'),800+i*80));
  },700);
  // Video chip
  setTimeout(()=>document.getElementById('hero-video-wrapper').classList.add('revealed'),1000);
});

/* Hero parallax on scroll */
window.addEventListener('scroll',()=>{
  const sy=window.scrollY,vh=window.innerHeight;
  if(sy<vh){
    const p=sy/vh;
    const logo=document.getElementById('hero-center-logo');
    if(logo){logo.style.transform=`scale(${1+p*.08}) translateY(${-p*50}px)`;logo.style.opacity=`${1-p*.95}`;}
    const tag=document.getElementById('hero-top-tagline');
    if(tag)tag.style.transform=`translateY(${-p*22}px)`;
    const copy=document.getElementById('hero-copy');
    if(copy)copy.style.transform=`translateY(${-p*18}px)`;
    const card=document.getElementById('hero-card');
    if(card)card.style.transform=`translate3d(${p*-8}px,0,0)`;
  }
},{passive:true});

/* ══════════════════════════════════════
   INTERSECTION OBSERVER — REVEAL LINES
══════════════════════════════════════ */
function makeRevealObserver(threshold=0.12){
  return new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(!e.isIntersecting)return;
      // Get all reveal-lines and fade-ups inside this container or the element itself
      const el=e.target;
      // If it's a reveal-line
      if(el.classList.contains('reveal-line')){
        const delay=parseInt(el.dataset.delay||0);
        setTimeout(()=>el.querySelector('.rl-inner')?.classList.add('on'),delay);
        return;
      }
      // If it's a fade-up
      if(el.classList.contains('fade-up')||el.classList.contains('fade-in')){
        const delay=parseInt(el.dataset.delay||0);
        setTimeout(()=>el.classList.add('on'),delay);
      }
    });
  },{threshold,rootMargin:'0px 0px -40px 0px'});
}

const revealObs = makeRevealObserver();

// Observe all reveal-line and fade-* elements
document.querySelectorAll('.reveal-line,.fade-up,.fade-in').forEach(el=>{
  revealObs.observe(el);
});

// Features items stagger
const featureItems=document.querySelectorAll('[data-fi]');
const fIO=new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  featureItems.forEach((f,i)=>setTimeout(()=>f.classList.add('on'),i*130));
  fIO.disconnect();
},{threshold:.1});
if(featureItems[0])fIO.observe(featureItems[0]);

// Sustainability items stagger
const sustItems=document.querySelectorAll('[data-si]');
const sIO=new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  sustItems.forEach((s,i)=>setTimeout(()=>s.classList.add('on'),i*140));
  sIO.disconnect();
},{threshold:.1});
if(sustItems[0])sIO.observe(sustItems[0]);

// Testimonies stagger
const testItems=document.querySelectorAll('[data-ti]');
const tIO=new IntersectionObserver(([e])=>{
  if(!e.isIntersecting)return;
  testItems.forEach((t,i)=>setTimeout(()=>t.classList.add('on'),i*110));
  tIO.disconnect();
},{threshold:.08});
if(testItems[0])tIO.observe(testItems[0]);

/* ══════════════════════════════════════
   ENCRYPTION
══════════════════════════════════════ */
const encInput=document.getElementById('encryption-field-input');
const encBtn=document.getElementById('encryption-field-flip-btn');
const encFlipper=document.getElementById('enc-flipper');
let isEncoded=false;
function rot13(s){
  return s.split('').map(c=>{
    if(c>='A'&&c<='Z')return String.fromCharCode((c.charCodeAt(0)-65+13)%26+65);
    if(c>='a'&&c<='z')return String.fromCharCode((c.charCodeAt(0)-97+13)%26+97);
    return c;
  }).join('');
}
if(encBtn){
  encBtn.addEventListener('click',()=>{
    isEncoded=!isEncoded;
    encFlipper.style.transform=isEncoded?'translateY(-50%)':'translateY(0)';
    encBtn.classList.toggle('flipped',isEncoded);
    const orig=encInput.value;
    const target=rot13(orig);
    const chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let frame=0;const total=16;
    const iv=setInterval(()=>{
      frame++;
      if(frame>=total){clearInterval(iv);encInput.value=target;return;}
      encInput.value=orig.split('').map((c,i)=>{
        if(i<frame/total*orig.length)return target[i]||c;
        return chars[Math.floor(Math.random()*26)];
      }).join('');
    },36);
  });
}
</script>
</body>
</html>"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"Written: {len(html)} bytes")
