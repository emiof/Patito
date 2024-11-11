from collections.abc import Iterator
from ..classifications import NumericOperator, VariableType
from ..semantics import SemanticCube
from ..containers import  Pair, OperatorPair, OperandPair
from ..exceptions import SemanticError

class ExpQuadruple:
    result_counter: int = 0
    semantic_cube: SemanticCube = SemanticCube()

    def __init__(self, operator: OperatorPair, operand_1: OperandPair, operand_2: OperandPair):
        result_type: VariableType | None = ExpQuadruple.semantic_cube.get_result_type(operator.second, operand_1.second, operand_2.second)
        if result_type is None:
            raise SemanticError.invalid_operation(operand_1.second, operator.second, operand_2.second)
        
        result: OperandPair = Pair(f"t{ExpQuadruple.result_counter}", result_type)
        self.items: tuple[OperatorPair, OperandPair, OperandPair, OperandPair] = (operator, operand_1, operand_2, result)
        ExpQuadruple.result_counter += 1

    def __iter__(self) -> Iterator[OperatorPair | OperandPair]:
        yield from self.items

    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"
    
    @property
    def result(self) -> OperandPair:
        return self.items[-1]

    @staticmethod
    def assignment(operand_1: OperandPair, operand_2: OperandPair) -> 'ExpQuadruple':
        return ExpQuadruple(Pair("=", NumericOperator.ASIGNACION), operand_1, operand_2)