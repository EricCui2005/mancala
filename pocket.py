# Holds the representation of a pocket
class Pocket:
    def __init__(self, numStones, player):
        self.numStones = numStones
        self.player = player

    def __str__(self):
        return f"P({self.numStones}, {self.player}）"

    # Accessors
    def pocket_stones(self):
        return self.numStones
    def pocket_player(self):
        return self.player

    # Mutators
    # Flexibly changes the number of stones in a pocket
    def set_stones(self, stones):
        self.numStones = stones

    # Adds one stone to the pocket (as in when it is "moved over" over the course of a move)
    def increment_stones(self):
        self.numStones += 1



