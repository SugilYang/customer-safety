# -*- coding: utf-8 -*-
# index.html 조립: 공통 CSS + 새 홈/검색/더보기 + 기존 교육/OPS/벌점표 코드
import re
import os; base=os.path.dirname(os.path.abspath(__file__))+'/'
css=open(base+'_css.txt',encoding='utf-8').read()
train=open(base+'_train.js',encoding='utf-8').read()
ops_fn=open(base+'_ops.js',encoding='utf-8').read()
pen=open(base+'_pen.js',encoding='utf-8').read()

GAS='https://script.google.com/macros/s/AKfycbxLZvGIZvX2daaUTSKVGgOfpLOZV1JOiJeJFmazq_Diaxx2OW8VIACi_w9No29K3f_bKg/exec'

extra_css='''

ul.sub{margin:4px 0 2px;padding:0;list-style:none}
ul.sub li{position:relative;padding-left:4px;margin:3px 0;font-size:13.5px;color:#2b332f;line-height:1.5}
ul.sub li:before{content:none}
.gsec li ul.sub li:before,.ob li ul.sub li:before{content:none}

/* ---- 스플래시 ---- */
.splash{position:fixed;inset:0;z-index:200;background:linear-gradient(rgba(255,255,255,.28),rgba(255,255,255,.28)),#eef6f3 url(img/splash_bg.jpg) center/cover no-repeat;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;cursor:pointer}
.splash .glow{position:absolute;width:70vmin;height:70vmin;border-radius:50%;background:radial-gradient(circle,rgba(0,128,111,.14),rgba(0,128,111,0) 70%);animation:sp-glow 2.4s ease-out forwards}
.splash .logos{display:flex;align-items:center;gap:0;position:relative;padding:30px 40px}
.splash .logos:before{content:"";position:absolute;inset:-30px -50px;border-radius:50%;background:radial-gradient(ellipse at center,rgba(255,255,255,.95) 0%,rgba(255,255,255,.75) 40%,rgba(255,255,255,0) 72%);z-index:-1}
.splash .lgo{height:46px;max-width:40vw;object-fit:contain;opacity:0;will-change:transform,opacity}
.splash .lgo.lglogo{animation:sp-in-l .9s cubic-bezier(.2,.8,.2,1) .35s forwards}
.splash .lgo.ets{animation:sp-in-r .9s cubic-bezier(.2,.8,.2,1) .85s forwards}
.splash .x{width:0;height:2px;margin:0 16px;flex:none;background:linear-gradient(90deg,#A50034,#00806F);border-radius:2px;opacity:0;animation:sp-line .7s ease-out 1.5s forwards}
.splash .tag{margin-top:26px;text-align:center;opacity:0;transform:translateY(10px);animation:sp-up .8s ease-out 2.0s forwards;position:relative;padding:14px 28px}
.splash .tag:before{content:"";position:absolute;inset:-10px -30px;border-radius:50%;background:radial-gradient(ellipse at center,rgba(255,255,255,.95) 0%,rgba(255,255,255,.7) 45%,rgba(255,255,255,0) 75%);z-index:-1}
.splash .tag b{display:block;font-size:22px;font-weight:900;color:#0b1f1b;letter-spacing:-.3px;letter-spacing:-.2px}
.splash .tag small{display:block;margin-top:7px;font-size:14px;font-weight:500;color:#1f3d36}
.splash .skip{position:absolute;bottom:max(28px,env(safe-area-inset-bottom));font-size:12px;color:#6f7d77;text-align:center;line-height:1.7;opacity:0;animation:sp-up .6s ease-out 1.2s forwards}
.splash.out{animation:sp-out .75s ease-in forwards}
@keyframes sp-glow{0%{transform:scale(.4);opacity:0}40%{opacity:1}100%{transform:scale(1.6);opacity:.6}}
@keyframes sp-in-l{0%{opacity:0;transform:translateX(-40px) scale(.9)}100%{opacity:1;transform:none}}
@keyframes sp-in-r{0%{opacity:0;transform:translateX(40px) scale(.9)}100%{opacity:1;transform:none}}
@keyframes sp-line{0%{width:0;opacity:0}100%{width:28px;opacity:1}}
@keyframes sp-up{to{opacity:1;transform:none}}
@keyframes sp-out{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(1.18)}}
@media (prefers-reduced-motion:reduce){.splash *{animation-duration:.01s!important;animation-delay:0s!important}}
/* ---- 새 홈/검색 ---- */
.hsearch{background:#fff;border-radius:16px;padding:14px;box-shadow:0 2px 10px rgba(0,0,0,.08);margin-bottom:12px}
.hsearch h2{margin:0 0 10px;font-size:19px;line-height:1.3}
.hsearch .sbox{margin-bottom:10px}
.topics{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.topics button{background:var(--g3);border-radius:12px;padding:10px 4px 8px;font-size:12px;color:var(--ink);display:flex;flex-direction:column;align-items:center;gap:3px;line-height:1.2}
.topics button span{font-size:22px}
.hero2{display:flex;align-items:center;gap:12px;background:linear-gradient(135deg,#00806F,#0A5A4E);color:#fff;border-radius:16px;padding:14px 16px;margin-bottom:12px;text-align:left;width:100%}
.hero2 .i{font-size:30px;flex:none}
.hero2 b{display:block;font-size:16px}
.hero2 small{opacity:.9;font-size:12.5px;display:block;margin-top:2px}
.hero2 .go{margin-left:auto;background:#fff;color:var(--g);border-radius:10px;padding:8px 12px;font-weight:700;font-size:13px;flex:none}
.acc{background:#fff;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.06);margin-bottom:10px;overflow:hidden}
.acc>button{width:100%;background:none;text-align:left;padding:14px 16px;display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;color:var(--ink)}
.acc>button .ar{margin-left:auto;color:var(--mute);transition:transform .2s}
.acc.open>button .ar{transform:rotate(90deg)}
.acc .bd{display:none;padding:0 16px 14px}
.acc.open .bd{display:block}
.emg{display:flex;gap:8px;margin-bottom:12px}
.emg a{flex:1;background:#fff;border-radius:12px;padding:10px 12px;text-decoration:none;color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,.06);display:flex;align-items:center;gap:8px;font-size:13px}
.emg a b{display:block;font-size:14px;color:var(--red);white-space:nowrap}
.emg a span{min-width:0}
.ctr{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);font-size:14px}
.ctr span{min-width:0;line-height:1.35}.ctr span small{display:block;font-size:12.5px;color:var(--mute)}
.ctr b{color:var(--g);white-space:nowrap;flex-shrink:0}
.emg.sp a b{color:var(--g)}
/* 답변 카드 */
.gcard{background:#fff;border-radius:16px;box-shadow:0 2px 8px rgba(0,0,0,.07);margin-bottom:12px;overflow:hidden}
.gcard .gh{padding:16px 16px 12px;display:flex;gap:12px;align-items:flex-start}
.gcard .gh .ic{font-size:34px;line-height:1;flex:none}
.gcard .gh h2{margin:0;font-size:19px;line-height:1.25}
.gcard .gh p{margin:4px 0 0;font-size:14px;color:var(--red);font-weight:700;line-height:1.4}
.gsec{padding:10px 16px 4px}
.gsec h5{margin:0 0 6px;font-size:13px;letter-spacing:.2px;display:flex;align-items:center;gap:6px}
.gsec.do h5{color:#1B6E4A}.gsec.dont h5{color:var(--red)}.gsec.viol h5{color:var(--amber)}
.gsec ul{margin:0;padding:0;list-style:none}
.gsec li{position:relative;padding-left:22px;margin:0 0 7px;font-size:14.5px;line-height:1.5}
.gsec li:before{position:absolute;left:0;top:1px;font-size:14px}
.gsec.do li:before{content:"✓";color:#1B6E4A;font-weight:900}
.gsec.dont li:before{content:"✕";color:var(--red);font-weight:900}
.gsec.viol li:before{content:"!";color:var(--amber);font-weight:900;left:4px}
.gsec.viol{background:var(--amber-bg);margin:8px 12px 0;border-radius:10px;padding:10px 12px}
.gsec.viol li{font-size:13.5px;margin-bottom:5px}
.chip{display:inline-block;font-size:11.5px;font-weight:700;padding:1px 7px;border-radius:999px;background:var(--red-bg);color:var(--red);vertical-align:middle;margin:0 1px;white-space:nowrap}
.chip.pt{background:#eef1ef;color:var(--ink)}
.chip.red{background:var(--red);color:#fff}
.gimg{margin:10px 16px 0;border-radius:10px;overflow:hidden;background:#eef1ef}
.gimg img{width:100%;display:block}
.gfoot{padding:12px 16px 14px}
.gfoot .btn{margin-top:6px}
.refs{font-size:12.5px;color:var(--mute);display:flex;flex-wrap:wrap;gap:4px;align-items:center}
.refs span{background:#f1f4f2;border-radius:6px;padding:2px 7px;color:var(--ink)}
.sugg{background:#fff;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.08);margin:-6px 0 12px;overflow:hidden}
.sugg button{display:block;width:100%;text-align:left;background:none;padding:11px 14px;border-bottom:1px solid var(--line);font-size:14.5px;color:var(--ink)}
.sugg button b{color:var(--g)}
.sugg button small{color:var(--mute);margin-left:6px;font-size:12px}
.more-list button{width:100%;background:#fff;border-radius:12px;padding:14px 16px;text-align:left;box-shadow:0 1px 3px rgba(0,0,0,.06);margin-bottom:8px;display:flex;align-items:center;gap:12px;font-size:15px;color:var(--ink)}
.more-list button span{font-size:22px}
.more-list button small{display:block;color:var(--mute);font-size:12px;font-weight:400;margin-top:1px}
.more-list button i{margin-left:auto;font-style:normal;color:var(--mute)}
'''

