from typing import Sequence

from makler.room import Room
from makler_cli.inputs.question import yes_no_question
from makler_cli.inputs.room.complex import input_complex_room
from makler_cli.inputs.room.parts import input_room_out_of_rectangles
from makler_cli.inputs.room.rectangle import input_rectangle_room


def input_multiple_rooms(count: int) -> Sequence[Room]:
    return tuple(input_room() for _ in range(count))


def input_room() -> Room:
    print('input room:')
    if yes_no_question(message='is the room a rectangle? '):
        return input_rectangle_room()

    elif yes_no_question(message='can the room easily be split into rectangles? '):
        return input_room_out_of_rectangles()

    return input_complex_room()
