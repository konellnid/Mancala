from mancala import *

TOTAL_NUMBER_OF_SEEDS = 48
SECURED_DRAW_SEEDS = 24


class EvaluationFunctionSettings:
    def __init__(self, secured_win_points=3, secured_draw_points=1):
        self.secured_win_points = secured_win_points
        self.secured_win_points = secured_draw_points


class EvaluationFunction:
    def evaluate(self, position: MancalaPosition) -> int:
        pass
