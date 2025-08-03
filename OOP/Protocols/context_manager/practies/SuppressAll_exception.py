

class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        return True if traceback is not None else False # подавляем любые исключения



