from decimal import Decimal


def input_integer(message: str) -> int:
    while not (integer_value := input(message)) or not integer_value.isdecimal():
        print('please input a whole number!')
    return int(integer_value)


def input_decimal(message: str) -> Decimal:
    while not (decimal_value := input(message)) or not is_decimal_number(decimal_value):
        print('please input a number!')
    return Decimal(decimal_value)


def is_decimal_number(string: str) -> bool:
    number_parts = string.replace(',', '.', 1).split(sep='.', maxsplit=1)
    return all(map(str.isdecimal, number_parts))
