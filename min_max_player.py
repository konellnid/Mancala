from typing import List

from evaluation_function import EvaluationFunction
from game_controller import Player
from mancala import MancalaPosition

MIN_BOUND = -1000000
MAX_BOUND = 1000000


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
            chosen_position = self.choose_best_reachable_position(position, 0)
            chosen_move_sequence = self.find_move_sequece(position, chosen_position)

            self.current_move_sequence = chosen_move_sequence
            return self.current_move_sequence.pop(0)

    def choose_best_reachable_position(self, position, current_depth):
        reachable_positions = position.get_reachable_positions_for_current_player()
        best_found_position = reachable_positions[0]

        if position.is_player_a_move:
            found_max = MIN_BOUND
            for reachable_position in reachable_positions:
                evaluation = self.choose_min_from_position(reachable_position, 1)
                if evaluation > found_max:
                    found_max = evaluation
                    best_found_position = reachable_position
        else:
            found_min = MAX_BOUND
            for reachable_position in reachable_positions:
                evaluation = self.choose_max_from_position(reachable_position, 1)
                if evaluation < found_min:
                    found_min = evaluation
                    best_found_position = reachable_position

        return best_found_position

    def choose_max_from_position(self, current_position, current_depth):
        current_max = MIN_BOUND

        if current_depth < self.max_depth:
            reachable_positions = current_position.get_reachable_positions_for_current_player()
            if len(reachable_positions) > 0:
                for reachable_position in reachable_positions:
                    evaluation = self.choose_min_from_position(reachable_position, current_depth + 1)
                    if evaluation > current_max:
                        current_max = evaluation

                return current_max
            else:
                return self.evaluation_function.evaluate(current_position)
        else:
            return self.evaluation_function.evaluate(current_position)

    def choose_min_from_position(self, current_position, current_depth):
        current_min = MAX_BOUND

        if current_depth < self.max_depth:
            reachable_positions = current_position.get_reachable_positions_for_current_player()
            if len(reachable_positions) > 0:
                for reachable_position in reachable_positions:
                    evaluation = self.choose_min_from_position(reachable_position, current_depth + 1)
                    if evaluation < current_min:
                        current_min = evaluation

                return current_min
            else:
                return self.evaluation_function.evaluate(current_position)
        else:
            return self.evaluation_function.evaluate(current_position)

    def find_move_sequece(self, current_position, chosen_position):
        move_sequences = current_position.get_possible_move_sequences()

        for move_sequence in move_sequences:
            if current_position.get_position_after_move_sequence(move_sequence) == chosen_position:
                return move_sequence