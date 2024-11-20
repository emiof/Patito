from typing import TYPE_CHECKING
from ..classifications import QuadrupleType, FlowOperator, StmtOperator, NumericOperator, FuncOperator, VariableType, token_mapper
from ..containers import Stack, Pair
from ..exceptions import SemanticException
from .memory import Memory, MemoryRequirements
from .operator_code_translation import numeric_operator, flow_operator, stmt_operator, func_operator

if TYPE_CHECKING:
    from ..quadruples import TrueQuadruple

class Executor:
    def __init__(self, *, quadruples: list['TrueQuadruple'], function_requirements: dict[str, MemoryRequirements], constants: dict[int, int | float | str]):
        self.quadruples: list['TrueQuadruple'] = quadruples
        self.function_requirements: dict[str, MemoryRequirements] = function_requirements
        self.constants: dict[int, int | float | str] = constants
        self.memory_stack: Stack[Memory] = Stack([Memory(function_requirements['global'])])
        self.num_max_calls: int = 500
        self.argument_stack: Stack[Pair[int | float, VariableType]] = Stack()
        self.index_stack: Stack[int] = Stack()
    
    def run(self) -> None:
        self.__process_quadrurple(curr_quadurple_index=0)

    def get_global_memory(self) -> Memory:
        return self.memory_stack.first()

    def __process_quadrurple(self, curr_quadurple_index: int) -> None:
        while curr_quadurple_index < len(self.quadruples):
            curr_quadruple: 'TrueQuadruple' = self.quadruples[curr_quadurple_index]
            match curr_quadruple.quadruple_type:
                case QuadrupleType.EXP:
                    next_index: int = self.__handle_exp_quadruple(curr_quadruple, curr_quadurple_index)
                case QuadrupleType.FLOW:
                    next_index: int = self.__handle_flow_quadruple(curr_quadruple, curr_quadurple_index)
                case QuadrupleType.STMT:
                    next_index: int = self.__handle_stmt_quadruple(curr_quadruple, curr_quadurple_index)
                case QuadrupleType.FUNC:
                    next_index: int = self.__handle_func_quadruple(curr_quadruple, curr_quadurple_index)
                case _:
                    raise ValueError("Encountered quadruple of unknown type") 
            
            curr_quadurple_index = next_index
        
    def __handle_exp_quadruple(self, exp_quadurple: 'TrueQuadruple', curr_quadruple_index: int) -> int:
        if exp_quadurple.operator == NumericOperator.ASIGNACION.value:
            assigne_address, assigner_address = exp_quadurple.operands
            self.__add_to_memory(self.__get_from_memory(address=assigner_address), address=assigne_address)

            return curr_quadruple_index + 1

        operand_1, operand_2 = exp_quadurple.operands
        result = numeric_operator(exp_quadurple.operator)(self.__get_from_memory(address=operand_1), self.__get_from_memory(address=operand_2))
        self.__add_to_memory(result, address=exp_quadurple.result)
        return curr_quadruple_index + 1

    def __handle_flow_quadruple(self, flow_quadurple: 'TrueQuadruple', curr_quadruple_index: int) -> int:
        match flow_operator(flow_quadurple.operator):
            case FlowOperator.GOTO:
                return flow_quadurple.jump
            case FlowOperator.GOTO_T:
                if self.__get_from_memory(address=flow_quadurple.jump_condition):
                    return flow_quadurple.jump
            case FlowOperator.GOTO_F:
                if not self.__get_from_memory(address=flow_quadurple.jump_condition):
                    return flow_quadurple.jump
        
        return curr_quadruple_index + 1
    
    def __handle_stmt_quadruple(self, stmt_quadruple: 'TrueQuadruple', curr_quadruple_index: int) -> int:
        match stmt_operator(stmt_quadruple.operator):
            case StmtOperator.IMPRIME:
                print(self.__get_from_memory(address=stmt_quadruple.operands[0]))
                return curr_quadruple_index + 1
            
    def __handle_func_quadruple(self, func_quadruple: 'TrueQuadruple', curr_quadruple_index: int) -> int:
        match func_operator(func_quadruple.operator):
            case FuncOperator.ERA:
                _, _, _, function_id = func_quadruple
                self.__create_function_memory(function_id)
                self.__emplace_function_arguments()
                return curr_quadruple_index + 1
            case FuncOperator.PARAM:
                _, argument_address, _, _ = func_quadruple
                argument: int | float | str = self.__get_from_memory(address=argument_address)
                self.argument_stack.push(Pair(argument, token_mapper(str(argument)))) #
                return curr_quadruple_index + 1
            case FuncOperator.GOSUB:
                _, _, _, jump = func_quadruple
                self.index_stack.push(curr_quadruple_index+1)
                return jump
            case FuncOperator.ENDFUNC:
                self.memory_stack.pop()
                return self.index_stack.pop()
            
    def __get_from_memory(self, *, address: int) -> int | float | str:
        if address in self.constants:
            return self.constants[address]
        
        try:
            return self.memory_stack.peek().get_at(at=address)
        except (ValueError, IndexError) as _:
            if self.memory_stack.size() == 1:
                raise
            return self.memory_stack.first().get_at(at=address)
    
    def __add_to_memory(self, val: int | float, *, address: int) -> None:
            try:
                self.memory_stack.peek().emplace_at(val, at=address)
            except ValueError as _: 
                self.memory_stack.first().emplace_at(val, at=address)

    def __create_function_memory(self, function_id: str) -> None:
        if self.memory_stack.size() == self.num_max_calls:
            raise SemanticException.stack_overflow(self.num_max_calls)
        self.memory_stack.push(Memory(self.function_requirements[function_id]))

    def __emplace_function_arguments(self) -> None:
        for argument, argument_type in self.argument_stack.pop_all(as_queue=True):
            self.memory_stack.peek().linear_emplace(argument, variable_type=argument_type)