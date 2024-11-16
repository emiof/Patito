from enum import Enum

class StmtOperator(Enum):
    IMPRIME = 200

    def __str__(self) -> str:
        return f"{self.name}"

STMT_OPERATOR_CODES: set[int] = set([operator.value for operator in StmtOperator])
