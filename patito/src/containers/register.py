from typing import TypeVar, Generic
from itertools import count

T = TypeVar('T')

class Register(Generic[T]):
    def __init__(self):
        self.__records: list[T] = []
        self.curr_index: int = -1

    def add_record(self, record: T) -> None:
        self.__records.append(record)
        self.curr_index += 1

    def add_records(self, records: list[T]) -> None:
        self.__records += records
        self.curr_index += len(records)

    @property
    def records(self) -> list[T]:
        return self.__records

    @property
    def curr_record_index(self) -> int:
        if self.curr_index == -1:
            raise LookupError("no records in the register")
        return self.curr_index

    @property
    def next_record_index(self) -> int:
        return self.curr_index + 1
    
    def __str__(self) -> str:
        return self.__to_string(list(zip(count(0), self.__records)))

    def __to_string(self, records: list[tuple[int, T]]) -> str:
        if not records:
            return ""
        record_index, record = records[0]
        return f"\n{record_index}. {str(record)}" + self.__to_string(records[1:])