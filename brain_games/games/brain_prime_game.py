from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message


def game_process():
    initial_welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    name = welcome_user()

    is_game_successful = True
    for i in range(0, 3):
        random_number = randrange(0, 100)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        correct_answer = check_prime_number(random_number)

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            is_game_successful = False
            break

    final_message(name, is_game_successful)


def check_prime_number(number):
    counter = 0
    for i in range(2, number):
        if number % i == 0:
            counter += 1

    if counter == 0 and number > 1:
        return 'yes'
    return 'no'
