from dataclasses import dataclass
from typing import Sequence

from makler.measurements import AreaInSquareMeters
from makler.shapes import Shape


@dataclass(frozen=True)
class Room:
    parts: Sequence[Shape]

    def get_area(self) -> AreaInSquareMeters:
        part_areas = map(Shape.get_area, self.parts)
        return sum(part_areas)
