


class Fruit:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        """Сравнение на равенство"""
        if isinstance(other, Fruit):
            return self.mass == other.mass
        return NotImplemented

    def __lt__(self, other):
        """Сравнение на меньше"""
        if isinstance(other, Fruit):
            return self.mass < other.mass
        return NotImplemented

    def __gt__(self, other):
        """Сравнение на больше"""
        if isinstance(other, Fruit):
            return not self.__lt__(other) and not self.__eq__(other)
        return NotImplemented

    def __le__(self, other):
        """Сравнение на меньше или равно"""
        if isinstance(other, Fruit):
            return self.__lt__(other) or self.__eq__(other)
        return NotImplemented

    def __ge__(self, other):
        """Сравнение на больше или равно"""
        if isinstance(other, Fruit):
            return not self.__lt__(other)
        return NotImplemented


# Реализовать данные методы сравнения слишком утомительно, гораздо проще реализовать несколько нужных методов
# И по их аналогии автоматически реализовать все остальные

from functools import total_ordering


@total_ordering
# Достаточно реализовать только два метода сравнения - равно и любой из других методов (кроме не равенства)
class Fruit:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.mass == other.mass
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.mass < other.mass
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fruit):
            return self.mass <= other.mass and self.name == other.name
        return NotImplemented



frome = Fruit('apple', 200)
too = Fruit('orange', 300)

print(frome >= too)
