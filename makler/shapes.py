from abc import ABC, abstractmethod
from dataclasses import dataclass

from makler.measurements import AreaInSquareMeters, LengthInMeters


@dataclass(frozen=True)
class Shape(ABC):

    @abstractmethod
    def get_area(self) -> AreaInSquareMeters:
        pass


@dataclass(frozen=True)
class Rectangle(Shape):
    length: LengthInMeters
    width: LengthInMeters

    def get_area(self) -> AreaInSquareMeters:
        return self.length * self.width
