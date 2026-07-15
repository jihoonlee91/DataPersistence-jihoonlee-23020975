from persistence.json_store import JsonStore


class SampleRepository:
    """시료(Sample) 데이터에 대한 CRUD 저장소."""

    def __init__(self, file_path: str = "data/samples.json"):
        self.store = JsonStore(file_path)

    def create(self, sample_id: str, name: str, avg_process_time: float,
               yield_rate: float, stock: int = 0) -> dict:
        record = {
            "sample_id": sample_id,
            "name": name,
            "avg_process_time": avg_process_time,
            "yield_rate": yield_rate,
            "stock": stock,
        }
        self.store.insert(record)
        return record

    def read_all(self) -> list[dict]:
        return self.store.find_all()

    def read(self, sample_id: str) -> dict | None:
        return self.store.find_by_id("sample_id", sample_id)

    def update(self, sample_id: str, **updates) -> bool:
        return self.store.update("sample_id", sample_id, updates)

    def delete(self, sample_id: str) -> bool:
        return self.store.delete("sample_id", sample_id)
