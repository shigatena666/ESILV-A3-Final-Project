class BitBoard:

    def __init__(self):

        # index 0 will be for the player X's board.
        # index 1 will be for the player O's board.
        self.__encoded_boards = [
            0b000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000,
            0b000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000
        ]

        # index of where we can insert our player's character.
        self.__height_indexes = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]

        # used to know which player should play the next move.
        self.__counter = 0

        # used so that we can 'undo' the moves. This will slightly increase the speed of our algorithm as we won't make
        # any copy of X and O board, only making moves and undo them.
        self.__moves = []

    def current_player(self):

        # return 0 if self.__counter % 2 == 0 else 1
        # should be slightly faster than the version above. Using the least significant bit (LSB) [rightmost bit] to get
        # whether it's odd (1) or even (0).
        # Example:  0 = 0000 : LSB is 0 => even
        #           1 = 0001 : LSB is 1 => odd
        #           2 = 0010 : LSB is 0 => even
        #           3 = 0011 : LSB is 1 => even
        return 0 if self.__counter & 1 == 0 else 1

    def get_encoded_boards(self):
        return self.__encoded_boards

    def set(self, column_index):
        move = 1 << self.__height_indexes[column_index]

        # add one to our height indexes so that even if the next player plays into the same column, its pawn goes
        # above.
        self.__height_indexes[column_index] += 1

        # set the board depending on the current player.
        self.__encoded_boards[self.current_player()] = move

        # store the column where we made our move inside our list.
        self.__moves.append(column_index)

        # increment our counter so that the next player will be playing.
        self.__counter += 1
