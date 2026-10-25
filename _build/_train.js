/* ===== 교육 ===== */
function trainView(){
  const n=D.slides.length, sec=Number(setting('장당_초',30));
  if(T.finished) return doneView();
  if(!T.started){
    return `<div class="card">
      <h3><span class="ic">▶</span>LGES 현장 출입 전 안전교육</h3>
      <p style="margin:0 0 10px;font-size:14px">LG에너지솔루션 협의체 자료와 내규에서 가장 중요한 내용만 ${n}장으로 정리했습니다. 한 장당 <b>${sec}초</b> 이상 읽어야 다음 장으로 넘어갑니다.</p>
      <ul class="list" style="font-size:14px;color:var(--mute)">
        <li>소요시간 약 ${Math.ceil(n*sec/60)}분 · 중간에 나가면 처음부터 다시 시작</li>
        <li>마지막에 이름·업체명·연락처·이메일을 입력하면 이수 처리</li>
        <li>유효기간 ${esc(setting('유효기간_개월',6))}개월 · 만료 전 이메일로 재교육 안내</li>
      </ul>
      <button class="btn" style="margin-top:14px" onclick="startTrain()">교육 시작</button>
    </div>
    <div class="sec">교육 내용</div>
    <div class="card" style="padding:8px 16px">${D.slides.map((s,i)=>`<div style="display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--line);font-size:14px"><b style="color:var(--g);width:22px;flex:none">${i+1}</b>${esc(s['제목'])}</div>`).join('')}</div>`;
  }
  const s=D.slides[T.i]; const items=String(s['본문']).split('|').map(x=>x.trim()).filter(Boolean);
  const nw=t=>hlHtml(esc(t).replace(/((?:EP\d\s)?\d{2,3}-\d{3,4}-\d{4})/g,'<span style="white-space:nowrap">$1</span>'));
  const li=items.map(x=>{ let cls=''; if(/^→/.test(x)) cls='arrow'; else if(/^DO:/.test(x)) cls='do'; else if(/^DON'?T:/.test(x)) cls='dont'; return `<li class="${cls}">${nw(x)}</li>`; }).join('');
  const img = s['이미지'] ? `<img src="${IMG}${esc(s['이미지'])}" alt="">` : fallbackArt(T.i);
  const r=22, c=2*Math.PI*r;
  return `<div class="prog"><i style="width:${(T.i)/n*100}%"></i></div>
  <div class="slide">
    <div class="img">${img}</div>
    <div class="body">
      <div class="no">${T.i+1} / ${n}</div>
      <h2>${dash(s['제목'])}</h2>
      <ul>${li}</ul>
      <div class="src">${esc(s['출처'])}</div>
      <div class="ctr">
        <div class="ring"><svg width="52" height="52"><circle class="bg" cx="26" cy="26" r="${r}"/><circle class="fg" id="ringFg" cx="26" cy="26" r="${r}" stroke-dasharray="${c}" stroke-dashoffset="0"/></svg><b id="ringTxt">${sec}</b></div>
        <button class="btn" id="nextBtn" disabled onclick="nextSlide()">${T.i+1<n?'다음':'교육 완료 → 정보 입력'}</button>
      </div>
    </div>
  </div>`;
}
function fallbackArt(i){
  const t=D.slides[i]['제목'];
  if(/주요안전수칙/.test(t)){
    const R=[['🔒','안전장치 임의<br>해제 금지'],['📝','작업 전<br>위험성평가'],['🚫','무허가<br>작업 금지'],['⚡','전원 OFF 후<br>LOTO'],['🏗️','중장비 정격하중<br>반경 출입금지'],['🫧','밀폐작업<br>가스 측정'],['🪢','추락방지<br>안전대'],['🔥','방화포 설치<br>화재감시자']];
    return `<div class="art"><div class="g8">${R.map((r,k)=>`<div><b>${k+1}</b><span class="e">${r[0]}</span><small>${r[1]}</small></div>`).join('')}</div><div class="cap">LG에너지솔루션 공사 안전관리 내규 — 공사 주요안전수칙</div></div>`;
  }
  if(/허가서/.test(t)) return `<div class="art"><div class="flow"><span>허가서<br>수령</span><i>→</i><span>내용<br>확인</span><i>→</i><span>교육</span><i>→</i><span>서명</span><i>→</i><span>현장<br>비치</span></div>
    <div class="stop"><b>즉시 작업중지</b><div>❌ 카페·편의점·흡연실·사무실에서 허가서 작성</div><div>❌ 현장에 맞지 않는 체크리스트에 "V" 표시</div></div><div class="cap">26년 3월 Safety Police — 안전작업허가서 실태</div></div>`;
  if(/규칙/.test(t)) return `<div class="art"><div class="g4"><div><span class="e">🕘</span><b>09:00</b><small>작업 시작<br>연장 17~22시</small></div><div><span class="e">🚗</span><b>20km/h</b><small>횡단보도 일시정지<br>운전 중 휴대폰 ✕</small></div><div><span class="e">🚭</span><b>지정장소</b><small>실내·전자담배<br>전부 금지</small></div><div><span class="e">🍺</span><b>0.03↑</b><small>음주·마약<br>영구퇴출</small></div></div></div>`;
  return `<div class="noimg"><div class="big">🦺</div></div>`;
}
function startTrain(){ T={started:true,i:0,finished:false,log:[]}; render(); }
function startTimer(){
  clearInterval(T.tm); const perSlide=Number(D.slides[T.i]['초'])||Number(setting('장당_초',30));
  if(T.slideStart===undefined || T.timerFor!==T.i){ T.slideStart=Date.now(); T.timerFor=T.i; }
  const fg=$('#ringFg'), tx=$('#ringTxt'), btn=$('#nextBtn'); if(!fg) return;
  const c=2*Math.PI*22;
  const tick=()=>{ const left=Math.max(0, perSlide-Math.floor((Date.now()-T.slideStart)/1000)); tx.textContent=left; fg.style.strokeDashoffset=c*(1-left/perSlide); if(left<=0){ clearInterval(T.tm); btn.disabled=false; tx.textContent='✓'; } };
  tick(); T.tm=setInterval(tick,500);
}
document.addEventListener('visibilitychange',()=>{ if(!document.hidden && view==='train' && T.started && !T.finished) startTimer(); });
function nextSlide(){ clearInterval(T.tm); T.log.push(Date.now()); if(T.i+1<D.slides.length){ T.i++; render(); window.scrollTo(0,0);} else { T.finished=true; render(); window.scrollTo(0,0);} }
function doneView(){
  if(T.sent) return `<div class="card done">
      <div class="ok">✓</div><h2 style="margin:0 0 6px">교육 이수 완료</h2>
      <p style="margin:0;color:var(--mute);font-size:14px"><b style="color:var(--ink)">${esc(T.sent.name)}</b>님 (${esc(T.sent.company)})</p>
      <div class="kv" style="justify-content:center;margin:14px auto 0;max-width:260px;text-align:left"><b>이수일</b><span>${fmt(new Date().toISOString())}</span><b>유효기간</b><span><b>${esc(T.sent.expire)}</b>까지</span></div>
      ${T.sent.queued?`<div class="alert" style="text-align:left;margin-top:14px"><b>통신 상태가 좋지 않아 기록을 폰에 저장했습니다.</b><br>통신이 되는 곳에서 이 앱을 다시 열면 자동으로 전송됩니다 (앱을 닫아도 기록은 폰에 남습니다). 전송되면 확인 메일이 갑니다.</div>`:`<p style="font-size:13px;color:var(--mute);margin:14px 0 0">이수 확인 메일을 ${esc(T.sent.email)}로 보냈습니다. 생산관리 확인 후 고객사 현장에 출입할 수 있습니다.</p>`}
      <button class="btn ghost" style="margin-top:14px" onclick="T={};go('home')">홈으로</button></div>`;
  return `<div class="prog"><i style="width:100%"></i></div>
  <div class="card f">
    <h3><span class="ic">✎</span>교육 이수 정보 입력</h3>
    <p style="margin:0;font-size:13.5px;color:var(--mute)">${D.slides.length}장을 모두 확인하셨습니다. 아래 정보를 입력하면 이수 처리되고 확인 메일이 발송됩니다.</p>
    <label>이름 *</label><input id="fName" autocomplete="name" placeholder="홍길동">
    <label>업체명 *</label><input id="fComp" autocomplete="organization" placeholder="주식회사 이티에스 / 협력사명">
    <label>연락처 *</label><input id="fPhone" type="tel" autocomplete="tel" placeholder="010-0000-0000">
    <label>이메일 * <span style="font-weight:400">(만료 알림 수신)</span></label><input id="fMail" type="email" autocomplete="email" placeholder="name@example.com">
    <label style="display:flex;gap:8px;align-items:flex-start;margin-top:14px;font-size:13.5px;color:var(--ink)"><input type="checkbox" id="fAgree" style="width:auto;margin-top:4px">위 교육 내용을 확인하였으며 LGES 사업장 안전수칙을 준수하겠습니다. 입력한 정보는 교육 이수 관리와 만료 알림에만 사용됩니다.</label>
    <button class="btn" id="sendBtn" style="margin-top:16px" onclick="submitTrain()">완료 · 전송</button>
  </div>`;
}
const QKEY='lges_pending';
function getQueue(){ try{ return JSON.parse(localStorage.getItem(QKEY)||'[]'); }catch(e){ return []; } }
function setQueue(q){ try{ localStorage.setItem(QKEY, JSON.stringify(q)); }catch(e){} }
async function postRecord(rec){
  const r=await fetch(GAS_URL,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(rec)});
  const j=await r.json(); if(!j.ok) throw new Error(j.error||'서버 오류'); return j;
}
async function flushQueue(){
  if(!hasGas()||!navigator.onLine) return; let q=getQueue(); if(!q.length) return;
  const rest=[]; let ok=0;
  for(const rec of q){ try{ await postRecord(rec); ok++; }catch(e){ rest.push(rec); } }
  setQueue(rest); if(ok) toast(`대기 중이던 교육 기록 ${ok}건을 전송했습니다`);
}
window.addEventListener('online', flushQueue); setInterval(flushQueue, 60000);
// 연락처 정리: +82 10 … / 821012345678 / 01012345678 → 010-1234-5678
function normPhone(v){ let d=String(v||'').replace(/\D/g,''); if(d.startsWith('82')) d='0'+d.slice(2); if(!/^01[016789]\d{7,8}$/.test(d)) return ''; return d.length===11 ? d.replace(/(\d{3})(\d{4})(\d{4})/,'$1-$2-$3') : d.replace(/(\d{3})(\d{3})(\d{4})/,'$1-$2-$3'); }
async function submitTrain(){
  const name=$('#fName').value.trim(), company=$('#fComp').value.trim(), phone=normPhone($('#fPhone').value), email=$('#fMail').value.trim();
  if(!name||!company||!$('#fPhone').value.trim()||!email) return toast('모든 항목을 입력해 주세요');
  if(!phone){ toast('연락처를 확인해 주세요 (예: 010-1234-5678)'); $('#fPhone').focus(); return; }
  if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return toast('이메일 형식을 확인해 주세요');
  if(!$('#fAgree').checked) return toast('확인 체크가 필요합니다');
  if(!hasGas()){ toast('서버 미연결(테스트 모드) — 기록되지 않았습니다'); T.sent={name,company,email,expire:'(배포 후 표시)'}; render(); return; }
  const btn=$('#sendBtn'); btn.disabled=true; btn.textContent='전송 중…';
  const rec={name,company,phone,email,note:'slides:'+D.slides.length+' at:'+new Date().toISOString().slice(0,16)};
  let j=null, lastErr=null;
  for(let a=0;a<2&&!j;a++){ try{ j=await postRecord(rec); }catch(e){ lastErr=e; await new Promise(r=>setTimeout(r,1500)); } }
  if(j){ T.sent={name,company,email,expire:j.expire}; render(); window.scrollTo(0,0); return; }
  // 전송 실패 → 폰에 저장 후 자동 재전송
  const q=getQueue(); q.push(rec); setQueue(q);
  const exp=new Date(); exp.setMonth(exp.getMonth()+Number(setting('유효기간_개월',6)));
  T.sent={name,company,email,expire:exp.toISOString().slice(0,10),queued:true}; render(); window.scrollTo(0,0);
}

