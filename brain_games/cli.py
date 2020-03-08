from brain_games import prompt_string


def welcome_user():
    name = prompt_string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name
