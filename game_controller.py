import copy
import random
import time
from statistics import mean

from mancala import MancalaPosition, STARTING_BOARD
from typing import List

IS_PLAYER_A_STARTING = True


class PlayerData:
    def __init__(self):
        self.nodes_counter_list = []
        self.current_tree_nodes_counter = 0

        self.move_times = []
        self.current_choosing_start_time = -1

    def save_current_nodes_counter(self):
        self.nodes_counter_list.append(self.current_tree_nodes_counter)

    def new_node_is_being_visited(self):
        self.current_tree_nodes_counter = self.current_tree_nodes_counter + 1

    def save_current_choosing_time(self):
        self.move_times.append(time.time() - self.current_choosing_start_time)

    def new_move_is_being_chosen(self):
        self.current_choosing_start_time = time.time()
        self.current_tree_nodes_counter = 0


class GameInfo:
    def __init__(self, player_a_data: PlayerData, player_b_data: PlayerData):
        self.player_a_data = player_a_data
        self.player_b_data = player_b_data

        self.player_a_avg_nodes_visited = mean(player_a_data.nodes_counter_list)
        self.player_b_avg_nodes_visited = mean(player_b_data.nodes_counter_list)

        self.player_a_avg_move_time = mean(player_a_data.move_times)
        self.player_b_avg_move_time = mean(player_b_data.move_times)

    def print_game_info(self):
        print('Player A avg time: ', self.player_a_avg_move_time)
        print('Player B avg time: ', self.player_b_avg_move_time)
        print()
        print('Player A avg nodes visited: ', self.player_a_avg_nodes_visited)
        print('Player B avg nodes visited: ', self.player_b_avg_nodes_visited)


class Player:
    def __init__(self):
        self.player_data = PlayerData()

    def info_choose_move_started(self):
        self.player_data.new_move_is_being_chosen()

    def info_choose_move_ended(self):
        self.player_data.save_current_choosing_time()
        self.player_data.save_current_nodes_counter()

    def info_new_node(self):
        self.player_data.new_node_is_being_visited()

    def choose_move(self, position: MancalaPosition, possible_moves: List[int]) -> int:
        pass


class GameControllerSettings:
    def __init__(self, should_make_first_random_move=True, should_first_player_be_chosen_at_random=True):
        self.should_make_first_random_move = should_make_first_random_move
        self.should_first_player_be_chosen_at_random = should_first_player_be_chosen_at_random


class GameController:
    def __init__(self, player_a: Player, player_b: Player, game_controller_settings: GameControllerSettings):
        self.player_a = player_a
        self.player_b = player_b
        self.game_controller_settings = game_controller_settings
        self.position: MancalaPosition = MancalaPosition(STARTING_BOARD, IS_PLAYER_A_STARTING)

    def run_game(self):
        if self.game_controller_settings.should_first_player_be_chosen_at_random:
            is_player_a_going_first = random.choice([True, False])
            self.position.is_player_a_move = is_player_a_going_first

        if self.game_controller_settings.should_make_first_random_move:
            possible_moves = self.position.get_possible_moves()
            random_first_move = random.choice(possible_moves)
            self.position = self.position.get_position_after_move(random_first_move)
            print('First random move made')

        while not self.position.is_game_finished():
            possible_moves = self.position.get_possible_moves()
            possible_moves_copy = copy.deepcopy(possible_moves)
            position_copy = copy.deepcopy(self.position)

            self.print_current_position_info()
            chosen_move = -1

            if self.position.is_player_a_move:
                chosen_move = self.player_a.choose_move(position_copy, possible_moves_copy)
            else:
                chosen_move = self.player_b.choose_move(position_copy, possible_moves_copy)

            if chosen_move in possible_moves:
                print(f'Chosen move: {chosen_move}')
                self.position: MancalaPosition
                self.position = self.position.get_position_after_move(chosen_move)

        print('FINAL POSITION')
        self.print_current_position_info()
        self.position.print_end_game_info()

        return GameInfo(self.player_a.player_data, self.player_b.player_data)

    def print_current_position_info(self):
        if self.position.is_player_a_move:
            print('Currently moving: Player A (' + type(self.player_a).__name__ + ')')
        else:
            print('Currently moving: Player B (' + type(self.player_b).__name__ + ')')

        print()
        self.position.print_position()
        print()
