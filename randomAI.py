import random

class RandomAI():

    def random_move(self, play_board, player):
        """
        Makes a random move
        :param play_board: (Board) The current board state
        :param player: (int) The player that will be making the random move. 1 for player1,
        2 for player 2
        :return: (bool) Performs the move and returns True if the move ended in
        the moving player's mancala, False if not
        """

        # Generating a list of valid moves and randomly selecting one of those moves
        moves = play_board.get_valid_moves(player)
        return play_board.move(player, moves[random.randint(0, len(moves) - 1)])

