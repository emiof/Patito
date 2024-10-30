from enum import Enum

class PatitoType(Enum):
    ENTERO = 0
    FLOTANTE = 1

class SymbolType(Enum):
    ENTERO = 0
    FLOTANTE = 1
    FUNCION = 2

    def __str__(self) -> str:
        return f"{self.name}"