from game_controller import GameController, Player
from human_player import HumanPlayer

if __name__ == "__main__":
    game_controller = GameController(HumanPlayer(), HumanPlayer())
    game_controller.run_game()
