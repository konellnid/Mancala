import unittest
from mancala import *

# board is represented as List[int] of length = 14
# [6 player A pockets, player A store,
#  6 player B pockets, player B store]
EXAMPLE_BOARD = [0, 0, 3, 3, 0, 2, 3,
                 0, 0, 0, 1, 2, 0, 4]
IS_PLAYER_A_STARTING = True


class MancalaPositionTest(unittest.TestCase):
    def test_starting_position_moves(self):
        starting_position = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_STARTING)
        expected_moves = [0, 1, 2, 3, 4, 5]

        returned_moves = starting_position.get_possible_moves()

        self.assertCountEqual(returned_moves, expected_moves)

    def test_starting_position_move_sequences(self):
        starting_position = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_STARTING)
        expected_move_sequences = [[0], [1], [3], [4], [5],
                                   [2, 0], [2, 1], [2, 3], [2, 4], [2, 5]]

        returned_move_sequences = starting_position.get_possible_move_sequences()

        self.assertCountEqual(returned_move_sequences, expected_move_sequences)


if __name__ == '__main__':
    unittest.main()
