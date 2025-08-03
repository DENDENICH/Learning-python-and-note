import time


class Obj:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c


class AttrsIterator:
    def __init__(self, obj):
        self.obj_attrs = [(key, value) for key, value in obj.__dict__.items()]

    def __create_iterator(self) -> iter:
        return iter(self.obj_attrs)

    def __iter__(self):
        self._iter = self.__create_iterator()
        return self._iter

    def __next__(self):
        return next(self._iter)


### FOR test in speed ###
start = time.time()
for i in range(3_000_000):
    atts = AttrsIterator(Obj(1, 2))
    for i in atts:
        pass
end = time.time()
print(f"Время выполнения: {end - start}") # на 3 миллиона операций = ~ 2.654456615447998 секунды