from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self, vals: list[T] | None = None):
        self.stack: list[T] = vals if vals is not None else []

    def push(self, val: T) -> None:
        self.stack.append(val)

    def pop(self) -> T:
        if len(self.stack) == 0:
            raise IndexError("empty stack")

        return self.stack.pop()
    
    def pop_n(self, n: int) -> list[T]:
        if n > len(self.stack):
            raise ValueError("number of items to remove is greater than the number of stack items")
        removed_items: list[T] = self.stack[-n:]
        self.stack = self.stack[:-n]
        return removed_items
    
    def pop_all(self, as_queue: bool = False) -> list[T]:        
        items: list[T] = self.stack.copy()
        self.stack.clear()
        return items if as_queue else items[::-1]
    
    def peek(self) -> T:
        if len(self.stack) == 0:
            raise IndexError("empty stack")
        
        return self.stack[-1]
    
    def peek_all(self, as_queue: bool = False) -> list[T]:
        return self.stack if as_queue else self.stack[::-1]
    
    def empty(self) -> bool:
        return len(self.stack) == 0
    
    def size(self) -> int:
        return len(self.stack)
    
    def __str__(self) -> str:
        return ", ".join([item.__str__() for item in self.stack])
    

