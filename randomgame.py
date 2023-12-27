import randomAI
import board


def randomGame():
    """
    Contains logic for playing a game where the two players make completely random moves
    :return: (int) 1 if player 1 wins, 2 if player 2 wins, and 0 for a draw
    """
    randy = randomAI.RandomAI()

    play_board = board.Board()

    # Play initially begins with player1
    current_player = 1

    # Game loop
    while not play_board.check_end():

        # Switches the player if the current player has no valid moves
        if play_board.empty_side(current_player):
            current_player = play_board.switch_player(current_player)

        # If the moving player landed in their mancala (they are allowed to move again), we do not switch the player
        if randy.random_move(play_board, current_player):
            continue

        # We switch players otherwise
        else:
            play_board.switch_player(current_player)

    # Game end
    if play_board.board[6].get_stones() > play_board.board[13].get_stones():
        return 1
    elif play_board.board[6].get_stones() < play_board.board[13].get_stones():
        return 2
    else:
        return 0

