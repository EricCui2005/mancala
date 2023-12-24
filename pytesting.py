"""
Name: pytesting.py
Author: Eric Cui
Created: December 2023
Description: Contains tests
"""
import pytest
import board
import game


# Testing for all illegal move types
def test_illegal_moves():
    play_board = board.Board()

    # Pocket belongs to other player
    assert not play_board.valid_move(1, 7)

    # Pocket is a mancala
    assert not play_board.valid_move(1, 6)

    # Position is out of bounds
    assert not play_board.valid_move(1, -1)


def test_double_moves():
    play_board = board.Board()

    # Successfully detects a double move for player 1 (player 1 landed in their mancala)
    play_board.set_board_state("0 0 0 0 2 0 0 1 0 0 0 0 0 0")
    assert play_board.move(1,4)

    # Successfully detects a double move for player 2 (player 2 landed in their mancala)
    play_board.set_board_state("0 1 0 0 0 0 0 0 0 0 0 2 0 0")
    assert play_board.move(2, 11)


def test_initial_end_state():
    play_board = board.Board()

    # Game instantly ends in a draw
    play_board.set_board_state("0 0 0 0 0 0 0 0 0 0 0 0 0 0")
    assert game.play_game(play_board) == 0

    # Game instantly ends and player 1 wins
    play_board.set_board_state("0 0 0 0 0 0 1 0 0 0 0 0 0 0")
    assert game.play_game(play_board) == 1

    # Game instantly ends and player 2 wins
    play_board.set_board_state("0 0 0 0 0 0 0 0 0 0 0 0 0 1")
    assert game.play_game(play_board) == 2

def test_get_valid_moves():
    play_board = board.Board()

    # No valid moves for player1
    play_board.set_board_state("0 0 0 0 0 0 0 0 0 0 0 0 0 0")
    assert set(play_board.get_valid_moves(1)) == set()

    # No valid moves for player2
    play_board.set_board_state("0 0 0 0 0 0 0 0 0 0 0 0 0 0")
    assert set(play_board.get_valid_moves(2)) == set()

    # All valid moves for player1
    play_board.set_board_state("1 1 1 1 1 1 0 0 0 0 0 0 0 0")
    assert set(play_board.get_valid_moves(1)) == {0, 1, 2, 3, 4, 5}

    # All valid moves for player2
    play_board.set_board_state("0 0 0 0 0 0 0 1 1 1 1 1 1 0")
    assert set(play_board.get_valid_moves(2)) == {7, 8, 9, 10, 11, 12}

    # Some valid moves for player1
    play_board.set_board_state("0 1 0 1 1 0 0 0 0 0 0 0 0 0")
    assert set(play_board.get_valid_moves(1)) == {1, 3, 4}

    # Some valid moves for player2
    play_board.set_board_state("0 0 0 0 0 0 0 1 0 1 1 1 0 0")
    assert set(play_board.get_valid_moves(2)) == {7, 9, 10, 11}







