from random import randrange


RULE = 'What number is missing in the progression?\n'


def generate_round():
    progression = create_arithmetic_progression()
    masked_progression = mask_progression(progression)

    print('Question: ', end='')
    print(*masked_progression)
    correct_answer = list(set(progression) - set(masked_progression))[0]
    return str(correct_answer)


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
    masked_progression[randrange(len(progression))] = '..'
    return masked_progression
