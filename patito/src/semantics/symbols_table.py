# Python Version: 3.11.8

from ..classifications import SymbolType, PatitoType
from typing import Union

class Symbol:
    """
    Represents an element in the symbols table and contains the symbol's value as well as its semantic 
    information. 
    """
    def __init__(
            self, *,
            id: str,
            symbol_type: SymbolType = SymbolType.UNDEFINED,
            table_id: str | None = None,
            is_initialized: bool = False,
            signature: list[PatitoType] | None = []
    ):
        self.id: str = id
        self.symbol_type: SymbolType = symbol_type
        self.parent_table: SymbolsTable | None = table_id
        self.is_initialized: bool = is_initialized
        self.signature: list[PatitoType] | None = signature

        self.symbols_table: None | SymbolsTable = None

    def has_table(self) -> bool:
        return self.symbols_table is not None
    
    @staticmethod
    def set_type(symbols: list['Symbol'], symbol_type: SymbolType) -> None:
        for s in symbols:
            s.symbol_type = symbol_type         

    @property 
    def table(self) -> 'SymbolsTable':
        """
        Returns the symbol's own table of symbols. If the symbol doesn't have one, one is initialized. 
        """
        if self.symbol_type != SymbolType.FUNCION:
            raise Exception("attempting to access table of non-function symbol")
        self.symbols_table = SymbolsTable(self.id, self) if self.symbols_table is None else self.symbols_table
        return self.symbols_table
    
    def __eq__(self, other: 'Symbol') -> bool:
        return self.id == other.id and self.table_id == other.table_id
    
    def __str__(self) -> str:
        parent_id: str | None = self.parent_table.id if self.parent_table is not None else None
        return f"[ID: {self.id}, TYPE: {self.symbol_type.name}, PARENT: {parent_id}, SIGNATURE: {self.signature}, INIT: {self.is_initialized}]"

class SymbolsTable:
    """
    Represents the table of symbols pertaining to the semantic analysis of Patito. Uses a dictionary 
    to store the program's symbols. 
    """
    def __init__(self, id: str, parent_symbol: Symbol | None = None):
        self.id = id
        self.symbols: dict[str, Symbol] = {}
        self.parent_symbol: Symbol = self if parent_symbol is None else parent_symbol

    def get_symbol(self, symbol_id: str, *, at: list[str] = []) -> Symbol:
        """
        Returns the symbol identified by symbol_id within the table. If not found, an error is raised. 
        The search is not outreaching and is performed only at the current table,
        and not at any nested tables contained within. 
        """
        target_table: 'SymbolsTable' = self.__get_table(curr_table=self, scope_path=at)

        if symbol_id not in target_table.symbols:
            raise Exception(f"unable to locate symbol with id {symbol_id}")
        
        return target_table.symbols[symbol_id]
    
    def add_symbol(self, symbol: Symbol, *, at: list[str] = []) -> Symbol:
        """
        Adds a new symbol to the table. If a symbol with the same id is already present in the table, an error is raised. 
        """
        target_table: 'SymbolsTable' = self.__get_table(curr_table=self, scope_path=at)

        if symbol.id in target_table.symbols:
            raise Exception("redeclaration of symbol")
        
        symbol.parent_table = self
        target_table.symbols[symbol.id] = symbol
        return target_table.symbols[symbol.id]
    
    def add_symbols(self, symbols: list[Symbol], *, at: list[str] = []) -> None:
        """
        Adds the given symbols to the table. 
        """
        for symbol in symbols:
            self.add_symbol(symbol, at=at)

    def symbol_exists(self, symbol_id: str, *, at: list[str] = []) -> bool:
        """
        Determines if a symbol with the given id exists in the table. 
        """
        target_table: 'SymbolsTable' = self.__get_table(curr_table=self, scope_path=at)
        return symbol_id in target_table.symbols
    
    def get_ids(self, at: list[str] = []) -> list[Symbol]:
        target_table: 'SymbolsTable' = self.__get_table(curr_table=self, scope_path=at)
        return list(target_table.symbols.values())
    
    def __str__(self) -> str:
        return self.__print_table(self.get_ids(), 1)

    def __print_table(self, symbols: list[Symbol], level: int) -> str:
        if not symbols:
            return ""
        
        curr_symbol: str = "\n" + "-" * level ** 2 + symbols[0].__str__()
        rest_table: str = self.__print_table(symbols[1:], level)
        
        return curr_symbol + (self.__print_table(symbols[0].table.get_ids(), level+1) if symbols[0].has_table() else "") + rest_table 
    
    def __get_table(self, *, curr_table: 'SymbolsTable', scope_path: list[str]) -> 'SymbolsTable':
        if not scope_path:
            return curr_table
        
        next_table: str = scope_path[0]
        if next_table in self.symbols:
            return self.__get_table(curr_table=self.symbols[next_table].table, scope_path=scope_path[1:])
        
        raise Exception(f"unable to locate target table of symbol {next_table}")
