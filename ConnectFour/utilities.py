from textwrap import wrap


def print_bitboard(bitboard):
    print('\n'.join([' '.join(wrap(line, 1)) for line in wrap(bitboard.__str__(), 12)]))