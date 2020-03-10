from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import check_answer
from math import gcd


def game_process():
    for i in range(0, 3):
        first_number = randrange(0, 100)
        second_number = randrange(0, 100)

        print(
            "Question: {} {}".format(first_number, second_number)
        )
        user_answer = prompt_string('Your answer: ')

        correct_answer = gcd(first_number, second_number)

        is_answer_correct = check_answer(user_answer, correct_answer)
        if not is_answer_correct:
            return False
    return True
