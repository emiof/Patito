# Python Version: 3.11.8

from antlr4.error.ErrorListener import ErrorListener
from ..exceptions import SyntaxException

class PatitoErrorListener(ErrorListener):
    """
    When attached to an ANTLR parser, listens to and registers error or anomalies encountered during the parsing process. 
    """
    def __init__(self):
        super(PatitoErrorListener, self).__init__()
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException.syntax(msg, (line, column))
