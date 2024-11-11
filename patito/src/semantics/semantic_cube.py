# Python Version: 3.11.8

from ..classifications import VariableType
from ..classifications import NumericOperator
import numpy as np
from itertools import product
from typing import Callable
from .operator_strategies import *

class SemanticCube:
    """
    
    """
    def __init__(self):
        self.cube: np.ndarray = SemanticCube.create_cube()

    def get_result_type(self, oper: NumericOperator, type_1: VariableType, type_2: VariableType) -> VariableType | None:
        x, y, z = type_1.value, type_2.value, oper.value
        return self.cube[x, y, z]

    def is_valid_operation(self, oper: NumericOperator, type_1: VariableType, type_2: VariableType) -> bool:
        x, y, z = type_1.value, type_2.value, oper.value
        return self.cube[x, y, z] is not None
    
    def __str__(self) -> str:
        return "".join(["\n" + self.cube[:, :, i].__str__() for i in range(self.cube.shape[2])])

    @staticmethod
    def create_cube() -> np.ndarray:
        def get_operator_strategy(operator: NumericOperator) -> Callable:
            match operator:
                case NumericOperator.SUMA | NumericOperator.RESTA | NumericOperator.MULTIPLICACION:
                    return numeric_strategy
                case NumericOperator.DIVISION:
                    return division_strategy
                case NumericOperator.MAYOR_A | NumericOperator.MENOR_A | NumericOperator.IGUALDAD | NumericOperator.INIGUALDAD:
                    return relational_strategy
                case NumericOperator.ASIGNACION:
                    return assignment_strategy
                case _: 
                    return none_strategy
                
        num_types: int = len(VariableType)
        num_operators: int = len(NumericOperator)
        cube: np.ndarray = np.full((num_types, num_types, num_operators), None, dtype=object)

        for type_1, type_2, oper in product(VariableType, VariableType, NumericOperator):
            x, y, z = type_1.value, type_2.value, oper.value
            cube[x, y, z] = get_operator_strategy(oper)(type_1, type_2) 

        return cube
