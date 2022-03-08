from makler_cli.inputs.house import input_house
from makler_cli.inputs.question import yes_no_question
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
    if yes_no_question(message='do you want to input another house [y/n]? '):
        raise KeyboardInterrupt
    print()
