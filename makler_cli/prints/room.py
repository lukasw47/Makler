from makler.room import Room
from makler_cli.index import to_human_readable_index
from makler_cli.prints.value import print_named_value


def print_room_area(index: int, room: Room) -> None:
    room_name = f'Room {to_human_readable_index(index)}'
    print_named_value(name=room_name, value=room.get_area())
