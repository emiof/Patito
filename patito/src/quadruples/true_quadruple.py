from typing import Literal
from ..classifications import QuadrupleType
from .utils import examinable

@examinable
class TrueQuadruple:
    def __init__(self, items: list[int | str], quadruple_type: QuadrupleType):
        self.items: list[int | str] = items
        self.quadruple_type: QuadrupleType = quadruple_type
    
    def set_jump(self, jump: int) -> None:
        if self.quadruple_type != QuadrupleType.FLOW:
            raise ValueError(f"attempting to add a jump action to a '{self.quadruple_type.name}' quadruple")
        self.items[-1] = jump

    @property
    def operator(self) -> int:
        return self.items[0]
    
    @property
    def operands(self) -> tuple[int, int]:
        return [self.items[1], self.items[2]]
    
    @property
    def result(self) -> int:
        if self.quadruple_type != QuadrupleType.EXP:
            raise ValueError(f"attempting to access result of a '{self.quadruple_type.name}' quadruple")
        return self.items[-1]
    
    @property
    def jump_condition(self) -> Literal[1, 0]:
        if self.quadruple_type != QuadrupleType.FLOW:
            raise ValueError(f"attempting to access jump condition of a '{self.quadruple_type.name}' quadruple")
        return self.items[1]

    @property
    def jump(self) -> int:
        if self.quadruple_type != QuadrupleType.FLOW:
            raise ValueError(f"attempting to access jump value of a '{self.quadruple_type.name}' quadruple")
        return self.items[-1]

    @staticmethod
    def extract_flow_quadruples(quadruples: list['TrueQuadruple']) -> list['TrueQuadruple']:
        return [quad for quad in quadruples if quad.quadruple_type == QuadrupleType.FLOW]
