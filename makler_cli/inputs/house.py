from makler.house import House
from makler_cli.inputs.number import input_integer
from makler_cli.inputs.room import input_multiple_rooms


def input_house() -> House:
    print(' input house '.center(30, '-'))
    room_count = input_integer(message='how many rooms does the house have? ')
    house_rooms = input_multiple_rooms(count=room_count)
    return House(rooms=house_rooms)
