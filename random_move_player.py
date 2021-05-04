import random
from typing import List

from game_controller import Player
from mancala import MancalaPosition


class RandomMovePlayer(Player):
    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        return random.choice(possible_moves)
