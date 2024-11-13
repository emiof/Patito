from typing import TypeVar, Generic
from .true_quadruple import TrueQuadruple
from .flow_quadruple import FlowQuadruple
from ..containers import Stack

JumpQuadruple = TypeVar('JumpQuadruple', TrueQuadruple, FlowQuadruple)

class JumpResolver(Generic[JumpQuadruple]):
    def __init__(self):
        self.jump_quadruples_stack: Stack[JumpQuadruple] = Stack()
        self.jump_stack: Stack[int] = Stack()

    def poise_quadruple(self, quadruple: JumpQuadruple) -> None:
        self.jump_quadruples_stack.push(quadruple)

    def poise_jump(self, jump: int) -> None:
        self.jump_stack.push(jump)

    def resolve_jump(self, qudaruple: JumpQuadruple) -> None:
        if self.jump_stack.empty():
            raise IndexError("attempting to provide a quadruple when there are no jumps in the stack")
        qudaruple.set_jump(self.jump_stack.pop())
    
    def resolve_quadruple(self, jump: int) -> None:
        if self.jump_quadruples_stack.empty():
            raise IndexError("attempting to provide a jump when there are no quadruples in the stack")
        self.jump_quadruples_stack.pop().set_jump(jump)