# LG 현장 안전 (customer-safety) — ETS 협력사 작업자용

- 앱: https://sugilyang.github.io/customer-safety/
- 관리자(생산관리): https://sugilyang.github.io/customer-safety/admin.html

## 구조
- `index.html` 앱 (홈·검색·교육·더보기) / `admin.html` 이수 현황
- `data.js` **모든 내용** — 작업가이드 27·OPS 규정 22·벌점표·슬라이드·공통수칙·강조사항·변경이력
- `img/` 슬라이드·가이드 그림, `img/ops/` LG 원문 페이지
- 구글 시트: `설정`(장당_초·유효기간·비밀번호·알림일수) + `교육이수`(기록) 만 사용. 나머지 탭은 사용 안 함
- GAS: 설정값 제공, 교육완료 기록, 이수 확인 메일, 매일 08시 만료 30/7/1일 전 알림

## 매달 업데이트
협의체 PDF를 Claude에 전달 → Claude가 `data.js`·`img/ops/` 갱신 후 GitHub에 반영. 시트·GAS는 손대지 않음.
