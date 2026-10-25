# 협력사 공용판: out/index.html → out/partners/index.html (교육·이수·관리자·서버 연결 제거, LGES 로고)
import os,re
base=os.path.dirname(os.path.abspath(__file__))+'/out/'
s=open(base+'index.html',encoding='utf-8').read()
def R(a,b,cnt=1):
    global s
    assert a in s, 'missing: '+a[:60]
    s=s.replace(a,b,cnt)
# 경로
s=s.replace('src="img/','src="../img/').replace("const IMG = 'img/'","const IMG = '../img/'").replace('src="data.js?v=','src="../data.js?v=')
s=re.sub(r"(['\"`])img/", r"\1../img/", s)
s=s.replace('../../img/','../img/')
# 헤더 로고·부제
R('<img src="../img/ets_logo_white.png" alt="ETS" onerror="this.outerHTML=\'<span class=wm>ETS</span>\'">','<img src="../img/lges_logo.png?v=3" alt="LG Energy Solution" class="lges">')
R('<small>출입 전 교육 · 작업수칙 검색</small>','<small>작업수칙 검색 · 오창</small>')
R('<a class="home" href="https://sugilyang.github.io/ets-safety/" title="ETS 안전포털">🏠</a>','')
# 스플래시: LGES 로고 하나
R('<img class="lgo lglogo" src="../img/lg_logo.png" alt="LG"><div class="x"></div><img class="lgo ets" src="../img/ets_logo.png" alt="ETS">','<img class="lgo lglogo" src="../img/lges_logo.png" alt="LG Energy Solution" style="height:40px;max-width:72vw">')
# 교육 탭·홈 교육 버튼 제거
s=re.sub(r'<button data-v="train" onclick="go\(\'train\'\)">.*?</button>','',s,count=1)
s=re.sub(r'<button class="hero2" onclick="go\(\'train\'\)">.*?</button>','',s,count=1,flags=re.S)
# 더보기: 이수확인·관리자·ETS포털 제거
R(",['✓','내 교육 이수 확인','이름 또는 연락처 뒤 4자리로 조회','status']]","]")
R("${adminBtn}${portalBtn}</div>","</div>")
# 서버 연결 끊기
s=re.sub(r"const GAS_URL = '[^']*';","const GAS_URL = '';",s,count=1)
R("showSplash(); loadData(); setTimeout(flushQueue, 2000);","showSplash(); loadData();")
# 하단 표기
R("function verLine(dev){ const v=D.version||{}; return `주식회사 이티에스 · ${esc(v['버전']||'')}<br>",
  "function verLine(dev){ const v=D.version||{}; return `LG에너지솔루션 오창 협력사 안전 · ${esc(v['버전']||'')}<br>")
