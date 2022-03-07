from makler_cli.inputs.house import input_house


def run_cli() -> None:
    try:
        while True:
            measure_house()

    except KeyboardInterrupt:
        pass


def measure_house() -> None:
    print()
    house = input_house()

    print()
    print(f'house area: {house.get_area()}')
    print()
    print()
