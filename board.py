import pocket
import mancala

class Board:
    # List to hold the representation of the mancala board
    pockets = []

    # The mancala board will be represented with a list of the 12 pockets and two
    # independently initialized mancalas
    def __init__(self):

        #Populating board with two mancalas and 12 pockets, placed accordingly
        for i in range(12):
            if (i < 6):
                self.pockets.append(pocket.Pocket(4, 2))
            else:
                self.pockets.append(pocket.Pocket(4, 1))

        # Initializing the two mancalas
        self.mancala_one = mancala.Mancala(0, 1)
        self.mancala_two = mancala.Mancala(0, 2)


    def move(self, player, position):

        # Invalid move checking (out of bounds, wrong player, empty pocket)
        if position < 0 or position > 12:
            raise Exception("Invalid Move: Position out of bounds (0-11)")

        current_pocket = pocket[position]
        if current_pocket.pocket_player() != player:
            raise Exception("Invalid Move: Pocket belongs to other player")
        if current_pocket.pocket_stones == 0:
            raise Exception("Invalid Move: Pocket is empty")

        # Accessing the number of stones we have to move with and setting the number of
        # stones in the originating pocket to 0 to start the move
        num_stones = current_pocket.pocket_stones
        current_pocket.set_stones(0)

        for i in range(num_stones):

            # Iterating through the pockets in the board
            current_pocket = self.pockets[position + 1 + i]


















