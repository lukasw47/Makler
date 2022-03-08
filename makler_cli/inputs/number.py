from decimal import Decimal


def input_integer(message: str) -> int:
    while not (integer_value := input(message)) or not integer_value.isdecimal():
        print('please input a whole number!')
    return int(integer_value)


def input_decimal(message: str) -> Decimal:
    while not (decimal_text := input(message)) or not is_decimal_number(decimal_text):
        print('please input a number!')
    decimal_value = format_decimal_text(decimal_text)
    return Decimal(decimal_value)


def is_decimal_number(decimal_text: str) -> bool:
    decimal_value = format_decimal_text(decimal_text)
    number_parts = decimal_value.split(sep='.', maxsplit=1)
    return all(map(str.isdecimal, number_parts))


def format_decimal_text(value: str) -> str:
    return value.replace(',', '.', 1)
