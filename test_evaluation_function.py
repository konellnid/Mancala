import copy
import unittest

from evaluation_function import *
from mancala import *

SAMPLE_BOARD = [0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0]

DEFAULT_EVALUATION_FUNCTION_SETTINGS = EvaluationFunctionSettings(secured_win_points=3, secured_draw_points=1)
DEFAULT_EVALUATION_FUNCTION = EvaluationFunction(DEFAULT_EVALUATION_FUNCTION_SETTINGS)


class DefaultEvaluationFunctionTest(unittest.TestCase):
    def test_draw_end_game(self):
        tested_board = copy.deepcopy(SAMPLE_BOARD)
        tested_board[PLAYER_A_STORE] = 24
        tested_board[PLAYER_B_STORE] = 24
        tested_position = MancalaPosition(tested_board, True)

        evaluation = DEFAULT_EVALUATION_FUNCTION.evaluate(tested_position)

        self.assertEqual(evaluation, 0)

    def test_example_with_secured_winning(self):
        tested_board = copy.deepcopy(SAMPLE_BOARD)
        tested_board[PLAYER_A_STORE] = 25
        tested_board[PLAYER_B_STORE] = 21
        tested_board[0] = 1
        tested_board[12] = 1
        tested_position = MancalaPosition(tested_board, True)
        expected_evaluation = (25 - 21) + 3

        evaluation = DEFAULT_EVALUATION_FUNCTION.evaluate(tested_position)

        self.assertEqual(evaluation, expected_evaluation)

    def test_example_with_secured_draw(self):
        tested_board = copy.deepcopy(SAMPLE_BOARD)
        tested_board[PLAYER_A_STORE] = 21
        tested_board[PLAYER_B_STORE] = 24
        tested_board[0] = 1
        tested_board[12] = 2
        tested_position = MancalaPosition(tested_board, True)
        expected_evaluation = (21 - 24) - 1

        evaluation = DEFAULT_EVALUATION_FUNCTION.evaluate(tested_position)

        self.assertEqual(evaluation, expected_evaluation)


if __name__ == '__main__':
    unittest.main()
