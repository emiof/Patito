from typing import Optional
from ..classifications import NumericOperator, VariableType
from ..semantics import SemanticCube
from ..containers import  Pair, OperatorPair, OperandPair
from ..exceptions import SemanticError
from .utils import examinable

@examinable
class ExpQuadruple:
    result_counter: int = 0
    semantic_cube: SemanticCube = SemanticCube()

    def __init__(self, operator: OperatorPair, operand_1: OperandPair, operand_2: OperandPair, result_is_none: bool = False):
        result_type: VariableType | None = ExpQuadruple.semantic_cube.get_result_type(operator.second, operand_1.second, operand_2.second)
        if result_type is None:
            raise SemanticError.invalid_operation(operand_1.second, operator.second, operand_2.second)
        
        if not result_is_none:
            result: OperandPair = Pair(f"t{ExpQuadruple.result_counter}", result_type)
            ExpQuadruple.result_counter += 1
        else:
            result = None
        
        self.items: tuple[OperatorPair, OperandPair, OperandPair, Optional[OperandPair]] = (operator, operand_1, operand_2, result)
    
    @property
    def result(self) -> OperandPair:
        return self.items[-1]

    @staticmethod
    def assignment(operand_1: OperandPair, operand_2: OperandPair) -> 'ExpQuadruple':
        return ExpQuadruple(Pair("=", NumericOperator.ASIGNACION), operand_1, operand_2, result_is_none=True)