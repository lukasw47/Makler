from typing import Generator

from makler.room import Room
from makler.shapes import Rectangle
from makler_cli.mesurements import input_length_in_meters
from makler_cli.question import yes_no_question


def input_room_out_of_rectangles() -> Room:
    room_parts = tuple(input_many_rectangle_room_parts())
    return Room(parts=room_parts)


def input_many_rectangle_room_parts() -> Generator[Rectangle]:
    yield input_rectangle_room_part()
    while yes_no_question(message='add another room part? '):
        yield input_rectangle_room_part()


def input_rectangle_room_part() -> Rectangle:
    rectangle_width = input_length_in_meters(message='input width of room part: ')
    rectangle_length = input_length_in_meters(message='input length of room part: ')
    return Rectangle(width=rectangle_width, length=rectangle_length)
