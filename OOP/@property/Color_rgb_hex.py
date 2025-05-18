

class Color:
    def __init__(self, hexcode: str):
        # Сразу вызвать сеттер для присвоения нового значения и
        # распарсить в rgb
        self.hexcode = hexcode
        self.r, self.g, self.b = self.__get_rgb()

    def __get_rgb(self):
        r = int(self.hexcode[1:3], 16)
        g = int(self.hexcode[3:5], 16)
        b = int(self.hexcode[5:7], 16)
        return r, g, b

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self.r, self.g, self.b = self.__get_rgb()

