from enum import Enum

class FlowOperator(Enum):
    GOTO = 0
    GOTO_T = 1
    GOTO_F = 2

    def __str__(self) -> str:
        return self.name
