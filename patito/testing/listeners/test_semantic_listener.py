import pytest
from ..utils import build_parser
from ...src.listeners import PatitoSemanticListener
from antlr4 import ParseTreeWalker
from ...src.semantics import SymbolsTable

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
    print(symbols_table)