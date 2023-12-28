import randomAI
import board
import copy
import smartplayer
import scorers


def randomGame(play_board):
    """
    Contains logic for playing a game where the two players make completely random moves
    :return: (int) 1 if player 1 wins, 2 if player 2 wins, and 0 for a draw
    """
    randy = randomAI.RandomAI()

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


def random_vs_simple(play_board):
    randy = randomAI.RandomAI()
    sam = smartplayer.smart_player()

    # SimpleAI is defined to be player1
    current_player = 1

    # Game loop
    while not play_board.check_end():

        # Switch players if the current player has no moves
        if play_board.empty_side(current_player):
            current_player = play_board.switch_player(current_player)

        # SimpleAI moves if current_player is 1
        if current_player == 1:

            # Checks if the SimpleAI landed in their mancala
            if play_board.move(1, sam.MM_best_move(play_board, 1, 3, scorers.simple_score), False):
                continue

            # We switch players if the SimpleAI did not land in their mancala
            else:
                play_board.switch_player(current_player)

        # Random player moves if current_player is 2
        else:

            # Checks if the random player landed in their mancala
            if randy.random_move(play_board, 2):
                continue

            # We switch players if the random player did not land in their mancala
            else:
                play_board.switch_player(current_player)

    # Game end
    if play_board.board[6].get_stones() > play_board.board[13].get_stones():
        return 1
    elif play_board.board[6].get_stones() < play_board.board[13].get_stones():
        return 2
    else:
        return 0


def game_trials(num_trials, game):
    """
    Runs a random vs random game trials
    :param num_trials: (int) The number of trials to be run
    :return: (list) of (int) Returns a list containing the win information. The first entry is the number of
    player1 wins, the second is player2 wins, and the third is the number of draws
    """

    # List to contain win information
    win_data = [0, 0, 0]
    default_board = board.Board()

    # Executing trials according to num_trials
    for i in range(num_trials):
        play_board = copy.deepcopy(default_board)
        result = game(play_board)
        if result == 1:
            win_data[0] += 1
        elif result == 2:
            win_data[1] += 1
        else:
            win_data[2] += 1
    return win_data
