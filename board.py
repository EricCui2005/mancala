"""
Name: board.py
Author: Eric Cui
Created: December 2023
Description: Contains the Board class. The Board class contains all the logic for game representation,
move initiation, and game-state-checking
"""
import pocket


class Board:
    # List to hold the representation of the mancala board
    board = []

    # The mancala board will be represented with a list of length 14
    # with 12 pockets and two mancalas
    def __init__(self):

        # Initializing player1's playable pockets
        for i in range(6):
            self.board.append(pocket.Pocket("pocket", 4, 1, i))

        # Adding player1's mancala
        self.board.append(pocket.Pocket("mancala", 0, 1, 6))

        # Initializing player2's playable pockets
        for i in range(7, 13):
            self.board.append(pocket.Pocket("pocket", 4, 2, i))

        # Adding player2's mancala
        self.board.append(pocket.Pocket("mancala", 0, 2, 13))

    # Comprehensive string representation of the board
    def __str__(self):
        bottom_row = ""
        top_row = ""

        for i in range(7):
            bottom_row += f" {self.board[i]}"
        for i in range(13, 6, -1):
            top_row += f"{self.board[i]} "

        return f"{top_row}\n{bottom_row}"

    # Returns a simple version of the board containing the correct pockets in the correct orientation
    # Player1's pockets and mancala is on the bottom row, player2's pockets and mancala is on the top row
    def simple_string(self):
        bottom_row = ""
        top_row = ""

        for i in range(7):
            bottom_row += f" {self.board[i].simple_string()}"
        for i in range(13, 6, -1):
            top_row += f"{self.board[i].simple_string()} "

        return f"{top_row}\n   {bottom_row}"

    def print_board(self, print_type):
        """
        Prints the board
        :param print_type: (str) determines which type of board representation to print. Inputting "raw"
        prints out the __str__ representation of the class while "simple" prints out the simple_string() representation
        :return: (void)
        """
        if print_type == "raw":
            print(str(self))
        if print_type == "simple":
            print(self.simple_string())

    def valid_move(self, player, position):
        """
        Checks if inputted move is valid
        :param player: (int) The player moving. 1 indicates player1, 2 indicates player2
        :param position: (int) Indicates which pocket to move from. It is the index of the pocket
        :return:
        """

        # Checking to make sure the move is in bounds
        if position < 0 or position > 12:
            print("Invalid position")
            return False

        current_pocket = self.board[position]

        # Checking to make sure the move is not from a mancala, the pocket does not belong to the
        # other player, and the pocket is not empty
        if current_pocket.get_type() == "mancala":
            print(f"Pocket type = {current_pocket.get_type()}")
            return False
        if current_pocket.get_player() != player:
            print(f"Pocket player = {current_pocket.get_player()}")
            return False
        if current_pocket.get_stones() == 0:
            print(f"Pocket stones = {current_pocket.get_stones()}")
            return False

        # Move is valid if other cases do not fire
        return True

    def empty_side(self, player):
        """
        Checks if a player's side is empty (meaning they have no valid moves)
        :param player: (int) The player moving. 1 indicates player1, 2 indicates player2
        :return: (bool) False if the player's side is not empty, True if the player's side is empty
        """
        if player == 1:
            for i in range(6):
                if self.board[i].get_stones() != 0:
                    return False
        else:
            for i in range(7, 13):
                if self.board[i].get_stones() != 0:
                    return False
        return True

    def move(self, player, position):
        """
        Performs a mancala cascade move and tracks whether the player landed in their own mancala
        :param player: (int) The player moving. 1 indicates player1, 2 indicates player2
        :param position: (int) Indicates which pocket to move from. It is the index of the pocket
        (note: mancalas are illegal to move from)
        :return: (bool) True if the player's final move is in their own mancala, false if not
        """

        current_pocket = self.board[position]

        # Accessing the number of stones we have to move with and setting the number of
        # stones in the originating pocket to 0 to start the move
        num_stones = current_pocket.get_stones()
        current_pocket.empty()

        # Iterating through the pockets in the board and incrementing accordingly
        # shift if used to check if the opposing player's mancala has been encountered. If it has,
        # we simply "shift" the pockets that we increment by 1 to make sure we do not place within
        # the mancala
        shift = 0
        for i in range(num_stones):
            current_pocket = self.board[(position + shift + 1 + i) % 14]

            # Checking if the pocket we are iterating over is the mancala of the other player
            # If it is, we increment shift to track the new shift
            if current_pocket.get_player() != player and current_pocket.get_type() == "mancala":
                shift += 1

            # Uses modulus to ensure the moves properly wrap around
            current_pocket = self.board[(position + shift + 1 + i) % 14]
            current_pocket.increment_stones()

        # Tracking the ending pocket to determine whether the move continues
        end_pocket = self.board[current_pocket.get_position()]

        # Move continues if the ending pocket belongs to the player, it is not a mancala, and it has more than one stone
        if end_pocket.get_player() == player and end_pocket.get_type() == "pocket" and end_pocket.get_stones() > 1:
            self.print_board("simple")
            self.move(player, end_pocket.get_position())
            return False

        # Player is allowed another move if their final move lands in their mancala
        if end_pocket.get_player() == player and end_pocket.get_type() == "mancala":
            self.print_board("simple")
            return True

        self.print_board("simple")
        return False

    # Function to check if the game is finished
    # The game is finished when all the pockets have 0 stones
    def check_end(self):
        for i in range(14):
            if i == 6 or i == 13:
                continue
            else:
                if self.board[i].get_stones() != 0:
                    return False
        return True

    def set_board_state(self, state):
        """
        Sets each pocket and mancala on the board to contain a certain number of stones
        :param state: (str) A string of 14 numbers separated by spaces. Each number represents the
        number of stones in the pocket at the corresponding "index" of the number
        :return: (void)
        """

        # Splitting the string
        split_string = state.split()

        # Container for the stone counts in the form of (ints)'s
        stone_counts = []

        # Adding the stone counts
        for char in split_string:
            stone_counts.append(int(char))

        # Assigning the stone counts
        for i in range(14):
            self.board[i].set_stones(stone_counts[i])

    def switch_player(self, player):
        if player == 1:
            return 2
        else:
            return 1


