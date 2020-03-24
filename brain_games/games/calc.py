from random import randrange
from random import choice
from operator import add
from operator import sub
from operator import mul


RULE = 'What is the result of the expression?\n'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def generate_round():
    symbol, operation = choice(OPERATIONS)
    first_number = randrange(30)
    second_number = randrange(30)
    return (first_number, second_number, symbol, operation)


def question_text(expressions_parts):
    first_number, second_number, symbol, operation = expressions_parts
    return 'Question: {} {} {}'.format(
        first_number, symbol, second_number
    )


def correct_answer(expressions_parts):
    first_number, second_number, symbol, operation = expressions_parts
    return str(operation(first_number, second_number))
