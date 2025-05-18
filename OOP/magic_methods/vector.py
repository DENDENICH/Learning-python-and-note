import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __abs__(self):
        """
        Абсолютная величина
        """
        return math.hypot(self.x, self.y) # это как нахождение гиппотенузы в прямоугольном треугольнике
    
    def __add__(self, other):
        """
        Сложение векторов и возвращение нового
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("A vector can only sum with a vector of the same class")

    def __mul__(self, other):
        """
        Произведение векторов и возвращение числа
        """
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("A vector can only be multiplied by a number")

    def __repr__(self):
        """
        Вывод вектора в формате (x, y)
        """
        return f"Vector({self.x!r}, {self.y!r})"

    def __bool__(self):
        """
        Проверка на нулевой модуль вектора
        """
        return bool(abs(self))


v1 = Vector(1, 2)
v2 = Vector(4, 6)

v_sum = v2 + v1
print(v_sum)

v_mul = v2 * 5
print(v_mul)

print(abs(v1))
