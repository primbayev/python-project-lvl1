from random import randrange
from random import choice


RULE = 'What number is missing in the progression?\n'


def generate_round():
    arithmetic_progression = []
    element = randrange(0, 8)
    difference = randrange(1, 11)
    counter = 0
    question = ''

    while counter < 10:
        question = question + str(element) + ' '
        arithmetic_progression.append(str(element))
        element += difference
        counter += 1

    masked_element = choice(arithmetic_progression)
    print('Question: {}'.format(question.replace(masked_element, '..', 1)))

    return masked_element
