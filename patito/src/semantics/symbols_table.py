# Python Version: 3.11.8

from typing import Optional, TYPE_CHECKING, Union
from ..exceptions import SemanticException
from ..classifications import SymbolType, VariableType
from ..containers import AddressTable, OperandPair
from ..virtual_machine import MemoryRequirements

if TYPE_CHECKING:
    from .symbol import VariableSymbol, FunctionSymbol

class SymbolsTable:
    def __init__(self, *, table_id: str, parent_function: Optional['FunctionSymbol'] = None, is_global: bool = False):
        self.table_id = table_id
        self.variables: dict[str, 'VariableSymbol'] = {}
        self.functions: dict[str, 'FunctionSymbol'] = {}
        self.parent_function: Optional['FunctionSymbol'] = parent_function

        base: int = 5000 if is_global else 9000
        self.integers_table: AddressTable = AddressTable(base_address=base, size=1000)
        self.floats_table: AddressTable = AddressTable(base_address=base+1001, size=1000)

    @property
    def parent_table(self) -> 'SymbolsTable':
        if self.parent_function is None:
            raise IndexError("trying to access non-existent parent table")
        return self.parent_function.parent_table
    
    def has_parent_table(self) -> bool:
        return self.parent_function is not None

    def get_symbol(self, symbol_id: str, symbol_type: SymbolType) -> Union['VariableSymbol', 'FunctionSymbol']:
        if not self.symbol_exists(symbol_id, symbol_type):
            raise ValueError(f"unable to locate symbol with id '{symbol_id}'")
        
        return self.variables[symbol_id] if symbol_type == SymbolType.VARIABLE else self.functions[symbol_id]
    
    def get_symbols_dict(self, symbol_type: SymbolType) -> dict[str, Union['VariableSymbol', 'FunctionSymbol']]:
        return self.variables if symbol_type == SymbolType.VARIABLE else self.functions
    
    def add_symbol(self, symbol: Union['VariableSymbol', 'FunctionSymbol']) -> Union['VariableSymbol', 'FunctionSymbol']:
        if self.symbol_exists(symbol.symbol_id, symbol.symbol_type):
            raise SemanticException.redeclaration(symbol.symbol_id)
        
        match symbol.symbol_type:
            case SymbolType.VARIABLE:
                self.variables[symbol.symbol_id] = symbol
                self.__set_variable_symbol_address(symbol)
            case SymbolType.FUNCTION:
                self.functions[symbol.symbol_id] = symbol

    def add_symbols(self, symbols: list[Union['VariableSymbol', 'FunctionSymbol']]) -> None:
        for symbol in symbols:
            self.add_symbol(symbol)

    def symbol_exists(self, symbol_id: str, symbol_type: SymbolType) -> bool:
        return symbol_id in self.variables if symbol_type == SymbolType.VARIABLE else symbol_id in self.functions

    def get_all_symbols(self) -> list[Union['VariableSymbol', 'FunctionSymbol']]:
        return list(self.variables.values()) + list(self.functions.values())
    
    def __str__(self) -> str:
        return self.__print_table(self.get_all_symbols(), 1)

    def __print_table(self, symbols: list[Union['VariableSymbol', 'FunctionSymbol']], level: int) -> str:
        if not symbols:
            return ""
        
        curr_symbol: str = "\n" + "-" * level ** 2 + symbols[0].__str__()
        rest_table: str = self.__print_table(symbols[1:], level)
        
        return curr_symbol + (self.__print_table(symbols[0].table.get_all_symbols(), level+1) if symbols[0].is_function() else "") + rest_table
    
    def get_temporary_address(self, operand: OperandPair) -> int:
        token, token_type = operand 
        match token_type:
            case VariableType.ENTERO:
                return self.integers_table.get_address(token)
            case VariableType.FLOTANTE:
                return self.floats_table.get_address(token)
            case _:
                raise ValueError(f"Operand with token {token} has no variable type")
            
    def build_memory_requirements(self) -> MemoryRequirements:
        return MemoryRequirements(self.integers_table.get_real_range(), self.floats_table.get_real_range()) 
    
    def __set_variable_symbol_address(self, symbol: 'VariableSymbol') -> None:
        match symbol.variable_type:
            case VariableType.ENTERO:
                symbol.set_address(self.integers_table.get_address(symbol.symbol_id))
            case VariableType.FLOTANTE:
                symbol.set_address(self.floats_table.get_address(symbol.symbol_id))
            case _:
                raise ValueError(f"Symbol with id {symbol.symbol_id} has no variable type")