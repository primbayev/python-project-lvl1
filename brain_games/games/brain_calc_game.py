from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import check_answer


def game_process():
    operations = ('+', '-', '*')
    for i in range(0, 3):
        random_operation = operations[i]
        first_number = randrange(0, 30)
        second_number = randrange(0, 30)

        print(
            "Question: {} {} {}".format(
                first_number, random_operation, second_number
            )
        )
        user_answer = prompt_string('Your answer: ')

        correct_answer = eval(
            '{} {} {}'.format(first_number, random_operation, second_number)
        )

        is_answer_correct = check_answer(user_answer, correct_answer)
        if not is_answer_correct:
            return False
    return True
