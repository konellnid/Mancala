from threading import Timer
from typing import List

from game_controller import Player
from mancala import MancalaPosition


class IterativeDeepeningPlayer(Player):
    def __init__(self, max_depth: int, max_seconds, player):
        super().__init__()
        self.max_seconds = max_seconds
        self.max_iterative_depth = max_depth
        self.is_over_time_limit = False
        self.player = player
        self.current_move_sequence = []

    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        if len(self.current_move_sequence) > 0:
            return self.current_move_sequence.pop(0)

        self.info_choose_move_started()

        self.is_over_time_limit = False
        t = Timer(self.max_seconds, self.manage_time_is_over)
        t.start()
        current_iteration_move_sequence = []
        current_iteration_depth_limit = 1

        while not self.is_over_time_limit and current_iteration_depth_limit <= self.max_iterative_depth:
            self.player.current_move_sequence = []
            self.player.max_depth = current_iteration_depth_limit

            chosen_move = self.player.choose_move(position, possible_moves)
            chosen_sequence = [chosen_move] + self.player.current_move_sequence

            if not self.is_over_time_limit:
                self.info_current_iteration_depth_limit(current_iteration_depth_limit)
                current_iteration_move_sequence = chosen_sequence
                current_iteration_depth_limit = current_iteration_depth_limit + 1

            print(current_iteration_depth_limit)

        t.cancel()

        self.current_move_sequence = current_iteration_move_sequence

        self.info_choose_move_ended()

        return self.current_move_sequence.pop(0)

    def manage_time_is_over(self):
        # makes max and min methods return evaluations instead of checking children
        self.player.max_depth = 1

        self.is_over_time_limit = True

