

### Декораторы можно реализовывать как стандартным метод (спомощьжю функций)
### Так и спомощью класса и метода __call__


class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()

@UpperCaseDecorator
def say_text(text: str):
    return f"Hello, {text}"

print(say_text("World"))  # >> HELLO, WORLD