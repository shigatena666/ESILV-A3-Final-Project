from min_max_algorithm import MinMaxAlgorithm
from board import Board
from action import Action


def new_game_state(board_state: Board, action_move: Action):

    # update our board with that action.
    board_state = board_state.result(action_move)

    # re-show the game after the play.
    print(board_state)

    # check if there is a winner after that play.
    return board_state


if __name__ == "__main__":

    # instantiate our board and algorithm.
    board = Board()
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
            action = min_max_algo.minimize_or_maximize(board)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.winner(), "won")
                break

        # ask the user to play and set it inside the board.
        user_input = input("x, y: ")
        coordonates = user_input.split(',')
        action = Action(int(coordonates[0]), int(coordonates[1]))

        # TODO: Add a try except there to see if user provided right input.
        # actualize the board state.
        board = new_game_state(board, action)

        # if true, it means there is a winner.
        if board.has_game_ended():
            print(board.winner(), "won")
            break

        # if IA plays second, put its play on the board.
        if not ia_plays_first:

            # get the best move out of the board.
            action = min_max_algo.minimize_or_maximize(board)

            # actualize the board state.
            board = new_game_state(board, action)

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.winner(), "won")
                break