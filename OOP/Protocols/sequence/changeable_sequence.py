from typing import Any


class Order:
    """Изменяемая последовательность"""
    def __init__(self, carts: list, customer: int):
        self.carts = carts
        self.customer = customer

    def __len__(self) -> int:
        return len(self.carts)

    def __getitem__(self, index: int) -> Any:
        if isinstance(index, slice): # slice - срез
            return Order(self.carts[index], self.customer)
        return self.carts[index]

    def __setitem__(self, index: int, value: Any):
        self.carts[index] = value

    def __delitem__(self, index: int):
        del self.carts[index]

    def __contains__(self, item) -> bool:
        return item in self.carts

    def __iter__(self):
        yield from self.carts
