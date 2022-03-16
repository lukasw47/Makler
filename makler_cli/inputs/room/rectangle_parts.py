from typing import Sequence

from makler.room import Room
from makler.parts import Rectangle
from makler_cli.index import to_human_readable_index
from makler_cli.inputs.mesurements import input_length_in_meters
from makler_cli.inputs.number import input_integer
from makler_cli.prints.headline import headline4


def input_room_with_rectangle_parts() -> Room:
    room_rectangle_parts = input_rectangle_parts()
    return Room(parts=room_rectangle_parts)


def input_rectangle_parts() -> Sequence[Rectangle]:
    part_count = input_integer('how many rectangles can the room be split into? ')
    print()
    rectangle_parts = map(input_rectangle_part, range(part_count))
    return tuple(rectangle_parts)


def input_rectangle_part(index: int) -> Rectangle:
    headline4(title=f'room part {to_human_readable_index(index)}')
    rectangle_width = input_length_in_meters(message='width of room part: ')
    rectangle_length = input_length_in_meters(message='length of room part: ')
    print()
    return Rectangle(width=rectangle_width, length=rectangle_length)
