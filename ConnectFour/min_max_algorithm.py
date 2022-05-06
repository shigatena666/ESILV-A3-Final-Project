import math

from transposition_tables import *


class MinMaxAlgorithm:

    # who_am_i represents the player the AI has been given
    # returns a tuple containing first the chosen_column and second the score of this column for the iterations
    def alpha_beta_search(self, board_state: Board, depth, alpha=-math.inf, beta=math.inf):

        if depth == 0:
            return None, 0

        # winning, loosing or draw conditions.
        if board_state.has_game_ended():
            return None, board_state.get_winner_as_int()

        # setting possible action list and choosing whether we should minimize or maximize.
        allowed_actions = board_state.get_allowed_actions()

        # let's see if we should start by minimizing or maximizing.
        should_maximize = board_state.get_current_player_char() == board_state.get_player_char()

        # initialize our value to +/-infinity depending on should we maximize or minimize.
        value = -math.inf if should_maximize else math.inf
        chosen_column = None

        # iterate through all possible actions on the board.
        for allowed_action in allowed_actions:

            # get the board result.
            board_result = board_state.result(allowed_action)

            # get the maximum between the previous value and the minimized result of the board.
            child_score = self.alpha_beta_search(board_result, depth - 1, alpha, beta)[1]

            # Set the new best value in case we have a better score
            if (child_score > value and should_maximize) or (child_score < value and not should_maximize):

                chosen_column = allowed_action
                value = child_score

            if should_maximize:
                # assign our alpha as in the pseudocode.
                alpha = max(alpha, value)
            else:
                # assign our beta as in the pseudocode.
                beta = min(beta, value)

            if alpha >= beta:
                break

        # return that value
        return chosen_column, value
