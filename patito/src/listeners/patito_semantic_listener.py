from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, Symbol
from ..semantics import SemanticCube
from ..classifications import SymbolType
from ..misc import Stack

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        self.symbols_table = SymbolsTable("global")
        
        self.scope_stack = Stack()
        self.id_stack = Stack()

    def enterFunc(self, ctx: PatitoParser.FuncContext) -> None:
        func_symbol: Symbol = Symbol(id=ctx.ID().getText(), value=None, symbol_type=SymbolType.FUNCION)
        self.symbols_table.get_table_at(self.scope_stack.items).add_symbol(func_symbol)

        self.scope_stack.push(ctx.ID().getText())

    def exitFunc(self, ctx: PatitoParser.FuncContext) -> None:
        self.scope_stack.pop()

    def enterLista_id(self, ctx: PatitoParser.Lista_idContext):
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))
    
    def enterLista_id_1(self, ctx: PatitoParser.Lista_idContext):
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))

    def enterId_tipo(self, ctx: PatitoParser.Id_tipoContext):
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))

    def enterTipo(self, ctx: PatitoParser.TipoContext):
        symbol_type: SymbolType = SymbolType.to_type(ctx.getChild(0).getText())
        Symbol.set_type(self.id_stack.items, symbol_type)
        self.symbols_table.get_table_at(self.scope_stack.items).add_symbols(self.id_stack.pop_all())

    def getSymbolsTable(self) -> SymbolsTable:
        return self.symbols_table

