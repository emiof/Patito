from typing import TypeVar, Generic
from collections.abc import Iterator
from ..semantics import VariableSymbol
from ..classifications import VariableType, NumericOperator

T1 = TypeVar('T1') 
T2 = TypeVar('T2') 

class Pair(Generic[T1, T2]):
    def __init__(self, first: T1, second: T2) -> None:
        self.__first: T1 = first
        self.__second: T2 = second

    def __str__(self) -> str:
        return f"{self.__first}[{self.__second}]"
    
    def __iter__(self) -> Iterator[T1 | T2]:
        yield self.__first
        yield self.__second

    @property
    def first(self) -> T1:
        return self.__first
    
    @property
    def second(self) -> T2:
        return self.__second
    
    @staticmethod
    def to_operand_pair(variable: VariableSymbol) -> 'Pair[str, VariableType]':
        return Pair(variable.symbol_id, variable.variable_type)
    
OperandPair = Pair[str, VariableType]
OperatorPair = Pair[str, NumericOperator]
