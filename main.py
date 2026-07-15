"""
DataPersistence-jihoonlee-23020975 데모 스크립트.
CRUD 동작과 재시작 후 데이터 유지(영속성)를 증명한다.

사용법:
  python main.py seed    # 초기 데이터 생성 (Create)
  python main.py list    # 저장된 데이터 조회 (Read)
  python main.py update  # 임의 레코드 수정 (Update)
  python main.py delete  # 임의 레코드 삭제 (Delete)
"""
import sys

from persistence.sample_repository import SampleRepository
from persistence.order_repository import OrderRepository


def seed(samples: SampleRepository, orders: OrderRepository) -> None:
    samples.create("S-001", "실리콘 웨이퍼-8인치", 0.5, 0.92, 480)
    samples.create("S-002", "GaN 에피택셜-4인치", 0.3, 0.78, 220)
    orders.create("ORD-0001", "S-001", "삼성전자 파운드리", 200)
    print("초기 데이터 생성 완료 (Create).")


def list_data(samples: SampleRepository, orders: OrderRepository) -> None:
    print("== 시료 목록 ==")
    for s in samples.read_all():
        print(s)
    print("== 주문 목록 ==")
    for o in orders.read_all():
        print(o)


def update_data(samples: SampleRepository, orders: OrderRepository) -> None:
    ok = samples.update("S-001", stock=680)
    print(f"S-001 재고 수정: {'성공' if ok else '대상 없음'} (Update)")
    ok = orders.update("ORD-0001", status="CONFIRMED")
    print(f"ORD-0001 상태 수정: {'성공' if ok else '대상 없음'} (Update)")


def delete_data(samples: SampleRepository, orders: OrderRepository) -> None:
    ok = samples.delete("S-002")
    print(f"S-002 삭제: {'성공' if ok else '대상 없음'} (Delete)")


def main() -> None:
    samples = SampleRepository()
    orders = OrderRepository()

    command = sys.argv[1] if len(sys.argv) > 1 else "list"
    commands = {
        "seed": seed,
        "list": list_data,
        "update": update_data,
        "delete": delete_data,
    }
    action = commands.get(command)
    if action is None:
        print(f"알 수 없는 명령어: {command}")
        return
    action(samples, orders)


if __name__ == "__main__":
    main()
