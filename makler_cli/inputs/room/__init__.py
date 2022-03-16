from typing import Sequence

from makler.room import Room
from makler_cli.index import to_human_readable_index
from makler_cli.inputs.question import ask_yes_no
from makler_cli.inputs.room.complex import input_complex_room
from makler_cli.inputs.room.rectangle_parts import input_room_with_rectangle_parts
from makler_cli.inputs.room.rectangle import input_rectangle_room
from makler_cli.prints.headline import headline2, headline3


def input_multiple_rooms(count: int) -> Sequence[Room]:
    headline2(title='rooms')
    print()
    return tuple(map(input_room, range(count)))


def input_room(index: int) -> Room:
    headline3(title=f'room {to_human_readable_index(index)}')

    if ask_yes_no(message='is the room a rectangle [y/n]? '):
        print()
        return input_rectangle_room()

    elif True or ask_yes_no(message='can the room easily be split into rectangles [y/n]? '):
        print()
        return input_room_with_rectangle_parts()

    return input_complex_room()
