from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, VariableSymbol, FunctionSymbol, symbol_exists_uphill, get_symbol_uphill
from ..classifications import VariableType, token_mapper, Signature, SymbolType
from ..containers import Stack, Pair
from ..quadruples import ExpQuadruple, ExpQuadrupleBuilder, FlowQuadruple, OperandPair, MemoryQuadruple, MemoryQuadrupleBuilder
from ..exceptions import SemanticError
from .tree_traversal import extract_id, extract_type, extract_expression, extract_signature

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        # symbol tables 
        self.root_table = SymbolsTable(table_id="global", is_global=True)
        self.curr_table: SymbolsTable = self.root_table
        # stacks
        self.variable_stack: Stack[VariableSymbol] = Stack()
        # quadruples
        self.quadruples: list[ExpQuadruple | FlowQuadruple] = []
        self.memory_quadruples: list[MemoryQuadruple] = []
        # address dispatcher
        self.memory_quadruple_builder: MemoryQuadrupleBuilder = MemoryQuadrupleBuilder()

    def enterFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Entering function declaration 
        func_name: str = extract_id(ctx)
        func_signature: Signature = extract_signature(ctx.opc_lista_id_tipo())
        function: FunctionSymbol = FunctionSymbol(function_id=func_name, signature=func_signature, parent_table=self.curr_table)

        self.curr_table.add_symbol(function)
        self.curr_table = function.table

    def exitFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Exiting function body.
        self.curr_table = self.curr_table.parent_table

    def enterLista_id(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration.
        if ctx.getChildCount() > 0:
            self.variable_stack.push(VariableSymbol(variable_id=extract_id(ctx), parent_table=self.curr_table))
    
    def enterLista_id_1(self, ctx: PatitoParser.Lista_idContext):
        # Entering variable declaration.
        if ctx.getChildCount() > 0:
            self.variable_stack.push(VariableSymbol(variable_id=extract_id(ctx), parent_table=self.curr_table))

    def enterId_tipo(self, ctx: PatitoParser.Id_tipoContext):
        # Entering function parameter declaration.
        if ctx.getChildCount() > 0:
            self.variable_stack.push(VariableSymbol(variable_id=extract_id(ctx), parent_table=self.curr_table))

    def enterTipo(self, ctx: PatitoParser.TipoContext):
        # Exiting type token.
        variable_type: VariableType = VariableType.to_type(extract_type(ctx))
        VariableSymbol.set_type(self.variable_stack.peek_all(as_queue=True), variable_type)

        self.curr_table.add_symbols(self.variable_stack.pop_all(as_queue=True))

    def enterAsigna(self, ctx: PatitoParser.AsignaContext):
        # Entering variable assignment.
        variable_id: str = extract_id(ctx)
        if not symbol_exists_uphill(self.curr_table, variable_id, SymbolType.VARIABLE):
            raise SemanticError.undeclared_symbol(variable_id)
        
    def exitAsigna(self, ctx: PatitoParser.AsignaContext):
        # Existing variable assignment.
        variable: VariableSymbol = get_symbol_uphill(self.curr_table, extract_id(ctx), SymbolType.VARIABLE)
        assignee: OperandPair = VariableSymbol.to_operand_pair(variable)
        expression_tokens: list[str] = extract_expression(ctx)
        context_quadruples: list[ExpQuadruple | FlowQuadruple] = []

        if len(expression_tokens) == 1:
            assigner: OperandPair = Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
        else:
            context_quadruples += ExpQuadrupleBuilder(expression_tokens, self.curr_table).build_quadruples()
            assigner: OperandPair = context_quadruples[-1].result

        context_quadruples.append(ExpQuadruple.assignment(assignee, assigner))
        self.__add_quadruples_batch(context_quadruples)
        variable.is_initialized = True
        
    def enterLlamada(self, ctx: PatitoParser.LlamadaContext):
        # Entering function call.
        function_id: str = extract_id(ctx)
        if not symbol_exists_uphill(self.curr_table, function_id, SymbolType.FUNCTION):
            raise SemanticError.undeclared_symbol(function_id)
        
    def enterCondicion(self, ctx: PatitoParser.CicloContext):
        # Entering if statement.
        expression_tokens: list[str] = extract_expression(ctx)
        context_quadruples: list[ExpQuadruple | FlowQuadruple] = []

        if len(expression_tokens) == 1:
            operand: OperandPair = Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
        else:
            context_quadruples += ExpQuadrupleBuilder(expression_tokens, self.curr_table).build_quadruples()
            operand: OperandPair = context_quadruples[-1].result
        
        context_quadruples.append(FlowQuadruple.GOTO_F_quadruple(operand))
        self.__add_quadruples_batch(context_quadruples)

    def enterOpc_sino(self, ctx: PatitoParser.Opc_sinoContext):
        # Entering 'else' body of the if statement. 
        self.quadruples.append(FlowQuadruple.GOTO_quadruple())

    def enterCiclo(self, ctx: PatitoParser.CicloContext):
        # Entering while loop. 
        expression_tokens: list[str] = extract_expression(ctx)
        context_quadruples: list[ExpQuadruple | FlowQuadruple] = []

        if len(expression_tokens) == 1:
            operand: OperandPair = Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
        else:
            context_quadruples += ExpQuadrupleBuilder(expression_tokens, self.curr_table).build_quadruples()
            operand: OperandPair = context_quadruples[-1].result
        
        context_quadruples.append(FlowQuadruple.GOTO_F_quadruple(operand))
        self.__add_quadruples_batch(context_quadruples)

    def exitCiclo(self, ctx: PatitoParser.CicloContext):
        # Existing while loop.
        self.quadruples.append(FlowQuadruple.GOTO_quadruple())

    def getSymbolsTable(self) -> SymbolsTable:
        return self.root_table
    
    def getQuadruples(self) -> list[ExpQuadruple]:
        return self.quadruples
    
    def getMemoryQuadruples(self) -> list[MemoryQuadruple]:
        return self.memory_quadruples
    
    def __add_quadruples_batch(self, quadruples_batch: list[ExpQuadruple, FlowQuadruple]) -> None:
        self.quadruples += quadruples_batch
        self.memory_quadruples += self.memory_quadruple_builder.build_quadruples(quadruples_batch, self.curr_table)