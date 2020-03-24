from random import randrange
from random import choice
from operator import add
from operator import sub
from operator import mul


RULE = 'What is the result of the expression?\n'


def generate_round():
    operations = [['+', add], ['-', sub], ['*', mul]]
    random_operation = choice(operations)
    first_number = randrange(30)
    second_number = randrange(30)
    print(
        "Question: {} {} {}".format(
            first_number, random_operation[0], second_number
        )
    )

    correct_answer = str(random_operation[1](first_number, second_number))
    return correct_answer
