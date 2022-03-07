from makler.room import Room
from makler_cli.question import yes_no_question
from makler_cli.room.complex import input_complex_room
from makler_cli.room.parts import input_room_out_of_rectangles
from makler_cli.room.rectangle import input_rectangle_room


def input_room() -> Room:
    print('### INPUT ROOM '.ljust(50, '#'))
    if yes_no_question(message='is the room a rectangle? '):
        return input_rectangle_room()

    elif yes_no_question(message='can the room easily be split into rectangles? '):
        return input_room_out_of_rectangles()

    return input_complex_room()
