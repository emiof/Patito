from typing import Optional
from ..classifications import StmtOperator, VariableType
from ..containers import Pair, OperandPair
from .utils import examinable

@examinable
class StmtQuadruple:
    def __init__(self, operator: StmtOperator, operand: OperandPair):        
        self.items: list[StmtOperator, Pair[str, Optional[VariableType]], None, None] = [operator, operand, None, None]

    @staticmethod
    def IMPRIME_quadruple(operand: OperandPair) -> 'StmtQuadruple':
        return StmtQuadruple(StmtOperator.IMPRIME, operand)

