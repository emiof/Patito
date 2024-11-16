from typing import Optional
from ..classifications import NumericOperator, VariableType, token_mapper, SymbolType, QuadrupleType, FuncOperator
from ..containers import OperandPair, AddressTable
from ..semantics import SymbolsTable, symbol_exists_uphill, get_symbol_uphill
from .true_quadruple import TrueQuadruple
from .exp_quadruple import ExpQuadruple
from .flow_quadruple import FlowQuadruple
from .stmt_quadurple import StmtQuadruple
from .func_quadruple import FuncQuadruple
from .utils import cast

class TrueQuadrupleBuilder:
    def __init__(self):
        self.constants_table: AddressTable = AddressTable(base_address=1000, size=1000)
        self.constants_storage: dict[int, int | float | str] = {}
        self.symbols_table: Optional[SymbolsTable] = None

    def build_quadruple(self, quadruple: ExpQuadruple | FlowQuadruple | StmtQuadruple | FuncQuadruple, symbols_table: SymbolsTable) -> TrueQuadruple:
        self.symbols_table = symbols_table
        match quadruple:
            case ExpQuadruple():
                return self.__build_quadruple_exp(quadruple)
            case FlowQuadruple():
                return self.__build_quadruple_flow(quadruple)
            case StmtQuadruple():
                return self.__build_quadruple_stmt(quadruple)
            case FuncQuadruple():
                return self.__build_quadruple_func(quadruple)
                        
    def build_quadruples(self, quadruples: list[ExpQuadruple | FlowQuadruple], symbols_table: SymbolsTable) -> list[TrueQuadruple]:
        return [self.build_quadruple(quad, symbols_table) for quad in quadruples]
    
    def get_constants_storage(self) -> dict[int, int | float | str]:
        return self.constants_storage

    def __build_quadruple_exp(self, exp_quadruple: ExpQuadruple) -> TrueQuadruple:
        operator, *operands = exp_quadruple
        quad_items: list[int] = [operator.second.value] + [self.__operand_to_address(operand) for operand in operands]
        return TrueQuadruple(quad_items, QuadrupleType.EXP)
    
    def __build_quadruple_flow(self, flow_quadruple: FlowQuadruple) -> TrueQuadruple:
        operator, operand, _, jump  = flow_quadruple
        quad_items: list[int] = [operator.value, self.__operand_to_address(operand), -1, jump]
        return TrueQuadruple(quad_items, quadruple_type=QuadrupleType.FLOW)
    
    def __build_quadruple_stmt(self, stmt_quadruple: StmtQuadruple) -> TrueQuadruple:
        operator, operand, _, _ = stmt_quadruple
        return TrueQuadruple([operator.value, self.__operand_to_address(operand), -1, -1], QuadrupleType.STMT)
    
    def __build_quadruple_func(self, func_quadruple: FuncQuadruple) -> TrueQuadruple:
        operator, operand, _, func_reference = func_quadruple
        match operator:
            case FuncOperator.ERA | FuncOperator.GOSUB:
                return TrueQuadruple([operator.value, None, None, func_reference], QuadrupleType.FUNC)
            case FuncOperator.PARAM:
                return TrueQuadruple([operator.value, self.__operand_to_address(operand), None, None], QuadrupleType.FUNC)
            case FuncOperator.ENDFUNC:
                return TrueQuadruple([operator.value, None, None, None], QuadrupleType.FUNC)


    def __is_constant(self, token: str) -> bool:
        token_type: NumericOperator | VariableType | None = token_mapper(token)
        return isinstance(token_type, VariableType)
    
    def __operand_to_address(self, operand: Optional[OperandPair]) -> int:
        if operand is None:
            return -1
        
        token, token_type = operand
        if self.__is_constant(token):
            constant_address: int = self.constants_table.get_address(token)
            self.constants_storage[constant_address] = cast(token, token_type)
            return constant_address
        else:
            if symbol_exists_uphill(self.symbols_table, token, SymbolType.VARIABLE):
                return get_symbol_uphill(self.symbols_table, token, SymbolType.VARIABLE).address
            else:
                return self.symbols_table.get_temporary_address(operand)