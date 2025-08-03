

class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return True
        if not hasattr(self.obj, 'close'):
            print("Незакрываемый объект")
        else:
            self.obj.close()
        return False


with Closer("hello") as obj:
    print(obj)


print(obj)