# 기존 CSS에서 .topics 등 충돌 없음. hero 등은 유지(교육 인트로에서 미사용).
html = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>고객사 현장 안전 길잡이 — ETS</title>
<meta name="theme-color" content="#00806F">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
''' + css + extra_css + '''</style>
</head>
<body>
<div class="splash hid" id="splash" onclick="endSplash(true)">
  <div class="glow"></div>
  <div class="logos"><img class="lgo lglogo" src="img/lg_logo.png" alt="LG"><div class="x"></div><img class="lgo ets" src="img/ets_logo.png" alt="ETS"></div>
  <div class="tag"><b>함께 만드는 안전한 현장</b><small>고객사 현장 안전 길잡이 · 주식회사 이티에스</small></div>
  <div class="skip"><span id="spVer"></span><br>화면을 누르면 건너뜁니다</div>
</div>
<div class="app">
  <header class="top">
    <div class="logo"><img src="img/ets_logo_white.png" alt="ETS" onerror="this.outerHTML='<span class=wm>ETS</span>'"></div>
    <div class="t">고객사 현장 안전 길잡이<small>출입 전 교육 · 작업수칙 검색</small></div>
    <div class="hbtns"><button class="back hid" id="backBtn" onclick="goBack()">‹ <span class="bt">뒤로</span></button><a class="home" href="https://sugilyang.github.io/ets-safety/" title="ETS 안전포털">🏠</a></div>
  </header>
  <main id="main"></main>
  <nav class="nav"><div class="w">
    <button data-v="home" onclick="go('home')"><svg viewBox="0 0 24 24"><path d="M3 11l9-8 9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>홈</button>
    <button data-v="search" onclick="go('search')"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>검색</button>
    <button data-v="train" onclick="go('train')"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg>교육</button>
    <button data-v="more" onclick="go('more')"><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg>더보기</button>
  </div></nav>
