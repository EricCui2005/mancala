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
    :return: (void)
    """

    # Initializing the play board and printing out its initial state
    play_board = board.Board()
    play_board.print_board("simple")

    # Play initially begins with player1
    current_player = 1

    # Game loop
    while not play_board.check_end():

        # Information output and move input gathering
        print(f"Player {current_player}'s Move")
        move_position = int(input("Move: "))

        # Valid move check
        while not play_board.valid_move((current_player), move_position):
            print("Invalid move")
            move_position = int(input("Move: "))

        # We first check if the moving player has landed in their mancala
        # We evaluate if the moving player has valid moves in this case
        if play_board.move(current_player, move_position):

            # If the player landed in their mancala, we check if they have
            # any valid moves left
            if play_board.empty_side(current_player):

                # We change players if the current moving player landed in their own mancala but
                # does not have any valid moves left (their side is empty)
                current_player = play_board.switch_player(current_player)
            else:

                # If the player lands in their mancala, and they have valid moves, we print the board
                # and allow the player to move again (through the continue statement)
                play_board.print_board("simple")
                continue

        # We evaluate if the other player has valid moves if the current moving player did not land
        # in their own mancala
        else:
            current_player = play_board.switch_player(current_player)

            # If the moving player did not land in their own mancala but the opposite player has
            # no valid moves, we allow the current moving player to continue moving
            if play_board.empty_side(current_player):
                current_player = play_board.switch_player(current_player)
                continue
            else:
                # We change players if the current moving player did not land in their own mancala
                continue

    # Game end and winner output
    print("Game end")
    if play_board.board[6].get_stones() > play_board.board[13].get_stones():
        print("Player1 Wins")
    elif play_board.board[6].get_stones() < play_board.board[13].get_stones():
        print("Player2 Wins")
    else:
        print("Draw")









