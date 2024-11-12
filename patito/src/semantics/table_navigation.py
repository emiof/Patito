from ..classifications import SymbolType
from .symbols_table import SymbolsTable, VariableSymbol

def symbol_exists_uphill(curr_table: SymbolsTable, symbol_id: str, symbol_type: SymbolType) -> bool:
    if curr_table.symbol_exists(symbol_id, symbol_type):
        return True
    elif not curr_table.has_parent_table():
        return False
    
    return symbol_exists_uphill(curr_table.parent_table, symbol_id, symbol_type)

def get_symbol_uphill(curr_table: 'SymbolsTable', symbol_id: str, symbol_type: SymbolType) -> VariableSymbol:
    if curr_table.symbol_exists(symbol_id, symbol_type):
        return curr_table.get_symbol(symbol_id, symbol_type)
    elif not curr_table.has_parent_table():
        raise LookupError(f"unable to locate symbol with id '{symbol_id}'")
    
    return get_symbol_uphill(curr_table.parent_table, symbol_id, symbol_type)