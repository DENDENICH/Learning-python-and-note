from functools import singledispatchmethod

class Cat:
    @singledispatchmethod
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    @__init__.register(list)
    def _from_list(self, data):
        self.breed, self.name, self.age = data

    def __repr__(self):
        return f"{self.breed=} {self.name=} {self.age=}"

cat1 = Cat(['breed1', 'name1', 'age1'])
print(cat1)