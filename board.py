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

    # Makes a move with built-in error checking
    def move(self, player, position):
        """
        Performs a mancala cascade move
        :param player: (int) The player moving. 1 indicates player1, 2 indicates player2
        :param position: (int) Indicates which pocket to move from. It is the index of the pocket
        (note: mancalas are illegal to move from)
        :return: (void)
        """

        # Checking to make sure the move is in bounds
        if position < 0 or position > 12:
            raise Exception("Invalid Move: Position out of bounds")

        current_pocket = self.board[position]

        # Checking to make sure the move is not from a mancala, the pocket does not belong to the
        # other player, and the pocket is not empty
        if current_pocket.get_type() == "mancala":
            raise Exception("Invalid Move: Cannot move from a mancala")
        if current_pocket.get_player() != player:
            raise Exception("Invalid Move: Pocket belongs to other player")
        if current_pocket.get_stones() == 0:
            raise Exception("Invalid Move: Pocket is empty")

        # Accessing the number of stones we have to move with and setting the number of
        # stones in the originating pocket to 0 to start the move
        num_stones = current_pocket.get_stones()
        current_pocket.empty()

        for i in range(num_stones):
            # Iterating through the pockets in the board and incrementing accordingly
            # Uses modulus to ensure the moves properly wrap around
            current_pocket = self.board[(position + 1 + i) % 14]
            current_pocket.increment_stones()

    # Function to check if the game is finished
    # The game is finished when all the pockets have 0 stones
    def check_end(self):
        for i in range(14):
            if i == 0 or i == 7:
                continue
            else:
                if self.board[i].get_stones() != 0:
                    return False
        return True
