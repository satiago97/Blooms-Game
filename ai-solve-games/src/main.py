from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.minimax import MinimaxConnect4Player
from games.connect4.players.random import RandomConnect4Player
from games.connect4.simulator import Connect4Simulator
from games.game_simulator import GameSimulator


from games.connect4.players.human import HumanConnect4Player


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("Blooms game")

    num_iterations = 10


    blooms_simulations = [
        {
            "name": "Blooms - Human vs Human",
            "player1": HumanConnect4Player("Human"),
            "player2": RandomConnect4Player("Human")
        },
    ]

    for sim in blooms_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)



if __name__ == "__main__":
    main()
