from random import randrange


RULE = 'Find the greatest common divisor of given numbers.\n'


def generate_round():
    first_number = randrange(0, 100)
    second_number = randrange(0, 100)
    print(
        "Question: {} {}".format(first_number, second_number)
    )

    correct_answer = determine_correct_answer(first_number, second_number)
    return correct_answer


def determine_correct_answer(first_number, second_number):
    greatest_divisor = 1
    greatest_number = max(first_number, second_number)

    for divisor in range(1, greatest_number + 1):
        if first_number % divisor == 0 and second_number % divisor == 0:
            greatest_divisor = divisor

    return str(greatest_divisor)
