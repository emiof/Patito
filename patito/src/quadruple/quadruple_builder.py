from typing import Any
from ..containers import Stack, Pair
from .quadruple import OperandPair, OperatorPair, Quadruple
from ..semantics import Symbol
from ..classifications import token_mapper, PatitoType, PatitoOperator

class QuadrupleBuilder:
    result_counter: int = 0

    def __init__(self, expression: list[str], global_variables: dict[str, Symbol], local_variables: dict[str, Symbol]):
        if len(expression) < 3:
            raise Exception("attempting to process simple expression")
        
        self.global_variables: dict[str, Symbol] = global_variables
        self.local_variables: dict[str, Symbol] = local_variables

        self.operand_stack: Stack[OperandPair] = Stack()
        self.operator_stack: Stack[OperatorPair] = Stack()
        self.quadruples: list[Quadruple] = []

        expression.append("$")
        self.token_stack: Stack[Pair[str, PatitoOperator | PatitoType | None]] = Stack([Pair(token, token_mapper(token)) for token in expression[::-1]])

    def build_quadruples(self) -> list[Quadruple]:
        while not self.token_stack.empty():
            curr_token, curr_token_type = self.token_stack.peek()
            if curr_token == "$": # reached end of expression
                self.__push_remaining_quadruples()
            elif isinstance(curr_token_type, PatitoType): # found constant operand
                self.__push_constant_operand()
            elif isinstance(curr_token_type, PatitoOperator): # found operator
                if not self.operator_stack.empty() and PatitoOperator.has_precedence(self.operator_stack.peek().second, curr_token_type):
                    self.__push_quadruple()
                self.__push_operator()
            elif curr_token == '(': # found opening parenthesis
                pass
            elif curr_token == ')': # found closing gparenthesis
                pass
            else: # found id operand 
                self.__push_id_operand()

        return self.quadruples

    def __push_quadruple(self) -> None:
        operand_1, operand_2 = self.operand_stack.pop_n(2)
        quadruple: Quadruple = Quadruple(self.operator_stack.pop(), operand_1, operand_2, f"t{QuadrupleBuilder.result_counter}")
        self.quadruples.append(quadruple)
        self.operand_stack.push(quadruple.result)
        QuadrupleBuilder.result_counter += 1

    def __push_remaining_quadruples(self) -> None:
        while not self.operator_stack.empty():
            self.__push_quadruple()

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