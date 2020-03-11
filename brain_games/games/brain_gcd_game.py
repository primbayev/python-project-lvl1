from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message
from math import gcd


def game_process():
    initial_welcome()
    print('Find the greatest common divisor of given numbers.\n')
    name = welcome_user()

    is_game_successful = True
    for i in range(0, 3):
        first_number = randrange(0, 100)
        second_number = randrange(0, 100)

        print(
            "Question: {} {}".format(first_number, second_number)
        )
        user_answer = prompt_string('Your answer: ')

        correct_answer = gcd(first_number, second_number)

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            is_game_successful = False
            break

    final_message(name, is_game_successful)
