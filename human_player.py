from typing import List

from game_controller import Player
from mancala import MancalaPosition


class HumanPlayer(Player):
    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        is_move_selected = False
        while not is_move_selected:
            print('Choose pocket index to make move: ')
            print(possible_moves)

            human_input = input()
            if human_input.isdigit():
                chosen_number = int(human_input)
                if chosen_number in possible_moves:
                    return chosen_number
                else:
                    print('No such pocket in possible moves')
            else:
                print('Provided input is not a digit')
