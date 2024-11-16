from enum import Enum

class FlowOperator(Enum):
    GOTO = 100
    GOTO_T = 101
    GOTO_F = 102

    def __str__(self) -> str:
        return self.name
    
FLOW_OPERATOR_CODES: set[int] = set([operator.value for operator in FlowOperator])
