# Holds the representation of a pocket
class Pocket:
    def __init__(self, pocket_type, num_stones, player, position):
        # (int) Number of stones in the pocket
        self.num_stones = num_stones

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

    # Returns a comprehensive string representation describing all the pocket's information
    def __str__(self):

        # Returns a point-like string of the form (pocket_type, num_stones, player, position)
        return f"({self.type}, {self.num_stones}, {self.player}, {self.position}）"

    #
    def simple_string(self):
        return f"({self.num_stones})"

    # Accessors
    def get_type(self):
        return self.type
    def get_stones(self):
        return self.num_stones
    def get_player(self):
        return self.player

    # Mutators
    def empty(self):
        self.num_stones = 0

    # Adds one stone to the pocket (as in when it is "moved over" over the course of a move)
    def increment_stones(self):
        self.num_stones += 1
