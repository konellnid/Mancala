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


if __name__ == "__main__":
    default_evaluation_function_settings = EvaluationFunctionSettings()
    evaluation_function = EvaluationFunction(default_evaluation_function_settings)

    game_controller_settings = GameControllerSettings(should_make_first_random_move=True,
                                                      should_first_player_be_chosen_at_random=True)
    game_controller = GameController(MinMaxPlayer(3, evaluation_function),
                                     AlphaBetaPlayer(3, evaluation_function), game_controller_settings)
    # game_controller = GameController(HumanPlayer(), HumanPlayer(), game_controller_settings)
    # game_controller = GameController(RandomMovePlayer(), RandomMovePlayer(), game_controller_settings)
    # just choose any two players

    game_data = game_controller.run_game()

    game_data.print_game_info()

    infos = [game_data]
    save_game_infos(infos, 'minmax_3-ab_3')
    infos_loaded = open_saved_infos('minmax_3-ab_3')
