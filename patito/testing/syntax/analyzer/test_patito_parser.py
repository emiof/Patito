# Python Version: 3.11.8

import pytest

from ...utils import build_parser
from ....src.syntax import PatitoParser
from ....src.syntax import PatitoLexer
from ....src.listeners.patito_error_listener import PatitoErrorListener

valid_programs: list[tuple[str]] = [
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program1.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program2.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program3.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program4.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program5.txt"),
]

invalid_programs: list[tuple[str, int]] = [
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program1.txt", 2),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program2.txt", 2),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program3.txt", 2),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program4.txt", 2),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program5.txt", 2),
]

@pytest.mark.parametrize("patito_program_path", valid_programs)
def test_valid_program(patito_program_path: str):
    """
    Tests the parser's ability to successfully parse a syntactically correct input program. 
    """
    patito_parser: PatitoParser = build_parser(patito_program_path)
    error_listener = PatitoErrorListener()
    patito_parser.addErrorListener(error_listener)

    patito_parser.programa() # Parsing is initialized, invoking the root rule 'programa'. 

    assert len(error_listener.error_list) == 0, "Failed to parse syntactically valid program"

@pytest.mark.parametrize("patito_program_path, num_errors", invalid_programs)
def test_invalid_program(patito_program_path: str, num_errors: int):
    """
    Tests the parser's ability to successfully identify syntax errors in a flawed input program. 
    """
    patito_parser: PatitoParser = build_parser(patito_program_path)
    error_listener = PatitoErrorListener()
    patito_parser.addErrorListener(error_listener)

    patito_parser.programa() # Parsing is initialized, invoking the root rule 'programa'. 

    assert len(error_listener.error_list) == num_errors, f"Failed to identify the {num_errors} syntax errors present in the program"