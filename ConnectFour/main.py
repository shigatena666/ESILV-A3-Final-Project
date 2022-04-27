from min_max_algorithm import *
from board import *
from action import *
import utilities


def new_game_state(board_state: Board, action_move):
    # warning, this will not directly modify the board_state.

    # update our board with that action.
    board_state = board_state.result(action_move)

    # re-show the game after the play.
    print(board_state)

    # check if there is a winner after that play.
    return board_state


if __name__ == "__main__":

    # instantiate our board and algorithm.
    board = Board()
    #board = board.result(0)
    
    
    i = 0
    board = board.result(i+0)
    board = board.result(i+1)
    board = board.result(i+1)
    board = board.result(i+2)
    board = board.result(i+2)
    board = board.result(i+3)
    board = board.result(i+2)
    board = board.result(i+3)
    board = board.result(11)
    board = board.result(i+3)
    board = board.result(i+3)
    #board = board.result(11)
    
    
    
    

    
    
    print(board)
    print(board.get_winner())


    """
    min_max_algo = MinMaxAlgorithm()

    # get who should play first, IA or player ?
    ia_plays_first = bool(int(input('IA should play first ? (Answer 1 if yes, 0 otherwise)')))

    # show the initial game state.
    print(board)

    # start our game.
    while True:

        # if IA plays first, put its first play onto the board.
        if ia_plays_first:

            # get the best move out of the board.
            action = min_max_algo.alpha_beta_search(board)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break

        # ask the user to play and set it inside the board.
        user_input = input("x, y: ")
        coordonates = user_input.split(',')

        # check if user provided right input types.
        while not utilities.is_int(coordonates[0]) and not utilities.is_int(coordonates[1]):

            # re-actualize user inputs.
            print("[Error]: Please provided two coordonates (0-2).")
            user_input = input("x, y: ")
            coordonates = user_input.split(',')

        # create the action the user provided.
        action = Action(int(coordonates[0]), int(coordonates[1]))

        # check if user provided right input coordonates.
        while board.get_current_game_state()[action.get_x()][action.get_y()] != ' ':

            # re-actualize user inputs.
            print("[Error]: Please provided two coordonates that are not already used (0-2).")
            user_input = input("x, y: ")
            coordonates = user_input.split(',')
            action = Action(int(coordonates[0]), int(coordonates[1]))

        # actualize the board state with the action.
        board = new_game_state(board, action)

        # if true, it means there is a winner.
        if board.has_game_ended():
            print(board.get_winner(), "won")
            break

        # if IA plays second, put its play on the board.
        if not ia_plays_first:

            # get the best move out of the board.
            action = min_max_algo.alpha_beta_search(board)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break
"""