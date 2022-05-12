from min_max_algorithm import *
import timeit


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

    # ask the user the input.
    user_input = input('IA should play first ? (Answer 1 if yes, 0 otherwise)')

    # validate it as long as it's not a char.
    while not user_input.isdigit():

        # re-actualize user inputs.
        print("[Error]: Please provide a valid char number.")
        user_input = input("You should enter a number that is 0 or 1: ")

    # get who should play first, IA or player ?
    ia_plays_first = bool(int(user_input))

    # show the initial game state.
    print(board)

    # start our game.
    while True:

        # if IA plays first, put its first play onto the board.
        if ia_plays_first:

            # retrieve the start time.
            start = timeit.default_timer()

            # get the best move out of the board.
            alpha_beta_result = min_max_algo.alpha_beta_search(board, depth)

            # retrieve the finished action time.
            stop = timeit.default_timer()

            # print the time to the user.
            print('Time (s): ', stop - start)

            # retrieve the action from the result.
            action = alpha_beta_result[0]

            print(alpha_beta_result[0] + 1)

            # actualize the board state with the action.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break

        # ask the user to play and set it inside the board.
        user_input = input("x: ")

        # validate the user input.
        while not user_input.isdigit():

            # re-actualize user inputs.
            print("[Error]: Please provide a valid char number.")
            user_input = input("x: ")

        coordonates = int(user_input)

        # check if user provided right input types.
        while not (1 <= coordonates <= columns):

            # re-actualize user inputs.
            print("[Error]: Please provide a valid number.")
            coordonates = int(input("x: "))

        # check if user provided right input coordonates.
        while coordonates - 1 not in board.get_allowed_actions():

            # re-actualize user inputs.
            print("[Error]: Please provided a non-full column.")
            coordonates = int(input("x:"))

        # actualize the board state with the action in the column. -1 because player plays with 1-12.
        board = new_game_state(board, coordonates - 1)

        # if true, it means there is a winner.
        if board.has_game_ended():
            print(board.get_winner(), "won")
            break

        # if IA plays second, put its play on the board.
        if not ia_plays_first:

            # retrieve the start time.
            start = timeit.default_timer()

            # get the best move out of the board.
            alpha_beta_result = min_max_algo.alpha_beta_search(board, depth)

            # retrieve the finished action time.
            stop = timeit.default_timer()

            # print the time to the user.
            print('Time (s): ', stop - start)

            # retrieve the action from the result.
            action = alpha_beta_result[0]

            print(alpha_beta_result[0] + 1)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break
