# Python Version: 3.11.8

import pytest
from ...src.semantics.symbols_table import SymbolsTable, Symbol
from ...src.classifications import SymbolType

@pytest.fixture
def table() -> SymbolsTable:
    var1 = Symbol(id='var1', value=10, symbol_type=SymbolType.ENTERO)
    var2 = Symbol(id='var2', value=1.5, symbol_type=SymbolType.FLOTANTE)
    fun1 = Symbol(id='fun1', value=None, symbol_type=SymbolType.FUNCION)
    
    var3 = Symbol(id='var3', value=5, symbol_type=SymbolType.ENTERO)
    fun1.table.add_symbol(var3)
    
    table = SymbolsTable('global')

    table.add_symbol(var1)
    table.add_symbol(var2)
    table.add_symbol(fun1)

    return table

def test_search(table: SymbolsTable) -> None:
    assert table.symbol_exists("var1") and table.search_symbol("var1").id == 'var1'
    assert table.symbol_exists("var2") and table.search_symbol("var2").id == 'var2'
    assert table.symbol_exists("fun1") and table.search_symbol("fun1").id == 'fun1'

def test_deep_search(table: SymbolsTable) -> None:
    fun1: Symbol | None = table.search_symbol('fun1')
    assert fun1 is not None
    assert fun1.table.symbol_exists('var3') and fun1.table.search_symbol('var3').id == 'var3'

def test_add(table: SymbolsTable) -> None:
    table.add_symbol(Symbol(id='new_var', value=10, symbol_type=SymbolType.ENTERO))
    assert table.search_symbol('new_var') is not None and table.search_symbol('new_var').id == 'new_var'

def test_deep_add(table: SymbolsTable) -> None:
    fun2: Symbol = Symbol(id='fun2', value=None, symbol_type=SymbolType.FUNCION)
    fun2.table.add_symbol(Symbol(id='var4', value=10, symbol_type=SymbolType.ENTERO))
    table.add_symbol(fun2)

    assert table.symbol_exists('fun2') and table.search_symbol('fun2').table.symbol_exists('var4')
    