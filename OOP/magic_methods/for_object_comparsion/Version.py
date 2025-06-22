from typing import List

from functools import total_ordering
from random import randint as rd
import time

@total_ordering
class Version:
    def __init__(self, version):
        self.version, self._version_tuple = self._parsing_version(version)

    def _parsing_version(self, value: str) -> tuple[str, tuple]:
        """Парсинг версии для заполнения недостающих значений"""
        nums = value.split(".")
        if isinstance(value, str) or len(nums) > 3:
            for num in nums:
                if not num.isdigit():
                    raise ValueError("'version' must be in format 'num1.num2.num3'")
            return self._add_numbers_in_version(nums)
        raise TypeError("'version' must be a string in format 'num1.num2.num3'")

    @staticmethod
    def _add_numbers_in_version(value: List[str]) -> tuple[str, tuple]:
        if len(value) == 1:
            value.append("0.0")
        elif len(value) == 2:
            value.append("0")
        return ".".join(value), tuple(map(int, value))

    def __repr__(self):
        return f"{__class__.__name__}('{self.version}')"

    def __str__(self):
        return f"{self.version}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.version == other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._version_tuple < other._version_tuple
        return NotImplemented


# test
start = time.time()

list = [Version(f"{rd(1, 100)}.{rd(1, 100)}.{rd(1, 100)}") for _ in range(1000000)]
sorted(list)

end = time.time()
print(f"Затраченное время - {end - start}")
# 2.10332
# 0.5129

# 1.000.000 элементов
# 6.71256