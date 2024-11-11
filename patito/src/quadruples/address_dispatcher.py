from .memory_quadruple import MemoryQuadruple
from .exp_quadruple import ExpQuadruple
from .flow_quadruple import FlowQuadruple
from ..classifications import NumericOperator, VariableType, token_mapper, FlowOperator
from ..containers import OperandPair, AddressTable

class AddressDispatcher:
    def __init__(self):
        self.integers_table: AddressTable = AddressTable(base_address=0, size=1000)
        self.floats_table: AddressTable = AddressTable(base_address=1001, size=1000)
        self.constants_table: AddressTable = AddressTable(base_address=2001, size=1000)

    def build_quadruple(self, quadruple: ExpQuadruple | FlowQuadruple) -> MemoryQuadruple:
        match quadruple:
            case ExpQuadruple():
                return self.__build_quadruple_exp(quadruple)
            case FlowQuadruple():
                return self.__build_quadruple_flow(quadruple)

    def __build_quadruple_exp(self, exp_quadruple: ExpQuadruple) -> MemoryQuadruple:
        operator, *operands = exp_quadruple
        quad_items: list[int] = [self.__numeric_operator_to_code(operator.second)] + [self.__operand_to_address(operand) for operand in operands]
        return MemoryQuadruple(quad_items)
    
    def __build_quadruple_flow(self, flow_quadruple: FlowQuadruple) -> MemoryQuadruple:
        operator, operand, _, jump  = flow_quadruple
        return MemoryQuadruple([self.__flow_operator_to_code(operator), self.__operand_to_address(operand), -1, jump])
    
    def __is_constant(self, token: str) -> bool:
        token_type: NumericOperator | VariableType | None = token_mapper(token)
        return token_type == VariableType.FLOTANTE or token_type == VariableType.ENTERO
    
    def __operand_to_address(self, operand: OperandPair) -> int:
        token, token_type = operand
        
        if self.__is_constant(token):
            return self.constants_table.get_address(token)
        else:
            return self.integers_table.get_address(token) if token_type == VariableType.ENTERO else self.floats_table.get_address(token)

    def __numeric_operator_to_code(self, num_operator: NumericOperator) -> int:
        return num_operator.value

    def __flow_operator_to_code(self, flow_oprerator: FlowOperator) -> int:
        return flow_oprerator.value + len(NumericOperator)

    