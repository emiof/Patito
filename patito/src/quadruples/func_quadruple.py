from typing import Optional
from ..classifications import FuncOperator
from ..containers import OperandPair
from .utils import examinable

@examinable
class FuncQuadruple:
    def __init__(self, operator: FuncOperator, operand: Optional[OperandPair], func_reference: Optional[str | int]):        
        self.items: list[FuncOperator, Optional[OperandPair], None, Optional[str | int]] = [operator, operand, None, func_reference]

    @staticmethod
    def ERA_quadruple(func_reference: str) -> 'FuncQuadruple':
        return FuncQuadruple(FuncOperator.ERA, None, func_reference)
    
    @staticmethod
    def PARAM_quadruple(operand: OperandPair) -> 'FuncQuadruple':
        return FuncQuadruple(FuncOperator.PARAM, operand, None)
    
    @staticmethod
    def GOSUB_quadruple(func_reference: int) -> 'FuncQuadruple':
        return FuncQuadruple(FuncOperator.GOSUB, None, func_reference)
    
    @staticmethod
    def ENDFUNC_quadruple() -> 'FuncQuadruple':
        return FuncQuadruple(FuncOperator.ENDFUNC, None, None)


