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

    question = 'Question: {} {} {}'.format(
        first_number, symbol, second_number
    )
    answer = str(operation(first_number, second_number))

    return (question, answer)
