from prompt import string as prompt_string


WELCOME = 'Welcome to the Brain Games!'


def welcome_user():
    name = prompt_string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name


def prompt_user_answer():
    return prompt_string('Your answer: ')
