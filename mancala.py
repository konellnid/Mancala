from __future__ import annotations

import copy
from typing import List

STARTING_BOARD = [4, 4, 4, 4, 4, 4, 0,
                  4, 4, 4, 4, 4, 4, 0]
BOARD_LENGTH = 14
PLAYER_A_POCKETS = [0, 1, 2, 3, 4, 5]
PLAYER_A_STORE = 6
PLAYER_B_POCKETS = [7, 8, 9, 10, 11, 12]
PLAYER_B_STORE = 13
NUMBER_OF_SEEDS_FOR_LOOP = 13

CORRESPONDING_POCKETS = {
    0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7,
    7: 5, 8: 4, 9: 3, 10: 2, 11: 1, 12: 0
}
RIGHT_ALIGNMENT_SIZE = 4


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
        updated_board = copy.deepcopy(self.board)

        number_of_seeds = updated_board[move]
        updated_board[move] = 0
        current_index = move

        while number_of_seeds > 0:
            current_index = current_index + 1

            if current_index == PLAYER_A_STORE and not self.is_player_a_move:
                current_index = current_index + 1
            elif current_index == PLAYER_B_STORE and self.is_player_a_move:
                current_index = 0
            elif current_index == BOARD_LENGTH:
                current_index = 0

            updated_board[current_index] = updated_board[current_index] + 1
            number_of_seeds = number_of_seeds - 1

        is_next_turn_player_a_move = not self.is_player_a_move

        # check if player gets additional turn
        if self.is_move_end_in_store(move):
            is_next_turn_player_a_move = self.is_player_a_move
            # check for capture
        elif updated_board[current_index] == 1 and current_index in self.get_pockets_to_check():
            corresponding_index = CORRESPONDING_POCKETS[current_index]
            number_of_seeds_in_corresponding_pocket = updated_board[corresponding_index]
            if number_of_seeds_in_corresponding_pocket > 0:
                updated_board[current_index] = 0
                updated_board[corresponding_index] = 0

                captured_seeds = number_of_seeds_in_corresponding_pocket + 1
                current_player_store = self.get_current_player_store_index()
                updated_board[current_player_store] = updated_board[current_player_store] + captured_seeds

        updated_position = MancalaPosition(updated_board, is_next_turn_player_a_move)
        if updated_position.is_game_finished():
            updated_position.finish_game()

        return MancalaPosition(updated_board, is_next_turn_player_a_move)

    def get_possible_move_sequences(self) -> List[List[int]]:
        possible_move_sequences = []
        possible_moves = self.get_possible_moves()

        for possible_move in possible_moves:
            if self.is_move_end_in_store(possible_move):
                position_from_move = self.get_position_after_move(possible_move)
                move_sequences_from_position = position_from_move.get_possible_move_sequences()

                for additional_move_sequence in move_sequences_from_position:
                    new_move_sequence = [possible_move] + additional_move_sequence
                    possible_move_sequences.append(new_move_sequence)

                if len(move_sequences_from_position) == 0:
                    possible_move_sequences.append([possible_move])
            else:
                possible_move_sequences.append([possible_move])

        return possible_move_sequences

    def get_position_after_move_sequence(self, move_sequence: List[int]) -> MancalaPosition:
        current_position = self
        for move in move_sequence:
            current_position = current_position.get_position_after_move(move)

        return current_position

    def print_position(self):
        player_b_pockets_indexes = ""
        player_b_pockets_seeds = ""
        store_info = ""
        player_a_pockets_indexes = ""
        player_a_pockets_seeds = ""

        for pocket_index in PLAYER_B_POCKETS:
            aligned_index = str(pocket_index).rjust(RIGHT_ALIGNMENT_SIZE)
            aligned_seeds = str(self.board[pocket_index]).rjust(RIGHT_ALIGNMENT_SIZE)
            player_b_pockets_indexes = aligned_index + player_b_pockets_indexes
            player_b_pockets_seeds = aligned_seeds + player_b_pockets_seeds

        for pocket_index in PLAYER_A_POCKETS:
            aligned_index = str(pocket_index).rjust(RIGHT_ALIGNMENT_SIZE)
            aligned_seeds = str(self.board[pocket_index]).rjust(RIGHT_ALIGNMENT_SIZE)
            player_a_pockets_indexes = player_a_pockets_indexes + aligned_index
            player_a_pockets_seeds = player_a_pockets_seeds + aligned_seeds

        player_a_seeds = self.board[PLAYER_A_STORE]
        player_b_seeds = self.board[PLAYER_B_STORE]
        a_store_aligned = str(player_a_seeds).rjust(2)
        b_store_aligned = str(player_b_seeds).rjust(2)
        store_info = b_store_aligned + ('-' * (6 * RIGHT_ALIGNMENT_SIZE)) + a_store_aligned

        print('B indexes: ' + player_b_pockets_indexes)
        print('B pockets: ' + player_b_pockets_seeds)
        print('stores    ' + store_info)
        print('A pockets: ' + player_a_pockets_seeds)
        print('A indexes: ' + player_a_pockets_indexes)

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

    def is_move_end_in_store(self, move):
        number_of_seeds_to_check = self.board[move]

        player_store_index = self.get_current_player_store_index()
        offset_from_store = player_store_index - move

        while number_of_seeds_to_check > offset_from_store:
            # eliminate loop
            number_of_seeds_to_check = number_of_seeds_to_check - NUMBER_OF_SEEDS_FOR_LOOP

        return number_of_seeds_to_check == offset_from_store

    def get_current_player_store_index(self):
        if self.is_player_a_move:
            return PLAYER_A_STORE
        else:
            return PLAYER_B_STORE

    def is_game_finished(self):
        possible_moves = self.get_possible_moves()

        return len(possible_moves) == 0

    def finish_game(self):
        if self.is_player_a_move:
            self.move_remaining_seeds_to_store(PLAYER_B_POCKETS, PLAYER_B_STORE)
        else:
            self.move_remaining_seeds_to_store(PLAYER_A_POCKETS, PLAYER_A_STORE)

    def move_remaining_seeds_to_store(self, pockets_to_check, store_to_add_seeds):
        number_of_remaining_seeds = 0
        for pocket_index in pockets_to_check:
            if self.board[pocket_index] > 0:
                number_of_remaining_seeds = number_of_remaining_seeds + self.board[pocket_index]
                self.board[pocket_index] = 0

        self.board[store_to_add_seeds] = self.board[store_to_add_seeds] + number_of_remaining_seeds

    def print_end_game_info(self):
        player_a_seeds = self.board[PLAYER_A_STORE]
        player_b_seeds = self.board[PLAYER_B_STORE]

        print('A vs B')
        print(f'{player_a_seeds} - {player_b_seeds}')
        if player_a_seeds > player_b_seeds:
            print('Player A won!')
        elif player_b_seeds > player_a_seeds:
            print('Player B won!')
        else:
            print('Draw!')

    def get_players_seeds_in_stores(self):
        return self.board[PLAYER_A_STORE], self.board[PLAYER_B_STORE]

    def get_reachable_positions_for_current_player(self):
        reachable_positions = []

        possible_moves = self.get_possible_moves()

        for possible_move in possible_moves:
            after_move_position = self.get_position_after_move(possible_move)

            if self.is_player_a_move == after_move_position.is_player_a_move:
                reachable_positions_after_move = after_move_position.get_reachable_positions_for_current_player()
                if len(reachable_positions_after_move) == 0:
                    reachable_positions.append(after_move_position)
                else:
                    reachable_positions = reachable_positions + reachable_positions_after_move
            else:
                reachable_positions.append(after_move_position)

        return reachable_positions
