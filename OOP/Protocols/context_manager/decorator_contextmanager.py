
# @contextmanager - декоратор для контекстных менеджеров

### Прмиер

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

