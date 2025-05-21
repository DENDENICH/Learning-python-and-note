from functools import singledispatchmethod
from datetime import date

class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @__init__.register(date)
    def _from_datetime_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_iso_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except TypeError:
            raise TypeError("Неверный формат ISO")


    @__init__.register(list)
    @__init__.register(tuple)
    def _from_nums_array(self, birth_date):
        if len(birth_date) != 3:
            raise ValueError("Массив должен содержать ровно три числа")
        self.birth_date = date(*birth_date)



b = BirthInfo("2020-09-18")
print()