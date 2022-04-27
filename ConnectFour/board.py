from copy import deepcopy
from action import Action

import numpy as np

import utilities


class Board:

    # TODO: Replace O and X by consts.
    def __init__(self, board_state=None,first_player='X', rows=6, columns=12):

        # check if a board has been provided for copy.
        if board_state is not None:
            self.__first_player = board_state.get_initial_player()
            self.__array = deepcopy(board_state.get_current_game_state())
            self.__rows = board_state.get_rows()
            self.__columns = board_state.get_columns()
            self.__heights = board_state.get_heights()
            self.__counter = board_state.get_counter()
        else:
            # set the first player in the board.
            self.__first_player = first_player
            
            self.__counter = 0
            self.__heights = [0,0,0,0,0,0,0,0,0,0,0,0]

       

            # set how many rows and columns for later computation.
            self.__rows = rows
            self.__columns = columns
    
            # create an empty board of rows * columns.
            self.__array = deepcopy(utilities.initial_state(self.__columns, self.__rows))
        
        self.__second_player='O' if self.__first_player == 'X' else 'X'
        
    
    def get_counter(self):
        return self.__counter
    def get_heights(self):
        return self.__heights
    
    def get_array(self):
        return self.__array

    def get_initial_player(self):

        # get the char of the first player.
        return self.__first_player

    def get_current_game_state(self):

        # get the array of the game.
        return self.__array

    def get_rows(self):

        # get the amount of rows in the board.
        return self.__rows

    def get_columns(self):

        # get the amount of columns in the board.
        return self.__columns

    def current_player(self):
        
        
        return self.__first_player if self.__counter%2==0 else self.__second_player

    def get_allowed_actions(self):

        # prepare an array of actions.
        actions = []

        # iterate through all elements.
        for column in range (0, self.__columns):
            if self.__heights[column] != self.__rows:
                actions.append(column)

        # return our array of actions.
        return np.array(actions)

    def set(self, column):

        # set the slot to the player who needs to play.
        self.__array[self.__rows - 1- self.__heights[column]][column] = self.current_player()
        self.__heights[column]+=1
        self.__counter = self.__counter + 1

    def result(self, column):
        
        if self.__heights[column] == 6:
            raise Exception('The slot is already occupied, this should never happen.')
        
        # create a deep-copy of the board.
        
        new_board = Board(self)

        # set the actions and return the new board.
        new_board.set(column)

        # return the new board.
        return new_board

    def get_winner(self):

        # let's look into the lines.
        
        for line in range(self.__rows):
            for i in range (0, self.__columns -3):
                
                # create a set for the line.
                line_set = set(self.__array[line][i:i+4])
                
    
                # if the length is 1 and the first character isn't a space then it means someone won.
                if len(line_set) == 1 and ' ' not in line_set:
                    return self.__array[line][i]

        # let's look into the columns, use the property of a matrix to make it easier.
        transpose = np.transpose(self.__array)
        
        
        # iterate through the columns (which are now lines).
        for line in range(self.__columns):
            for i in range (0, self.__rows -3):
                # create a set for the transpose.
                transpose_set = set(transpose[line][i:i+4])
                
                
                # if the length is 1 and the first character isn't a space then it means someone won.
                if len(transpose_set) == 1 and ' ' not in transpose_set:
                    return transpose[line][i]
        """
        # check for diagonals and create our sets.
        descending_diagonal_set = set([self.__array[i][i] for i in range(len(self.__array))])
        ascending_diagonal_set = set([self.__array[i][len(self.__array[i]) - 1 - i]
                                      for i in range(0, len(self.__array))])

        # return the player in the diagonal that has won if there is any.
        if len(descending_diagonal_set) == 1 and ' ' not in descending_diagonal_set:
            return 'X' if self.__array[0][0] == 'X' else 'O'

        # same thing.
        if len(ascending_diagonal_set) == 1 and ' ' not in ascending_diagonal_set:
            return 'X' if self.__array[0][2] == 'X' else 'O'
        """
        # check for equality.
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

        # let's check if the board is full or if there is a winner.
        if (self.__array != utilities.initial_state(self.__rows,
                                                    self.__columns)).all() or self.get_winner() is not None:
            return True

        # else return False.
        return False

    def __str__(self):
        st = '_________________________\n'
        for i in range(len(self.__array)):
            st += '|'
            st += '|'.join(self.__array[i])
            st += '|\n'
        st += '_________________________'
        return st
