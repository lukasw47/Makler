from abc import ABC, abstractmethod
from dataclasses import dataclass

from makler.measurements import AreaInSquareMeters, LengthInMeters


@dataclass(frozen=True)
class Shape(ABC):

    @abstractmethod
    def get_area(self) -> AreaInSquareMeters:
        return self.get_area()


@dataclass(frozen=True)
class Rectangle(Shape):
    width: LengthInMeters
    length: LengthInMeters

    def get_area(self) -> AreaInSquareMeters:
        area = self.length * self.width
        return AreaInSquareMeters(area)
