# Holds the representation of a pocket
class Pocket:
    def __init__(self, pocket_type, num_stones, player, position):
        # (int) Number of stones in the pocket
        self.numStones = num_stones

        # (int) The player to which the pocket belongs to
        # 1 for player1, 2 for player2
        self.player = player

        # (string) The type of pocket it is
        # "pocket" for regular pocket, "mancala" for mancala
        self.type = pocket_type

        # (int) The of the pocket on the player's side
        # Pockets go from 0-5. 0 indicates the first pocket the corresponding player can play from
        # -1 designates that player's mancala
        self.position = position

    def __str__(self):

        # Returns a point-like string of the form (pocket_type, num_stones, player, position)
        return f"({self.type}, {self.numStones}, {self.player}, {self.position}）"

    # Accessors
    def get_type(self):
        return self.type
    def get_stones(self):
        return self.numStones
    def get_player(self):
        return self.player

    # Mutators
    def empty(self):
        self.numStones = 0

    # Adds one stone to the pocket (as in when it is "moved over" over the course of a move)
    def increment_stones(self):
        self.numStones += 1
