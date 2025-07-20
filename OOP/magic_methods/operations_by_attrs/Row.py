

class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    def __setattr__(self, name, value):
        if self.__dict__.get(name) is not None:
            raise AttributeError(f"Изменение значения атрибута невозможно")
        else:
            raise AttributeError("Установка нового атрибута невозможна")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(self.__get_list_args())})"

    def __get_list_args(self) -> list[str]:
        """Возвращает список аргументов и их значений"""
        args_list = list()
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                args_list.append(f"{key}='{value}'")
            else:
                args_list.append(f"{key}={value}")
        return args_list

print(Row(l=0))