from typing import Sequence

from makler.room import Room
from makler.shapes import Rectangle
from makler_cli.mesurements import input_length_in_meters
from makler_cli.number import input_integer


def input_room_out_of_rectangles() -> Room:
    part_count = input_integer('how many rectangle can the room be split into? ')
    room_parts = input_multiple_rectangle_room_parts(count=part_count)
    return Room(parts=room_parts)


def input_multiple_rectangle_room_parts(count: int) -> Sequence[Rectangle]:
    return tuple(input_rectangle_room_part() for _ in range(count))


def input_rectangle_room_part() -> Rectangle:
    rectangle_width = input_length_in_meters(message='input width of room part: ')
    rectangle_length = input_length_in_meters(message='input length of room part: ')
    return Rectangle(width=rectangle_width, length=rectangle_length)
