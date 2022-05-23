from random import randint

from games.connect4.action import Connect4Action
from games.connect4.player import Connect4Player
from games.connect4.state import Connect4State
from games.state import State


class RandomConnect4Player(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: Connect4State):
            #state.display()

            selected_col = randint(0, state.get_num_cols() - 1)
            selected_row = randint(0, state.get_num_rows() - 1)
            play = Connect4Action(selected_col, selected_row)
            #print("Random: ")
            #print(selected_col, selected_row)
            return play


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
