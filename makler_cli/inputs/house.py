from makler.house import House
from makler_cli.inputs.number import input_integer
from makler_cli.inputs.room import input_multiple_rooms
from makler_cli.prints import headline1, headline2


def input_house() -> House:
    headline1(title='house')
    room_count = input_integer(message='how many rooms does the house have? ')
    print()
    house_rooms = input_multiple_rooms(count=room_count)
    return House(rooms=house_rooms)
