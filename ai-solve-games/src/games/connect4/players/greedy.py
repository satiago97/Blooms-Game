from random import choice
from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
from games.state import State


class GreedyConnect4Player(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: Connect4State):
        grid = state.get_grid()

        selected_col = None
        selected_row = None
        max_count = 0

        for col in range(0, state.get_num_cols()):
            for row in range(0, state.get_num_rows()):
                count = 0
                if grid[row][col] == self.get_current_pos():
                    count += 1
                if grid[row][col] == state.EMPTY_CELL:
                    count += 5


            # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
                if selected_row is None or selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                    selected_col = col
                    selected_row = row
                    max_count = count

        if selected_col is None:
            raise Exception("There is no valid action")

        if selected_row is None:
            raise Exception("There is no valid action")

        play = Connect4Action(selected_col, selected_row)
        #print("Greedy: ")
        #print(selected_col, selected_row)
        return play

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
