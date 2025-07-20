# ### Наследование с использованием приватных свойств ### #

from dataclasses import dataclass, field


class UserBase:
    def __init__(self, name, age):
        self._name = name
        self._age = age


@dataclass(init=False)
class User(UserBase):

    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email


u = User('John', 20, email='john@example.com')

print(u.__dict__)
