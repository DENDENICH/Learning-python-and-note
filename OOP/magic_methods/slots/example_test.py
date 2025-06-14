from functools import singledispatchmethod


class User:
    __slots__ = ["name", "age"]
    @singledispatchmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @__init__.register(dict)
    def _from_dict(self, user_info: dict):
        self.name = user_info.get("name")
        self.age = user_info.get("age")

    def __setattr__(self, name, value):
        if value is None:
            raise ValueError(f"argument '{name}' can't be None")


class UserProf(User):
    __slots__ = ["surname"] # в классе потомке нужно указать новые слоты, а не перезаписывать все
    @singledispatchmethod
    def __init__(self, surname, *args):
        self.surname = surname
        super().__init__(*args)

    @__init__.register(dict)
    def _from_dict(self, user_info: dict):
        self.surname = user_info.get("surname")
        super()._from_dict(user_info)


user = User("John", 25)
user2 = User({"name": "John", "age": 25})

user_prof = UserProf({"name": "John", "age": 25, "surname": "Smith"})