
class AddressTable:
    def __init__(self, *, base_address: int, size: int):
        self.curr_slot: int = base_address
        self.n: int = 0
        self.max_size: int = size
        self.address_table: dict[str, int] = {}

    def get_real_range(self) -> tuple[int, int]:
        return (self.curr_slot - self.n, self.curr_slot)

    def get_size(self) -> int:
        return self.n

    def get_address(self, token: str) -> int:
        if token in self.address_table:
            return self.address_table[token]
        
        return self.__add_to_table(token)
        
    def __add_to_table(self, token: str) -> int:
        if self.n == self.max_size:
            raise MemoryError("address table overloaded")
        
        self.address_table[token] = self.curr_slot
        self.curr_slot += 1
        self.n += 1
        return self.curr_slot - 1