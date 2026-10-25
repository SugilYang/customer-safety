# _build — 앱 제작 파일 (앱 주소에는 노출되지 않음)

두 앱을 같은 자료로 만듭니다.
- ETS판 `index.html` — 고객사 현장 안전 길잡이 (교육·이수·관리자 포함)
- 협력사판 `partners/index.html` — 협력사 현장 안전 길잡이 (교육 없음, LG에너지솔루션 로고, 개발자 연락처)

## 매달 협의체 자료 반영
1. 새 협의체 PDF 내용을 `guides_data.py`(작업 가이드) · `ops_data.py`(OPS 원문) · `penalty_versions.json`(벌점표) · `build_data.py`(공통수칙·강조사항·변경이력·슬라이드)에 반영
2. OPS 원문 페이지 이미지는 저장소 `img/ops/`에 추가
3. `build_data.py`의 `APP_VERSION`에서 버전·배포일·최근반영 갱신
4. `python3 _build/make_all.py` → data.js, index.html, partners/index.html 자동 갱신
5. 커밋·push (1~2분 뒤 두 앱 모두 반영)

## 각자 따로 고칠 것
- ETS판만: `build_app.py`, `_css.txt`, `_train.js`(교육), `_ops.js`, `_pen.js`
- 협력사판만: `build_partner.py` (ETS판 결과에서 교육·관리자 제거, 로고·명칭·연락처 변경을 여기서 처리)
- 공통 화면을 고치면 make_all.py 한 번으로 두 판이 함께 바뀜

## 여기 없는 것
구글 Apps Script(교육 기록·체감온도), 시트 ID, 관리자 비밀번호, 협의체 PDF 원본 — 별도 관리
