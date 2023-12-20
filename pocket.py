# Holds the representation of a pocket
class Pocket:
    def __init__(self, type, numStones, player):
        self.numStones = numStones
        self.player = player
        self.type = type

    def __str__(self):
        return f"P({self.type}, {self.numStones}, {self.player}）"

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
