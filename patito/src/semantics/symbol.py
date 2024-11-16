from typing import Optional
from ..classifications import Signature, SymbolType, VariableType
from ..containers import  Pair
from .symbols_table import SymbolsTable

class Symbol:
    def __init__(self, *, symbol_id: str, symbol_type: SymbolType, parent_table: 'SymbolsTable'):
        self.symbol_id: str = symbol_id
        self.symbol_type: SymbolType = symbol_type
        self.parent_table: 'SymbolsTable' = parent_table

    def is_function(self) -> bool:
        return self.symbol_type == SymbolType.FUNCTION

    def __str__(self) -> str:
        parent_id: str = self.parent_table.table_id if self.parent_table is not None else "-"
        return f"[ID: {self.symbol_id}, TYPE: {self.symbol_type.name}, PARENT: {parent_id}]"
    
class VariableSymbol(Symbol):
    def __init__(self, *, variable_id: str, parent_table: 'SymbolsTable', variable_type: Optional[VariableType] = None, is_initialized: bool = False):
        super().__init__(symbol_id=variable_id, symbol_type=SymbolType.VARIABLE, parent_table=parent_table)
        self.is_initialized: bool = is_initialized
        self.variable_type: Optional[VariableType] = variable_type

        self.__address: Optional[int] = None

    @property
    def address(self) -> int:
        if self.__address is None:
            raise LookupError(f"the variable {self.symbol_id} has an undefined address")
        return self.__address
    
    def set_address(self, address: int) -> None:
        self.__address = address

    def __str__(self) -> str:
        return super().__str__() + f" (TYPE: {self.variable_type.name}, INIT: {self.is_initialized}, ADDRESS: {self.address})"
    
    @staticmethod
    def set_type(variables: list['VariableSymbol'], variable_type: VariableType) -> None:
        for var in variables:
            var.variable_type = variable_type

    @staticmethod
    def to_operand_pair(variable: 'VariableSymbol') -> 'Pair[str, VariableType]':
        return Pair(variable.symbol_id, variable.variable_type)
    
class FunctionSymbol(Symbol):
    def __init__(self, function_id: str, signature: Signature, parent_table: 'SymbolsTable', index: int, is_defined: bool = True):
        super().__init__(symbol_id=function_id, symbol_type=SymbolType.FUNCTION, parent_table=parent_table)

        self.signature: Signature = signature
        self.index: int = index
        self.is_defined: bool = is_defined
        self.table: 'SymbolsTable' = SymbolsTable(table_id=function_id, parent_function=self)

    def __str__(self) -> str:
        return super().__str__() + f" (SIGNATURE: {'->'.join(var_type.name for var_type in self.signature)})"