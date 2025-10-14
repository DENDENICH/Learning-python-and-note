from contextlib import contextmanager


@contextmanager
def safe_open(filename: str, mode: str = 'r'):
    try:
        f = open(filename, mode)
        yield (f, None)
        f.close()
    except Exception as e:
        yield (None, e)

