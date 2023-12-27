"""
Name: setboardtesting.py
Author: Eric Cui
Created: December 2023
Description: Contains a selection of tests utilizing the set_board_state() function
"""
import game
import board
import boardGUI
import randomgame


def console_testing():
    play_board = board.Board()
    board_state = input("Input Board State: ")
    play_board.set_board_state(board_state)
    game.play_game(play_board)


def GUI_testing():
    play_board = board.Board()
    board_state = input("Input Board State: ")
    play_board.set_board_state(board_state)
    bGUI = boardGUI.BoardGUI(play_board, 1)


def random_vs_random_testing():
    play_board = board.Board()
    board_state = input("Input Board State: ")
    play_board.set_board_state(board_state)
    print(randomgame.randomGame(play_board))


print("(1): Console testing")
print("(2): GUI testing")
print("(3): Random vs. Random testing")
selection = int(input("Enter your selection: "))

if selection == 1:
    console_testing()
elif selection == 2:
    GUI_testing()
elif selection == 3:
    random_vs_random_testing()
