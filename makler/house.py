from dataclasses import dataclass
from typing import Sequence

from makler.measurements import AreaInSquareMeters
from makler.room import Room


@dataclass(frozen=True)
class House:
    rooms: Sequence[Room]

    def get_area(self) -> AreaInSquareMeters:
        room_areas = map(Room.get_area, self.rooms)
        area = sum(room_areas)
        return AreaInSquareMeters(area)
