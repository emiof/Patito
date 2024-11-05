from ..containers import Stack, Pair
from .exp_quadruple import OperandPair, OperatorPair, ExpQuadruple
from ..semantics import Symbol
from ..classifications import token_mapper, PatitoType, PatitoOperator

class ExpQuadrupleBuilder:
    def __init__(self, expression: list[str], global_variables: dict[str, Symbol], local_variables: dict[str, Symbol]):
        if len(expression) < 3:
            raise Exception("attempting to process simple expression")
        
        self.global_variables: dict[str, Symbol] = global_variables
        self.local_variables: dict[str, Symbol] = local_variables

        self.operand_stack: Stack[OperandPair] = Stack()
        self.operator_stack: Stack[OperatorPair | None] = Stack([None])
        self.quadruples: list[ExpQuadruple] = []

        expression.append("$")
        self.token_stack: Stack[Pair[str, PatitoOperator | PatitoType | None]] = Stack([Pair(token, token_mapper(token)) for token in expression[::-1]])

    def build_quadruples(self) -> list[ExpQuadruple]:
        while not self.token_stack.empty():
            curr_token, curr_token_type = self.token_stack.peek()
            if curr_token == "$": # reached end of expression
                self.__push_remaining_quadruples()
            elif isinstance(curr_token_type, PatitoType): # found constant operand
                self.__push_constant_operand()
            elif isinstance(curr_token_type, PatitoOperator): # found operator
                if self.operator_stack.peek() is not None and PatitoOperator.has_precedence(self.operator_stack.peek().second, curr_token_type):
                    self.__push_quadruple()
                self.__push_operator()
            elif curr_token == '(': # found opening parenthesis
                self.__push_stack_botttom()
            elif curr_token == ')': # found closing gparenthesis
                self.__push_remaining_quadruples()
            else: # found id operand 
                self.__push_id_operand()

        return self.quadruples
    
    def __push_stack_botttom(self) -> None:
        self.operator_stack.push(None)
        self.token_stack.pop()

    def __push_quadruple(self) -> None:
        operand_1, operand_2 = self.operand_stack.pop_n(2)
        quadruple: ExpQuadruple = ExpQuadruple(self.operator_stack.pop(), operand_1, operand_2)
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
        curr_token, _ = self.token_stack.peek()
        symbol: Symbol | None = self.local_variables.get(curr_token, self.global_variables.get(curr_token, None)) 
        if symbol is None:
            raise Exception(f"encountered unidentified variable: '{curr_token}'")
        
        self.operand_stack.push(Pair.to_operand_pair(symbol))
        self.token_stack.pop()

    def __push_operator(self) -> None:
        self.operator_stack.push(self.token_stack.pop())