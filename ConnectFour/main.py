from bitboard import *
from utilities import *

if __name__ == '__main__':
    bitboard = BitBoard()
    # print_bitboard(bitboard.get_encoded_boards()[0])

    bitboard.set(0)
    bitboard.set(1)

    bitboard.set(0)

    print_bitboard(bitboard)

    print(bitboard.get_allowed_actions())
    print(bitboard.get_winner())
