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


def run_for_task_3_iterative_data(max_seconds: int, eval_function: EvaluationFunction,
                                  settings: GameControllerSettings):
    infos_to_save = []
    for i in range(5):
        controller = GameController(IterativeDeepeningPlayer(50, max_seconds, MinMaxPlayer(1, eval_function)),
                                    IterativeDeepeningPlayer(50, max_seconds, AlphaBetaPlayer(1, eval_function)),
                                    settings)
        game_info = controller.run_game()
        infos_to_save.append(game_info)

    title = 'task3_mm-ab_iterative_' + str(max_seconds)
    save_game_infos(infos_to_save, title)


def show_data_from_task_3(depth: int, is_iterative=False, max_seconds=0):
    title = 'task3_mm-ab_' + str(depth)
    if is_iterative:
        title = 'task3_mm-ab_iterative_' + str(max_seconds)

    infos: List[GameInfo] = open_saved_infos(title)

    avg_a_time = mean(o.player_a_avg_move_time for o in infos)
    avg_b_time = mean(o.player_b_avg_move_time for o in infos)
    avg_a_nodes = mean(o.player_a_avg_nodes_visited for o in infos)
    avg_b_nodes = mean(o.player_b_avg_nodes_visited for o in infos)
    avg_a_seeds = mean(o.player_a_seeds for o in infos)
    avg_b_seeds = mean(o.player_b_seeds for o in infos)
    avg_a_depth = mean(o.player_a_avg_depth for o in infos)
    avg_b_depth = mean(o.player_b_avg_depth for o in infos)

    if is_iterative:
        print('Info for seconds:', max_seconds)
    else:
        print('Info for depth=', depth)
    print('A time', avg_a_time)
    print('B time', avg_b_time)
    print('A nodes', avg_a_nodes)
    print('B nodes', avg_b_nodes)
    print('A seeds', avg_a_seeds)
    print('B seeds', avg_b_seeds)
    print('A depth', avg_a_depth)
    print('B depth', avg_b_depth)
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

    # run_for_task_3_iterative_data(2, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(3, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(4, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(5, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(6, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(7, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(8, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(9, evaluation_function, game_controller_settings)
    # run_for_task_3_iterative_data(10, evaluation_function, game_controller_settings)
    #
    show_data_from_task_3(2, is_iterative=True, max_seconds=2)
    show_data_from_task_3(2, is_iterative=True, max_seconds=3)
    show_data_from_task_3(2, is_iterative=True, max_seconds=4)
    show_data_from_task_3(2, is_iterative=True, max_seconds=5)
    show_data_from_task_3(2, is_iterative=True, max_seconds=6)
    show_data_from_task_3(2, is_iterative=True, max_seconds=7)
    show_data_from_task_3(2, is_iterative=True, max_seconds=8)
    show_data_from_task_3(2, is_iterative=True, max_seconds=9)
    show_data_from_task_3(2, is_iterative=True, max_seconds=10)
