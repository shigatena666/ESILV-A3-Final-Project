from board import Board


class TranspositionTables:

    def __init__(self):
        self.__cache = {}

    @staticmethod
    def __compute_hash(board_state: Board):

        # compute the hash of the numpy array and return it. Takes less memory than storing the array.
        return hash(str(board_state.get_current_game_state()))

    def add(self, board_state: Board, board_score):

        # get the hash of the numpy array.
        board_hash = self.__compute_hash(board_state)

        # store it inside our cache dictionary.
        self.__cache[board_hash] = board_score

    def get(self, board_state: Board):

        # retrieve the hash from the board numpy array.
        board_hash = self.__compute_hash(board_state)

        # get the score associated to the hash of the numpy array.
        return self.__cache[board_hash] if board_hash in self.__cache else None



