

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


class SortKey:
    """Класс для создания ключей сортировки"""
    def __init__(self, *keys):
        self.keys = keys

    def __call__(self, obj: object) -> tuple:
        values = list()
        for key in self.keys:
            if hasattr(obj, key):
                values.append(getattr(obj, key))
            else:
                raise AttributeError(f"object '{obj.__class__.__name__}' has no attribute '{key}'")
        return tuple(values)


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('age')))            # сортировка на основе атрибута age
print(sorted(users, key=SortKey('name', 'age')))