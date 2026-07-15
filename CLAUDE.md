# CLAUDE.md

이 파일은 Claude Code가 이 리포지토리에서 작업할 때 참고하는 규칙을 담는다.

## 기술 스택

- Python 3 (표준 라이브러리 `json`만 사용, 외부 의존성 없음)

## 실행 / 테스트

```
python main.py seed     # 데이터 생성 (Create)
python main.py list     # 조회 (Read)
python main.py update   # 수정 (Update)
python main.py delete   # 삭제 (Delete)
```

각 명령을 별도 프로세스로 실행해도 `data/*.json`에 반영된 상태가 유지되는지 확인하는 것이
이 PoC의 핵심 검증 포인트다(영속성 증명).

## 저장소 설계 원칙

- `JsonStore`는 스키마를 모르는 범용 CRUD 계층이며, 레코드 식별자 필드명(`id_field`)을 인자로 받는다.
- `SampleRepository`/`OrderRepository`는 `JsonStore`를 감싸 도메인 전용 메서드만 노출한다.
- 파일 I/O는 매 호출마다 전체를 읽고 쓰는 단순한 방식이며, 동시성 제어는 하지 않는다(PoC 범위 밖).
