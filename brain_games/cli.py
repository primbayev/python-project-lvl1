from brain_games import prompt_string


def welcome_user():
    name = prompt_string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name


def final_message(name, is_game_successful):
    if is_game_successful:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))
