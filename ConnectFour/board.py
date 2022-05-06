from copy import deepcopy, copy
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

    def __init__(self, first_player='X', rows=6, columns=12, board_state=None):

        # check if a board has been provided for copy.
        if board_state is not None:

            # set our attributes for the copy.
            self.__player_char = board_state.get_player_char()
            self.__array = deepcopy(board_state.get_current_game_state())
            self.__rows = board_state.get_rows()
            self.__columns = board_state.get_columns()
            self.__heights = copy(board_state.get_heights())
            self.__counter = board_state.get_counter()
            self.__winner = board_state.get_winner()

        else:

            # set the first player in the board.
            self.__player_char = first_player

            self.__counter = 0
            self.__heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # set how many rows and columns for later computation.
            self.__rows = rows
            self.__columns = columns

            # create an empty board of rows * columns.
            self.__array = deepcopy(utilities.initial_state(self.__rows, self.__columns))

            # initialize our winner. This will cache it as it takes some time to process.
            self.__winner = None

        self.__ia_char = 'O' if self.__player_char == 'X' else 'X'

    def get_counter(self):
        return self.__counter

    def get_heights(self):
        return self.__heights

    def get_array(self):
        return self.__array

    def get_winner(self):
        return self.__winner

    def get_player_char(self):

        # get the char of the first player.
        return self.__player_char

    def get_ia_char(self):

        # get the char of the IA.
        return self.__ia_char

    def get_current_game_state(self):

        # get the array of the game.
        return self.__array

    def get_rows(self):

        # get the amount of rows in the board.
        return self.__rows

    def get_columns(self):

        # get the amount of columns in the board.
        return self.__columns

    def get_current_player_char(self):

        return self.__player_char if self.__counter % 2 == 0 else self.__ia_char

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

    def __set(self, column):

        # set the slot to the player who needs to play.
        self.__array[self.__rows - 1 - self.__heights[column]][column] = self.get_current_player_char()
        self.__heights[column] += 1
        self.__counter += 1

    def result(self, column):

        if self.__heights[column] == 6:
            raise Exception('The slot is already occupied, this should never happen.')

        # create a deep-copy of the board.

        new_board = Board(self.__player_char, self.__rows, self.__columns, self)

        # set the actions and return the new board.
        new_board.__set(column)

        # return the new board.
        return new_board

    def __find_winner(self):

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

        # retrieve the cached winner, if X won, return 1.
        if self.__winner == self.get_player_char():
            return 1

        # if O won, return -1.
        elif self.__winner == self.get_ia_char():
            return -1

        # else it's a draw, return 0.
        else:
            return 0

    def has_game_ended(self):

        # first check for a winner:
        winner = self.__find_winner()

        # cache the winner to prevent performances loss.
        self.__winner = winner

        # let's check if the board is full or if there is a winner.
        if winner is not None \
                or (self.__array != utilities.initial_state(self.__rows, self.__columns)).all()\
                or self.__counter >= 42:
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
