from random import randrange


RULE = 'Find the greatest common divisor of given numbers.\n'


def generate_round():
    first_number = randrange(0, 100)
    second_number = randrange(0, 100)
    print(
        "Question: {} {}".format(first_number, second_number)
    )

    correct_answer = find_gcd(first_number, second_number)
    return correct_answer


def find_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        elif second_number > first_number:
            second_number -= first_number
    return str(first_number)
