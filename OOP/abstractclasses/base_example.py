from typing import Any, TypeVar, Type
from abc import abstractmethod, ABC

T = TypeVar("T", bound="Base")

class Base(ABC):
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_class_method(cls: Type[T], value: int) -> T: # аннотация возвращаемого экземпляра класса дочернего класса
        return cls(value)


    @abstractmethod
    def get_data(self):
        pass


class BaseModify(Base):
    def __init__(self, value: int, data: Any):
        super().__init__(value=value)
        self.data = data


