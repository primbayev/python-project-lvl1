from random import randrange


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def generate_round():
    return randrange(0, 100)


def question_text(random_number):
    return 'Question: {}'.format(random_number)


def correct_answer(random_number):
    counter = 0
    for i in range(2, random_number):
        if random_number % i == 0:
            counter += 1

    if counter == 0 and random_number > 1:
        return 'yes'
    return 'no'
