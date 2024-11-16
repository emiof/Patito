from typing import Any, Optional
from collections.abc import Iterator
from ..classifications import VariableType

def examinable(cls):
    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"
    def __iter__(self) -> Iterator[Any]:
        yield from self.items

    cls.__str__ = __str__
    cls.__iter__ = __iter__
    return cls

def cast(token: str, token_type: Optional[VariableType]) -> int | float | str:
    match token_type:
        case VariableType.ENTERO:
            return int(token)
        case VariableType.FLOTANTE:
            return float(token)
        case _:
            return token