from makler.cli_input.number import input_integer
from makler.cli_input.room import input_room
from makler.house import House


def input_house() -> House:
    room_count = input_integer(message='how many rooms does the house have? ')
    house_rooms = tuple(input_room() for _ in range(room_count))
    return House(rooms=house_rooms)
