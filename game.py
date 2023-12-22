"""
Name: game.py
Author: Eric Cui
Created: December 2023
Description: Contains the logic to initiate a mancala game loop
"""
import board


def play_game(play_board):
    """
    Mancala cascade game loop
    :param play_board: (Board) Takes in a board object
    :return: (int) Returns 1 if player1 wins, 2 if player2 wins, and 0 if it is a draw
    """

    # Initializing the play board and printing out its initial state
    play_board = board.Board()
    play_board.print_board("simple")

    # Play initially begins with player1
    current_player = 1

    # Game loop
    while not play_board.check_end():

        # Switches the player if the current player has no valid moves
        if play_board.empty_side(current_player):
            current_player= play_board.switch_player(current_player)

        # Information output and move input gathering
        print(f"Player {current_player}'s Move")
        move_position = int(input("Move: "))

        # Valid move check
        while not play_board.valid_move((current_player), move_position):
            print("Invalid move")
            move_position = int(input("Move: "))

        # If the moving player landed in their mancala (they are allowed to move again), we do not switch the player
        if play_board.move(current_player, move_position):
            continue

        # We switch players otherwise
        else:
            play_board.switch_player(current_player)

    # Game end and winner output
    print("Game end")
    if play_board.board[6].get_stones() > play_board.board[13].get_stones():
        print("Player1 Wins")
        return 1
    elif play_board.board[6].get_stones() < play_board.board[13].get_stones():
        print("Player2 Wins")
        return 2
    else:
        print("Draw")
        return 0









