# Магический метод __hash__()
# Предназначен для создания из объекта класса ключа, элемента множества

# По умолчанию, hash(<object>) == id(<object>) // 16


class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """ТАкже рекомендуется реализовывать метод для сравнения на равенство"""
        if isinstance(other, Cat):
            return self.name == other.name
        return NotImplemented

    def __hash__(self):
        """Метод хэширования"""
        return hash(self.name)