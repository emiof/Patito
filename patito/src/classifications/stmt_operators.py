from enum import Enum

class StmtOperator(Enum):
    IMPRIME = 200

STMT_OPERATOR_CODES: set[int] = set([operator.value for operator in StmtOperator])
