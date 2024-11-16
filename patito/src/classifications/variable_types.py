from enum import Enum
from typing import Literal

class VariableType(Enum):
    ENTERO = 0
    FLOTANTE = 1
    LETRERO = 2

    def __str__(self) -> str:
        return f"{self.name}"
    
    @staticmethod
    def to_type(type_token: Literal["entero", "flotante", "ENTERO", "FLOTANTE", 'letrero', "LETRERO"]) -> 'VariableType':
        match type_token:
            case "entero" | "ENTERO":
                return VariableType.ENTERO
            case "flotante" | "FLOTANTE":
                return VariableType.FLOTANTE
            case "letrero" | "LETRERO": 
                return VariableType.LETRERO
            case _:
                raise ValueError(f"cannot convert token {type_token} to PatitoType")


        