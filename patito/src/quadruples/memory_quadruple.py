from collections.abc import Iterator

class MemoryQuadruple:
    def __init__(self, items: list[int]):
        self.items: list[int] = items

    def __iter__(self) -> Iterator[int]:
        yield from self.items

    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"