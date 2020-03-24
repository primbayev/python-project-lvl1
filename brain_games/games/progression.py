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

    masked_element = choice(progression_str.split(' ')[:-1])
    return (progression_str, masked_element)


def question_text(progression_and_masked_element):
    progression_str, masked_element = progression_and_masked_element

    return 'Question: {}'.format(progression_str.replace(
        masked_element, '..', 1
    ))


def correct_answer(progression_and_masked_element):
    progression_str, masked_element = progression_and_masked_element
    return masked_element
