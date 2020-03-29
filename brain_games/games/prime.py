from random import randrange


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def generate_round():
    random_number = randrange(0, 100)
    question = 'Question: {}'.format(random_number)
    answer = 'yes' if is_prime(random_number) else 'no'

    return (question, answer)


def is_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    return False
