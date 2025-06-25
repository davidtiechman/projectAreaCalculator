from abc import ABC,abstractmethod
from msilib.schema import Class
from typing import ClassVar


class Shape(ABC):
    Type = ClassVar[str]

    @abstractmethod
    def Type(self):
        pass

    @abstractmethod
    def get_area(self):
        arae = 0
        return arae
    @abstractmethod
    def get_perimeter(self):
        perimeter =0
        return perimeter
