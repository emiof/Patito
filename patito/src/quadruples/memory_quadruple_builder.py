from typing import Optional
from ..classifications import NumericOperator, VariableType, token_mapper, FlowOperator, SymbolType
from ..containers import OperandPair, AddressTable
from ..semantics import SymbolsTable, symbol_exists_uphill, get_symbol_uphill
from .memory_quadruple import MemoryQuadruple
from .exp_quadruple import ExpQuadruple
from .flow_quadruple import FlowQuadruple

class MemoryQuadrupleBuilder:
    def __init__(self):
        self.constants_table: AddressTable = AddressTable(base_address=1000, size=1000)
        self.symbols_table: Optional[SymbolsTable] = None

    def build_quadruple(self, quadruple: ExpQuadruple | FlowQuadruple, symbols_table: SymbolsTable) -> MemoryQuadruple:
        self.symbols_table = symbols_table
        match quadruple:
            case ExpQuadruple():
                return self.__build_quadruple_exp(quadruple)
            case FlowQuadruple():
                return self.__build_quadruple_flow(quadruple)
                        
    def build_quadruples(self, quadruples: list[ExpQuadruple | FlowQuadruple], symbols_table: SymbolsTable) -> list[MemoryQuadruple]:
        return [self.build_quadruple(quad, symbols_table) for quad in quadruples]

    def __build_quadruple_exp(self, exp_quadruple: ExpQuadruple) -> MemoryQuadruple:
        operator, *operands = exp_quadruple
        return MemoryQuadruple([self.__numeric_operator_to_code(operator.second)] + [self.__operand_to_address(operand) for operand in operands])
    
    def __build_quadruple_flow(self, flow_quadruple: FlowQuadruple) -> MemoryQuadruple:
        operator, operand, _, jump  = flow_quadruple
        return MemoryQuadruple([self.__flow_operator_to_code(operator), self.__operand_to_address(operand), -1, jump])
    
    def __is_constant(self, token: str) -> bool:
        token_type: NumericOperator | VariableType | None = token_mapper(token)
        return token_type == VariableType.FLOTANTE or token_type == VariableType.ENTERO
    
    def __operand_to_address(self, operand: OperandPair) -> int:
        token, _ = operand
        
        if self.__is_constant(token):
            return self.constants_table.get_address(token)
        else:
            if symbol_exists_uphill(self.symbols_table, token, SymbolType.VARIABLE):
                return get_symbol_uphill(self.symbols_table, token, SymbolType.VARIABLE).address
            else:
                return self.symbols_table.get_temporary_address(operand)

    def __numeric_operator_to_code(self, num_operator: NumericOperator) -> int:
        return num_operator.value

    def __flow_operator_to_code(self, flow_oprerator: FlowOperator) -> int:
        return flow_oprerator.value + len(NumericOperator)