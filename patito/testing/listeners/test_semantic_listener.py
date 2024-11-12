import pytest
from antlr4 import ParseTreeWalker
from ..utils import build_parser
from ...src.listeners import PatitoSemanticListener
from ...src.semantics import SymbolsTable
from ...src.quadruples import ExpQuadruple, MemoryQuadruple, FlowQuadruple
from ...src.containers import Register

programs: list[tuple[str]] = [
    ("testing/listeners/patito_programs/patito_program1.txt"),
    ("testing/listeners/patito_programs/patito_program2.txt"),
    ("testing/listeners/patito_programs/patito_program3.txt")
]

@pytest.mark.parametrize('program', programs)
def test_listener(program: str) -> None:
    parser = build_parser(program)

    listener = PatitoSemanticListener()
    tree = parser.programa()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    symbols_table: SymbolsTable = listener.getSymbolsTable()
    quadruples: Register[ExpQuadruple | FlowQuadruple] = listener.getQuadruples()
    memory_quadruples: Register[MemoryQuadruple] = listener.getMemoryQuadruples()

    print("\n" + "=" * 50)
    print(symbols_table, end="\n\n")
    print(quadruples, end="\n\n")
    print(memory_quadruples, end="\n\n")