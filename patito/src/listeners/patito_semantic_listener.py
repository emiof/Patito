from ..syntax import PatitoListener, PatitoParser
from ..semantics import SymbolsTable, VariableSymbol, FunctionSymbol, symbol_exists_uphill, get_symbol_uphill, build_memory_requiremnts_downhill
from ..classifications import VariableType, token_mapper, Signature, SymbolType
from ..containers import Stack, Pair, Register
from ..quadruples import ExpQuadruple, ExpQuadrupleBuilder, FlowQuadruple, OperandPair, TrueQuadruple, TrueQuadrupleBuilder, JumpResolver, StmtQuadruple, FuncQuadruple
from ..exceptions import SemanticError
from ..virtual_machine import MemoryRequirements
from .tree_traversal import extract_id, extract_type, extract_expression, extract_signature, extract_expression_list

class PatitoSemanticListener(PatitoListener):
    def __init__(self):
        # symbol tables 
        self.root_table = SymbolsTable(table_id="global", is_global=True)
        self.curr_table: SymbolsTable = self.root_table
        # stacks
        self.variable_stack: Stack[VariableSymbol] = Stack()
        # quadruples
        self.quadruples_register: Register[ExpQuadruple | FlowQuadruple | StmtQuadruple | FuncQuadruple] = Register()
        self.true_quadruples_register: Register[TrueQuadruple] = Register()
        # jump resolvers 
        self.quadruple_jump_resolver: JumpResolver[FlowQuadruple] = JumpResolver()
        self.true_quadruple_jump_resolver: JumpResolver[TrueQuadruple] = JumpResolver()
        # address dispatcher
        self.true_quadruple_builder: TrueQuadrupleBuilder = TrueQuadrupleBuilder()

    def enterPrograma(self, ctx: PatitoParser.ProgramaContext):
        goto__quadruple: FlowQuadruple = FlowQuadruple.GOTO_quadruple()
        true__goto_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(goto__quadruple, self.curr_table)
        self.__register_quadruple(goto__quadruple, true__goto_quadruple)
        self.__poise_quadruple(goto__quadruple, true__goto_quadruple)

    def exitOpc_lista_func(self, ctx: PatitoParser.Opc_lista_funcContext):
        if ctx.getChildCount() == 0:
            self.__resolve_quadruple(self.quadruples_register.next_record_index)

    def enterFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Entering function declaration 
        func_name: str = extract_id(ctx)
        func_signature: Signature = extract_signature(ctx.opc_lista_id_tipo())
        function: FunctionSymbol = FunctionSymbol(function_id=func_name, signature=func_signature, parent_table=self.curr_table, index=self.quadruples_register.next_record_index)

        self.curr_table.add_symbol(function)
        self.curr_table = function.table

    def exitFunc(self, ctx: PatitoParser.FuncContext) -> None:
        # Exiting function body.
        self.curr_table = self.curr_table.parent_table
        endfunc_quadruple: FuncQuadruple = FuncQuadruple.ENDFUNC_quadruple()
        true_endfunc_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(endfunc_quadruple, self.curr_table)
        self.__register_quadruple(endfunc_quadruple, true_endfunc_quadruple)

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
            self.variable_stack.push(VariableSymbol(variable_id=extract_id(ctx), parent_table=self.curr_table, is_initialized=True))

    def enterTipo(self, ctx: PatitoParser.TipoContext):
        # Exiting variable type token.
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

        assigner: OperandPair = self.__process_expresion(extract_expression(ctx.expresion()))

        context_quadruple: ExpQuadruple = ExpQuadruple.assignment(assignee, assigner)
        true_context_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(context_quadruple, self.curr_table)
        self.__register_quadruple(context_quadruple, true_context_quadruple)
        variable.is_initialized = True
        
    def enterLlamada(self, ctx: PatitoParser.LlamadaContext):
        # Entering function call.
        function_id: str = extract_id(ctx)
        if not symbol_exists_uphill(self.curr_table, function_id, SymbolType.FUNCTION):
            raise SemanticError.undeclared_symbol(function_id)
        
    def exitLlamada(self, ctx: PatitoParser.LlamadaContext):
        function_symbol: FunctionSymbol = get_symbol_uphill(self.curr_table, extract_id(ctx), SymbolType.FUNCTION)
        provided_signature: Signature = []
        # param 
        for argument_expression in extract_expression_list(ctx.opc_lista_expresion()):
            operand: OperandPair = self.__process_expresion(extract_expression(argument_expression))
            provided_signature.append(operand.second)
            param_quadruple: FuncQuadruple = FuncQuadruple.PARAM_quadruple(operand)
            true_param_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(param_quadruple, self.curr_table)
            self.__register_quadruple(param_quadruple, true_param_quadruple)

        self.__validate_function_signature(provided_signature, function_symbol.signature, function_symbol.symbol_id)
        
        # era
        era_quadruple: FuncQuadruple = FuncQuadruple.ERA_quadruple(function_symbol.symbol_id)
        true_era_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(era_quadruple, self.curr_table)
        self.__register_quadruple(era_quadruple, true_era_quadruple)

        # gosub
        gosub_quadruple: FuncQuadruple = FuncQuadruple.GOSUB_quadruple(function_symbol.index)
        true_gosub_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(gosub_quadruple, self.curr_table)
        self.__register_quadruple(gosub_quadruple, true_gosub_quadruple)
    
    def enterCondicion(self, ctx: PatitoParser.CicloContext):
        # Entering if statement.
        operand: OperandPair = self.__process_expresion(extract_expression(ctx.expresion()))
        
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

        operand: OperandPair = self.__process_expresion(extract_expression(ctx.expresion()))

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

    def exitExpresion_o_letrero(self, ctx: PatitoParser.Expresion_o_letreroContext):
        # Entering an argument of an 'imprime' statement.
        if ctx.LETRERO() is not None:
            operand: OperandPair = Pair(ctx.LETRERO().getText(), VariableType.LETRERO)
        else:
            operand: OperandPair = self.__process_expresion(extract_expression(ctx.expresion()))

        imprime_quadruple: StmtQuadruple = StmtQuadruple.IMPRIME_quadruple(operand)
        true_print_quadruple: TrueQuadruple = self.true_quadruple_builder.build_quadruple(imprime_quadruple, self.curr_table)
        self.__register_quadruple(imprime_quadruple, true_print_quadruple)

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
    
    def __process_expresion(self, expression_tokens: list[str]) -> OperandPair:
        if len(expression_tokens) == 1:
            return Pair(expression_tokens[0], token_mapper(expression_tokens[0]))
        
        *quadruples, final_quadruple = ExpQuadrupleBuilder(expression_tokens, self.curr_table).build_quadruples()
        self.__register_quadruples_batch([*quadruples, final_quadruple], self.true_quadruple_builder.build_quadruples([*quadruples, final_quadruple], self.curr_table))

        return final_quadruple.result
    
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

    def __register_quadruple(self, quadruple: ExpQuadruple | FlowQuadruple | StmtQuadruple | FuncQuadruple, true_quadruple: TrueQuadruple) -> None:
        self.quadruples_register.add_record(quadruple)
        self.true_quadruples_register.add_record(true_quadruple)
    
    def __register_quadruples_batch(self, quadruples_batch: list[ExpQuadruple | FlowQuadruple], true_quadruples_batch: list[TrueQuadruple]) -> None:
        if len(quadruples_batch) != len(true_quadruples_batch):
            raise ValueError("providing batches of different sizes")
        self.quadruples_register.add_records(quadruples_batch)
        self.true_quadruples_register.add_records(true_quadruples_batch)

    def __validate_function_signature(self, provided_signature: Signature, expected_signature: Signature, function_id: str) -> None:
        if len(provided_signature) != len(expected_signature):
            raise SemanticError.arity_mismatch(function_id, len(provided_signature), len(expected_signature))
        
        for provided_param_type, expected_param_type in zip(provided_signature, expected_signature):
            if provided_param_type != expected_param_type:
                raise SemanticError.type_mismatch(provided_param_type, expected_param_type)
