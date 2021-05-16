from typing import List

from evaluation_function import EvaluationFunction
from game_controller import Player
from mancala import MancalaPosition

MIN_BOUND = -1000000
MAX_BOUND = 1000000


class AlphaBetaPlayer(Player):
    def __init__(self, max_depth: int, evaluation_function: EvaluationFunction):
        super().__init__()
        self.max_depth = max_depth
        self.current_move_sequence = []
        self.evaluation_function = evaluation_function

    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        if len(self.current_move_sequence) > 0:
            chosen_move = self.current_move_sequence.pop(0)
            return chosen_move
        else:
            self.info_choose_move_started()
            chosen_position = self.choose_best_reachable_position(position)
            chosen_move_sequence = position.find_move_sequence_leading_to(chosen_position)

            self.current_move_sequence = chosen_move_sequence
            self.info_choose_move_ended()
            return self.current_move_sequence.pop(0)

    def choose_best_reachable_position(self, position):
        reachable_positions = position.get_reachable_positions_for_current_player()
        best_found_position = reachable_positions[0]

        if position.is_player_a_move:
            found_max = MIN_BOUND
            for reachable_position in reachable_positions:
                evaluation = self.choose_min_from_position(reachable_position, 1, MIN_BOUND, MAX_BOUND)
                if evaluation > found_max:
                    found_max = evaluation
                    best_found_position = reachable_position
        else:
            found_min = MAX_BOUND
            for reachable_position in reachable_positions:
                evaluation = self.choose_max_from_position(reachable_position, 1, MIN_BOUND, MAX_BOUND)
                if evaluation < found_min:
                    found_min = evaluation
                    best_found_position = reachable_position

        return best_found_position

    def choose_max_from_position(self, current_position, current_depth, alpha, beta):
        # self.info_new_node()
        current_max = MIN_BOUND

        if current_depth < self.max_depth:
            reachable_positions = current_position.get_reachable_positions_for_current_player()
            if len(reachable_positions) > 0:
                for reachable_position in reachable_positions:
                    evaluation = self.choose_min_from_position(reachable_position, current_depth + 1, alpha, beta)
                    if evaluation > current_max:
                        current_max = evaluation
                    if current_max >= beta:
                        return current_max
                    if current_max > alpha:
                        alpha = current_max

                return current_max
            else:
                return self.evaluation_function.evaluate(current_position)
        else:
            return self.evaluation_function.evaluate(current_position)

    def choose_min_from_position(self, current_position, current_depth, alpha, beta):
        # self.info_new_node()
        current_min = MAX_BOUND

        if current_depth < self.max_depth:
            reachable_positions = current_position.get_reachable_positions_for_current_player()
            if len(reachable_positions) > 0:
                for reachable_position in reachable_positions:
                    evaluation = self.choose_min_from_position(reachable_position, current_depth + 1, alpha, beta)
                    if evaluation < current_min:
                        current_min = evaluation
                    if current_min <= alpha:
                        return current_min
                    if current_min < beta:
                        beta = current_min

                return current_min
            else:
                return self.evaluation_function.evaluate(current_position)
        else:
            return self.evaluation_function.evaluate(current_position)
