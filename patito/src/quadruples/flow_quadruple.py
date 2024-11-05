from typing import Optional
from ..classifications import PatitoType, FlowOperator
from ..exceptions import SemanticError
from ..containers import Pair, OperandPair

class FlowQuadruple:
    def __init__(self, flow_operator: FlowOperator, operand: OperandPair, jump_location: Optional[int] = None):
        if operand.second != PatitoType.ENTERO:
            raise SemanticError.expected_boolean(operand.first)
        self.items: tuple[FlowOperator, OperandPair, None, Optional[int]] = (flow_operator, operand, None, jump_location)

    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"
    
    @staticmethod
    def GOTO_F_quadruple(operand: OperandPair) -> 'FlowQuadruple':
        return FlowQuadruple(FlowOperator.GOTO_F, operand)
    
    @staticmethod
    def GOTO_quadruple() -> 'FlowQuadruple':
        return FlowQuadruple(FlowOperator.GOTO, Pair(1, PatitoType.ENTERO))