from typing import Optional

from games.connect4.action import Connect4Action
from games.connect4.result import Connect4Result
from games.state import State


class Connect4State(State):

    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 6, num_cols: int = 6):
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
        self.__grid = [[Connect4State.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

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

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: Connect4Action) -> bool:
        col = action.get_col()
        row = action.get_row()

        #   VALIDA COLUNA E LINHAS
        if (col < 0 or col >= self.__num_cols) and (row < 0 or row >= self.__num_rows):
            print("\tJOGADA INVALIDA")
            return False

        if(row == 0 and col == 0) or (row == 0 and col == 1) or (row == 1 and col == 0) or \
        (row == 0 and col == 6) or (row == 1 and col == 6) or (row == 2 and col == 0) or \
        (row == 6 and col == 0) or (row == 6 and col == 1) or (row == 5 and col == 0) or \
        (row == 6 and col == 6) or (row == 5 and col == 6) or (row == 4 and col == 0):
            print("\tJOGADA INVALIDA")
            return False

        return True


    # ONDE SE FAZ O UPDATE DO JOGO
    def update(self, action: Connect4Action):
        col = action.get_col()
        row = action.get_row()

      
        self.__grid[row][col] = self.__acting_player

    

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
            print({
                0:                              'X/ ',
                1:                              '0/ ',
                Connect4State.EMPTY_CELL:       '_/ '
            }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print('  ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
    

        for row in range(0, self.__num_rows):
            print(row, end= " ")
            if row == 1 or row == 0 or row == 5 or row == 6:
                print("  ", end="")
            for col in range(0, self.__num_cols):
                if (row == 0 and col == 0) or (row == 0 and col == 1) or (row == 1 and col == 0) or \
                (row == 0 and col == 6) or (row == 1 and col == 6) or (row == 2 and col == 0) or \
                (row == 6 and col == 0) or (row == 6 and col == 1) or (row == 5 and col == 0) or \
                (row == 6 and col == 6) or (row == 5 and col == 6) or (row == 4 and col == 0):
                    print("  ", end="")
                else:
                    print("\\", end="")
                    self.__display_cell(row, col)
            print("")


        self.__display_numbers()
        print(" ")

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
