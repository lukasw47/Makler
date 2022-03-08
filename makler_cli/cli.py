from makler_cli.inputs.house import input_house
from makler_cli.inputs.question import ask_yes_no
from makler_cli.prints import print_house


def run_cli() -> None:
    try:
        while True:
            measure_house()
            ask_to_repeat()

    except KeyboardInterrupt:
        pass


def measure_house() -> None:
    house = input_house()
    print_house(house)


def ask_to_repeat() -> None:
    measure_another_house = ask_yes_no(message='do you want to measure another house [y/n]? ')
    if not measure_another_house:
        raise KeyboardInterrupt
    print()
