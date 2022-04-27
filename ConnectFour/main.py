from min_max_algorithm import *
from utilities import *



def new_game_state(board_state, action_move):
    # warning, this will not directly modify the board_state.

    # update our board with that action.
    board_state = board_state.set(action)

    # re-show the game after the play.
    print_bitboard(board_state)

    # check if there is a winner after that play.
    return board_state
"""

if __name__ == "__main__":

<<<<<<< Updated upstream
    # instantiate our board and algorithm.
    board = BitBoard()
=======
    
    
    # instantiate our board and algorithm.
    rows = 6
    columns = 12
    board = Board()
>>>>>>> Stashed changes
    min_max_algo = MinMaxAlgorithm()


    # get who should play first, IA or player ?
    ia_plays_first = bool(int(input('IA should play first ? (Answer 1 if yes, 0 otherwise)')))

    # show the initial game state.
    print_bitboard(board)

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
<<<<<<< Updated upstream
        coordonates = input("x:")
        coordonates = int(coordonates)
=======
        coordonates = int(input("x: "))
>>>>>>> Stashed changes

        # check if user provided right input types.
        while not coordonates < 12 and coordonates > 0:

            # re-actualize user inputs.
<<<<<<< Updated upstream
            print("[Error]: Please provided a column.")
            coordonates = input("x:")
            coordonates = int(coordonates)



        # check if user provided right input coordonates.
        while coordonates not in board.get_allowed_actions():

            # re-actualize user inputs.
            print("[Error]: Please provided a non-full column.")
            coordonates = input("x:")
            coordonates = int(coordonates)
=======
            print("[Error]: Please provided a valid number")
            coordonates = int(input("x: "))
            

        

        # check if user provided right input coordonates.
        while board.get_heights()[coordonates] >= 6:

            # re-actualize user inputs.
            print("[Error]: Please provided two coordonates that are not already used (0-2).")
            coordonates = int(input("x: "))
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
"""

if __name__ == '__main__':


    bitboard = BitBoard()
    # print_bitboard(bitboard.get_encoded_boards()[0])

    bitboard.set(0)
    bitboard.set(2)
    bitboard.set(4)
    bitboard.set(5)
    bitboard.set(1)

    print_bitboard(bitboard)

    min_max_algo = MinMaxAlgorithm()
    column = min_max_algo.alpha_beta_search(bitboard)
    print(column)

    print(' ')

    print_bitboard(bitboard)

    print(bitboard.get_allowed_actions())
    print(bitboard.get_winner())
=======
            
    
>>>>>>> Stashed changes
