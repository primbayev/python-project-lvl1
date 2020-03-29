from random import randrange


RULE = 'Answer "yes" if number even otherwise answer "no".\n'


def generate_round():
    random_number = randrange(0, 100)
    question = 'Question: {}'.format(random_number)

    if random_number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return (question, answer)
