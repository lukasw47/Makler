from typing import Sequence

from makler.room import Room
from makler.shapes import Rectangle
from makler_cli.inputs.mesurements import input_length_in_meters
from makler_cli.inputs.number import input_integer
from makler_cli.prints import headline4


def input_room_out_of_rectangles() -> Room:
    part_count = input_integer('how many rectangle can the room be split into? ')
    print()
    room_parts = input_multiple_rectangle_room_parts(count=part_count)
    return Room(parts=room_parts)


def input_multiple_rectangle_room_parts(count: int) -> Sequence[Rectangle]:
    return tuple(map(input_rectangle_room_part, range(1, count + 1)))


def input_rectangle_room_part(index: int) -> Rectangle:
    headline4(title=f'room part {index}')
    rectangle_width = input_length_in_meters(message='width of room part: ')
    rectangle_length = input_length_in_meters(message='length of room part: ')
    print()
    return Rectangle(width=rectangle_width, length=rectangle_length)
