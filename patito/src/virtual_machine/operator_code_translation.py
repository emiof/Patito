from typing import Callable
import operator as op
from ..classifications import FlowOperator, NumericOperator, StmtOperator

Numeric = float | int

def numeric_operator(operator_code: int) -> Callable[[Numeric, Numeric], Numeric]:
    match operator_code:
        case NumericOperator.MAYOR_A.value:
            return op.gt
        case NumericOperator.MENOR_A.value:
            return op.lt
        case NumericOperator.INIGUALDAD.value:
            return op.ne
        case NumericOperator.IGUALDAD.value:
            return op.eq
        case NumericOperator.SUMA.value:
            return op.add
        case NumericOperator.RESTA.value:
            return op.sub
        case NumericOperator.MULTIPLICACION.value:
            return op.mul
        case NumericOperator.DIVISION.value:
            return op.truediv
        case _:
            raise ValueError(f"provied an invalid numeric operator code '{operator_code}'")

def flow_operator(operator_code: int) -> FlowOperator:
    match operator_code:
        case FlowOperator.GOTO.value:
            return FlowOperator.GOTO
        case FlowOperator.GOTO_T.value:
            return FlowOperator.GOTO_T
        case FlowOperator.GOTO_F.value:
            return FlowOperator.GOTO_F
        case _:
            raise ValueError(f"provied an invalid flow operator code '{operator_code}'")
        
def stmt_operator(operator_code: int) -> StmtOperator:
    match operator_code:
        case StmtOperator.IMPRIME.value:
            return StmtOperator.IMPRIME
        case _:
            raise ValueError(f"provied an invalid flow operator code '{operator_code}'")
        