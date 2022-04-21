class BitBoard:

    def __init__(self):

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

        # get the boards for X and O.
        return self.__encoded_boards

    def set(self, column_index):

        # reverse column_index so that when we play on 0, we play on the left side of the board.
        column_index = abs(column_index - 11)

        # shift bits to the left
        move = 1 << self.__height_indexes[column_index]

        # add one to our height indexes so that even if the next player plays into the same column, its pawn goes
        # above.
        self.__height_indexes[column_index] += 1

        # set the board depending on the current player.
        self.__encoded_boards[self.current_player()] ^= move

        # store the column where we made our move inside our list.
        self.__moves.append(column_index)

        # increment our counter so that the next player will be playing.
        self.__counter += 1

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
        self.__encoded_boards[self.current_player()] ^= move

    @staticmethod
    def get_winner(bitboard):

        # there is a difference of 1 vertically.
        # there is a difference of 12 horizontally.
        # there is a difference of either 13 or 11 vertically.
        row_column_diagonal_numbers = [1, 12, 13, 11]

        # iterate through our "magic numbers".
        for row_column_diagonal_number in row_column_diagonal_numbers:

            # get the current bitboard with the shifted one.
            # this will prevent us to make more computation and multiply by 3.
            shifted_bitboard = bitboard & (bitboard >> row_column_diagonal_number)

            # TODO: understand this better.
            if shifted_bitboard & (shifted_bitboard >> (2 * row_column_diagonal_number)) != 0:
                return True

        # else return false.
        return False

    def get_allowed_actions(self):

        # prepare our list of moves.
        moves = []

        # create a mask for the additional column.
        mask = 0b100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000_100000000000

        # iterate through our columns.
        for column in range(0, 12):

            # the bit isn't supposed to land in the additional column, which will mark it as full (1).
            # get the ones that aren't full after the move (0).
            if mask & (1 << self.__height_indexes[column]) == 0:
                moves.append(column)

        # return our list of move.
        return moves

    def __str__(self):

        # format our encoded board for O as a 144 bits string.
        format_to_full_bits = format(int(bin(self.__encoded_boards[0]), 2), '{fill}{width}b'.format(width=144, fill=0))

        # get every 12 character so that instead of setting players in columns we can set them in rows.
        return ''.join([format_to_full_bits[i::12] for i in range(12)])
