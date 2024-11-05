from collections.abc import Iterator
from ..classifications import PatitoOperator, PatitoType, token_mapper
from ..semantics import SymbolsTable, SemanticCube, Symbol
from ..containers import Stack, Pair

OperatorPair = Pair[str, PatitoOperator]
OperandPair = Pair[str, PatitoType]

class Quadruple:
    semantic_cube: SemanticCube = SemanticCube()

    def __init__(
            self,
            operator: OperatorPair,
            operand_1: OperandPair,
            operand_2: OperandPair,
            result_name: str | None = None
    ):
        result_type: PatitoType | None = Quadruple.semantic_cube.get_result_type(operator.second, operand_1.second, operand_2.second)
        if result_type is None:
            raise Exception(f"semantically invalid operation:{operand_1.second.name} {operator.second.name} {operand_2.second.name}")
        
        result: OperandPair = Pair("result" if result_name is None else result_name, result_type)
        self.items: tuple[OperatorPair, OperandPair, OperandPair, OperandPair] = (operator, operand_1, operand_2, result)

    def __iter__(self) -> Iterator[OperatorPair | OperandPair]:
        yield from self.items

    def __str__(self) -> str:
        return "(" + " ".join(item.__str__() for item in self.items) + ")"
    
    @property
    def result(self) -> OperandPair:
        return self.items[-1]

    @staticmethod
    def assignment(operand_1: OperandPair, operand_2: OperandPair) -> 'Quadruple':
        return Quadruple(Pair("=", PatitoOperator.ASIGNACION), operand_1, operand_2)
    
    @staticmethod
    def print_quadruples(quadruples: list['Quadruple']) -> None:
        print("\n=====")
        for quad in quadruples:
            print(quad.__str__())
        print("=====")
