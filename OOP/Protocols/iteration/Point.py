from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield from [self.y, self.x, self.z]

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


p = Point(3, 4, 5)
print(p)

for i in p:
    print(i)

x, y, z = p