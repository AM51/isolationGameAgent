if __name__ == "__main__":
    from isolation import Board
    from sample_players import RandomPlayer,GreedyPlayer
    from game_agent import MinimaxPlayer

    player2 = RandomPlayer()
    player1 = MinimaxPlayer()
    game = Board(player1, player2)
    game.apply_move((2, 3))
    game.apply_move((0, 5))
    print(game.to_string())

    print (player1.get_move(game,1000))
