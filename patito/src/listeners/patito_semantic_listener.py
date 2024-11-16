from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, VariableSymbol, FunctionSymbol, symbol_exists_uphill, get_symbol_uphill, build_memory_requiremnts_downhill
from ..classifications import VariableType, token_mapper, Signature, SymbolType, QuadrupleType
from ..containers import Stack, Pair, Register
from ..quadruples import ExpQuadruple, ExpQuadrupleBuilder, FlowQuadruple, OperandPair, TrueQuadruple, TrueQuadrupleBuilder, JumpResolver
from ..exceptions import SemanticError
from ..virtual_machine import MemoryRequirements
from .tree_traversal import extract_id, extract_type, extract_expression, extract_signature

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        # symbol tables 
        self.root_table = SymbolsTable(table_id="global", is_global=True)
        self.curr_table: SymbolsTable = self.root_table
        # stacks
        self.variable_stack: Stack[VariableSymbol] = Stack()
        # quadruples
        self.quadruples_register: Register[ExpQuadruple | FlowQuadruple] = Register()
        self.true_quadruples_register: Register[TrueQuadruple] = Register()
        # jump resolvers 
        self.quadruple_jump_resolver: JumpResolver[FlowQuadruple] = JumpResolver()
        self.true_quadruple_jump_resolver: JumpResolver[TrueQuadruple] = JumpResolver()
        # address dispatcher
        self.true_quadruple_builder: TrueQuadrupleBuilder = TrueQuadrupleBuilder()

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
        self.__register_quadruples_batch(context_quadruples, self.true_quadruple_builder.build_quadruples(context_quadruples, self.curr_table))

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
        
        self.__register_quadruples_batch(context_quadruples, self.true_quadruple_builder.build_quadruples(context_quadruples, self.curr_table))
        
        goto_f: FlowQuadruple = FlowQuadruple.GOTO_F_quadruple(operand)
        true_goto_f: TrueQuadruple = self.true_quadruple_builder.build_quadruple(goto_f, self.curr_table)
        self.__register_quadruple(goto_f, true_goto_f)
        self.__poise_quadruple(goto_f, true_goto_f)

    def enterOpc_sino(self, ctx: PatitoParser.Opc_sinoContext):
        # Entering 'else' body of the if statement, or end of the if statement if 'else' body isn't present. 
        goto: FlowQuadruple = FlowQuadruple.GOTO_quadruple()
        true_goto: TrueQuadruple = self.true_quadruple_builder.build_quadruple(goto, self.curr_table)
        self.__register_quadruple(goto, true_goto)
        self.__resolve_quadruple(self.__get_next_record_index())
        self.__poise_quadruple(goto, true_goto)

    def exitOpc_sino(self, ctx: PatitoParser.Opc_sinoContext):
        self.__resolve_quadruple(self.__get_next_record_index())

    def enterCiclo(self, ctx: PatitoParser.CicloContext):
        # Entering while loop. 
        self.__poise_jump(self.__get_next_record_index())
        expression_tokens: list[str] = extract_expression(ctx)
        context_quadruples: list[ExpQuadruple | FlowQuadruple] = []

        if len(expression_tokens) == 1:
            operand: OperandPair = Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
        else:
            context_quadruples += ExpQuadrupleBuilder(expression_tokens, self.curr_table).build_quadruples()
            operand: OperandPair = context_quadruples[-1].result

        self.__register_quadruples_batch(context_quadruples, self.true_quadruple_builder.build_quadruples(context_quadruples, self.curr_table))
        
        goto: FlowQuadruple = FlowQuadruple.GOTO_F_quadruple(operand)
        true_goto: TrueQuadruple = self.true_quadruple_builder.build_quadruple(goto, self.curr_table)
        self.__register_quadruple(goto, true_goto)
        self.__poise_quadruple(goto, true_goto)

    def exitCiclo(self, ctx: PatitoParser.CicloContext):
        # Existing while loop.
        goto: FlowQuadruple = FlowQuadruple.GOTO_quadruple()
        true_goto: TrueQuadruple = self.true_quadruple_builder.build_quadruple(goto, self.curr_table)
        self.__register_quadruple(goto, true_goto)
        self.__resolve_jump(goto, true_goto)
        self.__resolve_quadruple(self.__get_next_record_index())

    def get_symbols_table(self) -> SymbolsTable:
        return self.root_table
    
    def get_quadruples(self) -> Register[ExpQuadruple | FlowQuadruple]:
        return self.quadruples_register
    
    def get_true_quadruples(self) -> Register[TrueQuadruple]:
        return self.true_quadruples_register
    
    def get_constants_storage(self) -> dict[int, int | float | str]:
        return self.true_quadruple_builder.get_constants_storage()
    
    def get_all_memory_requirements(self) -> dict[str, MemoryRequirements]:
        return build_memory_requiremnts_downhill(self.root_table)
    
    def __get_next_record_index(self) -> int:
        if self.quadruples_register.next_record_index != self.true_quadruples_register.next_record_index:
            raise Exception("quadruple registers have become desynchronized")
        return self.quadruples_register.next_record_index
    
    def __poise_quadruple(self, quadruple: FlowQuadruple, true_quadruple: TrueQuadruple) -> None:
        self.quadruple_jump_resolver.poise_quadruple(quadruple)
        self.true_quadruple_jump_resolver.poise_quadruple(true_quadruple)

    def __poise_jump(self, jump: int) -> None:
        self.quadruple_jump_resolver.poise_jump(jump)
        self.true_quadruple_jump_resolver.poise_jump(jump)

    def __resolve_jump(self, quadruple: FlowQuadruple, true_quadruple: TrueQuadruple) -> None:
        self.quadruple_jump_resolver.resolve_jump(quadruple)
        self.true_quadruple_jump_resolver.resolve_jump(true_quadruple)

    def __resolve_quadruple(self, jump: int) -> None:
        self.quadruple_jump_resolver.resolve_quadruple(jump)
        self.true_quadruple_jump_resolver.resolve_quadruple(jump)

    def __register_quadruple(self, quadruple: ExpQuadruple | FlowQuadruple, true_quadruple: TrueQuadruple) -> None:
        self.quadruples_register.add_record(quadruple)
        self.true_quadruples_register.add_record(true_quadruple)
    
    def __register_quadruples_batch(self, quadruples_batch: list[ExpQuadruple, FlowQuadruple], true_quadruples_batch: list[TrueQuadruple]) -> None:
        if len(quadruples_batch) != len(true_quadruples_batch):
            raise ValueError("providing batches of different sizes")
        self.quadruples_register.add_records(quadruples_batch)
        self.true_quadruples_register.add_records(true_quadruples_batch)