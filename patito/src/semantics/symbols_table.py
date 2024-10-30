# Python Version: 3.11.8

from ..classifications import SymbolType

class Symbol:
    """
    Represents an element in the symbols table and contains the symbol's value as well as its semantic 
    information. 
    """
    def __init__(self, *, id: str, value: any, symbol_type: SymbolType, parent_table_id: str | None = None):
        self.id: str = id
        self.value: any = value
        self.symbol_type: SymbolType = symbol_type
        self.parent_table_id: str | None = parent_table_id

        self.symbols_table: None | SymbolsTable = None

    def has_table(self) -> bool:
        return self.symbols_table is not None

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

    def symbol_exists(self, symbol_id: str) -> bool:
        """
        Determines if a symbol with the given id exists in the table. 
        """
        return symbol_id in self.symbols
    
    def to_list(self) -> list['Symbol']:
        return list(self.symbols.values())
    
    def __str__(self) -> str:
        return self.__print_table(self.to_list(), 1)

    def __print_table(self, symbols: list[Symbol], level: int) -> str:
        if not symbols:
            return ""
        
        curr_symbol: str = "\n" + "-" * level ** 2 + symbols[0].__str__()
        rest_table: str = self.__print_table(symbols[1:], level)
        
        return curr_symbol + (self.__print_table(symbols[0].table.to_list(), level+1) if symbols[0].has_table() else "") + rest_table 