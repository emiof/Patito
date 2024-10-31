from enum import Enum
from typing import Literal

class PatitoType(Enum):
    ENTERO = 0
    FLOTANTE = 1

class SymbolType(Enum):
    ENTERO = 0
    FLOTANTE = 1
    FUNCION = 2
    UNDEFINED = 3

    def __str__(self) -> str:
        return f"{self.name}"
    
    @staticmethod
    def to_symbol_type(type_token: Literal["entero", "flotante"]) -> 'SymbolType':
        match type_token:
            case "entero":
                return SymbolType.ENTERO
            case "flotante":
                return SymbolType.FLOTANTE

        