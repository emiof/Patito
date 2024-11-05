from enum import Enum

class SymbolType(Enum):
    VARIABLE = 0
    FUNCTION = 1
    UNDEFINED = 2

    def __str__(self) -> str:
        return f"{self.name}"