from dataclasses import dataclass
from typing import Sequence

from makler.measurements import AreaInSquareMeters
from makler.parts import Part


@dataclass(frozen=True)
class Room:
    parts: Sequence[Part]

    def get_area(self) -> AreaInSquareMeters:
        part_areas = map(Part.get_area, self.parts)
        area = sum(part_areas)
        return AreaInSquareMeters(area)
