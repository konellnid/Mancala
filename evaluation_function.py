from mancala import *

TOTAL_NUMBER_OF_SEEDS = 48
SECURED_DRAW_SEEDS = 24


class EvaluationFunctionSettings:
    def __init__(self, secured_win_points=3, secured_draw_points=1, beating_possibilities_points=0):
        self.secured_win_points = secured_win_points
        self.secured_draw_points = secured_draw_points
        self.beating_possibilities_points = beating_possibilities_points


class EvaluationFunction:
    def __init__(self, settings: EvaluationFunctionSettings):
        self.settings = settings

    def evaluate(self, position: MancalaPosition) -> int:
        player_a_store, player_b_store = position.get_players_seeds_in_stores()

        evaluation = player_a_store - player_b_store

        if player_a_store > SECURED_DRAW_SEEDS:
            evaluation = evaluation + self.settings.secured_win_points
        elif player_b_store > SECURED_DRAW_SEEDS:
            evaluation = evaluation - self.settings.secured_win_points
        else:
            if player_a_store == SECURED_DRAW_SEEDS:
                evaluation = evaluation + self.settings.secured_draw_points
            if player_b_store == SECURED_DRAW_SEEDS:
                evaluation = evaluation - self.settings.secured_draw_points

        if self.settings.beating_possibilities_points > 0:
            beating_possibilities = 0
            beating_possibilities = beating_possibilities - position.get_player_a_beatable_pockets()
            beating_possibilities = beating_possibilities + position.get_player_b_beatable_pockets()
            evaluation = evaluation + beating_possibilities * self.settings.beating_possibilities_points

        return evaluation
