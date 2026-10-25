/* ===== 규정 원문 (OPS) ===== */
function opsCard(o, full){
  const kws=String(o['연관검색어']||'').split(',').map(x=>x.trim()).filter(Boolean);
  const items=String(o['내용']||'').split('|').map(x=>x.trim()).filter(Boolean);
  const show=full?items:items.slice(0,3);
  const li=show.map(x=>{ const m=x.match(/^\[(.+?)\]\s*(.*)$/); if(m&&!m[2]) return `<li class="h">${esc(m[1])}</li>`; const body=m?m[2]:x; const {head,subs}=splitNumbered(body); const hd=(m?`<b style="color:var(--g)">${esc(m[1])}</b> `:'')+(head?rich(head):''); return subs.length?`<li>${hd}<ul class="sub">${subs.map(z=>`<li>${rich(z)}</li>`).join('')}</ul></li>`:`<li>${hd||rich(body)}</li>`; }).join('');
  const imgs=String(o['원문이미지']||'').split(',').map(x=>x.trim()).filter(Boolean);
  const id='o'+String(o['코드']).replace(/[^\w]/g,'');
  return `<div class="card" id="${id}"><div class="tag"><span class="pill">${esc(o['코드'])}</span><span class="pill gray">${esc(o['분류'])}</span>${o['재개정일']?`<span style="font-size:11px;color:var(--mute)">${esc(o['재개정일'])} ${esc(o['개정번호']||'')}</span>`:''}${isNew(o['적용시작일'])?'<span class="pill red">변경됨</span>':''}</div>
  <h4 style="font-size:15.5px">${esc(o['제목'])}</h4>
  ${kws.length?`<div class="kwc">${kws.slice(0,8).map(k=>`<span>${esc(k)}</span>`).join('')}</div>`:''}
  <ul class="ob">${li}</ul>
  ${!full&&items.length>3?`<button class="more" onclick="go('ops','${esc(o['코드'])}')">전체 ${items.length}개 항목 보기 →</button>`:''}
  <div class="row" style="margin-top:10px">${imgs.length?`<button class="btn sm" onclick='openViewer(${JSON.stringify(imgs)},${JSON.stringify(String(o['코드'])+' '+String(o['제목']))})'>📄 LG 원문 보기 (${imgs.length}p)</button>`:''}</div>
  <div class="src">${esc(o['출처'])}</div></div>`;
}
function opsView(){
  const list=D.ops||[]; const focus=T.arg; T.arg=null;
  if(focus){ const o=list.find(x=>String(x['코드'])===String(focus)); if(o) return `<div class="ops">${opsCard(o,true)}<button class="btn ghost" onclick="go('ops')">규정 목록으로</button></div>`; }
  const groups={}; list.forEach(o=>{ const g=String(o['분류']||'').split('-')[0]||'기타'; (groups[g]=groups[g]||[]).push(o); });
  const order=['작업종류','공사설비','PPE','고위험작업','안전작업허가서','작업허가서','작업시간','면허제도','작업중지','비상','기타'];
  const keys=Object.keys(groups).sort((a,b)=>(order.indexOf(a)+99)%99-(order.indexOf(b)+99)%99);
  return `<div class="alert" style="background:var(--g3);border-color:var(--g)"><b>LG에너지솔루션 공사안전 OPS·규정 원문</b> — 협의체 자료에 공유된 ${list.length}건. 제목을 누르면 전체 내용, "원문 보기"를 누르면 LG 자료 페이지를 확대해서 볼 수 있습니다.</div>
  ${keys.map(k=>`<div class="sec">${esc(k)}</div><div class="card" style="padding:4px 14px">${groups[k].map(o=>`<div style="display:flex;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line);cursor:pointer" onclick="go('ops','${esc(o['코드'])}')"><span class="pill" style="flex:none">${esc(o['코드'])}</span><span style="flex:1;font-size:14px">${esc(o['제목'])}${isNew(o['적용시작일'])?' <span class="pill red">변경됨</span>':''}<div style="font-size:11.5px;color:var(--mute)">${esc(o['분류'])} · ${esc(o['재개정일']||'')}</div></span><span style="color:var(--mute)">›</span></div>`).join('')}</div>`).join('')}`;
}
function openViewer(imgs,title){
  const v=document.createElement('div'); v.className='viewer'; v.id='viewer';
  v.innerHTML=`<div class="vh"><b>${esc(title)}</b><button onclick="closeViewer()">닫기 ✕</button></div><div class="vb">${imgs.map(i=>`<img src="${IMG}ops/${esc(i)}" alt="">`).join('')}<div class="tip">두 손가락으로 확대해서 보세요 · 출처: LG에너지솔루션 공사업체 안전보건 협의회 자료</div></div>`;
  document.body.appendChild(v); document.body.style.overflow='hidden'; history.pushState({v:1},'');
}
function closeViewer(){ const v=$('#viewer'); if(v){ v.remove(); document.body.style.overflow=''; } }
window.addEventListener('popstate',()=>closeViewer());

