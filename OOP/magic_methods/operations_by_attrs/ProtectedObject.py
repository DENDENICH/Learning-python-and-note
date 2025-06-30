

class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            raise AttributeError(f"Доступ к защищенному атрибуту невозможен")
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(f"Доступ к защищенному атрибуту невозможен")
        else:
            super().__delattr__(name)

    def __getattribute__(self, name):
        if name.startswith("_"):
            raise AttributeError(f"Доступ к защищенному атрибуту невозможен")
        return super().__getattribute__(name)


protected_obj = ProtectedObject(_password="123456", login="admin", l="123456", _l="123456")
print(protected_obj._login)  # >> Доступ к защищенному атрибуту невозможен
