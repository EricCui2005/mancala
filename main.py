"""
Name: main.py
Author: Eric Cui
Created: December 2023
Description: This is the main file for the mancala project
"""
import game
import board
import boardGUI
import gametests


def main():

    # Initializing the game board
    play_board = board.Board()

    # Outputting and receiving task selection
    print("(1): Two player console game")
    print("(2): Two player GUI game")
    print("(3): Random vs random trials")
    print("(4): Simple vs random trials")
    selection = int(input("Select task: "))

    # BoardGUI selection
    if selection == 1:
        game.play_game(play_board)
    if selection == 2:
        bGUI = boardGUI.BoardGUI(play_board, 1)
    if selection == 3:
        random_trials_routine()

def random_trials_routine():
    """
    Runs random trials and outputs information
    :return: (void) Simply prints information
    """
    num_trials = int(input("Enter number of trials: "))
    win_data = gametests.game_trials(num_trials, gametests.randomGame)
    print(win_data)

def simple_vs_random_routine():
    """
    Runs random vs simple game trials and outputs information
    :return: (void) Simply prints information
    """
    num_trials = int(input("Enter number of trials: "))
    win_data = gametests.game_trials(num_trials, gametests.random_vs_simple)
    print(win_data)


if __name__ == "__main__":
    main()
