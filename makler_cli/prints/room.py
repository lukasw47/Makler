from makler.room import Room
from makler_cli.index import to_human_readable_index


def print_room_area(index: int, room: Room) -> None:
    readable_index = to_human_readable_index(index)
    print(f'Room {readable_index:<6}: {str(room.get_area()):>6}')
