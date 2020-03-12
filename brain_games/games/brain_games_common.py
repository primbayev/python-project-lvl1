from brain_games import prompt_string, randrange


def initial_welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt_string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name


def check_answer(user_answer, correct_answer):
    if user_answer != str(correct_answer):
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, str(correct_answer)
        ))
    else:
        print('Correct!')
    return user_answer == str(correct_answer)


def final_message(name, is_user_answer_correct):
    if is_user_answer_correct:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


def check_prime_number(number):
    counter = 0
    for i in range(2, number):
        if number % i == 0:
            counter += 1

    if counter == 0 and number > 1:
        return 'yes'
    return 'no'


def check_is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def find_correct_answer(checker, random_number):
    if checker == 'check_even_number':
        return check_is_even(random_number)
    elif checker == 'check_prime_number':
        return check_prime_number(random_number)


def common_game_prime_and_even_processes(task_message, checker):
    initial_welcome()
    print(task_message)
    name = welcome_user()

    for i in range(0, 3):
        random_number = randrange(0, 100)
        print('Question: {}'.format(random_number))

        user_answer = prompt_string('Your answer: ')
        correct_answer = find_correct_answer(checker, random_number)

        is_user_answer_correct = check_answer(user_answer, correct_answer)
        if not is_user_answer_correct:
            break

    final_message(name, is_user_answer_correct)
