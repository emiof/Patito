from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, Symbol
from ..semantics import SemanticCube
from ..classifications import SymbolType, PatitoType
from ..containers import Stack

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        self.root_table = SymbolsTable("global")
        self.curr_table: SymbolsTable = self.root_table
        
        # stacks
        self.id_stack: Stack[Symbol] = Stack()
        self.function_param_stack: Stack[PatitoType] = Stack()

        # flags
        self.in_param_list: bool = False

    def enterFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Entering function declaration 
        func_name: str = ctx.ID().getText()
        func_symbol: Symbol = Symbol(id=func_name, symbol_type=SymbolType.FUNCION, is_initialized=True)
        self.curr_table.add_symbol(func_symbol)

        self.curr_table = func_symbol.table

    def exitFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Exiting function body 
        self.curr_table = self.curr_table.parent_symbol.parent_table

    def enterOpc_lista_id_tipo(self, ctx: PatitoParser.Opc_lista_id_tipoContext):
        # Entering function parameter list 
        self.in_param_list = True

    def exitOpc_lista_id_tipo(self, ctx: PatitoParser.Opc_lista_id_tipoContext):
        # Exiting function parameter list 
        self.in_param_list = False
        self.curr_table.parent_symbol.signature = self.function_param_stack.pop_all(as_queue=True)

    def enterLista_id(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration 
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))
    
    def enterLista_id_1(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration 
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))

    def enterId_tipo(self, ctx: PatitoParser.Id_tipoContext):
        # Entering function parameter declaration 
        if ctx.getChildCount() > 0:
            self.id_stack.push(Symbol(id=ctx.ID().getText()))

    def enterTipo(self, ctx: PatitoParser.TipoContext):
        # Exiting type token 
        type_token: str = ctx.getChild(0).getText()
        symbol_type: SymbolType = SymbolType.to_type(type_token)
        Symbol.set_type(self.id_stack.peek_all(as_queue=True), symbol_type)

        self.curr_table.add_symbols(self.id_stack.pop_all(as_queue=True))

        if self.in_param_list:
            self.function_param_stack.push(PatitoType.to_type(type_token))

    def getSymbolsTable(self) -> SymbolsTable:
        return self.root_table

