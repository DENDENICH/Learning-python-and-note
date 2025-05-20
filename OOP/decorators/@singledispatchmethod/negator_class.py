from functools import singledispatchmethod


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @neg.register(bool)
    def neg_bool(data: bool) -> bool:
        return not data
    
    @neg.register
    def neg_int_float(data: int | float) -> int | float:
        return data * -1