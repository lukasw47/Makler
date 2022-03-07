def yes_no_question(message: str) -> bool:
    while True:
        boolean_input = input(message)

        if boolean_input in ('y', 'yes'):
            return True

        elif boolean_input in ('n', 'no'):
            return False

        print('please answer with [y/yes] or [n/no]!')
