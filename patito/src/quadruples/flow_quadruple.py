from typing import Optional, Union
from ..classifications import VariableType, FlowOperator
from ..exceptions import SemanticError
from ..containers import Pair, OperandPair
from .exp_quadruple import ExpQuadruple
from .utils import examinable

@examinable
class FlowQuadruple:
    def __init__(self, flow_operator: FlowOperator, operand: OperandPair, jump_location: Optional[int] = None):
        if operand.second != VariableType.ENTERO:
            raise SemanticError.expected_boolean(operand.first)
        self.items: list[FlowOperator, OperandPair, None, Optional[int]] = [flow_operator, operand, None, jump_location]

    def set_jump(self, jump: int) -> None:
        if self.items[-1] is not None:
            raise ValueError("attempting to overwrite a jump action")
        self.items[-1] = jump
    
    @staticmethod
    def GOTO_F_quadruple(operand: OperandPair) -> 'FlowQuadruple':
        return FlowQuadruple(FlowOperator.GOTO_F, operand)
    
    @staticmethod
    def GOTO_quadruple() -> 'FlowQuadruple':
        return FlowQuadruple(FlowOperator.GOTO, Pair("1", VariableType.ENTERO))
    
    @staticmethod
    def extract_flow_quadruples(quadruples: list[Union['FlowQuadruple', ExpQuadruple]]) -> list['FlowQuadruple']:
        return [quad for quad in quadruples if isinstance(quad, FlowQuadruple)]