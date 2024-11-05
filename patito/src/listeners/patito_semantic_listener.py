from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, Symbol
from ..classifications import SymbolType, PatitoType, token_mapper
from ..containers import Stack, Pair
from .tree_traversal import extract_id, extract_type, extract_expression
from ..quadruple import Quadruple, QuadrupleBuilder, OperandPair, OperatorPair

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        # symbol tables 
        self.root_table = SymbolsTable("global")
        self.curr_table: SymbolsTable = self.root_table
        
        # stacks
        self.id_stack: Stack[Symbol] = Stack()
        self.function_param_stack: Stack[PatitoType] = Stack()

        # flags
        self.in_param_list: bool = False

        # quadruples
        self.quadruples: list[Quadruple] = []

    def enterFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Entering function declaration 
        func_name: str = extract_id(ctx)
        func_symbol: Symbol = Symbol(id=func_name, symbol_type=SymbolType.FUNCTION, is_initialized=True)
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
        self.curr_table.parent_symbol.function_attrs.signature = self.function_param_stack.pop_all(as_queue=True)

    def enterLista_id(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration 
        if ctx.getChildCount() > 0:
            self.__push_to_id_stack(extract_id(ctx))
    
    def enterLista_id_1(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration 
        if ctx.getChildCount() > 0:
            self.__push_to_id_stack(extract_id(ctx))

    def enterId_tipo(self, ctx: PatitoParser.Id_tipoContext):
        # Entering function parameter declaration 
        if ctx.getChildCount() > 0:
            self.__push_to_id_stack(extract_id(ctx))

    def enterTipo(self, ctx: PatitoParser.TipoContext):
        # Exiting type token 
        type_token: str = extract_type(ctx)
        symbol_type: PatitoType = PatitoType.to_type(type_token)
        Symbol.set_type(self.id_stack.peek_all(as_queue=True), symbol_type)

        self.curr_table.add_symbols(self.id_stack.pop_all(as_queue=True))

        if self.in_param_list:
            self.function_param_stack.push(PatitoType.to_type(type_token))

    def enterAsigna(self, ctx: PatitoParser.AsignaContext):
        # Entering variable assignment 
        id_token: str = extract_id(ctx)
        if not self.__symbol_exists(id_token):
            raise Exception (f"undeclared variable: '{id_token}'")
        
    def exitAsigna(self, ctx: PatitoParser.AsignaContext):
        assignee: OperandPair = Pair.to_operand_pair(self.__get_symbol(extract_id(ctx)))
        expression_tokens: list[str] = extract_expression(ctx)

        if len(expression_tokens) == 1:
            assigner: OperandPair = Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
            self.quadruples.append(Quadruple.assignment(assignee, assigner))
        else:
            self.quadruples += QuadrupleBuilder(expression_tokens, self.root_table.get_variables(), self.curr_table.get_variables()).build_quadruples()
            assignment_quadr = Quadruple.assignment(assignee, self.quadruples[-1].result)
            self.quadruples.append(assignment_quadr)
        
    def enterLlamada(self, ctx: PatitoParser.LlamadaContext):
        # Entering function call 
        id_token: str = extract_id(ctx)
        if not self.__symbol_exists(id_token):
            raise Exception (f"undeclared function: '{id_token}'")
        
    def exitCiclo(self, ctx: PatitoParser.CicloContext):
        return super().exitCiclo(ctx)

    def getSymbolsTable(self) -> SymbolsTable:
        return self.root_table
    
    def getQuadruples(self) -> list[Quadruple]:
        return self.quadruples
    
    def __push_to_id_stack(self, id_token: str):
        self.id_stack.push(Symbol(id=id_token, symbol_type=SymbolType.VARIABLE))
    
    def __get_symbol(self, id_token: str) -> Symbol:
        if self.curr_table.symbol_exists(id_token):
            return self.curr_table.get_symbol(id_token)
        return self.root_table.get_symbol(id_token)        
    
    def __symbol_exists(self, id_token: str) -> bool:
        return self.curr_table.symbol_exists(id_token) or self.root_table.symbol_exists(id_token)
