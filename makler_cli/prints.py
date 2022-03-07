def headline1(title: str) -> None:
    headline(title, length=30)


def headline2(title: str) -> None:
    headline(title, length=24)


def headline(title: str, length: int) -> None:
    print(f' {title} '.title().center(length, '-'))
