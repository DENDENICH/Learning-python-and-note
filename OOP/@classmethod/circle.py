from typing import TypeVar

CircleT = TypeVar('CircleT', bound='Circle')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # альтернативный конструктор, возвращающий круг по заданному диаметру
    @classmethod
    def from_diameter(cls, diameter: float) -> CircleT:
        """Возвращает круг по заданному диаметру
        parameters: diameter: float - диаметр круга
        """
        return cls(diameter/2)

