def headline1(message: str) -> None:
    headline(message, length=30)


def headline2(message: str) -> None:
    headline(message, length=24)


def headline(message: str, length: int) -> None:
    print(f' {message} '.title().center(length, '-'))
