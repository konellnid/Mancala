import pickle

from game_controller import GameController, Player, GameControllerSettings
from human_player import HumanPlayer
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


if __name__ == "__main__":
    default_evaluation_function_settings = EvaluationFunctionSettings()
    evaluation_function = EvaluationFunction(default_evaluation_function_settings)

    game_controller_settings = GameControllerSettings(should_make_first_random_move=True,
                                                      should_first_player_be_chosen_at_random=True)

    # run_for_task_3_data(3, evaluation_function, game_controller_settings)
    # run_for_task_3_data(4, evaluation_function, game_controller_settings)
    # run_for_task_3_data(5, evaluation_function, game_controller_settings)
    # run_for_task_3_data(6, evaluation_function, game_controller_settings)
