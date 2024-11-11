# Python Version: 3.11.8

from typing import Optional
from ..exceptions import SemanticError
from ..classifications import Signature, SymbolType, VariableType

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

    def __str__(self) -> str:
        return super().__str__() + f" (TYPE: {self.variable_type.name}, INIT: {self.is_initialized})"
    
    @staticmethod
    def set_type(variables: list['VariableSymbol'], variable_type: VariableType) -> None:
        for var in variables:
            var.variable_type = variable_type

class FunctionSymbol(Symbol):
    def __init__(self, function_id: str, signature: Signature, parent_table: 'SymbolsTable', is_defined: bool = True):
        super().__init__(symbol_id=function_id, symbol_type=SymbolType.FUNCTION, parent_table=parent_table)

        self.is_defined: bool = is_defined
        self.signature: Signature = signature
        self.table: 'SymbolsTable' = SymbolsTable(table_id=function_id, parent_function=self)

    def __str__(self) -> str:
        return super().__str__() + f" (SIGNATURE: {'->'.join(var_type.name for var_type in self.signature)})"

class SymbolsTable:
    def __init__(self, *, table_id: str, parent_function: Optional[FunctionSymbol] = None):
        self.table_id = table_id
        self.variables: dict[str, VariableSymbol] = {}
        self.functions: dict[str, FunctionSymbol] = {}
        self.parent_function: Optional[FunctionSymbol] = parent_function

    @property
    def parent_table(self) -> 'SymbolsTable':
        if self.parent_function is None:
            raise IndexError("trying to access non-existent parent table")
        return self.parent_function.parent_table
    
    def has_parent_table(self) -> bool:
        return self.parent_function is not None

    def get_symbol(self, symbol_id: str, symbol_type: SymbolType) -> VariableSymbol | FunctionSymbol:
        if not self.symbol_exists(symbol_id, symbol_type):
            raise ValueError(f"unable to locate symbol with id '{symbol_id}'")
        
        return self.variables[symbol_id] if symbol_type == SymbolType.VARIABLE else self.functions[symbol_id]
    
    def get_symbols_dict(self, symbol_type: SymbolType) -> dict[str, VariableSymbol | FunctionSymbol]:
        return self.variables if symbol_type == SymbolType.VARIABLE else self.functions
    
    def add_symbol(self, symbol: VariableSymbol | FunctionSymbol) -> VariableSymbol | FunctionSymbol:
        if self.symbol_exists(symbol.symbol_id, symbol.symbol_type):
            raise SemanticError.redeclaration(symbol.symbol_id)
        
        match symbol.symbol_type:
            case SymbolType.VARIABLE:
                self.variables[symbol.symbol_id] = symbol
            case SymbolType.FUNCTION:
                self.functions[symbol.symbol_id] = symbol
    
    def add_symbols(self, symbols: list[VariableSymbol | FunctionSymbol]) -> None:
        for symbol in symbols:
            self.add_symbol(symbol)

    def symbol_exists(self, symbol_id: str, symbol_type: SymbolType) -> bool:
        return symbol_id in self.variables if symbol_type == SymbolType.VARIABLE else symbol_id in self.functions

    def get_all_symbols(self) -> list[VariableSymbol | FunctionSymbol]:
        return list(self.variables.values()) + list(self.functions.values())
    
    def __str__(self) -> str:
        return self.__print_table(self.get_all_symbols(), 1)

    def __print_table(self, symbols: list[VariableSymbol | FunctionSymbol], level: int) -> str:
        if not symbols:
            return ""
        
        curr_symbol: str = "\n" + "-" * level ** 2 + symbols[0].__str__()
        rest_table: str = self.__print_table(symbols[1:], level)
        
        return curr_symbol + (self.__print_table(symbols[0].table.get_all_symbols(), level+1) if symbols[0].is_function() else "") + rest_table