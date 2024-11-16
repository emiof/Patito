# Python Version: 3.11.8

import pytest
from ...src.semantics import SymbolsTable, VariableSymbol, FunctionSymbol
from ...src.classifications import SymbolType, VariableType

@pytest.fixture
def table() -> SymbolsTable:
    root_table = SymbolsTable(table_id='global')
    curr_table: SymbolsTable = root_table
    
    var1 = VariableSymbol(variable_id='var1', parent_table=root_table)
    var2 = VariableSymbol(variable_id='var2', parent_table=root_table)
    VariableSymbol.set_type([var1, var2], VariableType.ENTERO) 
    
    fun1 = FunctionSymbol(function_id='fun1', signature=[VariableType.ENTERO], parent_table=root_table, index=0)

    curr_table.add_symbol(var1)
    curr_table.add_symbol(var2)
    curr_table.add_symbol(fun1)

    var3 = VariableSymbol(variable_id='var3', parent_table=fun1.table)  
    VariableSymbol.set_type([var3], VariableType.ENTERO) 

    return root_table

def test_search(table: SymbolsTable) -> None:
    assert table.symbol_exists("var1", SymbolType.VARIABLE) and table.get_symbol("var1", SymbolType.VARIABLE).symbol_id == 'var1'
    assert table.symbol_exists("var2", SymbolType.VARIABLE) and table.get_symbol("var2", SymbolType.VARIABLE).symbol_id == 'var2'
    assert table.symbol_exists("fun1", SymbolType.FUNCTION) and table.get_symbol("fun1", SymbolType.FUNCTION).symbol_id == 'fun1'


def test_add(table: SymbolsTable) -> None:
    table.add_symbol(VariableSymbol(variable_id='new_var', parent_table=table, variable_type=VariableType.FLOTANTE))
    assert table.get_symbol('new_var', SymbolType.VARIABLE).symbol_id == 'new_var'