import sys
from random import randint

from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.result import Connect4Result
from games.connect4.state import Connect4State
from games.state import State


class MinimaxConnect4Player(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    '''
    This heuristic will simply count the maximum number of consecutive pieces that the player has
    It's not a great heuristic as it doesn't take into consideration a defensive approach
    '''

    def __heuristic(self, state: Connect4State):
        grid = state.get_grid()
        longest = 0

        # check each line
        for row in range(0, state.get_num_rows()):
            seq = 0
            for col in range(0, state.get_num_cols()):
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > longest:
                        longest = seq
                    seq = 0

            if seq > longest:
                longest = seq

    
        # check each upward diagonal
        for row in range(3, state.get_num_rows()):
            for col in range(0, state.get_num_cols() - 3):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 2][col + 2] == self.get_current_pos() else 0)

                seq2 = (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 2][col + 2] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 3][col + 3] == self.get_current_pos() else 0)

                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        # check each downward diagonal
        for row in range(0, state.get_num_rows() - 3):
            for col in range(0, state.get_num_cols() - 3):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 2][col + 2] == self.get_current_pos() else 0)

                seq2 = (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 2][col + 2] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 3][col + 3] == self.get_current_pos() else 0)

                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        return longest

    """Implementation of minimax search (recursive, with alpha/beta pruning) :param state: the state for which the 
    search should be made :param depth: maximum depth of the search :param alpha: to optimize the search :param beta: 
    to optimize the search :param is_initial_node: if true, the function will return the action with max ev, 
    otherwise it return the max ev (ev = expected value) """

    def minimax(self, state: Connect4State, depth: int, alpha: int = -sys.maxsize, beta: int = sys.maxsize,
                is_initial_node: bool = True):

        
        #grid = state.get_grid()
        
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_finished():
            return {
                Connect4Result.WIN: 5,
                Connect4Result.LOOSE: -5,
                Connect4Result.DRAW: 0
            }[state.get_result(self.get_current_pos())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.__heuristic(state)

        # if we are the acting player
        if self.get_current_pos() == state.get_acting_player():
            # very small integer
            value = -sys.maxsize
            selected_pos = -1

            for pos in range(0, state.get_num_cols()):
                linha = randint(0, state.get_num_rows() - 1)
                action = Connect4Action(pos, linha)
                if state.validate_action(action):
                    previous_a = value
                    next_state = state.clone()
                    next_state.play(action)
                    value = max(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                    alpha = max(alpha, value)

                    if value >= previous_a:
                        selected_pos = pos
                    if alpha >= beta:
                        break

            if is_initial_node:
                return selected_pos
            return value
        # if it is the opponent's turn
        else:
            # very big integer
            value = sys.maxsize
            for pos in range(0, state.get_num_cols()):
                linha = randint(0, state.get_num_rows() - 1)
                action = Connect4Action(pos, linha)
                if state.validate_action(action):
                    next_state = state.clone()
                    next_state.play(action)
                    value = min(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return value

    def minimax1(self, state: Connect4State, depth: int, alpha: int = -sys.maxsize, beta: int = sys.maxsize,
                is_initial_node: bool = True):

        
        #grid = state.get_grid()
        
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_finished():
            return {
                Connect4Result.WIN: 5,
                Connect4Result.LOOSE: -5,
                Connect4Result.DRAW: 0
            }[state.get_result(self.get_current_pos())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.__heuristic(state)

        # if we are the acting player
        if self.get_current_pos() == state.get_acting_player():
            # very small integer
            value = -sys.maxsize
            selected_pos = -1

            for pos in range(0, state.get_num_rows()):
                linha = randint(0, state.get_num_cols() - 1)
                action = Connect4Action(linha, pos)
                if state.validate_action(action):
                    previous_a = value
                    next_state = state.clone()
                    next_state.play(action)
                    value = max(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                    alpha = max(alpha, value)

                    if value >= previous_a:
                        selected_pos = pos
                    if alpha >= beta:
                        break

            if is_initial_node:
                return selected_pos
            return value
        # if it is the opponent's turn
        else:
            # very big integer
            value = sys.maxsize
            for pos in range(0, state.get_num_rows()):
                linha = randint(0, state.get_num_cols() - 1)
                action = Connect4Action(linha, pos)
                if state.validate_action(action):
                    next_state = state.clone()
                    next_state.play(action)
                    value = min(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return value


    def get_action(self, state: Connect4State):
        return Connect4Action(self.minimax(state, 5), self.minimax1(state, 5))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
