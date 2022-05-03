import math
from board import *
from random import choice

#who_am_i represents the player the AI has been given
#returns a tuple containing first the chosen_column and second the score of this column for the iterations
def alpha_beta_search(board_state, depth, who_am_i, alpha=-math.inf, beta=math.inf, should_maximize=True):
    
    #Winning, loosing or draw conditions
    current_score = board_state.has_game_ended(who_am_i)
    if isinstance(current_score, int):
        #print("Origine : max_value : " + str(current_score))
        return (None,current_score)
    elif depth == 0 or current_score == 'Draw':
        return (None,0)
    
    #Setting possible action list and choosing whether we should minimize or maximize
    allowed_actions = board_state.get_allowed_actions()
    #should_maximize = who_am_i == board_state.current_player()
    print(should_maximize)
    
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
            child_score = alpha_beta_search(new_board_state, depth-1, who_am_i, alpha, beta, False)[1]
           
            #Set the new best value in case we have a better score
            if child_score > value:
                #print ("New max_value : " + str(value) +" at depth : "+ str(depth))
                if(depth == 3):
                    print("New max value : "+str(value))
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
            child_score = alpha_beta_search(new_board_state, depth-1, who_am_i, alpha, beta, True)[1]

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
        


class MinMaxAlgorithm:
    #who_am_i represents the player the AI has been given
    #returns a tuple containing first the chosen_column and second the score of this column for the iterations
    def alpha_beta_search(self, board_state, depth, who_am_i, alpha=-math.inf, beta=math.inf, should_maximize=True):
        
        #Winning, loosing or draw conditions
        current_score = board_state.has_game_ended(who_am_i)
        if isinstance(current_score, int):
            print("Origine : max_value : " + str(current_score))
            return (None,current_score)
        elif depth == 0 or current_score == 'Draw':
            return (None,0)
        
        #Setting possible action list and choosing whether we should minimize or maximize
        allowed_actions = board_state.get_allowed_actions()
        #should_maximize = who_am_i == board_state.current_player()
        print(should_maximize)
        
        if should_maximize:
            # initialize our value to -infinity.
            value = -math.inf
            # assign any colum in the allowed ones to initiate the variable that contains the best choice
            chosen_column = choice(allowed_actions)
            # iterate through all possible actions on the board.
            for allowed_action in allowed_actions:
                
                new_board_state = board_state.result(allowed_action)

                # get the maximum between the previous value and the minimized result of the board.
                child_score = self.alpha_beta_search(new_board_state, depth-1, who_am_i, alpha, beta, False)[1]
               
                #Set the new best value in case we have a better score
                if child_score >= value:
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
                
                new_board_state = board_state.result(allowed_action)

                # get the minimum between the previous value and the maximized result of the board.
                child_score = self.alpha_beta_search(new_board_state, depth-1, who_am_i, alpha, beta, True)[1]

                #Set the new worst value in case we have a better score
                if child_score <= value:
                    chosen_column = allowed_action
                    value = child_score
                    
                # assign our alpha as in the pseudocode.
                beta = min(beta, value)
                
                # in case our value is lesser than alpha, return it.
                if alpha >= beta:
                    break

                

            # return that value
            return (chosen_column,value)
            
"""
    def alpha_beta_search(self, board_state, depth, player):

        # let's see what moves return the best result.
        action = None

        # let's see if we should start by minimizing or maximizing.
        #should_minimize = board_state.current_player() == board_state.get_initial_player()

        # initialize our value to +/-infinity depending on should we maximize or minimize.
        #value = -math.inf if should_minimize else math.inf

        scored_actions = dict()
        # iterate through the possible actions of the board.
        
        
        # iterate through the possible actions of the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the score of the move depending on maximizing or minimizing.
            # this will get the score recursively, by trying to find the best move for the AI whilst still taking in
            # consideration the best move for the opponent.
            # This will either result in a win for the AI or a draw.
            
            
           
                action_score = self.max_value(board_state.result(allowed_action), player, -math.inf, math.inf, depth, 0)

                # depending on the result, store it.
                scored_actions[allowed_action]=action_score

           
        
        scored_actions = {key : val for key, val in scored_actions.items() if val == max(scored_actions.values())}
        print('possible actions : ')
        print(scored_actions)
        chosen_action = choice(list(scored_actions.keys()))
        print ('Chosen actions  : ' + str(chosen_action))

        return chosen_action
"""
def max_value(self, board_state, player, alpha, beta, depth, count):

            
        current_score = board_state.has_game_ended(player)
        if isinstance(current_score, int):
            print("Origine : max_value : " + str(current_score))
            return current_score
        elif count >= depth or current_score == 'Draw':
            return 0
        

        
        # initialize our value to -infinity.
        value = -math.inf

        # iterate through all possible actions on the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the maximum between the previous value and the minimized result of the board.
            value = max(value,self.min_value(board_state.result(allowed_action), player,alpha,beta,depth, count+1))

            # assign our alpha as in the pseudocode.
            alpha = max(alpha, value)
            
            # in case our value is lesser than alpha, return it.
            if alpha >= beta:
               break

            

        # return that value
        return value

def min_value(self, board_state, player, alpha, beta, depth, count):

        # check if someone has won in case the game has ended.

        current_score = board_state.has_game_ended(player)
        if isinstance(current_score, int):
            print("Origine : max_value : " + str(current_score))
            return current_score
        elif count >= depth or current_score == 'Draw':
            return 0
          
        


        # initialize our value to +infinity.
        value = math.inf

        # iterate through all possible actions on the board.
        for allowed_action in board_state.get_allowed_actions():

            # get the minimum between the previous value and the maximized result of the board.
            value = min(value, self.max_value(board_state.result(allowed_action), player,alpha,beta, depth, count +1))

            # assign our alpha as in the pseudocode.
            beta = min(beta, value)
            
            # in case our value is lesser than alpha, return it.
            if alpha >= beta:
                break

            

        # return that value
        return value
