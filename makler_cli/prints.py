from makler.house import House
from makler.room import Room
from makler_cli.index import to_human_readable_index


def headline1(title: str) -> None:
    headline(title, length=40)


def headline2(title: str) -> None:
    headline(title, length=34)


def headline3(title: str) -> None:
    headline(title, length=28)


def headline4(title: str) -> None:
    headline(title, length=22)


def headline(title: str, length: int) -> None:
    print(f' {title} '.title().center(length, '-'))


def print_house(house: House) -> None:
    headline1('house')
    print()
    print_house_area(house)


def print_house_area(house: House) -> None:
    for index, room in enumerate(house.rooms):
        print_room(index, room)
    print('-' * 18)
    print(f'House Area: {str(house.get_area()):>6}')
    print()


def print_room(index: int, room: Room) -> None:
    string_index = f'{to_human_readable_index(index)}:'
    print(f'Room {string_index:<6} {str(room.get_area()):>6}')
