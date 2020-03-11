from brain_games import prompt_string


def initial_welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt_string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name


def answer_yes_or_no():
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')


def check_answer(user_answer, correct_answer):
    if user_answer != str(correct_answer):
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, str(correct_answer)
        ))
    else:
        print('Correct!')
    return user_answer == str(correct_answer)


def final_message(name, is_game_successful):
    if is_game_successful:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))
