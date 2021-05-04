from typing import List

from evaluation_function import EvaluationFunction
from game_controller import Player
from mancala import MancalaPosition


class MinMaxPlayer(Player):
    def __init__(self, max_depth: int, evaluation_function: EvaluationFunction):
        self.max_depth = max_depth
        self.current_move_sequence = []
        self.evaluation_function = evaluation_function

    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        if len(self.current_move_sequence) > 0:
            chosen_move = self.current_move_sequence.pop(0)
            return chosen_move
        else:
            reachable_positions = position.get_reachable_positions_for_current_player()
