# DataPersistence-jihoonlee-23020975

**데이터 영속성 처리** PoC입니다. JSON 파일 기반으로 Sample/Order 데이터를
저장·조회·수정·삭제(CRUD)하며, 프로세스를 재시작해도 데이터가 유지됨을 증명합니다.

## 구조

```
persistence/
  json_store.py         # 범용 JSON 파일 저장소 (find_all/find_by_id/insert/update/delete)
  sample_repository.py  # Sample CRUD
  order_repository.py   # Order CRUD
data/
  samples.json           # 실제 저장 파일 (최초 실행 시 자동 생성)
  orders.json
main.py                  # CRUD 데모 스크립트
```

## 실행 (영속성 검증 순서)

```
python main.py seed     # 1) 데이터 생성
python main.py list     # 2) 조회 -> 생성 데이터 확인
                         # 3) 프로세스 종료 후 재실행해도 아래 list 결과가 유지됨
python main.py update    # 4) 재고/상태 수정
python main.py list      # 5) 수정 결과 확인
python main.py delete    # 6) 레코드 삭제
python main.py list      # 7) 삭제 결과 확인
```

data/*.json 파일을 직접 열어 봐도 동일한 결과를 확인할 수 있습니다.
