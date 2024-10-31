from antlr4 import FileStream, CommonTokenStream
from ..src.syntax import PatitoParser, PatitoLexer

def build_parser(patito_program_path: str) -> PatitoParser:
    """
    Intializes an instance of the Patito parser, using as token stream the text file located in the provided path. 
    """
    patito_lexer = PatitoLexer(FileStream(patito_program_path))
    token_stream = CommonTokenStream(patito_lexer)
    return PatitoParser(token_stream)