</div>
<div class="toast" id="toast"></div>
<script src="data.js?v=__DATAV__"></script>
<script>
/* ===== 설정 ===== */
const GAS_URL = \'''' + GAS + '''\'; // GAS 웹앱 URL (교육이수 기록·설정값 전용)
const IMG = 'img/';
/* 내용(가이드·규정·슬라이드·벌점표)은 data.js 에 있습니다. 매달 업데이트 = data.js 교체 */
let D = null, view = 'home', T = {};
const $ = s => document.querySelector(s);
const esc = s => String(s==null?'':s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function verLine(dev){ const v=D.version||{}; return `주식회사 이티에스 · ${esc(v['버전']||'')}<br>최초 개발 ${esc((v['최초개발']||'').replace(/-/g,'.'))} · 최근 업데이트 ${esc((v['배포일']||'').replace(/-/g,'.'))}<br>${esc(v['자료기준']||'')}<br>최근 반영 ${esc(v['최근반영']||'')}${dev?`<br><span class="dev">개발 · ${esc(v['개발']||'')}</span>`:''}`; }
function prereport(small){ const r=(D.version||{}).prereport||{}; if(!r.EP1) return ''; return `<div class="prer${small?' sm':''}"><div class="ph">📲 7대 고위험 사전신고방 <small>공사 전일 14~15시 · 참여코드 <b>${esc(r.code)}</b></small></div><div class="pb"><a href="${r.EP1}" target="_blank" rel="noopener">EP1 신고방 열기</a><a href="${r.EP2}" target="_blank" rel="noopener">EP2 신고방 열기</a></div></div>`; }
function dash(t){ const a=esc(t).split(' — '); return a.length>1 ? a.map(x=>`<span style="white-space:nowrap">${x}</span>`).join(' — ') : esc(t); }
// **굵게** 와 |칩| 표기 → HTML
const rich0 = s => esc(s).replace(/\\*\\*(.+?)\\*\\*/g,'<b>$1</b>').replace(/\\|([^|]+?)\\|/g,(m,t)=>`<span class="chip ${/점$/.test(t)?'pt':(/퇴출|거래제한/.test(t)?'red':'')}">${t}</span>`);
// 현장용 자동 강조: 금지·중지 계열은 빨강, 필수 계열은 청록, 수치+단위는 굵게 (태그·칩 내부는 건드리지 않음)
const HL_RED = /(영구\s?퇴출|퇴출|작업\s?중지|전면\s?중지|즉시\s?중지|거래\s?제한|입찰\s?제한|중지|금지|불가|절대|즉시|위반)/g;
const HL_REQ = /(반드시|필수|2인\s?1조|사전\s?신고|허가서|그네식|화재감시자|신호수|LOTO)/g;
const HL_NUM = /(\d+(?:\.\d+)?\s?(?:~\s?\d+(?:\.\d+)?\s?)?(?:m|M|mm|cm|kg|ton|T|t|점|시간|시|분|초|회|개|℃|%|km\/h|배|층|명|일))(?![\w가-힣])/g;
function hlText(t){ return t.replace(HL_RED,'<em class="hr">$1</em>').replace(HL_REQ,'<em class="hq">$1</em>').replace(HL_NUM,'<em class="hn">$1</em>'); }
function hlHtml(html){ let out='', inChip=0; html.split(/(<[^>]+>)/).forEach(seg=>{ if(!seg) return; if(seg[0]==='<'){ if(/^<span class="chip/.test(seg)||/^<em/.test(seg)) inChip++; else if(/^<\/(span|em)>/.test(seg)&&inChip) inChip--; out+=seg; } else out+= inChip?seg:hlText(seg); }); return out; }
const rich = s => hlHtml(rich0(s));
// "머리말 1) … 2) … ① … ②" 처럼 한 줄에 이어진 번호 항목을 줄 단위로 분리
function splitNumbered(t){
  const parts=String(t).split(/\s+(?=(?:\d{1,2}\)|[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮])\s*)/);
  if(parts.length<2) return {head:t, subs:[]};
  const first=parts[0]; const isHead=!/^(\d{1,2}\)|[①-⑮])/.test(first.trim());
  return isHead ? {head:first, subs:parts.slice(1)} : {head:'', subs:parts};
}
function liRich(x, cls){ const {head,subs}=splitNumbered(x); if(!subs.length) return `<li class="${cls||''}">${rich(x)}</li>`;
  return `<li class="${cls||''}">${head?rich(head):''}<ul class="sub">${subs.map(z=>`<li>${rich(z)}</li>`).join('')}</ul></li>`; }
const toast = m => { const t=$('#toast'); t.textContent=m; t.classList.add('show'); clearTimeout(t._h); t._h=setTimeout(()=>t.classList.remove('show'),2600); };
const setting = (k,def) => (D && D.settings && D.settings[k]!==undefined && D.settings[k]!=='') ? D.settings[k] : def;
const pd = d => { const m=String(d||'').match(/(\\d{4})-(\\d{2})-(\\d{2})/); return m? new Date(+m[1],+m[2]-1,+m[3]) : new Date(d); };
const daysSince = d => { if(!d) return 9e9; return Math.round((Date.now()-pd(d))/86400000); };
const isNew = d => { const n=daysSince(d); return n>=-400 && n<=Number(setting('변경됨_표시_일수',45)); };
const fmt = d => String(d||'').slice(0,10);
const hasGas = () => GAS_URL.startsWith('http');

async function loadData(){
  D = window.FALLBACK_DATA; render();
  if(!hasGas()) return;
  try{ // 서버에서는 설정값만 받아옴 (장당_초, 유효기간 등)
    const r = await fetch(GAS_URL+'?action=data', {cache:'no-store'}); const j = await r.json();
    if(j && j.settings && Object.keys(j.settings).length){ D.settings = Object.assign({}, D.settings, j.settings); if(view!=='train') render(); }
  }catch(e){ console.warn('settings fetch fail', e); }
}
// 화면 이동을 브라우저 기록에 연결: 폰 뒤로가기 = 앱 뒤로가기 (홈에서 한 번 더 누르면 앱을 나감)
const snap = () => ({view, arg:T.arg, q:T.q, chip:T.chip, pcat:T.pcat});
function apply(h){ view=h.view; T.arg=h.arg; T.q=h.q; T.chip=h.chip; T.pcat=h.pcat; render(); window.scrollTo(0,0); }
function go(v, arg){ const same = (v===view && !arg); if(!same){ try{ history.replaceState(snap(), ''); }catch(e){} } view=v; T.arg=arg; if(!same){ try{ history.pushState(snap(), ''); }catch(e){} } render(); window.scrollTo(0,0); }
function goBack(){ if(history.state && history.state.view){ history.back(); } else { apply({view:'home'}); try{ history.replaceState(snap(), ''); }catch(e){} } }
window.addEventListener('popstate', e => { apply((e.state && e.state.view) ? e.state : {view:'home'}); });
try{ history.replaceState({view:'home'}, ''); }catch(e){}
function render(){
  const navMap={home:'home',search:'search',guide:'search',train:'train',result:'train',more:'more',ops:'more',penalty:'more',detail:'more',status:'more'};
  document.querySelectorAll('.nav button').forEach(b=>b.classList.toggle('on', b.dataset.v===navMap[view]));
  $('#backBtn').classList.toggle('hid', view==='home');
  const m=$('#main');
  if(view==='home') m.innerHTML=homeView();
  else if(view==='search'){ m.innerHTML=searchView(); const i=$('#q'); if(i){ i.value=T.q||''; i.oninput=()=>{T.q=i.value; renderResults();}; i.onkeydown=e=>{ if(e.key==='Enter'){ i.blur(); } }; renderResults(); if(T.focus){ i.focus(); T.focus=false; } } }
  else if(view==='guide') m.innerHTML=guideView();
  else if(view==='train') m.innerHTML=trainView();
  else if(view==='more') m.innerHTML=moreView();
  else if(view==='ops') m.innerHTML=opsView();
  else if(view==='penalty') m.innerHTML=penaltyView();
  else if(view==='detail') m.innerHTML=detailView();
  else if(view==='status') m.innerHTML=statusView();
  if(view==='train' && T.started && !T.finished) startTimer();
}
const TOPICS = () => (D.guides||[]).slice(0,12);


/* ===== 스플래시: 하루 첫 실행 또는 ?splash ===== */
function showSplash(){
  const el=$('#splash'); if(!el) return;
  if(/[?&]nosplash/.test(location.search)) return; // 시연·점검용으로 끌 때만
  const v=(window.FALLBACK_DATA&&window.FALLBACK_DATA.version)||{}; const ve=$('#spVer'); if(ve) ve.innerHTML=`${esc(v['버전']||'')} · 최초 개발 ${esc((v['최초개발']||'').replace(/-/g,'.'))} · 최근 업데이트 ${esc((v['배포일']||'').replace(/-/g,'.'))}<br>${esc(v['자료기준']||'')} · 최근 반영 ${esc(v['최근반영']||'')}`;
  el.classList.remove('hid'); document.body.style.overflow='hidden';
  T.splashTimer=setTimeout(()=>endSplash(false), 3400);
}
function endSplash(skip){
  const el=$('#splash'); if(!el||el.classList.contains('hid')||el.classList.contains('out')) return;
  clearTimeout(T.splashTimer); el.classList.add('out');
  setTimeout(()=>{ el.classList.add('hid'); document.body.style.overflow=''; }, skip?300:750);
}

/* ===== 홈 ===== */
function homeView(){
  const os = D.onestrike.filter(r=>r['구분']==='One Strike Out');
  return `
  <div class="hsearch">
    <h2>어떤 작업 하세요?</h2>
    <div class="sbox"><input id="hq" placeholder="예: 사다리, 그라인더, 지게차, LOTO" onfocus="T.focus=true;go('search')"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></div>
    <div class="topics">${TOPICS().map(g=>`<button onclick="go('guide','${g.id}')"><span>${g['아이콘']}</span>${esc(g['짧은이름']||g['제목'])}</button>`).join('')}</div>
  </div>
  <button class="hero2" onclick="go('train')"><span class="i">▶</span><span><b>처음 출입이면 교육부터</b><small>${D.slides.length}장 · 약 ${Math.ceil(D.slides.length*Number(setting('장당_초',30))/60)}분 · 이수 후 ${esc(setting('유효기간_개월',6))}개월 유효</small></span><span class="go">시작</span></button>
  <div class="acc" id="accOS"><button onclick="this.parentNode.classList.toggle('open')"><span><span style="white-space:nowrap">⛔ 1회 적발 시 바로 퇴출</span> — <span style="white-space:nowrap">7가지</span></span><span class="ar">›</span></button>
    <div class="bd"><ol class="list" style="font-size:14px">${os.map(r=>`<li>${esc(r['위반내역'])}</li>`).join('')}</ol>
    <p style="margin:8px 0 0;font-size:13px;color:var(--mute)">근로자 영구 퇴출 · 회사 거래제한 (26.10.1 시행, LG에너지솔루션 One Strike Out)</p></div></div>
  <div class="sec" style="margin-top:4px">🚨 비상신고 — 화재·사고·누출 시 즉시</div>
  <div class="emg" title="누르면 전화"><a href="tel:0432197119">☎<span>방재센터 EP1<b>043-219-7119</b></span></a><a href="tel:0437180119">☎<span>방재센터 EP2<b>043-718-0119</b></span></a></div>
  <div class="sec">📞 작업·허가서·안전 문의 — Safety Police</div>
  <div class="emg sp"><a href="tel:01054873122">☎<span>EP1 이상억 팀장<b>010-5487-3122</b></span></a><a href="tel:01098006229">☎<span>EP2 변귀림 팀장<b>010-9800-6229</b></span></a></div>
  <p style="font-size:12px;color:var(--mute);margin:-4px 2px 12px">비상 외 안전 문의는 환경안전팀이 아닌 Safety Police로 연락하세요. 총괄·주정차 문의는 더보기에 있습니다.</p>
  <p class="foot">${verLine()}</p>`;
}

/* ===== 검색 ===== */
function norm(s){ return String(s||'').toLowerCase().replace(/\\s+/g,''); }
function hit(q, ...fields){ if(!q) return true; const qs=norm(q).split(/[,\\/]/).filter(Boolean); const hay=norm(fields.join(' ')); return qs.some(x=>hay.includes(x)); }
function searchView(){
  if(T.arg){ T.q=T.arg; T.arg=null; }
  return `<div class="sbox"><input id="q" placeholder="작업명으로 검색 (예: 사다리, 용접, 지게차)"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></div>
  <div id="sugg"></div><div class="res" id="res"></div>`;
}
function guideScore(g,q){ const n=norm(q); if(!n) return 0; let s=0; if(norm(g['제목']).includes(n)) s+=100; if(norm(g['검색어']).split(',').some(w=>w.includes(n)||n.includes(w)&&w.length>1)) s+=60; if(norm(g['한줄']).includes(n)) s+=20; if(norm(g['하세요'].join(' ')+g['금지'].join(' ')).includes(n)) s+=10; return s; }
function renderResults(){
  const box=$('#res'), sg=$('#sugg'); if(!box) return; const q=(T.q||'').trim();
  if(!q){ sg.innerHTML=''; box.innerHTML=`<div class="sec">자주 찾는 작업</div><div class="card" style="padding:12px"><div class="topics" style="grid-template-columns:repeat(3,1fr)">${(D.guides||[]).map(g=>`<button onclick="go('guide','${g.id}')"><span>${g['아이콘']}</span>${esc(g['제목'])}</button>`).join('')}</div></div>`; return; }
  const G=(D.guides||[]).map(g=>[guideScore(g,q),g]).filter(x=>x[0]>0).sort((a,b)=>b[0]-a[0]).map(x=>x[1]);
  sg.innerHTML = G.length>1 ? `<div class="sugg">${G.slice(0,5).map(g=>`<button onclick="go('guide','${g.id}')">${g['아이콘']} <b>${esc(g['제목'])}</b><small>${dash(g['한줄'])}</small></button>`).join('')}</div>` : '';
  let html='';
  if(G.length){ html+=guideCard(G[0], false); if(G.length>1) html+=`<div class="sec">관련 작업</div>`+G.slice(1,4).map(g=>`<div class="card" style="padding:12px 14px;cursor:pointer" onclick="go('guide','${g.id}')"><b>${g['아이콘']} ${esc(g['제목'])}</b><div style="font-size:13px;color:var(--mute)">${dash(g['한줄'])}</div></div>`).join(''); }
  // 가이드가 없을 때만 규정·벌점 직접 검색
  if(!G.length){
    const O=(D.ops||[]).filter(o=>hit(q,o['코드'],o['제목'],o['분류'],o['연관검색어'],o['내용']));
    if(O.length) html+='<div class="sec">LG 규정 원문</div><div class="ops">'+O.slice(0,5).map(o=>opsCard(o,false)).join('')+'</div>';
    const P=D.penalty.filter(p=>hit(q,p['대분류'],p['세부항목'],p['키워드'],p['코드']));
    if(P.length) html+='<div class="sec">벌점표</div>'+P.slice(0,8).map(p=>penaltyCard(p)).join('');
    const C=D.common.filter(c=>hit(q,c['구분'],c['항목'],c['내용']));
    if(C.length) html+='<div class="sec">사업장 공통수칙</div>'+C.map(c=>`<div class="card"><h4>${esc(c['항목'])}</h4><p>${esc(c['내용'])}</p><div class="src">${esc(c['출처'])}</div></div>`).join('');
  }
  if(!html) html=`<div class="empty">"${esc(q)}" 검색 결과가 없습니다.<br><span style="font-size:13px">작업 이름(예: 사다리, 용접, 지게차)으로 검색하거나 아래 목록에서 골라 보세요.</span></div><div class="card" style="padding:12px"><div class="topics" style="grid-template-columns:repeat(3,1fr)">${(D.guides||[]).map(g=>`<button onclick="go('guide','${g.id}')"><span>${g['아이콘']}</span>${esc(g['제목'])}</button>`).join('')}</div></div>`;
  box.innerHTML=html;
}
function guideCard(g, full){
  const pens=(g['벌점코드']||[]).map(c=>D.penalty.find(p=>p['코드']===c)).filter(Boolean);
  const opsL=(g['근거OPS']||[]).map(c=>(D.ops||[]).find(o=>o['코드']===c)).filter(Boolean);
  const li=(arr,cls)=>`<ul>${arr.map(x=>liRich(x)).join('')}</ul>`;
  return `<div class="gcard">
    <div class="gh"><span class="ic">${g['아이콘']}</span><div><h2>${esc(g['제목'])}</h2><p>${dash(g['한줄'])}</p></div></div>
    <div class="gsec do"><h5>✅ 이렇게 하세요</h5>${li(g['하세요'])}</div>
    <div class="gsec dont"><h5>⛔ 하면 안 됩니다</h5>${li(g['금지'])}</div>
    ${g['위반']&&g['위반'].length?`<div class="gsec viol"><h5>⚠️ 위반하면</h5>${li(g['위반'])}</div>`:''}
    ${g['고위험']?prereport(true):''}
    ${g['이미지']?`<div class="gimg"><img src="${IMG}${esc(g['이미지'])}" alt="" loading="lazy"></div>`:''}
    <div class="gfoot">
      ${opsL.length||pens.length?`<div class="refs">근거 ${opsL.map(o=>`<span>${esc(o['코드'])} ${esc(o['제목'])}</span>`).join('')}${pens.map(p=>`<span>벌점표 ${esc(p['코드'])}</span>`).join('')}</div>`:''}
      ${opsL.length?`<button class="btn ghost" onclick="go('guide','${g.id}');setTimeout(()=>{const e=document.getElementById('gops');if(e){e.classList.add('open');e.scrollIntoView({behavior:'smooth'});}},50)">📄 LG 원문 보기 (${opsL.length}건)</button>`:''}
      ${!full?`<button class="btn" style="margin-top:8px" onclick="go('guide','${g.id}')">자세히 보기</button>`:''}
    </div>
  </div>`;
}
function guideView(){
  const g=(D.guides||[]).find(x=>x.id===T.arg) || (D.guides||[])[0]; if(!g) return '<div class="empty">가이드가 없습니다</div>';
  const opsL=(g['근거OPS']||[]).map(c=>(D.ops||[]).find(o=>o['코드']===c)).filter(Boolean);
  const pens=(g['벌점코드']||[]).map(c=>D.penalty.find(p=>p['코드']===c)).filter(Boolean);
  const rel=(D.guides||[]).filter(x=>x.id!==g.id && (x['근거OPS']||[]).some(c=>(g['근거OPS']||[]).includes(c))).slice(0,3);
  return guideCard(g,true)
   + (opsL.length?`<div class="acc" id="gops"><button onclick="this.parentNode.classList.toggle('open')">📄 LG 규정 원문 (${opsL.length}건)<span class="ar">›</span></button><div class="bd"><div class="ops" style="margin-top:6px">${opsL.map(o=>opsCard(o,true)).join('')}</div></div></div>`:'')
   + (pens.length?`<div class="acc"><button onclick="this.parentNode.classList.toggle('open')">⚠️ 관련 벌점 항목 (${pens.length})<span class="ar">›</span></button><div class="bd">${pens.map(p=>penaltyCard(p)).join('')}</div></div>`:'')
   + (rel.length?`<div class="sec">함께 보면 좋은 작업</div>${rel.map(x=>`<div class="card" style="padding:12px 14px;cursor:pointer" onclick="go('guide','${x.id}')"><b>${x['아이콘']} ${esc(x['제목'])}</b><div style="font-size:13px;color:var(--mute)">${dash(x['한줄'])}</div></div>`).join('')}`:'');
}

function penaltyCard(p){
  const up = p['변경']==='상향'||p['변경']==='신설';
  return `<div class="card"><div class="ptrow"><div><div class="tag"><span class="pill gray">${esc(p['코드'])} ${esc(p['대분류'])}</span>${p['작업중지']?'<span class="pill red">작업중지</span>':''}${up?`<span class="pill amber">${esc(p['변경'])}</span>`:''}</div><h4 style="margin:0">${esc(p['세부항목'])}</h4></div><div class="pt">${esc(p['감점'])}<small>점</small></div></div>
  ${up?`<p class="sub" style="margin-top:6px">26.7.1 개정 전 ${esc(p['구감점_25년9월'])}점 → <b>${esc(p['감점'])}점</b></p>`:''}<div class="src">${esc(p['출처'])}</div></div>`;
}

/* ===== 더보기 ===== */
function moreView(){
  const items=[['📄','LG 규정 원문 (OPS)','협의체에 공유된 운영표준 '+(D.ops||[]).length+'건, 원문 페이지 보기','ops'],['⚠️','벌점표','위반 항목별 감점·작업중지 ('+D.penalty.length+'항목)','penalty'],['↻','규정 변경 이력 · 월별 강조사항','언제 무엇이 바뀌었는지','detail'],['✓','내 교육 이수 확인','이름 또는 연락처 뒤 4자리로 조회','status']];
  const portalBtn=`<button onclick="location.href='https://sugilyang.github.io/ets-safety/'"><span>🏠</span><div><div style="font-weight:700">ETS 안전포털</div><small>안전신문고 · TBM · 위험성평가 등</small></div><i>›</i></button>`;
  const adminBtn=`<button onclick="location.href='admin.html'"><span>🔐</span><div><div style="font-weight:700">관리자 · 교육 이수 현황</div><small>생산관리 전용 · 비밀번호 필요</small></div><i>›</i></button>`;
  const changes=[...D.changes].sort((a,b)=>b['시행일']<a['시행일']?-1:1).slice(0,2);
  return `<div class="more-list">${items.map(([i,t,s,v])=>`<button onclick="go('${v}')"><span>${i}</span><div><div style="font-weight:700">${t}</div><small>${s}</small></div><i>›</i></button>`).join('')}${adminBtn}${portalBtn}</div>
  <div class="sec">연락처 (누르면 전화)</div>
  <div class="card" style="padding:6px 14px">
    ${[['🚨 비상 — 화재·사고·누출 즉시 신고','방재센터 EP1','','043-219-7119'],['','방재센터 EP2','','043-718-0119'],['📞 작업·안전 문의, 교육 협의','Safety Police EP1','이상억 팀장','010-5487-3122'],['','Safety Police EP2','변귀림 팀장','010-9800-6229'],['안전 지도·법규·KOSHA 문의','Safety Police 총괄','곽충호 소장','010-3871-7939'],['주·정차 관련','LG 사무실','','043-718-0123']].map(([h,n,s,t])=>`${h?`<div style="font-size:12px;color:var(--mute);margin:10px 0 2px;font-weight:700">${h}</div>`:''}<a href="tel:${t.replace(/-/g,'')}" class="ctr"><span>${n}${s?`<small>${s}</small>`:''}</span><b>☎ ${t}</b></a>`).join('')}
    <div class="src">26년 5·7·8월 협의체 "공사 안전 관련 문의 사항 안내" · 이메일 ssmteam@lgensol.com / kch1004@lgensol.com</div>
  </div>
  <div class="sec">작업시간 · 사전신고</div>
  <div class="card"><div class="kv">
    <b>작업 시작</b><span>09:00<br><small>LG 담당자 협의 시 06:00~09:00</small></span>
    <b>연장 작업</b><span>17~22시<br><small>일반은 당일 17시, 크레인은 당일 13시까지 승인 · 고위험 불가</small></span>
    <b>주말 허가서</b><span>08~09시 / 13~13:30 발급<br><small>작업은 08시부터</small></span>
    <b>7대 고위험</b><span>전일 14~15시 사전신고방 <span style="white-space:nowrap">(코드 2119)</span><br><small>3m↑고소 · 화기 · 활성화 · 전기실 · 밀폐 · 고중량</small></span>
  </div>${prereport(false)}<div class="kv" style="display:none">
  </div></div>
  <div class="sec">최근 규정 변경</div>
  ${changes.map(c=>`<div class="card" style="padding:12px 14px"><span style="font-size:12px;color:var(--mute)">${esc(c['시행일'])}</span> ${isNew(c['시행일'])?'<span class="pill red">변경됨</span>':''}<div style="font-size:14px;margin-top:2px">${esc(c['내용'])}</div></div>`).join('')}
  <p class="foot">${verLine(true)}</p>`;
}
function statusView(){
  return `<div class="card"><h3><span class="ic">✓</span>내 교육 이수 상태</h3>
    <div class="row"><input id="chk" placeholder="이름 또는 연락처 뒤 4자리" style="flex:1;padding:11px 12px;border:1.5px solid var(--line);border-radius:10px"><button class="btn sm" onclick="checkMe()">조회</button></div>
    <div id="chkRes" style="margin-top:8px;font-size:13.5px"></div></div>`;
}
async function checkMe(){
  const q=$('#chk').value.trim(); const box=$('#chkRes'); if(!q) return;
  if(!hasGas()){ box.innerHTML='<span class="pill gray">서버 연결 전</span>'; return; }
  box.textContent='조회 중…';
  try{ const r=await fetch(GAS_URL+'?action=check&q='+encodeURIComponent(q)); const j=await r.json();
    if(!j.rows||!j.rows.length){ box.innerHTML='<span class="pill gray">기록 없음</span> 교육 이수 기록이 없습니다.'; return; }
    box.innerHTML=j.rows.map(r=>{ const left=Math.round((pd(r['만료일'])-new Date().setHours(0,0,0,0))/86400000); const st=left<0?'<span class="pill red">만료</span>':left<=30?'<span class="pill amber">만료 임박</span>':'<span class="pill">유효</span>';
      return `<div style="padding:6px 0;border-bottom:1px solid var(--line)">${st} <b>${esc(r['이름'])}</b> (${esc(r['업체명'])}) · 이수 ${esc(fmt(r['이수일시']))} · 만료 <b>${esc(fmt(r['만료일']))}</b></div>`; }).join('');
  }catch(e){ box.textContent='조회 실패. 네트워크를 확인하세요.'; }
}
function detailView(){
  const ch=[...D.changes].sort((a,b)=>b['시행일']<a['시행일']?-1:1);
  const hl=[...D.highlights].sort((a,b)=>b['월']<a['월']?-1:1);
  return `<div class="sec">규정 변경 이력</div><div class="card" style="padding:8px 16px">${ch.map(c=>`<div style="display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--line);font-size:14px"><span style="flex:none;color:var(--mute);font-size:12.5px;width:84px;padding-top:2px">${esc(c['시행일'])}</span><span>${esc(c['내용'])} ${isNew(c['시행일'])?'<span class="pill red">변경됨</span>':''}<div style="font-size:11.5px;color:var(--mute)">${esc(c['출처'])}</div></span></div>`).join('')}</div>
  <div class="sec">월별 협의체 강조사항</div>${hl.map(h=>`<div class="card" style="padding:12px 14px"><div class="tag"><span class="pill gray">${esc(h['월'])}</span></div><h4 style="margin:4px 0 6px;font-size:14.5px">${esc(h['제목'])}</h4><p style="margin:0;font-size:13.5px">${esc(h['내용'])}</p><div class="src">${esc(h['출처'])}</div></div>`).join('')}`;
}

''' + train + ops_fn + pen + '''
showSplash(); loadData(); setTimeout(flushQueue, 2000);
</script>
</body>
</html>
'''
# 교육 완료 후 홈 이동 등 기존 코드 내 go('home') 호환 OK. 교육 인트로의 'go("train")' 그대로.
import json as _j; _v=_j.load(open(base+'data.json',encoding='utf-8'))['version']
html=html.replace('__DATAV__', _v['버전'].lstrip('v')+'.'+_v['배포일'].replace('-',''))
open(base+'out/index.html','w',encoding='utf-8').write(html)
print('written', len(html))
