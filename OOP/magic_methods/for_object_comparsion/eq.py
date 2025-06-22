

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # метод __ne__(self, other) реализован по аналогии с методом __eq__ автоматически

p1 = Point(2, 3)
p2 = (3, 4)
print(p1 == p2)
