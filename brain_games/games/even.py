from random import randrange


RULE = 'Answer "yes" if number even otherwise answer "no".\n'


def generate_round():
    random_number = randrange(0, 100)
    print('Question: {}'.format(random_number))

    correct_answer = determine_correct_answer(random_number)
    return correct_answer


def determine_correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
