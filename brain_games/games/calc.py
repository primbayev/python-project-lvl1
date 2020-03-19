from random import randrange


RULE = 'What is the result of the expression?\n'


def generate_round():
    operations = ('+', '-', '*')
    random_operation = operations[randrange(3)]
    first_number = randrange(30)
    second_number = randrange(30)
    print(
        "Question: {} {} {}".format(
            first_number, random_operation, second_number
        )
    )

    correct_answer = calculate_expression(
        first_number, second_number, random_operation
    )
    return correct_answer


def calculate_expression(first_number, second_number, random_operation):
    if random_operation == '*':
        return str(first_number * second_number)
    elif random_operation == '-':
        return str(first_number - second_number)
    else:
        return str(first_number + second_number)
