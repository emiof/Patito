from ..exceptions import SemanticException
from ..classifications import SymbolType
from ..virtual_machine import MemoryRequirements
from .symbols_table import SymbolsTable
from .symbol import VariableSymbol

def symbol_exists_uphill(curr_table: SymbolsTable, symbol_id: str, symbol_type: SymbolType) -> bool:
    if curr_table.symbol_exists(symbol_id, symbol_type):
        return True
    elif not curr_table.has_parent_table():
        return False
    
    return symbol_exists_uphill(curr_table.parent_table, symbol_id, symbol_type)

def get_symbol_uphill(curr_table: SymbolsTable, symbol_id: str, symbol_type: SymbolType) -> VariableSymbol:
    if curr_table.symbol_exists(symbol_id, symbol_type):
        return curr_table.get_symbol(symbol_id, symbol_type)
    elif not curr_table.has_parent_table():
        raise LookupError(f"unable to locate symbol with id '{symbol_id}'")
    
    return get_symbol_uphill(curr_table.parent_table, symbol_id, symbol_type)

def build_memory_requiremnts_downhill(curr_table: SymbolsTable) -> dict[str, MemoryRequirements]:
    memory_requirements: dict[str, MemoryRequirements] = {curr_table.table_id : curr_table.build_memory_requirements()}

    for symbol in curr_table.get_all_symbols():
        if symbol.is_function():
            memory_requirements.update(build_memory_requiremnts_downhill(symbol.table))
    
    return memory_requirements

def validate_initialization_downhill(curr_table: SymbolsTable) -> None:
    for symbol in curr_table.get_all_symbols():
        if symbol.is_function():
            validate_initialization_downhill(symbol.table)
        elif not symbol.is_initialized:
            raise SemanticException.uninitialized(symbol.symbol_id)
            


