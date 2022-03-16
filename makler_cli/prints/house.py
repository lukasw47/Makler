from makler.house import House
from makler.room import Room
from makler_cli.index import to_human_readable_index
from makler_cli.prints.headline import headline1
from makler_cli.prints.room import print_room_area


def print_house(house: House) -> None:
    headline1('house')
    print()
    print_house_area(house)


def print_house_area(house: House) -> None:
    for index, room in enumerate(house.rooms):
        print_room_area(index, room)
    print('-' * 18)
    print(f'House Area: {str(house.get_area()):>6}')
    print()
