from sys import platlibdir
from typing import Optional

from games.connect4.action import Connect4Action
from games.connect4.result import Connect4Result
from games.state import State


class Connect4State(State):

    EMPTY_CELL = -1
    NOTPLAY_CELL = -3

    def __init__(self, num_rows: int = 9, num_cols: int = 17):
        super().__init__()

        if num_rows < 4:
            raise Exception("the number of rows must be 4 or over")
        if num_cols < 4:
            raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        

        """
        the grid
        """
        self.__grid = [
            [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3, -3],
            [-3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3],
            [-3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3],
            [-3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3],
            [-3, -3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -1, -3, -1, -3, -1, -3, -1, -3, -3, -3, -3, -3],
            [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]      
        ]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

        self.__has_right = False
        self.__has_left = False
        self.__has_upLeft = False
        self.__has_upRight = False
        self.__has_downLeft = False  
        self.__has_downRight = False

    def __check_right(self, player, col, row):
        j=1
        i=1
                #verifica para a direita
        if self.__grid[row][col + j + j] != player:
                    self.__has_right = True
                    return self.__has_right
        else:
                    while self.__grid[row][col + j + j] == player and (col + j + j) < self.__num_cols:
                        coluna_atual = col + j + j
                        j+=1
                        if row + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row - 1 >= self.__num_rows and coluna_atual - 1 >= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                            if self.__grid[row][coluna_atual + 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row - 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row - 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row + 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row + 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row][coluna_atual + 2] == player or \
                            self.__grid[row - 1][coluna_atual - 1] == player or \
                            self.__grid[row - 1][coluna_atual + 1] == player or \
                            self.__grid[row + 1][coluna_atual - 1] == player or \
                            self.__grid[row + 1][coluna_atual + 1] == player:
                                return False
                                break
                            else:
                                return True

    def __check_left(self, player, col, row):
        j=1
        i=1
        
                #verifica para a esquerda
        if self.__grid[row][col - j - j] != player:
                    return True
        else:
                    while self.__grid[row][col - j - j] == player and (col - j - j) >= self.__num_cols:
                        coluna_atual = col - j -j 
                        j+=1
                        if row + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row - 1 >= self.__num_rows and coluna_atual - 1 >= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                            if self.__grid[row][coluna_atual - 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row - 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row - 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row + 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row + 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row][coluna_atual - 2] == player or \
                            self.__grid[row - 1][coluna_atual - 1] == player or \
                            self.__grid[row - 1][coluna_atual + 1] == player or \
                            self.__grid[row + 1][coluna_atual - 1] == player or \
                            self.__grid[row + 1][coluna_atual + 1] == player:
                                return False
                                break
                            else:
                                return True

    def __check_upLeft(self, player, col, row):
        j=1
        i=1
        
        if self.__grid[row - 1][col - j] != player:
                    return True
        else:
                    while self.__grid[row - i][col - j] == player and (row - i) >= self.__num_rows and (col - j) < self.__num_rows:
                        row_atual = row - i
                        coluna_atual = col - j
                        j+=1
                        i+=1
                        if row_atual + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row_atual - 1 >= self.__num_rows and coluna_atual - 1 >= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                            if self.__grid[row_atual][coluna_atual + 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual - 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual - 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual - 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual + 2] == player or \
                            self.__grid[row_atual - 1][coluna_atual - 1] == player or \
                            self.__grid[row_atual - 1][coluna_atual + 1] == player or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == player or \
                            self.__grid[row_atual][coluna_atual - 2] == player:
                                return False
                                break
                            else:
                                return True

    def __check_upRight(self, player, col, row):
        j=1
        i=1
      
        if self.__grid[row - i][col + j] != player:
                    return True
        else:
                    while self.__grid[row - i][col + j] == player and (row - i) >= self.__num_rows and (col + j) < self.__num_cols:
                        row_atual = row - i
                        coluna_atual = col + j
                        i+=1
                        j+=1
                        if row_atual + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row_atual - 1 >= self.__num_rows and coluna_atual - 1 >= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                                if self.__grid[row_atual][coluna_atual + 2] == Connect4State.EMPTY_CELL or \
                                self.__grid[row_atual - 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                                self.__grid[row_atual - 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                                self.__grid[row_atual][coluna_atual - 2] == Connect4State.EMPTY_CELL or \
                                self.__grid[row_atual + 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                                self.__grid[row_atual][coluna_atual + 2] == player or \
                                self.__grid[row_atual - 1][coluna_atual - 1] == player or \
                                self.__grid[row_atual - 1][coluna_atual + 1] == player or \
                                self.__grid[row_atual][coluna_atual - 2] == player or \
                                self.__grid[row_atual + 1][coluna_atual + 1] == player:
                                    return False
                                    break
                                else:
                                    return True

    def __check_downLeft(self, player, col, row):
        j=1
        i=1
        
        if self.__grid[row + 1][col - j] != player:
                    return True
        else:
                    while self.__grid[row + i][col - j] == player and (row + i) < self.__num_rows and (col - j) >= self.__num_cols:
                        row_atual = row + i
                        coluna_atual = col - j
                        j+=1
                        i+=1
                        if row_atual + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row_atual - 1 >= self.__num_rows and coluna_atual>= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                            if self.__grid[row_atual][coluna_atual + 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual - 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual - 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual + 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual + 2] == player or \
                            self.__grid[row_atual - 1][coluna_atual - 1] == player or \
                            self.__grid[row_atual][coluna_atual - 2] == player or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == player or \
                            self.__grid[row_atual + 1][coluna_atual + 1] == player:
                                return False
                                break
                            else:
                                return True

    def __check_downRight(self, player, col, row):
        j=1
        i=1
     
        if self.__grid[row + 1][col + j] != player:
                    return True
        else:
                    while self.__grid[row + i][col + j] == player and (row + i) < self.__num_rows and (col + j) < self.__num_cols:
                        row_atual = row + i
                        coluna_atual = col + j
                        j+=1
                        i+=1
                        if row_atual + 1 < self.__num_rows and coluna_atual + 1 < self.__num_cols and \
                           row_atual - 1 >= self.__num_rows and coluna_atual - 1 >= self.__num_cols and \
                           coluna_atual + 2 < self.__num_cols:
                            if self.__grid[row_atual][coluna_atual + 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual - 2] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual - 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual + 1][coluna_atual + 1] == Connect4State.EMPTY_CELL or \
                            self.__grid[row_atual][coluna_atual + 2] == player or \
                            self.__grid[row_atual][coluna_atual - 2] == player or \
                            self.__grid[row_atual - 1][coluna_atual + 1] == player or \
                            self.__grid[row_atual + 1][coluna_atual - 1] == player or \
                            self.__grid[row_atual + 1][coluna_atual + 1] == player:
                                return False
                                break
                            else:
                                return True
        

    def __check_winner(self, player):
        # check for 4 across
        for row in range(1, self.__num_rows - 1):
            for col in range(2, self.__num_cols - 2):
                if  self.__grid[row][col] == player and \
                                    self.__grid[row][col + 2] != player and self.__grid[row][col + 2] != Connect4State.EMPTY_CELL and \
                                    self.__grid[row - 1][col - 1] != player and self.__grid[row - 1][col - 1] != Connect4State.EMPTY_CELL and \
                                    self.__grid[row - 1][col + 1] != player and self.__grid[row - 1][col + 1] != Connect4State.EMPTY_CELL and \
                                    self.__grid[row][col - 2] != player and self.__grid[row][col - 2] != Connect4State.EMPTY_CELL            and \
                                    self.__grid[row + 1][col - 1] != player and self.__grid[row + 1][col - 1] != Connect4State.EMPTY_CELL and \
                                    self.__grid[row + 1][col + 1] != player and self.__grid[row + 1][col + 1] != Connect4State.EMPTY_CELL:
                                    return True
                #verificador para qualquer posição exceto para as que são verificadas nos if's
                if self.__grid[row][col] == player and \
                     self.__grid[row][col + 2] != Connect4State.EMPTY_CELL and \
                     self.__grid[row - 1][col - 1] != Connect4State.EMPTY_CELL and \
                     self.__grid[row - 1][col + 1] != Connect4State.EMPTY_CELL and \
                     self.__grid[row][col - 2] != Connect4State.EMPTY_CELL            and \
                     self.__grid[row + 1][col - 1] != Connect4State.EMPTY_CELL and \
                     self.__grid[row + 1][col + 1] != Connect4State.EMPTY_CELL:

                            #verifica para a direita
                            self.__has_right = self.__check_right(player, col, row)
                            #verifica para a esquerda
                            self.__has_left = self.__check_left(player, col, row)

                            #verifica para a cima/esquerda
                            self.__has_upLeft = self.__check_upLeft(player, col, row)
          
                            #verifica cima/direita
                            self.__has_upRight = self.__check_upRight(player, col, row)
        
                            #verifica baixo/esquerda
                            self.__has_downLeft = self.__check_downLeft(player, col, row)
          
                            #verifica baixo/direita
                            self.__has_downRight = self.__check_downRight(player, col, row)
     
 
        if self.__has_right == True and self.__has_downLeft == True and \
           self.__has_downRight == True and self.__has_left == True and \
           self.__has_upRight == True and self.__has_upLeft == True:
            return True
        else: return False
                                
                
    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        col = action.get_col()
        row = action.get_row()

        #   VALIDA COLUNA E LINHAS
        if (col < 0 or col >= self.__num_cols) and (row < 0 or row >= self.__num_rows):
            #print("\tJOGADA INVALIDA")
            return False
        if action == Connect4State.NOTPLAY_CELL:
            #print("\tJOGADA INVALIDA")
            return False

        if self.__grid[row][col] is not Connect4State.EMPTY_CELL:
            #print("\tJOGADA INVALIDA")
            return False

        return True


    # ONDE SE FAZ O UPDATE DO JOGO
    def update(self, action: Connect4Action):
        self.__has_winner = self.__check_winner(self.__acting_player)

        col = action.get_col()
        row = action.get_row()

        self.__grid[row][col] = self.__acting_player

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
            print({
                0:                              '|0|',
                1:                              '|1|',
                Connect4State.EMPTY_CELL:       '|_|',
                Connect4State.NOTPLAY_CELL:     '   '
            }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
        
            if col < 10:
                print('', end=" ")
            print(col, end=" ")
        print(" ")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("---", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()
    

        for row in range(0, self.__num_rows):
            print(row, end= " ")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
            print("")

        self.__display_separator()
        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = Connect4State(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[Connect4Result]:
        if self.__has_winner:
            return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        if self.__is_full():
            return Connect4Result.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass
