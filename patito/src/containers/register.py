from typing import TypeVar, Generic
from itertools import count

T = TypeVar('T')

class Register(Generic[T]):
    def __init__(self):
        self.records: list[T] = []
        self.n: int = 0

    def add_record(self, record: T) -> None:
        self.records.append(record)
        self.n += 1

    def add_records(self, records: list[T]) -> None:
        self.records += records
        self.n += len(records)

    @property
    def last_record_index(self) -> int:
        if self.n == 0:
            raise LookupError("no records in the register")
        return self.n + 1

    @property
    def next_record_index(self) -> int:
        return self.n + 1
    
    def __str__(self) -> str:
        return self.__to_string(list(zip(count(1), self.records)))

    def __to_string(self, records: list[tuple[int, T]]) -> str:
        if not records:
            return ""
        record_index, record = records[0]
        return f"\n{record_index}. {str(record)}" + self.__to_string(records[1:])