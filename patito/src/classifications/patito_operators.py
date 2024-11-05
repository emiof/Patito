from enum import Enum 

class PatitoOperator(Enum):
    ASIGNACION = 0
    MAYOR_A = 1
    MENOR_A = 2
    INIGUALDAD = 3
    IGUALDAD = 4
    SUMA = 5
    RESTA = 6
    MULTIPLICACION = 7
    DIVISION = 8
    
    def __str__(self) -> str:
        return f"{self.name}"
        
    @staticmethod
    def precedence_level(operator: 'PatitoOperator') -> int:
        if operator.value == 0:
            return 0
        elif 1 <= operator.value <= 4:
            return 1
        elif 5 <= operator.value <=6:
            return 2
        else:
            return 3
    
    @staticmethod
    def has_precedence(operator_1: 'PatitoOperator', operator_2: 'PatitoOperator') -> bool:
        return PatitoOperator.precedence_level(operator_1) >= PatitoOperator.precedence_level(operator_2)



