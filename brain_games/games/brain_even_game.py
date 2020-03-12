from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message


def game_process():
    initial_welcome()
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()

    for i in range(0, 3):
        random_number = randrange(0, 50)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        correct_answer = check_is_even(random_number)

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            break

    final_message(name, is_user_answer_correct)


def check_is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
