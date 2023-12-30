import board
import copy


class smart_player():

    def minimax(self, play_board, depth, maximizing, scorer, player, prev_move):
        """
        Recursively returns the value of the best possible board state for a certain player given a
        current board state and assuming the opponent moves optimally. The current moving player
        is defined to be the maximizer who is seeking to maximize the value of the board state
        :param prev_move: (Tuple(int, int)) Information about the previous move for the purposes of 
        tracking if the previous move results in us landing in a mancala
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
        if play_board.check_end() or depth == 0 or play_board.empty_side(player):
            return scorer(play_board, player, prev_move)

        # Switch player before making a move
        current_player = player if maximizing else play_board.switch_player(player)

        if maximizing:
            max_eval = float('-inf')
            for position in play_board.get_valid_moves(current_player):
                
                # Copying the board
                new_board = copy.deepcopy(play_board)
                
                # Storing the move's position and the stones the pocket at that position holds
                prev_move = (position, play_board.board[position].get_stones())
                
                # Making the move and evaluating using minimax
                new_board.move(current_player, position, False)
                score = self.minimax(new_board, depth - 1, False, scorer, current_player, prev_move)
                max_eval = max(max_eval, score)
            return max_eval
        else:
            min_eval = float('inf')
            for position in play_board.get_valid_moves(current_player):
                
                # Copying the board
                new_board = copy.deepcopy(play_board)
                
                # Storing the move's position and the stones the pocket at that position holds
                prev_move = (position, play_board.board[position].get_stones())
                
                # Making the move and evaluating using minimax
                new_board.move(current_player, position, False)
                
                score = self.minimax(new_board, depth - 1, True, scorer, current_player, prev_move)
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
            new_board.move(player, position, False)

            # Returning the highest possible move from the position obtained from the current move
            # NOTE: prev_move is initially none
            score = self.minimax(new_board, depth, True, scorer, player, None)

            # Appropriately updating max_score and best_move
            if score > max_score:
                max_score = score
                best_move = position
        print(f"Sam moving at position {best_move} with a score of {max_score}")
        play_board.move(player, best_move, True)
