# Python Version: 3.11.8

import pytest

from ...utils import build_parser
from ....src.syntax import PatitoParser
from ....src.listeners.patito_error_listener import PatitoErrorListener
from ....src.exceptions import SyntaxException

valid_programs: list[tuple[str]] = [
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program1.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program2.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program3.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program4.txt"),
    ("testing/syntax/analyzer/patito_programs/valid/valid_patito_program5.txt"),
]

invalid_programs: list[tuple[str]] = [
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program1.txt"),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program2.txt"),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program3.txt"),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program4.txt"),
    ("testing/syntax/analyzer/patito_programs/invalid/invalid_patito_program5.txt"),
]

@pytest.mark.parametrize("patito_program_path", valid_programs)
def test_valid_program(patito_program_path: str):
    """
    Tests the parser's ability to successfully parse a syntactically correct input program. 
    """
    patito_parser: PatitoParser = build_parser(patito_program_path)
    error_listener = PatitoErrorListener()
    patito_parser.addErrorListener(error_listener)

    try: 
        patito_parser.programa() # Parsing is initialized, invoking the root rule 'programa'. 
        assert True, "Successfully compiled syntactically valid program"
    except SyntaxException as e:
        assert False, f"Encountered an unexpeced syntax error: {e}"

@pytest.mark.parametrize("patito_program_path", invalid_programs)
def test_invalid_program(patito_program_path: str):
    """
    Tests the parser's ability to successfully identify syntax errors in a flawed input program. 
    """
    patito_parser: PatitoParser = build_parser(patito_program_path)
    error_listener = PatitoErrorListener()
    patito_parser.addErrorListener(error_listener)

    try: 
        patito_parser.programa() # Parsing is initialized, invoking the root rule 'programa'. 
        assert False, "Failed to identify and terminate compilation when a syntax error was encountered"
    except SyntaxException as e:
        assert True, f"Successfully idenified the syntax error: {e}"