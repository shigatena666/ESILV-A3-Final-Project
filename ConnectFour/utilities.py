from textwrap import wrap


def print_bitboard(bitboard):
    print('\n'.join([' '.join(wrap(line, 1)) for line in wrap(bitboard.__str__(), 12)]))

def print_encoded_bitboard(encoded_bitboard):

    encoded_bitboard = format_encoded_bitboard(encoded_bitboard)
    print('\n'.join([' '.join(wrap(line, 1)) for line in wrap(encoded_bitboard, 12)]))

def format_encoded_bitboard(encoded_bitboard):

    # format our encoded board for O as a 144 bits string.
    format_to_full_bits = format(int(bin(encoded_bitboard), 2), '{fill}{width}b'.format(width=144, fill=0))

    # get every 12 character so that instead of setting players in columns we can set them in rows.
    return ''.join([format_to_full_bits[i::12] for i in range(12)])