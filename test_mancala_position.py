import unittest
from mancala import *

# board is represented as List[int] of length = 14
# [6 player A pockets, player A store,
#  6 player B pockets, player B store]
EXAMPLE_BOARD = [0, 0, 3, 3, 0, 2, 3,
                 0, 0, 0, 1, 2, 0, 4]
IS_PLAYER_A_MOVE = True


class MancalaPositionTest(unittest.TestCase):
    def test_starting_position_moves(self):
        starting_position = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_MOVE)
        expected_moves = [0, 1, 2, 3, 4, 5]

        returned_moves = starting_position.get_possible_moves()

        self.assertCountEqual(returned_moves, expected_moves)

    def test_starting_position_move_sequences(self):
        starting_position = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_MOVE)
        expected_move_sequences = [[0], [1], [3], [4], [5],
                                   [2, 0], [2, 1], [2, 3], [2, 4], [2, 5]]

        returned_move_sequences = starting_position.get_possible_move_sequences()

        self.assertCountEqual(returned_move_sequences, expected_move_sequences)


#
# EXAMPLE_BOARD = [0, 0, 3, 3, 0, 2, 3,
#                  0, 0, 0, 1, 2, 0, 4]
class ExampleBoardTest(unittest.TestCase):
    def test_moves_for_player_a(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        expected_moves = [2, 3, 5]

        returned_moves = example_position.get_possible_moves()

        self.assertCountEqual(returned_moves, expected_moves)

    def test_move_sequences_for_player_a(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        expected_move_sequences = [[2], [5], [3, 2], [3, 5]]

        returned_move_sequences = example_position.get_possible_move_sequences()

        self.assertCountEqual(returned_move_sequences, expected_move_sequences)

    def test_moves_for_player_b(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, not IS_PLAYER_A_MOVE)
        expected_moves = [10, 11]

        returned_moves = example_position.get_possible_moves()

        self.assertCountEqual(returned_moves, expected_moves)

    def test_move_sequences_for_player_b(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        expected_move_sequences = [[10], [11, 10]]

        returned_move_sequences = example_position.get_possible_move_sequences()

        self.assertCountEqual(returned_move_sequences, expected_move_sequences)

    def test_simple_move(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        chosen_move = 2
        expected_board = [0, 0, 0, 4, 1, 3, 3,
                          0, 0, 0, 1, 2, 0, 4]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = example_position.get_position_after_move(chosen_move)

        self.assertEqual(returned_position, expected_position)

    # if move ends in a store, player gets another turn
    def test_move_with_additional_turn(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        chosen_move = 3
        expected_board = [0, 0, 3, 0, 1, 3, 4,
                          0, 0, 0, 1, 2, 0, 4]
        expected_position = MancalaPosition(expected_board, IS_PLAYER_A_MOVE)

        returned_position = example_position.get_position_after_move(chosen_move)

        self.assertEqual(returned_position, expected_position)

    def test_move_sequence(self):
        example_position = MancalaPosition(EXAMPLE_BOARD, IS_PLAYER_A_MOVE)
        chosen_move_sequence = [3, 5]

        # board after first part of move sequence [3]
        # [0, 0, 3, 0, 1, 3, 4,
        #  0, 0, 0, 1, 2, 0, 4]

        expected_board = [0, 0, 3, 0, 1, 0, 5,
                          1, 1, 0, 1, 2, 0, 4]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = example_position.get_position_after_move_sequence(chosen_move_sequence)

        self.assertEqual(returned_position, expected_position)


class CapturingTest(unittest.TestCase):
    def test_standard_capturing(self):
        board = [0, 0, 1, 1, 0, 0, 10,
                 1, 2, 3, 4, 5, 6, 20]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)
        capturing_move = 3
        expected_board = [0, 0, 1, 0, 0, 0, 13,
                          1, 0, 3, 4, 5, 6, 20]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = position.get_position_after_move(capturing_move)

        self.assertEqual(returned_position, expected_position)

    # capture doesn't occur if corresponding pocket is empty
    def test_capturing_for_empty_enemy_pocket(self):
        board = [0, 0, 1, 1, 0, 0, 10,
                 1, 0, 3, 4, 5, 6, 20]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)
        not_capturing_move = 3
        expected_board = [0, 0, 1, 0, 1, 0, 10,
                          1, 2, 3, 4, 5, 6, 20]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = position.get_position_after_move(not_capturing_move)

        self.assertEqual(returned_position, expected_position)

    def test_full_circle_capturing(self):
        board = [0, 0, 1, 13, 0, 0, 10,
                 1, 2, 3, 4, 5, 6, 20]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)
        full_circle_move = 3
        expected_board = [1, 1, 2, 0, 1, 1, 15,
                          2, 3, 0, 5, 6, 7, 20]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = position.get_position_after_move(full_circle_move)

        self.assertEqual(returned_position, expected_position)

    # capturing can occur only on own pockets
    def test_capture_on_enemy_pockets(self):
        board = [0, 1, 0, 0, 3, 3, 10,
                 0, 0, 3, 4, 5, 6, 20]
        position = MancalaPosition(board, IS_PLAYER_A_MOVE)
        tested_move = 6
        expected_board = [0, 1, 0, 0, 3, 0, 11,
                          1, 1, 3, 4, 5, 6, 20]
        expected_position = MancalaPosition(expected_board, not IS_PLAYER_A_MOVE)

        returned_position = position.get_position_after_move(tested_move)

        self.assertEqual(returned_position, expected_position)


if __name__ == '__main__':
    unittest.main()
