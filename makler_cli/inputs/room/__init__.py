from typing import Sequence

from makler.room import Room
from makler_cli.inputs.question import yes_no_question
from makler_cli.inputs.room.complex import input_complex_room
from makler_cli.inputs.room.parts import input_room_out_of_rectangles
from makler_cli.inputs.room.rectangle import input_rectangle_room
from makler_cli.prints import headline3, headline2


def input_multiple_rooms(count: int) -> Sequence[Room]:
    headline2(title='rooms')
    print()
    return tuple(map(input_room, range(1, count + 1)))


def input_room(index: int) -> Room:
    headline3(title=f'room {index}')

    if yes_no_question(message='is the room a rectangle [y/n]? '):
        print()
        return input_rectangle_room()

    elif yes_no_question(message='can the room easily be split into rectangles [y/n]? '):
        print()
        return input_room_out_of_rectangles()

    return input_complex_room()
