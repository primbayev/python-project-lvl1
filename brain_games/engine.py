from brain_games.cli import WELCOME, welcome_user, prompt_user_answer


def run(game, rounds=3):
    print(WELCOME)
    print(game.RULE)
    user_name = welcome_user()

    for round in range(rounds):
        questions_main_part = game.generate_round()
        print(game.question_text(questions_main_part))

        correct_answer = game.correct_answer(questions_main_part)
        user_answer = prompt_user_answer()

        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_answer, correct_answer
            ))
            print("Let's try again, {}!".format(user_name))
            break

        print('Correct!')
    else:
        print('Congratulations, {}!'.format(user_name))
