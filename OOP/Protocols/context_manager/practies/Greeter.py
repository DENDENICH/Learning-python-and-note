from dataclasses import dataclass


@dataclass
class Greeter:
    name: str

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self):
        print(f"До встречи, {self.name}!")
