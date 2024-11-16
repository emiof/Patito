from enum import Enum

class FuncOperator(Enum):
    ERA = 300
    PARAM = 301    
    GOSUB = 302
    ENDFUNC = 303

    def __str__(self) -> str:
        return self.name
    
FUNC_OPERATOR_CODES: set[int] = set([operator.value for operator in FuncOperator])
