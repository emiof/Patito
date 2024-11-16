from dataclasses import dataclass
from typing import Optional
from itertools import count

@dataclass
class MemoryRequirements:
    int_range: tuple[int, int]
    float_range: tuple[int, int]

class Memory:
    def __init__(self, requirements: MemoryRequirements):
        int_lower_bound, int_upper_bound = requirements.int_range
        self.int_section: list[Optional[int]] = [None] * (int_upper_bound - int_lower_bound + 1)
        int_lower_bound, int_upper_bound = requirements.float_range
        self.float_section: list[Optional[float]] = [None] * (int_upper_bound - int_lower_bound + 1)

        self.requirements: MemoryRequirements = requirements

    def emplace_at(self, val: int | float, *, at: int) -> None:
        if self.__within_range(at, self.requirements.int_range):
            self.int_section[at - self.requirements.int_range[0]] = val
        elif self.__within_range(at, self.requirements.float_range):
            self.float_section[at - self.requirements.float_range[0]] = val
        else: 
            raise ValueError(f"an out-of-bounds address was provided: {at}")

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

    def __within_range(self, address: int, address_range: tuple[int, int]) -> bool:
        lower_bound, upper_bound = address_range
        return lower_bound <= address <= upper_bound
    
    def __str__(self) -> str:
        int_base, float_base = self.requirements.int_range[0], self.requirements.float_range[0]
        return (
            "INTEGERS/ " + " | ".join(f"{address}: {val}" for address, val in zip(count(int_base), self.int_section)) +
            "\nFLOATS/ " + " | ".join(f"{address}: {val}" for address, val in zip(count(float_base), self.float_section))
        )
