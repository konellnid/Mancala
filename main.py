from game_controller import GameController, Player, GameControllerSettings
from human_player import HumanPlayer
from min_max_player import MinMaxPlayer
from evaluation_function import *
from aplha_beta_player import *
from random_move_player import RandomMovePlayer

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
