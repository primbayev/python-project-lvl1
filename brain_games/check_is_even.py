from brain_games import prompt_string, randrange


def game_process():
    correct_counter = 0
    while correct_counter < 3:
        random_number = randrange(0, 50)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer != correct_answer:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'".format(
                    user_answer, correct_answer
                )
            )
            return False
        print('Correct!')
        correct_counter += 1
    return True


def final_message(name, is_game_successful):
    if is_game_successful:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))
