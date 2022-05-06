from min_max_algorithm import *
from board import *
from utilities import *
import math
from random import choice


def new_game_state(board_state, action_move):
    # warning, this will not directly modify the board_state.

    # update our board with that action.
    board_state = board_state.result(action_move)

    # re-show the game after the play.
    print(board_state)

    # check if there is a winner after that play.
    return board_state


if __name__ == "__main__":

    # instantiate our board and algorithm.
    rows = 6
    columns = 12
    depth = 5

    board = Board()
    min_max_algo = MinMaxAlgorithm()

    # get who should play first, IA or player ?
    ia_plays_first = bool(int(input('IA should play first ? (Answer 1 if yes, 0 otherwise)')))
    K_PLAYER = 'X' if ia_plays_first else 'O'

    # show the initial game state.
    print(board)

    # start our game.
    while True:

        # if IA plays first, put its first play onto the board.
        if ia_plays_first:

            # get the best move out of the board.
            alpha_beta_result = min_max_algo.alpha_beta_search(board, depth)

            # retrieve the action from the result.
            action = alpha_beta_result[0]

            print(alpha_beta_result)

            # actualize the board state with the action.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break

        # ask the user to play and set it inside the board.

        coordonates = int(input("x: "))

        # check if user provided right input types.
        while not (0 <= coordonates < columns):
            # re-actualize user inputs.
            print("[Error]: Please provide a valid number.")
            coordonates = int(input("x: "))

        # check if user provided right input coordonates.
        while coordonates not in board.get_allowed_actions():

            # re-actualize user inputs.
            print("[Error]: Please provided a non-full column.")
            coordonates = input("x:")
            coordonates = int(coordonates)

        # actualize the board state with the action.
        board = new_game_state(board, coordonates)

        # if true, it means there is a winner.
        if board.has_game_ended():
            print(board.get_winner(), "won")
            break

        # if IA plays second, put its play on the board.
        if not ia_plays_first:

            # get the best move out of the board.
            alpha_beta_result = min_max_algo.alpha_beta_search(board, depth)

            # retrieve the action from the result.
            action = alpha_beta_result[0]

            print(alpha_beta_result)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break
