from dataclasses import dataclass
from typing import Optional
from itertools import count
from ..classifications import VariableType
@dataclass
class MemoryRequirements:
    int_range: tuple[int, int]
    float_range: tuple[int, int]

class Memory:
    def __init__(self, requirements: MemoryRequirements):
        int_lower_bound, int_upper_bound = requirements.int_range
        self.int_section: list[Optional[int]] = [None] * (int_upper_bound - int_lower_bound + 1)
        float_lower_bound, float_upper_bound = requirements.float_range
        self.float_section: list[Optional[float]] = [None] * (float_upper_bound - float_lower_bound + 1)

        self.requirements: MemoryRequirements = requirements

    def emplace_at(self, val: int | float, *, at: int) -> None:
        if self.__within_range(at, self.requirements.int_range):
            self.int_section[at - self.requirements.int_range[0]] = val
        elif self.__within_range(at, self.requirements.float_range):
            self.float_section[at - self.requirements.float_range[0]] = val
        else: 
            raise ValueError(f"an out-of-bounds address was provided: {at}")
        
    def linear_emplace(self, val: int | float, *, variable_type: VariableType) -> None:
        match variable_type:
            case VariableType.ENTERO:
                self.int_section = self.__emplace_at_first_empty(val, self.int_section)
            case VariableType.FLOTANTE:
                self.float_section = self.__emplace_at_first_empty(val, self.float_section) 

    def get_at(self, *, at: int) -> int | float:
        if self.__within_range(at, self.requirements.int_range):
            if self.int_section[at - self.requirements.int_range[0]] is None:
                raise IndexError(f"attempting to access an empty memory slot with address: {at}")
            return self.int_section[at - self.requirements.int_range[0]]
        elif self.__within_range(at, self.requirements.float_range):
            if self.float_section[at - self.requirements.float_range[0]] is None:
                raise IndexError(f"attempting to access an empty memory slot with address: {at}")
            return self.float_section[at - self.requirements.float_range[0]]
        else: 
            raise ValueError(f"an out-of-bounds address was provided: {at}")
        
    def variable_type(self, address: int) -> VariableType:
        if self.__within_range(address, self.requirements.int_range):
            return VariableType.ENTERO
        elif self.__within_range(address, self.requirements.float_range):
            return VariableType.FLOTANTE
        else:
            raise ValueError(f"an out-of-bounds address was provided: {address}")

    def __within_range(self, address: int, address_range: tuple[int, int]) -> bool:
        lower_bound, upper_bound = address_range
        return lower_bound <= address <= upper_bound
    
    def __str__(self) -> str:
        int_base, float_base = self.requirements.int_range[0], self.requirements.float_range[0]
        return (
            "INTEGERS/ " + " | ".join(f"{address}: {val}" for address, val in zip(count(int_base), self.int_section)) +
            "\nFLOATS/ " + " | ".join(f"{address}: {val}" for address, val in zip(count(float_base), self.float_section))
        )
    
    def __emplace_at_first_empty(self, val: int | float, items: list[int | float]) -> list:
        for i, item in enumerate(items):
            if item is None:
                return items[:i] + [val] + (items[i+1:] if i != len(items) - 1 else [])
            
        raise IndexError("attempting to emplace value in overloaded memory")