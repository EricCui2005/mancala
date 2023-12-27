import board
import copy

class smart_player():

    def minimax(self, play_board, depth, maximizing, scorer, player):
        """
        Recursively returns the value of the best possible board state for a certain player given a
        current board state and assuming the opponent moves optimally. The current moving player
        is defined to be the maximizer who is seeking to maximize the value of the board state
        :param play_board: (Board) The current board position being evaluated
        :param depth: (int) The remaining number of "moves into the future" the function considers
        :param maximizing: (bool) Describes whether it is the maximizing player's turn or not
        :param scorer: (Function) The function that determines how board states are evaluated
        :param player: (int) 1 for player1, 2 for player2. Which player is defined as the maximizer is
        determined by how the function is called
        :return: (int) The value of the highest possible board state evaluation that is possible from the
        current board position with the assumption that the opposing player moves optimally
        """

        # Base case
        # Function calls terminate if the previous move results in an end state or the
        # search depth reaches 0
        if play_board.check_end() or depth == 0:
            return scorer(play_board, player)

        # Case when it is the maximizing player's turn
        # (maximizing = True)
        if maximizing:

            # Setting our max_eval to an infinitely small number for
            # the purposes of initialization
            max_eval = float('-inf')

            # Making recursive calls on every possible position of the board that can be reached
            # from moves made by the maximizing player
            for position in play_board.get_valid_moves(player):

                # Making a copy of play_board, making a legal move, and making a recursive call on the new board
                new_board = copy.deepcopy(play_board)
                new_board.move(player, position)

                # NOTE: We switch players in the recursive call
                score = self.minimax(new_board, depth - 1, False, scorer, play_board.switch_player(player))

                # Because the player is currently maximizing, we return the max value that can arise
                max_eval = max(max_eval, score)
            return max_eval

        # Case when it is the minimizing player's turn
        # (minimizing = False)
        else:

            # Setting our min_eval to an infinitely small number for
            # The purposes of initialization
            min_eval = float('inf')

            # Making recursive calls on every possible position of the board that can be reached
            # from moves made by the minimizing player
            for position in play_board.get_valid_moves(player):

                # Making a copy of play_board, making a legal move, and making a recursive call on the new board
                new_board = copy.deepcopy(play_board)
                new_board.move(play_board.switch_player(player), position)

                # NOTE: We switch players in the recursive call
                score = self.minimax(new_board, depth - 1, True, scorer, play_board.switch_player(player))

                # Because the player is currently minimizing, we return the min value that can arise
                min_eval = min(min_eval, score)
            return min_eval

    def MM_best_move(self, play_board, player, depth, scorer):
        """
        Algorithmically finds the best move for the current position
        :param play_board: (Board) The current board being evaluated
        :param player: (int) 1 for player1, 2 for player2
        :param depth: (int) The depth of the minimax tree
        :param scorer: (Function) The board evaluation function
        :return: (int) The position of the optimal move
        """

        # Initializing an infinitely small max_score (because we are maximizing) and
        # a variable to hold the eventually returned move
        max_score = float('-inf')
        best_move = None

        # Looping through all possible moves
        for position in play_board.get_valid_moves(player):

            # Copying the board and making a move for evaluation
            new_board = copy.deepcopy(play_board)
            new_board.move(player, position)

            # Returning the highest possible move from the position obtained from the current move
            score = self.minimax(new_board, depth, True, scorer, player)

            # Appropriately updating max_score and best_move
            if score > max_score:
                max_score = score
                best_move = position
        return best_move
