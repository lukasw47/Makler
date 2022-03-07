from makler.measurements import LengthInMeters
from makler_cli.inputs.number import input_decimal


def input_length_in_meters(message: str) -> LengthInMeters:
    length = input_decimal(message)
    return LengthInMeters(length)
