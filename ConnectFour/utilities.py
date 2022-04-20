from textwrap import wrap


def format_bitboard_to_str(bitboard_encoding):
    return format(int(str(bitboard_encoding), 2), '{fill}{width}b'.format(width=132, fill=0))


def print_bitboard(bitboard_encoding):
    print(bitboard_encoding)
    bitboard_as_str = format_bitboard_to_str(bitboard_encoding)
    print(bitboard_as_str)
    print('\n'.join(['  '.join(wrap(line, 1)) for line in wrap(bitboard_as_str, 12)]))
    # print('\n'.join(['  '.join(wrap(line, 1)) for line in wrap('.' * 12 * 11, 12)]))
