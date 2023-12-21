"""
Name: setboardtesting.py
Author: Eric Cui
Created: December 2023
Description: Manual game playing using set_board_state()
"""
import game
import board


play_board = board.Board()
board_state = input("Input Board State: ")
play_board.set_board_state(board_state)
game.play_game(play_board)
