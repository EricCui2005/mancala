import pytest
import board


# Testing for all illegal move types
def test_illegal_moves():
    play_board = board.Board()

    # Pocket belongs to other player
    with pytest.raises(Exception, match="Invalid Move: Pocket belongs to other player"):
        result = play_board.move(1, 7)

    with pytest.raises(Exception, match="Invalid Move: Cannot move from a mancala"):
        result = play_board.move(1, 6)

    with pytest.raises(Exception, match="Invalid Move: Position out of bounds"):
        result = play_board.move(1, -1)
