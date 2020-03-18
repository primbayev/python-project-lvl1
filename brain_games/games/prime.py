from random import randrange


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def generate_round():
    random_number = randrange(0, 100)
    print('Question: {}'.format(random_number))

    correct_answer = determine_correct_answer(random_number)
    return correct_answer


def determine_correct_answer(number):
    counter = 0
    for i in range(2, number):
        if number % i == 0:
            counter += 1

    if counter == 0 and number > 1:
        return 'yes'
    return 'no'
