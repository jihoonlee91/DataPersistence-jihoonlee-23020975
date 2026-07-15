# 작업 보고서 - DataPersistence PoC

## 요청 받은 작업

"데이터 영속성 처리" PoC. 팀(개인)이 선택한 방식(JSON)으로 데이터를 저장·불러오는 구조를 구현하고 CRUD를 포함해야 함.
요구사항: application을 다시 실행해도 데이터를 유지할 수 있어야 함.

## 해석

- CRUD 각 동작을 별도 CLI 서브커맨드(seed/list/update/delete)로 분리하여, 매번 새 프로세스로 실행됨을 이용해
  "재시작 후에도 데이터 유지"를 명시적으로 증명 가능하도록 설계함.
- 범용 JSON 저장소(`JsonStore`)와 도메인별 Repository를 분리하여 향후 SampleOrderSystem에서
  Sample/Order 외 다른 엔티티(예: 생산 큐)가 추가되어도 재사용 가능하도록 함.

## 변경 요약

- `persistence/json_store.py`: find_all/find_by_id/insert/update/delete를 제공하는 범용 JSON 저장소
- `persistence/sample_repository.py`, `order_repository.py`: 도메인 전용 CRUD 래퍼
- `main.py`: seed/list/update/delete CLI 데모

## 핵심 코드 요약

- `JsonStore`는 매 호출마다 파일 전체를 읽고 다시 써서(read-modify-write) 별도 캐시를 두지 않는다 — 단순하지만
  동시 접근에는 취약함을 인지하고 있으며, PoC 목적(영속성 증명)에는 충분하다고 판단함.

## 요청사항 충족 여부 체크리스트

- [x] JSON 파일 기반 저장/불러오기 구조 구현
- [x] CRUD(Create/Read/Update/Delete) 전부 구현
- [x] 프로세스 재시작 후 데이터 유지 확인 (별도 `python main.py` 호출 간 데이터 보존을 실제 실행으로 검증)

## 변경된 파일 목록

- `main.py` (신규)
- `persistence/__init__.py`, `persistence/json_store.py`, `persistence/sample_repository.py`, `persistence/order_repository.py` (신규)
- `README.md` (신규)
