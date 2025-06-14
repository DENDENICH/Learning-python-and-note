

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __get_list_args(self) -> list[str]:
        """Возвращает список аргументов и их значений"""
        args_list = list()
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                args_list.append(f"{key}='{value}'")
            else:
                args_list.append(f"{key}={value}")
        return args_list

    def __repr__(self):
        return f"{__class__.__name__}({', '.join(self.__get_list_args())})"

    def __str__(self):
        return f"{__class__.__name__}: {', '.join(self.__get_list_args())}"


obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))


value = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}