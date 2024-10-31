# Python Version: 3.11.8

from ..classifications import SymbolType
from typing import Union

class Symbol:
    """
    Represents an element in the symbols table and contains the symbol's value as well as its semantic 
    information. 
    """
    def __init__(self, *, id: str, value: any = None, symbol_type: SymbolType = SymbolType.UNDEFINED, parent_table_id: str | None = None):
        self.id: str = id
        self.value: any | None = value
        self.symbol_type: SymbolType = symbol_type
        self.parent_table_id: str | None = parent_table_id

        self.symbols_table: None | SymbolsTable = None

    def has_table(self) -> bool:
        return self.symbols_table is not None
    
    @staticmethod
    def set_symbols_type(symbols: list['Symbol'], symbol_type: SymbolType) -> None:
        for s in symbols:
            s.symbol_type = symbol_type
    
    @staticmethod
    def build_symbols(ids: list[str], symbol_type: SymbolType, values: list[any] | None = None) -> list['Symbol']:
        if values != None:
            if len(ids) != len(values):
                raise Exception("the number of ids doesn't match the number of values")
            return [Symbol(id=id, value=value, symbol_type=symbol_type) for id, value in zip(ids, values)]
        else:
            return [Symbol(id=id, value=None, symbol_type=symbol_type) for id in ids]            

    @property 
    def table(self) -> 'SymbolsTable':
        """
        Returns the symbol's own table of symbols. If the symbol doesn't have one, one is initialized. 
        """
        self.symbols_table = SymbolsTable(self.id) if self.symbols_table is None else self.symbols_table
        return self.symbols_table
    
    def __eq__(self, other: 'Symbol') -> bool:
        return self.id == other.id and self.parent_table_id == other.parent_table_id
    
    def __str__(self) -> str:
        return f"[{self.id}, {self.value}, {self.symbol_type.name}, {self.parent_table_id}]"

class SymbolsTable:
    """
    Represents the table of symbols pertaining to the semantic analysis of Patito. Uses a dictionary 
    to store the program's symbols. 
    """
    def __init__(self, table_id: str):
        self.table_id = table_id
        self.symbols: dict[str, Symbol] = {}

    def search_symbol(self, symbol_id: str) -> Symbol | None:
        """
        Returns the symbol identified by symbol_id within the table. If not found, returns None. 
        The search is not outreaching and is performed only at the current table,
        and not at any nested tables contained within. 
        """
        return self.symbols.get(symbol_id, None)        

    def add_symbol(self, symbol: Symbol) -> Symbol:
        """
        Adds a new symbol to the table. If a symbol with the same id is already present in the table, it is
        overwritten.
        """
        symbol.parent_table_id = self.table_id
        self.symbols[symbol.id] = symbol

        return self.symbols[symbol.id]
    
    def add_symbols(self, symbols: list[Symbol]) -> None:
        """
        Adds the given symbols to the table. 
        """
        for symbol in symbols:
            self.add_symbol(symbol)

    def symbol_exists(self, symbol_id: str) -> bool:
        """
        Determines if a symbol with the given id exists in the table. 
        """
        return symbol_id in self.symbols
    
    def get_table_at(self, scope_path: list[str]) -> Union['SymbolsTable', None]:
        if not scope_path:
            return self
        return self.___get_table_at_aux(self, scope_path)

    def ___get_table_at_aux(self, curr_table: Union['SymbolsTable', None], tables_path: list[str]) -> Union['SymbolsTable', None]:
        if not tables_path:
            return curr_table

        next_table: 'Symbol' | None = curr_table.search_symbol(tables_path[0]).table
        return self.___get_table_at_aux(next_table, tables_path[1:])
    
    def to_list(self) -> list[Symbol]:
        return list(self.symbols.values())
    
    def __str__(self) -> str:
        return self.__print_table(self.to_list(), 1)

    def __print_table(self, symbols: list[Symbol], level: int) -> str:
        if not symbols:
            return ""
        
        curr_symbol: str = "\n" + "-" * level ** 2 + symbols[0].__str__()
        rest_table: str = self.__print_table(symbols[1:], level)
        
        return curr_symbol + (self.__print_table(symbols[0].table.to_list(), level+1) if symbols[0].has_table() else "") + rest_table 