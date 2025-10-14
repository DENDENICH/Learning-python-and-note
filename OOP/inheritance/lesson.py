

# Общие методы, используемые в дочяерних классах, можно вынести в родительский класс
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"{self.name} is an animal, sound: {self.sound()}"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

### Однако в таком случае, мы должны проверять или перехватывать исключение, если в дочерних класса не реализованы методы sound()



### НАСЛЕДОВАНИЕ ОТ ТИПОВ DICT И LIST (USER_DICT, USER_LIST)

# для правильной работы класса UpperCaseDict необходимо переопределить много методов базового типа dict.
# При наследовании от dict мы ожидаем, что методы update(), __init__(), setdefault() вызовут метод __setitem__(),
# однако этого не происходит.

# При наследовании от базовых типов, нужно переопределять типы и кастомизировать их, т.к. они спроектированы с учетом принципы
# открытости/закрытости.
# открыты для расширения, но закрыты для модификации

# В случае UserDict и UserList (оберток над dict и лист), при наследовании от dict, мы можем переопределить методы __setitem__(), __getitem__(),
# не затрагивая остальных:

from collections import UserDict, UserList

class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        # Преобразуем ключ в верхний регистр
        key = key.upper()
        # Вызываем метод __setitem__ базового класса
        self.data.__setitem__(key, value)

d = UpperCaseDict({"a": 1, "b": 2})
d.update({"c": 3})
print(d)