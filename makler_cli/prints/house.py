from makler.house import House
from makler_cli.prints.headline import headline1
from makler_cli.prints.room import print_room_area
from makler_cli.prints.separator import print_separator
from makler_cli.prints.value import print_named_value


def print_house(house: House) -> None:
    headline1('house')
    print()
    print_house_area(house)


def print_house_area(house: House) -> None:
    for index, room in enumerate(house.rooms):
        print_room_area(index, room)
    print_separator()
    print_named_value(name='House Area', value=house.get_area())
    print()
