
class Obj:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c


class AttrsIterator:
    def __init__(self, obj):
        self.obj_attrs = [(key, value) for key, value in obj.__dict__.items()]
        self._index = 0
        self._high = len(self.obj_attrs) - 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._index += 1
            return self.obj_attrs[self._index - 1]
        except IndexError:
            raise StopIteration



att = AttrsIterator(Obj(1, 2))

for i in att:
    print(i)