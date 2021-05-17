import pickle

from typing import List

from game_controller import *
from human_player import HumanPlayer
from iterative_deepening_player import IterativeDeepeningPlayer
from min_max_player import MinMaxPlayer
from evaluation_function import *
from aplha_beta_player import *
from random_move_player import RandomMovePlayer


def save_game_infos(infos_to_save, title):
    with open('saved/' + title, 'wb') as solutions_file:
        pickle.dump(infos_to_save, solutions_file)


def open_saved_infos(title):
    with open('saved/' + title, 'rb') as solving_infos_file:
        infos_to_load = pickle.load(solving_infos_file)

        return infos_to_load


def run_for_task_3_data(depth: int, eval_function: EvaluationFunction, settings: GameControllerSettings):
    infos_to_save = []
    for i in range(10):
        controller = GameController(MinMaxPlayer(depth, eval_function),
                                    AlphaBetaPlayer(depth, eval_function), settings)
        game_info = controller.run_game()
        infos_to_save.append(game_info)

    title = 'task3_mm-ab_' + str(depth)
    save_game_infos(infos_to_save, title)


def show_data_from_task_3(depth: int):
    title = 'task3_mm-ab_' + str(depth)
    infos: List[GameInfo] = open_saved_infos(title)

    avg_a_time = mean(o.player_a_avg_move_time for o in infos)
    avg_b_time = mean(o.player_b_avg_move_time for o in infos)
    avg_a_nodes = mean(o.player_a_avg_nodes_visited for o in infos)
    avg_b_nodes = mean(o.player_b_avg_nodes_visited for o in infos)
    avg_a_seeds = mean(o.player_a_seeds for o in infos)
    avg_b_seeds = mean(o.player_b_seeds for o in infos)

    print('Info for depth=', depth)
    print('A time', avg_a_time)
    print('B time', avg_b_time)
    print('A nodes', avg_a_nodes)
    print('B nodes', avg_b_nodes)
    print('A seeds', avg_a_seeds)
    print('B seeds', avg_b_seeds)
    print()


if __name__ == "__main__":
    default_evaluation_function_settings = EvaluationFunctionSettings()
    evaluation_function = EvaluationFunction(default_evaluation_function_settings)

    game_controller_settings = GameControllerSettings(should_make_first_random_move=True,
                                                      should_first_player_be_chosen_at_random=True)

    # run_for_task_3_data(3, evaluation_function, game_controller_settings)
    # run_for_task_3_data(4, evaluation_function, game_controller_settings)
    # run_for_task_3_data(5, evaluation_function, game_controller_settings)
    # run_for_task_3_data(6, evaluation_function, game_controller_settings)
    # run_for_task_3_data(7, evaluation_function, game_controller_settings)
    #
    # show_data_from_task_3(3)
    # show_data_from_task_3(4)
    # show_data_from_task_3(5)
    # show_data_from_task_3(6)
    # show_data_from_task_3(7)

    controller = GameController(AlphaBetaPlayer(2, evaluation_function),
                                IterativeDeepeningPlayer(10, 2, AlphaBetaPlayer(1, evaluation_function)),
                                game_controller_settings)
    game_info = controller.run_game()
    game_info.print_game_info()
