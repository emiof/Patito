# Python Version: 3.11.8

from antlr4.error.ErrorListener import ErrorListener
from enum import Enum
from dataclasses import dataclass

ErrorType = Enum('ErrorType', ['SYNTAX', 'AMBIGUITY', 'FULL_CONTEXT', 'CONTEXT_SENSITIVITY'])

@dataclass
class PatitoError:
    """
    Represents an error or anomaly encountered by the parser during parsing. 
    """
    msg: str | None
    location: tuple[int, int]
    type: ErrorType

class PatitoErrorListener(ErrorListener):
    """
    When attached to an ANTLR parser, listens to and registers error or anomalies encountered during the parsing process. 
    """
    def __init__(self):
        super(PatitoErrorListener, self).__init__()
        self.error_list: list[PatitoError] = []
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error_list.append(PatitoError(msg=msg, location=(line, column), type=ErrorType.SYNTAX))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, fullCtx, ambiguous):
        self.error_list.append(PatitoError(msg=None, location=(startIndex, stopIndex), type=ErrorType.AMBIGUITY))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, fullCtx):
       self.error_list.append(PatitoError(msg=None, location=(startIndex, stopIndex), type=ErrorType.FULL_CONTEXT))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction):
        self.error_list.append(PatitoError(msg=None, location=(startIndex, stopIndex), type=ErrorType.CONTEXT_SENSITIVITY))
