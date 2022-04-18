import numpy as np


def initial_state():
    # returns a numpy array of the tic-tac-toe game.
    return np.array([[' '] * 3] * 3)


def is_int(number_as_str):
    try:
        int(number_as_str)
        return True
    except ValueError:
        return False
