from brain_games.cli import WELCOME, welcome_user, prompt_user_answer


def run(game):
    print(WELCOME)
    print(game.RULE)
    user_name = welcome_user()

    for round in range(3):
        correct_answer = game.generate_round()
        user_answer = prompt_user_answer()

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_answer, correct_answer
            ))
            print("Let's try again, {}!".format(user_name))
            break

        print('Correct!')

        if round == 2:
            print('Congratulations, {}!'.format(user_name))
