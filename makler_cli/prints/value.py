def print_named_value(name: str, value: object, length: int = 30):
    name_part = f'{name}: '
    actual_length = length - len(name_part)
    print(f'{name_part}{value:>{actual_length}}')
