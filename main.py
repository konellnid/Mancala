from game_controller import GameController, Player, GameControllerSettings
from human_player import HumanPlayer
from min_max_player import MinMaxPlayer
from evaluation_function import *
from random_move_player import RandomMovePlayer

if __name__ == "__main__":
    default_evaluation_function_settings = EvaluationFunctionSettings()
    evaluation_function = EvaluationFunction(default_evaluation_function_settings)

    game_controller_settings = GameControllerSettings(should_make_first_random_move=True)
    game_controller = GameController(MinMaxPlayer(2, evaluation_function),
                                     MinMaxPlayer(5, evaluation_function), game_controller_settings)
    # game_controller = GameController(HumanPlayer(), HumanPlayer())
    # game_controller = GameController(RandomMovePlayer(), RandomMovePlayer())
    # just choose any two players

    game_controller.run_game()
