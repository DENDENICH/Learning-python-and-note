from typing import Tuple


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, Tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented


vector1 = Vector(1, 10)
vector2 = Vector(1, 10)
vector2_tuple = (1, 10)
print(vector1 == vector2_tuple)
