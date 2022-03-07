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
    print(f'House Area: {str(house.get_area())}')
    print()
    for index, room in enumerate(house.rooms):
        print_room(index, room)
    print()


def print_room(index: int, room: Room) -> None:
    print(f'Room {to_human_readable_index(index)}: {str(room.get_area())}')
