from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, vals: list[T] | None = None):
        self.stack: list[T] = vals if vals is not None else []

    def push(self, val: T) -> None:
        self.stack.append(val)

    def pop(self) -> T:
        if len(self.stack) == 0:
            raise Exception("empty stack")

        return self.stack.pop()
    
    def pop_all(self, as_queue: bool = False) -> list[T]:        
        items: list[T] = self.stack.copy()
        self.stack.clear()
        return items if as_queue else items[::-1]
    
    def peek(self) -> T:
        if len(self.stack) == 0:
            raise Exception("empty stack")
        
        return self.stack[-1]
    
    def peek_all(self, as_queue: bool = False) -> list[T]:
        return self.stack if as_queue else self.stack[::-1]
    
    def empty(self) -> bool:
        return len(self.stack) == 0
    

