from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import check_answer


def game_process():
    for i in range(0, 3):
        random_number = randrange(0, 50)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        is_answer_correct = check_answer(user_answer, correct_answer)
        if not is_answer_correct:
            return False
    return True
