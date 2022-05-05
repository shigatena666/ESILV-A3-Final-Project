from min_max_algorithm import *
from board import *
from utilities import *
import math
from random import choice

#who_am_i represents the player the AI has been given
#returns a tuple containing first the chosen_column and second the score of this column for the iterations
def alpha_beta_search(board_state, depth, alpha=-math.inf, beta=math.inf, should_maximize=True):
    
    #Winning, loosing or draw conditions
    board_status = board_state.has_game_ended()
    if (board_status):
        if(board_status == K_PLAYER):
            return(None,10)
        elif board_status != 'Draw':
            return(None,-10)
    elif depth == 0 or board_status == 'Draw':
        return (None,0)
    
    #Setting possible action list and choosing whether we should minimize or maximize
    allowed_actions = board_state.get_allowed_actions()
    #should_maximize = who_am_i == board_state.current_player()
    #print(should_maximize)
    
    if should_maximize:
        # initialize our value to -infinity.
        value = -math.inf
        # assign any colum in the allowed ones to initiate the variable that contains the best choice
        chosen_column = choice(allowed_actions)
        # iterate through all possible actions on the board.
        for allowed_action in allowed_actions:
            new_board_state = copy(board_state)
            new_board_state = new_board_state.result(allowed_action)

            # get the maximum between the previous value and the minimized result of the board.
            child_score = alpha_beta_search(new_board_state, depth-1, alpha, beta, False)[1]
           
            #Set the new best value in case we have a better score
            if child_score > value:
                #print ("New max_value : " + str(value) +" at depth : "+ str(depth))

                chosen_column = allowed_action
                value = child_score
            
            # assign our alpha as in the pseudocode.
            alpha = max(alpha, value)
            
            # in case our value is lesser than alpha, return it.
            if alpha >= beta:
                break;
              
        return (chosen_column,value)

            

        # return that value
        
        
    else:
        # initialize our value to +infinity.
        value = math.inf
        # assign any colum in the allowed ones to initiate the variable that contains the best choice
        chosen_column = choice(allowed_actions)

        # iterate through all possible actions on the board.
        for allowed_action in allowed_actions:
            
            new_board_state = copy(board_state)
            new_board_state = new_board_state.result(allowed_action)

            # get the minimum between the previous value and the maximized result of the board.
            child_score = alpha_beta_search(new_board_state, depth-1, alpha, beta, True)[1]

            #Set the new worst value in case we have a better score
            if child_score < value:
                #print ("New min_value : " + str(value) + " at depth : "+ str(depth))
                chosen_column = allowed_action
                value = child_score
                
            # assign our alpha as in the pseudocode.
            beta = min(beta, value)
            
            # in case our value is lesser than alpha, return it.
            if alpha >= beta:
                break

            

        # return that value
        return (chosen_column,value)
        


def new_game_state(board_state, action_move):
    # warning, this will not directly modify the board_state.

    # update our board with that action.
    board_state = board_state.result(action_move)

    # re-show the game after the play.
    print(board_state)

    # check if there is a winner after that play.
    return board_state


if __name__ == "__main__":


    
    
    # instantiate our board and algorithm.
    rows = 6
    columns = 12
    depth = 5


    board = Board()
    #min_max_algo=MinMaxAlgorithm()
    #possibilities = min_max_algo.alpha_beta_search(board, 3)
    




    # get who should play first, IA or player ?
    ia_plays_first = bool(int(input('IA should play first ? (Answer 1 if yes, 0 otherwise)')))
    K_PLAYER = 'X' if ia_plays_first else 'O'


    # show the initial game state.
    print(board)

    # start our game.
    while True:

        # if IA plays first, put its first play onto the board.
        if ia_plays_first:

            # get the best move out of the board.
            action = alpha_beta_search(board, depth)
            print(action)
            # actualize the board state.
            board = new_game_state(board, action[0])

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break

        # ask the user to play and set it inside the board.

        coordonates = int(input("x: "))


        # check if user provided right input types.
        while not coordonates < 12 and coordonates >= 0:

            # re-actualize user inputs.

            print("[Error]: Please provide a valid number.")
            coordonates = int(input("x: "))


        # check if user provided right input coordonates.
        while coordonates not in board.get_allowed_actions():

            # re-actualize user inputs.
            print("[Error]: Please provided a non-full column.")
            coordonates = input("x:")
            coordonates = int(coordonates)


        # actualize the board state with the action.
        board = new_game_state(board, coordonates)

        # if true, it means there is a winner.
        if board.has_game_ended():
            print(board.get_winner(), "won")
            break

        # if IA plays second, put its play on the board.
        if not ia_plays_first:

            # get the best move out of the board.
            action = alpha_beta_search(board, depth)
            print(action)
            # actualize the board state.
            board = new_game_state(board, action[0])

            # if true, it means there is a winner.
            if board.has_game_ended():
                print(board.get_winner(), "won")
                break
