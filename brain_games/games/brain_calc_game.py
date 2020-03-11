from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message


def game_process():
    initial_welcome()
    print('What is the result of the expression?\n')
    name = welcome_user()

    is_game_successful = True
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

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            is_game_successful = False
            break

    final_message(name, is_game_successful)
