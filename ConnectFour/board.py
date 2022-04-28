from copy import deepcopy
from scipy.signal import convolve2d

import numpy as np

import utilities

# define our consts.

# these are our winning conditions.
HORIZONTAL_KERNEL = np.array([[1, 1, 1, 1]])
VERTICAL_KERNEL = np.transpose(HORIZONTAL_KERNEL)
ASCENDING_DIAGONAL_KERNEL = np.eye(4, dtype=np.uint8)
DESCENDING_DIAGONAL_KERNEL = np.fliplr(ASCENDING_DIAGONAL_KERNEL)

# this part will be used for winning detection.
# we will use convolution matrixes, which will result in the sum of the surrounding el
# multiplied by the element at the same position (index) in the kernel.
# the kernels will be what we defined below, and we will apply that on our 2D board.
# if any 4 is detected inside the convolution matrix, this means we have a winner.
DETECTION_KERNELS = [HORIZONTAL_KERNEL,
                     VERTICAL_KERNEL,
                     ASCENDING_DIAGONAL_KERNEL,
                     DESCENDING_DIAGONAL_KERNEL]


class Board:

    # TODO: Replace O and X by consts.
    def __init__(self, board_state=None, first_player='X', rows=6, columns=12):

        # check if a board has been provided for copy.
        if board_state is not None:

            # set our attributes for the copy.
            self.__first_player = board_state.get_initial_player()
            self.__array = deepcopy(board_state.get_current_game_state())
            self.__rows = board_state.get_rows()
            self.__columns = board_state.get_columns()
            self.__heights = board_state.get_heights()
            self.__counter = board_state.get_counter()

        else:

            # set the first player in the board.
            self.__first_player = first_player

            self.__counter = 0
            self.__heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # set how many rows and columns for later computation.
            self.__rows = rows
            self.__columns = columns

            # create an empty board of rows * columns.
            self.__array = deepcopy(utilities.initial_state(self.__rows, self.__columns))

        self.__second_player = 'O' if self.__first_player == 'X' else 'X'

    def get_counter(self):
        return self.__counter

    def get_heights(self):
        return self.__heights

    def get_array(self):
        return self.__array

    def get_initial_player(self):

        # get the char of the first player.
        return self.__first_player

    def get_current_game_state(self):

        # get the array of the game.
        return self.__array

    def get_rows(self):

        # get the amount of rows in the board.
        return self.__rows

    def get_columns(self):

        # get the amount of columns in the board.
        return self.__columns

    def current_player(self):

        return self.__first_player if self.__counter % 2 == 0 else self.__second_player

    def get_allowed_actions(self):

        # prepare an array of actions.
        actions = []

        # iterate through all elements.
        for column in range(0, self.__columns):

            # check if we haven't gone through the maximum amount of element per column (which is our rows)
            if self.__heights[column] < self.__rows:
                actions.append(column)

        # return our array of actions.
        return np.array(actions)

    def set(self, column):

        # set the slot to the player who needs to play.
        self.__array[self.__rows - 1 - self.__heights[column]][column] = self.current_player()
        self.__heights[column] += 1
        self.__counter += 1

    def result(self, column):

        if self.__heights[column] == 6:
            raise Exception('The slot is already occupied, this should never happen.')

        # create a deep-copy of the board.

        new_board = Board(self)

        # set the actions and return the new board.
        new_board.set(column)

        # return the new board.
        return new_board

    def get_winner(self):

        # initialize our player matrixes.
        x_matrix = []
        o_matrix = []

        # fill the right 2D matrix depending on whether it's an X or O.
        for row in self.__array:

            # fill with one more dimension.
            x_matrix.append([])
            o_matrix.append([])

            # iterate through our elements in the row.
            for element in row:
                x_matrix[len(x_matrix) - 1].append(1 if element == 'X' else 0)
                o_matrix[len(o_matrix) - 1].append(1 if element == 'O' else 0)

        # iterate through our kernels.
        for kernel in DETECTION_KERNELS:

            # check in our 2D boards if any element of the convolution matrix is equal to 4 (our winning condition).
            if (convolve2d(x_matrix, kernel, mode="valid") == 4).any():
                return 'X'
            elif (convolve2d(o_matrix, kernel, mode="valid") == 4).any():
                return 'O'

        return None

    def get_winner_as_int(self):

        # get the winner from the board.
        who_won = self.get_winner()

        # if X won, return 1
        if who_won == 'X':
            return 1

        # if O won, return -1.
        elif who_won == 'O':
            return -1

        # return 0 if it's a draw.
        else:
            return 0

    def has_game_ended(self):

        # let's check if the board is full or if there is a winner.
        if (self.__array != utilities.initial_state(self.__rows,
                                                    self.__columns)).all() or self.get_winner() is not None:
            return True

        # else return False.
        return False

    def __str__(self):
        st = '_________________________\n'
        for i in range(len(self.__array)):
            st += '|'
            st += '|'.join(self.__array[i])
            st += '|\n'
        st += '_________________________'
        return st
