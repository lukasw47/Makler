from typing import Sequence

from makler.house import House
from makler.room import Room
from makler_cli.inputs.number import input_integer
from makler_cli.inputs.room import input_multiple_rooms
from makler_cli.prints import headline1, headline2


def input_house() -> House:
    headline1(title='house')
    house_rooms = input_house_rooms()
    return House(rooms=house_rooms)


def input_house_rooms() -> Sequence[Room]:
    room_count = input_integer(message='how many rooms does the house have? ')
    print()
    return input_multiple_rooms(count=room_count)
