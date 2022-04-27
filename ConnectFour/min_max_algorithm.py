import math
from board import *


class MinMaxAlgorithm:

    def alpha_beta_search(self, board_state: Board):

        # let's see what moves return the best result.
        action = None

        # let's see if we should start by minimizing or maximizing.
        should_minimize = board_state.current_player() == board_state.get_initial_player()

        # initialize our value to +/-infinity depending on should we maximize or minimize.
        value = -math.inf if should_minimize else math.inf

        # iterate through the possible actions of the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the score of the move depending on maximizing or minimizing.
            # this will get the score recursively, by trying to find the best move for the AI whilst still taking in
            # consideration the best move for the opponent.
            # This will either result in a win for the AI or a draw.

            if should_minimize:
                action_score = self.min_value(board_state.result(allowed_action),
                                              -math.inf,
                                              math.inf)

                # depending on the result, store it.
                if action_score > value:
                    value = action_score
                    action = allowed_action

            else:
                action_score = self.max_value(board_state.result(allowed_action),
                                              -math.inf,
                                              math.inf)

                # depending on the result, store it.
                if action_score < value:
                    value = action_score
                    action = allowed_action

        # return the best move accordingly for maximizing or minimizing.
        return action

    def max_value(self, board_state: Board, alpha, beta):

        # check if someone has won in case the game has ended.
        if board_state.has_game_ended():
            return board_state.get_winner_as_int()

        # initialize our value to -infinity.
        value = -math.inf

        # iterate through all possible actions on the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the maximum between the previous value and the minimized result of the board.
            value = max(value, self.min_value(board_state.result(allowed_action),
                                              alpha,
                                              beta))

            # in case our value is lesser than alpha, return it.
            if value > beta:
                return value

            # assign our alpha as in the pseudocode.
            alpha = max(alpha, value)

        # return that value
        return value

    def min_value(self, board_state: Board, alpha, beta):

        # check if someone has won in case the game has ended.
        if board_state.has_game_ended():
            return board_state.get_winner_as_int()

        # initialize our value to +infinity.
        value = math.inf

        # iterate through all possible actions on the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the minimum between the previous value and the maximized result of the board.
            value = min(value, self.max_value(board_state.result(allowed_action),
                                              alpha,
                                              beta))

            # in case our value is lesser than alpha, return it.
            if value < alpha:
                return value

            # assign our alpha as in the pseudocode.
            beta = min(beta, value)

        # return that value
        return value
