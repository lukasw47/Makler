from makler.room import Room
from makler.shapes import Rectangle
from makler_cli.inputs.mesurements import input_length_in_meters


def input_rectangle_room() -> Room:
    room_parts = input_rectangle_room_part(),
    return Room(parts=room_parts)


def input_rectangle_room_part() -> Rectangle:
    rectangle_width = input_length_in_meters(message='room width: ')
    rectangle_length = input_length_in_meters(message='room length: ')
    print()
    return Rectangle(width=rectangle_width, length=rectangle_length)
