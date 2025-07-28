from dataclasses import dataclass, field


class Parent:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


c = Child.from_dict({"name": "John", "age": 20})
print(c.__dict__) # {'name': 'John', 'age': 20}
