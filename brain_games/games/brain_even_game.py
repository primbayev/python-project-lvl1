from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message
from brain_games.games.brain_games_common import anser_yes_or_no


def game_process():
    initial_welcome()
    anser_yes_or_no()
    name = welcome_user()

    is_game_successful = True
    for i in range(0, 3):
        random_number = randrange(0, 50)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        correct_answer = check_is_even(random_number)

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            is_game_successful = False
            break

    final_message(name, is_game_successful)


def check_is_even(number):
    if number % 2 == 0:
        return 'no'
    return 'yes'
