# Python Version: 3.11.8

import pytest
from ...src.semantics.symbols_table import SymbolsTable, Symbol
from ...src.classifications import SymbolType
from ...src.containers import Stack

@pytest.fixture
def table() -> SymbolsTable:
    root_table = SymbolsTable('global')
    curr_table: SymbolsTable = root_table
    
    var1 = Symbol(id='var1', symbol_type=SymbolType.ENTERO)
    var2 = Symbol(id='var2', symbol_type=SymbolType.FLOTANTE)
    fun1 = Symbol(id='fun1', symbol_type=SymbolType.FUNCION)

    curr_table.add_symbol(var1)
    curr_table.add_symbol(var2)
    curr_table.add_symbol(fun1)

    var3 = Symbol(id='var3', symbol_type=SymbolType.ENTERO)  

    curr_table.get_symbol('fun1').table.add_symbol(var3)

    return root_table

def test_search(table: SymbolsTable) -> None:
    assert table.symbol_exists("var1") and table.get_symbol("var1").id == 'var1'
    assert table.symbol_exists("var2") and table.get_symbol("var2").id == 'var2'
    assert table.symbol_exists("fun1") and table.get_symbol("fun1").id == 'fun1'

def test_deep_search(table: SymbolsTable) -> None:
    assert table.symbol_exists('var3', at=['fun1']) and table.get_symbol('var3', at=['fun1']).id == 'var3'

def test_add(table: SymbolsTable) -> None:
    table.add_symbol(Symbol(id='new_var', symbol_type=SymbolType.ENTERO))
    assert table.get_symbol('new_var').id == 'new_var'

def test_deep_add(table: SymbolsTable) -> None:
    fun2: Symbol = Symbol(id='fun2', symbol_type=SymbolType.FUNCION)
    fun2.table.add_symbol(Symbol(id='var4', symbol_type=SymbolType.ENTERO))
    table.add_symbol(fun2)

    assert table.symbol_exists('fun2') and table.get_symbol('fun2').table.symbol_exists('var4')    