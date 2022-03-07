from makler.house import House
from makler_cli.number import input_integer
from makler_cli.room import input_multiple_rooms


def input_house() -> House:
    room_count = input_integer(message='how many rooms does the house have? ')
    house_rooms = input_multiple_rooms(count=room_count)
    return House(rooms=house_rooms)
