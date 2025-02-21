# В этой игре игрок и компьютер каждый раунд бросают шестигранный кубик.
# Игрок, выбросивший 1, теряет все свои баллы.
# Выигрывает тот, кто раньше наберет 30 баллов.

import prompt
import random

def game_pig():
    player_sum = 0
    comp_sum = 0
    name = prompt.string('What is your name? ')
    input(f'Hello, {name}! Press Enter to start.')
    while True:
        player = random.randint(1, 6)
        comp = random.randint(1, 6)
        print(f'{name} turn: {player}')
        print(f'Computer turn: {comp}')
        player_sum = player_sum + player if player > 1 else 0
        comp_sum = comp_sum + comp if comp > 1 else 0
        print(f'Score {name}-computer: {player_sum}-{comp_sum}')
        if player_sum >= 30 and player_sum >= comp_sum:
            print(f'{name} wins!')
            break
        elif comp_sum >= 30:
            print('Computer wins!')
            break
        input()
    return


if __name__ == '__main__':
    game_pig()