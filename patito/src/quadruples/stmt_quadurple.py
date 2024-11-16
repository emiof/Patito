from typing import Optional
from ..classifications import StmtOperator, VariableType
from ..containers import Pair
from .utils import examinable

@examinable
class StmtQuadruple:
    def __init__(self, operator: StmtOperator, operand: Pair[str, Optional[VariableType]]):        
        self.items: list[StmtOperator, Pair[str, Optional[VariableType]], None, None] = [operator, operand, None, None]
