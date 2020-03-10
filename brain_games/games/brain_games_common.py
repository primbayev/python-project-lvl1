def check_answer(user_answer, correct_answer):
    if user_answer != str(correct_answer):
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            user_answer, str(correct_answer)
        ))
    else:
        print('Correct!')
    return user_answer == str(correct_answer)
