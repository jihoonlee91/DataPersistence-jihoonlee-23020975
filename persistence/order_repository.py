from persistence.json_store import JsonStore


class OrderRepository:
    """주문(Order) 데이터에 대한 CRUD 저장소."""

    def __init__(self, file_path: str = "data/orders.json"):
        self.store = JsonStore(file_path)

    def create(self, order_id: str, sample_id: str, customer: str,
               quantity: int, status: str = "RESERVED") -> dict:
        record = {
            "order_id": order_id,
            "sample_id": sample_id,
            "customer": customer,
            "quantity": quantity,
            "status": status,
        }
        self.store.insert(record)
        return record

    def read_all(self) -> list[dict]:
        return self.store.find_all()

    def read(self, order_id: str) -> dict | None:
        return self.store.find_by_id("order_id", order_id)

    def update(self, order_id: str, **updates) -> bool:
        return self.store.update("order_id", order_id, updates)

    def delete(self, order_id: str) -> bool:
        return self.store.delete("order_id", order_id)
