from __future__ import annotations

from typing import List

STARTING_BOARD = [4, 4, 4, 4, 4, 4, 0,
                  4, 4, 4, 4, 4, 4, 0]
PLAYER_A_POCKETS = [0, 1, 2, 3, 4, 5]
PLAYER_A_STORE = 6
PLAYER_B_POCKETS = [7, 8, 9, 10, 11, 12]
PLAYER_B_STORE = 13


class MancalaPosition:
    def __init__(self, board: List[int], is_player_a_move: bool):
        self.board = board
        self.is_player_a_move = is_player_a_move

    def get_possible_moves(self) -> List[int]:
        possible_moves = []
        indexes_to_check = self.get_pockets_to_check()

        for pocket_index in indexes_to_check:
            if self.board[pocket_index] > 0:
                possible_moves.append(pocket_index)

        return possible_moves

    def get_position_after_move(self, move: int) -> MancalaPosition:
        pass

    def get_possible_move_sequences(self) -> List[List[int]]:
        pass

    def get_position_after_move_sequence(self, move_sequence: List[int]) -> MancalaPosition:
        pass

    def __eq__(self, other):
        if isinstance(other, MancalaPosition):
            return self.board == other.board and self.is_player_a_move == other.is_player_a_move
        else:
            return False

    def get_pockets_to_check(self):
        if self.is_player_a_move:
            return PLAYER_A_POCKETS
        else:
            return PLAYER_B_POCKETS
