from random import randrange


RULE = 'Find the greatest common divisor of given numbers.\n'


def generate_round():
    first_number = randrange(0, 100)
    second_number = randrange(0, 100)
    return (first_number, second_number)


def question_text(numbers):
    first_number, second_number = numbers
    return 'Question: {} {}'.format(first_number, second_number)


def correct_answer(numbers):
    first_number, second_number = numbers

    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        elif second_number > first_number:
            second_number -= first_number
    return str(first_number)
