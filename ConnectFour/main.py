from bitboard import *
from utilities import *

if __name__ == '__main__':
    bitboard = BitBoard()
    print_bitboard(bitboard.get_encoded_boards()[0])
    bitboard.set(1)
    print(' ')
    print_bitboard(bitboard.get_encoded_boards()[0])
