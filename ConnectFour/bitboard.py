class BitBoard:

    def __init__(self, first_player='X'):

        # set the first player in the board.
        self.__first_player = first_player

        # index 0 will be for the player X's board.
        # index 1 will be for the player O's board.
        self.__encoded_boards = [
            0b000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000,
            0b000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000_000000000000
        ]

        # index of where we can insert our player's character.
        self.__height_indexes = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132]

        # used to know which player should play the next move.
        self.__counter = 0

        # used so that we can 'undo' the moves. This will slightly increase the speed of our algorithm as we won't make
        # any copy of X and O board, only making moves and undo them.
        self.__moves = []

    def get_current_player(self):

        # return 0 if self.__counter % 2 == 0 else 1
        # should be slightly faster than the version above. Using the least significant bit (LSB) [rightmost bit] to get
        # whether it's odd (1) or even (0).
        # Example:  0 = 0000 : LSB is 0 => even
        #           1 = 0001 : LSB is 1 => odd
        #           2 = 0010 : LSB is 0 => even
        #           3 = 0011 : LSB is 1 => even
        return 0 if self.__counter & 1 == 0 else 1

    def get_previous_player(self):

        # return the opposite of current player.
        return 0 if self.get_current_player() == 1 else 1

    def get_initial_player(self):
        return self.__first_player

    def get_encoded_boards(self):

        # get the boards for X and O.
        return self.__encoded_boards

    def get_allowed_actions(self):

        # prepare our list of moves.
        moves = []

        # create a mask for the additional column.
        mask = 0b100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000

        # iterate through our columns.
        for column in range(0, 12):

            # the bit isn't supposed to land in the additional column, which will mark it as full if it lands in (1).
            # get the ones that aren't full after the move (0).
            # since we reversed the set method with abs, the last height index is used for the first column.
            # we need to reverse it as well in order to work correctly.
            if mask & (1 << self.__height_indexes[11 - column]) == 0:
                moves.append(column)

        # return our list of move.
        return moves

    def set(self, column_index):

        # reverse column_index so that when we play on 0, we play on the left side of the board.
        column_index = 11 - column_index

        # shift bits to the left
        move = 1 << self.__height_indexes[column_index]

        # add one to our height indexes so that even if the next player plays into the same column, its pawn goes
        # above.
        self.__height_indexes[column_index] += 1

        # set the board depending on the current player.
        self.__encoded_boards[self.get_current_player()] ^= move

        # store the column where we made our move inside our list.
        self.__moves.append(column_index)

        # increment our counter so that the next player will be playing.
        self.__counter += 1

        return self

    def unset(self):

        # decrease counter by 1 because it got increased at the last move.
        self.__counter -= 1

        # get the last played column for the last move.
        last_played_column = self.__moves[self.__counter]

        # remove one to our height indexes because the next move will be removed and not added, we need the last one.
        self.__height_indexes[last_played_column] -= 1

        # shift bits to the left
        move = 1 << self.__height_indexes[last_played_column]

        # set the board depending on the current player.
        self.__encoded_boards[self.get_current_player()] ^= move

    def get_winner(self):

        # there is a difference of 1 vertically.
        # there is a difference of 12 horizontally.
        # there is a difference of either 13 or 11 diagonaly (normal and reversed).
        row_column_diagonal_numbers = [1, 12, 13, 11]

        # iterate through our "magic numbers".
        for row_column_diagonal_number in row_column_diagonal_numbers:

            # check if when shifting at least one bit will be in common. If yes it means that they are aligned.
            # Example   : 111100000000 (magic number will be one, thus shift by multiple of 1.)
            # >> 1      : 011110000000
            # >> 2      : 001111000000
            # >> 3      : 000111100000
            # &1,2,3    : 000100000000
            if self.__encoded_boards[0] & (self.__encoded_boards[0] >> row_column_diagonal_number) \
                    & (self.__encoded_boards[0] >> (2 * row_column_diagonal_number)) \
                    & (self.__encoded_boards[0] >> (3 * row_column_diagonal_number)) != 0:
                return 'X'

            elif self.__encoded_boards[1] & (self.__encoded_boards[1] >> row_column_diagonal_number) \
                    & (self.__encoded_boards[1] >> (2 * row_column_diagonal_number)) \
                    & (self.__encoded_boards[1] >> (3 * row_column_diagonal_number)) != 0:
                return 'O'

        # else return None.
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

        # create the combination of the two separate boards as a string.
        board = bin(self.__encoded_boards[0] | self.__encoded_boards[1])

        # let's check if the board is full (all the bits are 1) or if there is a winner.
        if (board == '1' * len(board)) or self.get_winner() is not None:
            return True

        # else return False.
        return False

    def __str__(self):

        # format our encoded board for X as a 144 bits string.
        format_to_full_bits_X = format(int(bin(self.__encoded_boards[0]), 2),
                                       '{fill}{width}b'.format(width=144, fill=0))

        # format our encoded board for O as a 144 bits string.
        format_to_full_bits_O = format(int(bin(self.__encoded_boards[1]), 2),
                                       '{fill}{width}b'.format(width=144, fill=0))

        # prepare our string as a list.
        format_to_board = ''

        for i in range(0, len(format_to_full_bits_X)):

            # if X's bit is 0 and O's bit is 1 then we put the character for O.
            if format_to_full_bits_X[i] == '0' and format_to_full_bits_O[i] == '1':
                format_to_board += 'O'

            # as opposite, put X.
            elif format_to_full_bits_X[i] == '1' and format_to_full_bits_O[i] == '0':
                format_to_board += 'X'

            else:
                format_to_board += '.'

        # get every 12 character so that instead of setting players in columns we can set them in rows.
        return ''.join([format_to_board[i::12] for i in range(12)])
