import copy
import random

from mancala import MancalaPosition, STARTING_BOARD
from typing import List

IS_PLAYER_A_STARTING = True


class Player:
    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        pass


class GameControllerSettings:
    def __init__(self, should_make_first_random_move=True):
        self.should_make_first_random_move = should_make_first_random_move


class GameController:
    def __init__(self, player_a: Player, player_b: Player, game_controller_settings: GameControllerSettings):
        self.player_a = player_a
        self.player_b = player_b
        self.game_controller_settings = game_controller_settings
        self.position: MancalaPosition = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_STARTING)

    def run_game(self):
        if self.game_controller_settings.should_make_first_random_move:
            possible_moves = self.position.get_possible_moves()
            random_first_move = random.choice(possible_moves)
            self.position = self.position.get_position_after_move(random_first_move)
            print('First random move made')

        while not self.position.is_game_finished():
            possible_moves = self.position.get_possible_moves()
            possible_moves_copy = copy.deepcopy(possible_moves)
            position_copy = copy.deepcopy(self.position)

            self.print_current_position_info()
            chosen_move = -1

            if self.position.is_player_a_move:
                chosen_move = self.player_a.choose_move(position_copy, possible_moves_copy)
            else:
                chosen_move = self.player_b.choose_move(position_copy, possible_moves_copy)

            if chosen_move in possible_moves:
                print(f'Chosen move: {chosen_move}')
                self.position: MancalaPosition
                self.position = self.position.get_position_after_move(chosen_move)

        print('FINAL POSITION')
        self.print_current_position_info()
        self.position.print_end_game_info()

    def print_current_position_info(self):
        if self.position.is_player_a_move:
            print('Currently moving: Player A (' + type(self.player_a).__name__ + ')')
        else:
            print('Currently moving: Player B (' + type(self.player_b).__name__ + ')')

        print()
        self.position.print_position()
        print()
