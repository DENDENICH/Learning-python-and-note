
# Вариант 1
class ColoredPoint:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __setattr__(self, name, value):
        if self.__dict__.get(name) is not None:
            raise AttributeError(f"Attribute '{name}' is read-only")
        super().__setattr__(name, value)

    @property
    def _data_of_tuple(self) -> tuple:
        return self.x, self.y, self.color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.color})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._data_of_tuple == other._data_of_tuple
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self._data_of_tuple)


# Вариант 2
class ColoredPoint2:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @property
    def _data_of_tuple(self) -> tuple:
        return self.x, self.y, self.color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.color})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._data_of_tuple == other._data_of_tuple
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self._data_of_tuple)


