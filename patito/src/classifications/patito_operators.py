from enum import Enum 

class PatitoOperator(Enum):
    MAYOR_A = 0
    MENOR_A = 1
    INIGUALDAD = 2
    IGUALDAD = 3
    SUMA = 4
    RESTA = 5
    MULTIPLICACION = 6
    DIVISION = 7 
    ASIGNACION = 8