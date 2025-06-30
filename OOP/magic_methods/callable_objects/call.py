

# __call__(self, *args, **kwargs): - магический метод, который срабатывает при вызове объекта спомощью круглых скобок
class Call:
    def __call__(self, *args, **kwargs):
        print('Hello')

call_ob = Call()
call_ob() # >> Hello


# Сценарии использования __call__:
# 1. альтернатива замыканиям

def line_generator(k, b):
    """Базовое замыкание"""
    def line(x):
        return k * x + b
    return line
line = line_generator(2, 3)
print(line(2))

class Line:
    """Реализация замыкания через класс и метод __call__"""
    def __init__(self, k, b):
        self.k = k
        self.b = b
    def __call__(self, x):
        if isinstance(x, (int, float)):
            return self.k * x + self.b
        else:
            raise TypeError("x must be int or float")

line_call = Line(2, 3)
print(line_call(2))

# 2. создание декораторов

class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()

@UpperCaseDecorator
def say_text(text: str):
    return f"Hello, {text}"

print(say_text("World"))  # >> HELLO, WORLD