from .numeric_operators import NumericOperator
from .variable_types import VariableType
import re

entero_pattern: re.Pattern = re.compile(r"[0-9]+")
flotante_pattern: re.Pattern = re.compile(r"[0-9]+\.[0-9]+")
letrero_pattern: re.Pattern = re.compile(r"(?:'[a-zA-Z0-9_\",;.: ]*')|(?:\"[a-zA-Z0-9_',;.: ]*\")")

def token_mapper(token: str) -> NumericOperator | VariableType | None:
    match token:
        case "*":
            return NumericOperator.MULTIPLICACION
        case "/":
            return NumericOperator.DIVISION
        case "+":
            return NumericOperator.SUMA
        case '-':
            return NumericOperator.RESTA
        case '==':
            return NumericOperator.IGUALDAD
        case '!=':
            return NumericOperator.INIGUALDAD
        case '>':
            return NumericOperator.MAYOR_A
        case '<':
            return NumericOperator.MENOR_A
        case '=':
            return NumericOperator.ASIGNACION
        case _ if entero_pattern.fullmatch(token):
            return VariableType.ENTERO
        case _ if flotante_pattern.fullmatch(token):
            return VariableType.FLOTANTE
        case _ if letrero_pattern.fullmatch(token):
            return VariableType.LETRERO

