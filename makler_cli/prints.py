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
