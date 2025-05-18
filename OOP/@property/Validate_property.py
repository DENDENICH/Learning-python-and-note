

class Expense:
    def __init__(self, quantity, reversed):
        self.quantity = quantity
        self.reversed = reversed

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Quantity must be greater than zero")
            self._quantity = value
        else:
            raise ValueError("Quantity must be a number")

    @property
    def reversed(self):
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        if isinstance(value, (int, float)):
            if value > self._quantity:
                raise ValueError("Reversed value must be less than or equal to quantity")
            self._reversed = value
        else:
            raise ValueError("Reversed value must be a boolean")


r = Expense(quantity=4, reversed=10)