from random import randrange
from random import choice


RULE = 'What number is missing in the progression?\n'


def generate_round():
    element = randrange(0, 8)
    difference = randrange(1, 11)
    counter = 0
    progression_str = ''

    while counter < 10:
        progression_str = progression_str + str(element) + ' '
        element += difference
        counter += 1

    answer = choice(progression_str.split(' ')[:-1])
    question = 'Question: {}'.format(
        progression_str.replace(
            answer, '..', 1
        )
    )

    return (question, answer)
