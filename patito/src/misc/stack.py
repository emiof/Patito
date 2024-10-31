from typing import TypeVar

T = TypeVar('T')

class Stack:
    def __init__(self, vals: list[T] | None = None):
        self.stack: list[T] = vals if vals is not None else []

    def push(self, val: T) -> None:
        self.stack.append(val)

    def pop(self) -> T:
        if len(self.stack) == 0:
            raise Exception("empty stack")

        return self.stack.pop()
    
    def pop_all(self) -> list[T]:        
        items: list[T] = self.stack.copy()
        self.stack.clear()
        return items

    def empty(self) -> bool:
        return len(self.stack) == 0
    
    def peek(self) -> T:
        if len(self.stack) == 0:
            raise Exception("empty stack")
        
        return self.stack[-1]
    
    @property
    def items(self) -> list[str]:
        return self.stack
    

