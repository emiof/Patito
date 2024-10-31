# Python Version: 3.11.8

from ..classifications import PatitoType
from ..classifications import PatitoOperator
import numpy as np
from itertools import product
from typing import Callable
from .operator_strategies import *

ResultType = PatitoType | None

class SemanticCube:
    """
    
    """
    def __init__(self):
        self.cube: np.ndarray = SemanticCube.create_cube()

    def get_result_type(self, type_1: PatitoType, type_2: PatitoType, oper: PatitoOperator) -> ResultType:
        x, y, z = type_1.value, type_2.value, oper.value
        return self.cube[x, y, z]

    def is_valid_operation(self, type_1: PatitoType, type_2: PatitoType, oper: PatitoOperator) -> bool:
        x, y, z = type_1.value, type_2.value, oper.value
        return self.cube[x, y, z] is not None
    
    def __str__(self) -> str:
        return "".join(["\n" + self.cube[:, :, i].__str__() for i in range(self.cube.shape[2])])

    @staticmethod
    def create_cube() -> np.ndarray:
        def get_operator_strategy(operator: PatitoOperator) -> Callable:
            match operator:
                case PatitoOperator.SUMA | PatitoOperator.RESTA | PatitoOperator.MULTIPLICACION:
                    return numeric_strategy
                case PatitoOperator.DIVISION:
                    return division_strategy
                case PatitoOperator.MAYOR_A | PatitoOperator.MENOR_A | PatitoOperator.IGUALDAD | PatitoOperator.INIGUALDAD:
                    return relational_strategy
                case PatitoOperator.ASIGNACION:
                    return assignment_strategy
                case _: 
                    return none_strategy
                
        num_types: int = len(PatitoType)
        num_operators: int = len(PatitoOperator)
        cube: np.ndarray = np.full((num_types, num_types, num_operators), None, dtype=object)

        for type_1, type_2, oper in product(PatitoType, PatitoType, PatitoOperator):
            x, y, z = type_1.value, type_2.value, oper.value
            cube[x, y, z] = get_operator_strategy(oper)(type_1, type_2) 

        return cube
