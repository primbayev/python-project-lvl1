from brain_games.games.brain_games_common import (
    common_game_prime_and_even_processes)


def game_process():
    task_message = 'Answer "yes" if given number is prime. \
Otherwise answer "no".\n'
    common_game_prime_and_even_processes(task_message, 'check_prime_number')
