from mancala import MancalaPosition, STARTING_BOARD
from typing import List

IS_PLAYER_A_STARTING = True


class Player:
    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        pass


class GameController:
    def __init__(self, player_a: Player, player_b: Player):
        self.player_a = player_a
        self.player_b = player_b
        self.position = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_STARTING)

    def run_game(self):
        pass
