from brain_games import prompt_string, randrange
from brain_games.games.brain_games_common import initial_welcome, check_answer
from brain_games.games.brain_games_common import welcome_user, final_message


def game_process():
    initial_welcome()
    print('What number is missing in the progression?\n')
    name = welcome_user()

    for i in range(0, 3):
        progression = create_arithmetic_progression()
        masked_progression = mask_progression(progression)

        print('Question: ', end='')
        print(*masked_progression)
        user_answer = prompt_string('Your answer: ')

        correct_answer = list(set(progression) - set(masked_progression))[0]

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            break

    final_message(name, is_user_answer_correct)


def create_arithmetic_progression():
    arithmetic_progression = []
    element = randrange(0, 8)
    difference = randrange(1, 11)

    counter = 0
    while counter < 10:
        new_element = element + difference
        arithmetic_progression.append(new_element)
        element = new_element
        counter += 1

    return arithmetic_progression


def mask_progression(progression):
    masked_progression = progression.copy()
    masked_progression[randrange(0, len(progression) - 1)] = '..'
    return masked_progression
