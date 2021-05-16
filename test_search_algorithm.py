import unittest

from evaluation_function import *
from min_max_player import *
from aplha_beta_player import *

DEFAULT_EVALUATION_FUNCTION_SETTINGS = EvaluationFunctionSettings(secured_win_points=3, secured_draw_points=1)
DEFAULT_EVALUATION_FUNCTION = EvaluationFunction(DEFAULT_EVALUATION_FUNCTION_SETTINGS)

IS_PLAYER_A_MOVE = True


class MinMaxTest(unittest.TestCase):
    def test_choosing_right_capture(self):
        player = MinMaxPlayer(2, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 4 allows to capture 15 seeds
        board = [1, 0, 1, 0, 1, 0, 2,
                 15, 1, 1, 1, 1, 1, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 4)

    def test_avoiding_getting_captured(self):
        player = MinMaxPlayer(3, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 1 allows to spread 15 seeds and avoid them being capture
        board = [1, 15, 1, 1, 1, 1, 2,
                 0, 1, 0, 1, 0, 1, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        # check for move sequence, which can save move for later use
        if chosen_move == 5 and len(player.current_move_sequence) > 0:
            position = position.get_position_after_move(chosen_move)
            chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 1)

    def test_stalling_to_leave_enemy_with_no_moves(self):
        player = MinMaxPlayer(3, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 2 leaves enemy with no seeds, meaning all remaining seeds go to player
        board = [0, 0, 3, 6, 6, 6, 2,
                 0, 0, 0, 0, 0, 0, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 2)


class AlphaBetaTest(unittest.TestCase):
    def test_choosing_right_capture(self):
        player = AlphaBetaPlayer(2, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 4 allows to capture 15 seeds
        board = [1, 0, 1, 0, 1, 0, 2,
                 15, 1, 1, 1, 1, 1, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 4)

    def test_avoiding_getting_captured(self):
        player = AlphaBetaPlayer(3, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 1 allows to spread 15 seeds and avoid them being capture
        board = [1, 15, 1, 1, 1, 1, 2,
                 0, 1, 0, 1, 0, 1, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        # check for move sequence, which can save move for later use
        if chosen_move == 5 and len(player.current_move_sequence) > 0:
            position = position.get_position_after_move(chosen_move)
            chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 1)

    def test_stalling_to_leave_enemy_with_no_moves(self):
        player = AlphaBetaPlayer(3, DEFAULT_EVALUATION_FUNCTION)
        # choosing move 2 leaves enemy with no seeds, meaning all remaining seeds go to player
        board = [0, 0, 3, 6, 6, 6, 2,
                 0, 0, 0, 0, 0, 0, 7]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)

        chosen_move = player.choose_move(position, position.get_possible_moves())

        self.assertEqual(chosen_move, 2)


if __name__ == '__main__':
    unittest.main()
