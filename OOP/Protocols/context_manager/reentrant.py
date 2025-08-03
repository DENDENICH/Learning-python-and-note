

# Реентерабельный - те объекты протокола контекстного менеджера, которые могут быть повторно использованы
# в вложеных контекстных менеджерах

### Пример


class Indent:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.level -= 1

    def print(self, text):
        print('  ' * self.level + text)


with Indent() as indent:
    with indent:
        indent.print('Hello')
        with indent:
            indent.print('World')
        indent.print('!!!')


