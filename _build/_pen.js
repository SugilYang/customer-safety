/* ===== 벌점표 ===== */
function penaltyView(){
  const cats=[...new Set(D.penalty.map(p=>p['대분류']))]; if(!T.pcat) T.pcat=cats[0];
  const rows=D.penalty.filter(p=>p['대분류']===T.pcat);
  const lv=D.onestrike.filter(o=>/^작업중지 Level|^누적/.test(o['구분']));
  return `<div class="alert"><b>26년 7월 1일 감점기준 전면 개정</b> — 위험성평가 미실시·추락방지·LOTO·인터락 해제·밀폐 환기 등 주요 항목이 <b>20점 + 작업중지</b>로 상향됐습니다. 누적 20점부터 사후조치, 70점 이상 입찰제한~거래중지.</div>
  <div class="chips">${cats.map(c=>`<button class="${T.pcat===c?'on':''}" onclick="T.pcat='${esc(c)}';render()">${esc(c)}</button>`).join('')}</div>
  <div class="card" style="padding:6px 10px"><table><thead><tr><th style="width:52px">코드</th><th>세부항목</th><th class="n">감점</th></tr></thead><tbody>
  ${rows.map(p=>`<tr><td style="color:var(--mute);font-size:12px">${esc(p['코드'])}</td><td>${esc(p['세부항목'])}${p['작업중지']?' <span class="pill red" style="font-size:10px">중지</span>':''}${(p['변경']==='상향')?` <span class="pill amber" style="font-size:10px">${esc(p['구감점_25년9월'])}→</span>`:''}</td><td class="n${String(p['감점']).includes('/')?' multi':''}" style="color:${Number(String(p['감점']).split('/')[0])>=10?'var(--red)':'var(--ink)'}">${esc(String(p['감점']).replace(/\//g,'/\u200b'))}</td></tr>`).join('')}
  </tbody></table><div class="src">${esc(rows[0]?.['출처']||'')}</div></div>
  <div class="sec">작업중지 Level · 누적 점수 사후조치</div>
  ${lv.map(o=>`<div class="card" style="padding:12px 14px"><div class="tag"><span class="pill ${/Level 3|70점|50점/.test(o['구분'])?'red':/Level 2|30점/.test(o['구분'])?'amber':''}">${esc(o['구분'])}</span></div><h4 style="margin:4px 0">${esc(o['위반내역'])}</h4><p class="sub">${esc(o['협력사페널티'])}</p>${o['비고']?`<p class="sub">${esc(o['비고'])}</p>`:''}</div>`).join('')}
  <p class="foot">우수사례는 건별 가산점 3점 · 반기 적격수급업체 평가에 반영</p>`;
}

