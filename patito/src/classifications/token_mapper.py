from ..classifications import PatitoOperator, PatitoType
import re

entero_pattern: re.Pattern = re.compile(r"[0-9]+")
flotante_pattern: re.Pattern = re.compile(r"[0-9]+\.[0-9]+")

def token_mapper(token: str) -> PatitoOperator | PatitoType | None:
    match token:
        case "*":
            return PatitoOperator.MULTIPLICACION
        case "/":
            return PatitoOperator.DIVISION
        case "+":
            return PatitoOperator.SUMA
        case '-':
            return PatitoOperator.RESTA
        case '==':
            return PatitoOperator.IGUALDAD
        case '!=':
            return PatitoOperator.INIGUALDAD
        case '>':
            return PatitoOperator.MAYOR_A
        case '<':
            return PatitoOperator.MENOR_A
        case '=':
            return PatitoOperator.ASIGNACION
        case _ if entero_pattern.fullmatch(token):
            return PatitoType.ENTERO
        case _ if flotante_pattern.fullmatch(token):
            return PatitoType.FLOTANTE
        case _:
            return None

