from game_controller import GameController, Player
from human_player import HumanPlayer
from random_move_player import RandomMovePlayer

if __name__ == "__main__":
    game_controller = GameController(HumanPlayer(), HumanPlayer())
    # game_controller = GameController(RandomMovePlayer(), RandomMovePlayer())
    game_controller.run_game()
