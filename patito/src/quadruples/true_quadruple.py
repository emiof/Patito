from collections.abc import Iterator
from ..classifications import QuadrupleType

class TrueQuadruple:
    def __init__(self, items: list[int], quadruple_type: QuadrupleType):
        self.items: list[int] = items
        self.quadruple_type: QuadrupleType = quadruple_type

    def __iter__(self) -> Iterator[int]:
        yield from self.items

    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"
    
    def set_jump(self, jump: int) -> None:
        if self.quadruple_type != QuadrupleType.FLOW:
            raise ValueError(f"attempting to add a jump action to a '{self.quadruple_type.name}' quadruple")
        self.items[-1] = jump