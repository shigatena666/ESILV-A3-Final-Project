from min_max_algorithm import *
from board import *


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
    
    board = board.result(0)
    board = board.result(0)
    board = board.result(0)
    board = board.result(0)
    board = board.result(0)
    board = board.result(0)
    board = board.result(2)
    board = board.result(1)
    board = board.result(1)
    board = board.result(1)
    board = board.result(1)
    board = board.result(1)
    board = board.result(1)
    board = board.result(2)
    board = board.result(2)
    board = board.result(2)
    board = board.result(2)
    board = board.result(2)
    board = board.result(3)
    board = board.result(3)
    board = board.result(3)
    board = board.result(3)
    board = board.result(3)
    board = board.result(3)
    board = board.result(4)
    board = board.result(4)
    board = board.result(4)
    board = board.result(4)
    board = board.result(4)
    board = board.result(4)
    board = board.result(6)
    board = board.result(5)
    board = board.result(5)
    board = board.result(5)
    board = board.result(5)
    board = board.result(5)
    board = board.result(5)
    board = board.result(6)
    board = board.result(6)
    board = board.result(6)
    board = board.result(6)
    board = board.result(6)
    board = board.result(7)
    board = board.result(7)
    board = board.result(7)
    board = board.result(7)
    board = board.result(7)
    board = board.result(7)
    board = board.result(8)
    board = board.result(8)
    board = board.result(8)
    board = board.result(8)
    board = board.result(8)








    print(board)

    min_max_algo = MinMaxAlgorithm()
    column = min_max_algo.alpha_beta_search(board)
    board = board.result(column)

    print(board)
    print(board.get_winner())
    print(board.get_allowed_actions())
    print(board.has_game_ended())


    """
       
    # instantiate our board and algorithm.
    rows = 6
    columns = 12
    board = Board()
    print(board.has_game_ended())
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

        coordonates = int(input("x: "))


        # check if user provided right input types.
        while not coordonates < 12 and coordonates >= 0:

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
            action = min_max_algo.alpha_beta_search(board)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break
            """