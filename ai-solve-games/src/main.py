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
            "name": "Blooms - Random - Random",
            "player1": HumanConnect4Player("Player1"),
            "player2": HumanConnect4Player("Player2")
        },
        {
            "name": "Blooms - Random - Greedy",
            "player1": RandomConnect4Player("Random"),
            "player2": GreedyConnect4Player("Greedy")
        },
        {
            "name": "Blooms - Random - Minimax",
            "player1": RandomConnect4Player("Random"),
            "player2": MinimaxConnect4Player("Minimax")
        },
        {
            "name": "Blooms - Greedy - Minimax",
            "player1": GreedyConnect4Player("Greedy"),
            "player2": MinimaxConnect4Player("Minimax")
        },
    ]

    for sim in blooms_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)



if __name__ == "__main__":
    main()