s=s.replace("${dev?`<br><span class=\"dev\">개발 · ${esc(v['개발']||'')}</span>`:''}","<br><span class=\"dev\">제작 · ㈜이티에스 환경안전팀</span>")
s=re.sub(r'<title>[^<]*</title>','<title>현장 안전 길잡이 — LG에너지솔루션 협력사</title>',s,count=1)
s=s.replace('고객사 현장 안전 길잡이<small>','현장 안전 길잡이<small>',1)
os.makedirs(base+'partners',exist_ok=True)
open(base+'partners/index.html','w',encoding='utf-8').write(s)
print('partners written', len(s))
s2=open(base+'partners/index.html',encoding='utf-8').read()
s2=s2.replace('</style>','.logo img.lges{height:20px;width:auto}\n.top{gap:14px;background:#fff!important;color:var(--ink)!important;box-shadow:0 1px 0 #E3E8E5,0 2px 8px rgba(0,0,0,.05)!important}\n.top .t{color:#1a1f1c}.top .t small{color:#6b7570;opacity:1}\n.top .back,.top .home{background:#F1F4F3!important;color:#3d4642!important}\nmeta{}\n.top .t{font-size:16px}\n@media(max-width:430px){.top{gap:10px;padding-left:12px;padding-right:12px}.logo img.lges{height:16px}.top .t{font-size:14.5px}.top .t small{font-size:11px}}\n@media(max-width:340px){.logo img.lges{height:13px}.top .t{font-size:13.5px}}\n</style>',1)
open(base+'partners/index.html','w',encoding='utf-8').write(s2)
s3=open(base+'partners/index.html',encoding='utf-8').read().replace('<meta name="theme-color" content="#00806F">','<meta name="theme-color" content="#FFFFFF">',1)
open(base+'partners/index.html','w',encoding='utf-8').write(s3)
s4=open(base+'partners/index.html',encoding='utf-8').read()
s4=s4.replace('<small>고객사 현장 안전 길잡이 · 주식회사 이티에스</small>','<small>협력사 현장 안전 길잡이 · LG에너지솔루션 오창</small>',1)
s4=s4.replace('<div class="t">현장 안전 길잡이<small>','<div class="t">협력사 현장 안전 길잡이<small>',1)
s4=s4.replace('<title>현장 안전 길잡이 — LG에너지솔루션 협력사</title>','<title>협력사 현장 안전 길잡이 — LG에너지솔루션</title>',1)
s4=s4.replace('생산관리 확인 후 고객사 현장에 출입할 수','확인 후 현장에 출입할 수')
open(base+'partners/index.html','w',encoding='utf-8').write(s4)
s5=open(base+'partners/index.html',encoding='utf-8').read()
s5=s5.replace('<span class="dev">제작 · ㈜이티에스 환경안전팀</span>','<span class="mk">기획·개발 <b>㈜이티에스 환경안전팀 양수길 책임</b></span>')
s5=s5.replace('<div class="skip"><span id="spVer"></span><br>화면을 누르면 건너뜁니다</div>','<div class="skip"><span class="spmk">기획·개발 ㈜이티에스 환경안전팀 양수길 책임</span><br><span id="spVer"></span><br>화면을 누르면 건너뜁니다</div>',1)
s5=s5.replace('</style>','.foot .mk{display:inline-block;margin-top:8px;padding:6px 12px;border-radius:999px;background:var(--g3);color:var(--g);font-size:11.5px}\n.foot .mk b{font-weight:800}\n.splash .spmk{display:inline-block;margin-bottom:6px;font-size:12px;font-weight:700;color:#3d4642}\n</style>',1)
open(base+'partners/index.html','w',encoding='utf-8').write(s5)
s6=open(base+'partners/index.html',encoding='utf-8').read()
s6=s6.replace('<span class="mk">기획·개발 <b>㈜이티에스 환경안전팀 양수길 책임</b></span>','<span class="mk">기획·개발 <b>㈜이티에스 환경안전팀 양수길 책임</b><br><a href="mailto:sgyang@ets1.co.kr">✉ sgyang@ets1.co.kr</a></span>',)
s6=s6.replace('.foot .mk b{font-weight:800}','.foot .mk b{font-weight:800}\n.foot .mk{line-height:1.7}.foot .mk a{color:var(--g);text-decoration:none;font-weight:700;white-space:nowrap}')
open(base+'partners/index.html','w',encoding='utf-8').write(s6)
s7=open(base+'partners/index.html',encoding='utf-8').read()
s7=s7.replace('<span class="mk">기획·개발 <b>㈜이티에스 환경안전팀 양수길 책임</b><br><a href="mailto:sgyang@ets1.co.kr">✉ sgyang@ets1.co.kr</a></span>',
 '<span class="mk">기획·개발 ㈜이티에스 환경안전팀 <b>양수길 책임</b><br>앱 관련 의견 <a href="mailto:sgyang@ets1.co.kr">sgyang@ets1.co.kr</a></span>')
s7=s7.replace('.foot .mk{display:inline-block;margin-top:8px;padding:6px 12px;border-radius:999px;background:var(--g3);color:var(--g);font-size:11.5px}',
 '.foot .mk{display:block;margin:12px auto 0;padding-top:10px;border-top:1px solid var(--line);max-width:260px;color:var(--mute);font-size:11px}')
s7=s7.replace('.foot .mk b{font-weight:800}','.foot .mk b{font-weight:700;color:var(--ink)}')
s7=s7.replace('.foot .mk a{color:var(--g);text-decoration:none;font-weight:700;white-space:nowrap}','.foot .mk a{color:var(--mute);text-decoration:underline;text-underline-offset:2px;white-space:nowrap}')
s7=s7.replace('.splash .spmk{display:inline-block;margin-bottom:6px;font-size:12px;font-weight:700;color:#3d4642}','.splash .spmk{display:inline-block;margin-bottom:6px;font-size:11.5px;color:#5f6b65}')
open(base+'partners/index.html','w',encoding='utf-8').write(s7)
s8=open(base+'partners/index.html',encoding='utf-8').read()
s8=s8.replace('<br>앱 관련 의견 <a href="mailto:sgyang@ets1.co.kr">sgyang@ets1.co.kr</a></span>',
 '<br><a href="tel:01034692346">☎ 010-3469-2346</a> · <a href="mailto:sgyang@ets1.co.kr">sgyang@ets1.co.kr</a></span>')
open(base+'partners/index.html','w',encoding='utf-8').write(s8)
s9=open(base+'partners/index.html',encoding='utf-8').read()
s9=s9.replace("['주·정차 관련','LG 사무실','','043-718-0123']]","['주·정차 관련','LG 사무실','','043-718-0123'],['💡 이 앱 문의 · 개선 제안','㈜이티에스 양수길 책임','환경안전팀','010-3469-2346']]",1)
open(base+'partners/index.html','w',encoding='utf-8').write(s9)
