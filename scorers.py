"""
Name: scorers.py
Author: Eric Cui
Created: December 2023
Description: Contains the board evaluation routines that will be fed into the minimax algorithm
"""

def simple_score(self, play_board, player):
    """
    Returns the simplest evaluation of the board state. It subtracts the moving player's mancala stones from
    the opposing player's mancala stones. Positive values are defined as more favorable for the moving player
    :param player: (int) The moving player. 1 for player1, 2 for player2
    :param play_board: (Board) An internal representation of the current state of the board
    :return: (int) The difference between the moving player's and opposing player's mancala stone count
    """
    return play_board.mancala_count(player) - play_board.mancala_count(play_board.switch_player(player))
