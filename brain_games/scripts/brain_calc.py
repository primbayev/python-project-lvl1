from brain_games.games.brain_calc_game import game_process
from brain_games.cli import welcome_user, final_message


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    name = welcome_user()
    is_game_successful = game_process()
    final_message(name, is_game_successful)


if __name__ == '__main__':
    main()
