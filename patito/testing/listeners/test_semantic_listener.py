import pytest
from antlr4 import ParseTreeWalker
from ..utils import build_parser
from ...src.listeners import PatitoSemanticListener, PatitoErrorListener
from ...src.semantics import SymbolsTable
from ...src.quadruples import ExpQuadruple, TrueQuadruple, FlowQuadruple
from ...src.containers import Register
from ...src.virtual_machine import Executor

programs: list[tuple[str]] = [
    ("testing/listeners/patito_programs/factorial.txt"),
    ("testing/listeners/patito_programs/num_combinaciones.txt"),
    ("testing/listeners/patito_programs/aritmetica.txt"),
    ("testing/listeners/patito_programs/permutaciones.txt")
]

@pytest.mark.parametrize('program', programs)
def test_listener(program: str) -> None:
    parser = build_parser(program)
    listener = PatitoSemanticListener()
    error_listener = PatitoErrorListener()
    parser.addErrorListener(error_listener)
    tree = parser.programa()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    symbols_table: SymbolsTable = listener.get_symbols_table()
    quadruples: Register[ExpQuadruple | FlowQuadruple] = listener.get_quadruples()
    true_quadruples: Register[TrueQuadruple] = listener.get_true_quadruples()

    print("\n" + "=" * 50)
    print(symbols_table, end="\n\n")
    print(quadruples, end="\n\n")
    print(true_quadruples, end="\n\n")

    print("EXECUTION")
    executor = Executor(
        quadruples=true_quadruples.records,
        function_requirements=listener.get_all_memory_requirements(),
        constants=listener.get_constants_storage())
    
    executor.run()

    print()
    print(executor.get_global_memory())