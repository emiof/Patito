import pytest
from antlr4 import ParseTreeWalker
from ..utils import build_parser
from ...src.listeners import PatitoSemanticListener
from ...src.semantics import SymbolsTable
from ...src.quadruples import ExpQuadruple, MemoryQuadruple, FlowQuadruple

programs: list[tuple[str]] = [
    ("testing/listeners/patito_programs/patito_program1.txt")
]

@pytest.mark.parametrize('program', programs)
def test_listener(program: str) -> None:
    parser = build_parser(program)

    listener = PatitoSemanticListener()
    tree = parser.programa()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    symbols_table: SymbolsTable = listener.getSymbolsTable()
    quadruples: list[ExpQuadruple | FlowQuadruple] = listener.getQuadruples()
    memory_quadruples: list[MemoryQuadruple] = listener.getMemoryQuadruples()

    print(symbols_table)
    print()

    for quad in quadruples:
        print(quad)

    print()
    for quad in memory_quadruples:
        print(quad)