from random import randrange


RULE = 'Answer "yes" if number even otherwise answer "no".\n'


def generate_round():
    return randrange(0, 100)


def question_text(random_number):
    return 'Question: {}'.format(random_number)


def correct_answer(random_number):
    if random_number % 2 == 0:
        return 'yes'
    return 'no'
