from enum import Enum
from typing import Literal

class PatitoType(Enum):
    ENTERO = 0
    FLOTANTE = 1

    def __str__(self) -> str:
        return f"{self.name}"
    
    @staticmethod
    def to_type(type_token: Literal["entero", "flotante", "ENTERO", "FLOTANTE"]) -> 'PatitoType':
        match type_token:
            case "entero" | "ENTERO":
                return PatitoType.ENTERO
            case "flotante" | "FLOTANTE":
                return PatitoType.FLOTANTE
            case _: 
                raise Exception(f"cannot convert token {type_token} to PatitoType")


        