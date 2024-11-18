import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from src.listeners import PatitoSemanticListener, PatitoErrorListener
from src.syntax import PatitoParser, PatitoLexer
from src.virtual_machine import Executor

file_path: str = sys.argv[1]

# build parser
patito_lexer = PatitoLexer(FileStream(file_path))
token_stream = CommonTokenStream(patito_lexer)
parser = PatitoParser(token_stream)

# initialize listeners 
listener = PatitoSemanticListener()
error_listener = PatitoErrorListener()
parser.addErrorListener(error_listener)

# build parse tree 
tree = parser.programa()

# navigate parse tree
walker = ParseTreeWalker()
walker.walk(listener, tree)

executor = Executor(
    quadruples=listener.get_true_quadruples().records,
    function_requirements=listener.get_all_memory_requirements(),
    constants=listener.get_constants_storage())

executor.run()
