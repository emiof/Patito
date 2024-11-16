from typing import TYPE_CHECKING
from ..classifications import QuadrupleType, FlowOperator, StmtOperator, NumericOperator
from ..containers import Stack
from .memory import Memory, MemoryRequirements
from .operator_code_translation import numeric_operator, flow_operator, stmt_operator

if TYPE_CHECKING:
    from ..quadruples import TrueQuadruple

class Executor:
    def __init__(self, *, quadruples: list['TrueQuadruple'], function_requirements: dict[str, MemoryRequirements], constants: dict[int, int | float | str]):
        self.quadruples: list['TrueQuadruple'] = quadruples
        self.constants: dict[int, int | float | str] = constants
        self.memory_stack: Stack[Memory] = Stack([Memory(function_requirements['global'])])
    
    def run(self) -> None:
        self.__process_quadrurple(curr_quadurple_index=0)

    def get_global_memory(self) -> Memory:
        return self.memory_stack.first()

    def __process_quadrurple(self, curr_quadurple_index: int) -> None:
        if curr_quadurple_index == len(self.quadruples):
            return 
        
        curr_quadruple: 'TrueQuadruple' = self.quadruples[curr_quadurple_index]
        match curr_quadruple.quadruple_type:
            case QuadrupleType.EXP:
                next_index: int = self.__handle_exp_quadruple(curr_quadruple, curr_quadurple_index)
            case QuadrupleType.FLOW:
                next_index: int = self.__handle_flow_quadruple(curr_quadruple, curr_quadurple_index)
            case QuadrupleType.STMT:
                next_index: int = self.__handle_stmt_quadruple(curr_quadruple, curr_quadurple_index)
            case _:
                raise ValueError("Encountered quadruple of unknown type") 
        
        self.__process_quadrurple(next_index)
            
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
        self.memory_stack.peek().emplace_at(val, at=address)