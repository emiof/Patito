from ..containers import Stack, Pair, OperatorPair, OperandPair
from ..semantics import VariableSymbol, SymbolsTable, symbol_exists_uphill, get_symbol_uphill
from ..classifications import token_mapper, VariableType, NumericOperator, SymbolType
from ..exceptions import SemanticError
from .exp_quadruple import ExpQuadruple

class ExpQuadrupleBuilder:
    def __init__(self, expression: list[str], symbols_table: SymbolsTable):
        if len(expression) < 3:
            raise ValueError("attempting to build quadruple from expression with less than three terms")
        
        expression.append("$")
        self.symbols_table: SymbolsTable = symbols_table

        self.operand_stack: Stack[OperandPair] = Stack()
        self.operator_stack: Stack[OperatorPair | None] = Stack([None])
        self.quadruples: list[ExpQuadruple] = []
        self.token_stack: Stack[Pair[str, NumericOperator | VariableType | None]] = Stack([Pair(token, token_mapper(token)) for token in expression[::-1]])

    def build_quadruples(self) -> list[ExpQuadruple]:
        while not self.token_stack.empty():
            curr_token, curr_token_type = self.token_stack.peek()
            if curr_token == "$" or curr_token == ')': # reached end of expression
                self.__push_remaining_quadruples()
            elif isinstance(curr_token_type, VariableType): # found constant operand
                self.__push_constant_operand()
            elif isinstance(curr_token_type, NumericOperator): # found operator
                if self.operator_stack.peek() is not None and NumericOperator.has_precedence(self.operator_stack.peek().second, curr_token_type):
                    self.__push_quadruple()
                self.__push_operator()
            elif curr_token == '(': # found opening parenthesis
                self.__push_stack_botttom()
            else: # found id operand 
                self.__push_id_operand()

        return self.quadruples
    
    def __push_stack_botttom(self) -> None:
        self.operator_stack.push(None)
        self.token_stack.pop()

    def __push_quadruple(self) -> None:
        quadruple: ExpQuadruple = ExpQuadruple(self.operator_stack.pop(), *self.operand_stack.pop_n(2))
        self.quadruples.append(quadruple)
        self.operand_stack.push(quadruple.result)

    def __push_remaining_quadruples(self) -> None:
        while self.operator_stack.peek() is not None:
            self.__push_quadruple()

        self.operator_stack.pop()
        self.token_stack.pop()

    def __push_constant_operand(self) -> None:
        self.operand_stack.push(self.token_stack.pop())

    def __push_id_operand(self) -> None:
        variable_id, _ = self.token_stack.peek()
        if not symbol_exists_uphill(self.symbols_table, variable_id, SymbolType.VARIABLE):
            raise SemanticError.undeclared_symbol(variable_id)
        
        variable: VariableSymbol = get_symbol_uphill(self.symbols_table, variable_id, SymbolType.VARIABLE)        
        self.operand_stack.push(VariableSymbol.to_operand_pair(variable))
        self.token_stack.pop()

    def __push_operator(self) -> None:
        self.operator_stack.push(self.token_stack.pop())