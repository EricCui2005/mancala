# Hold the representation of a mancala
class Mancala:
    def __init__(self, collectedStones, player):
        self.collectedStones = collectedStones
        self.player = player

    def __str__(self):
        return f"M({self.collectedStones}, {self.player}）"

    # Accessors
    def mancala_stones(self):
        return self.collectedStones
    def mancala_player(self):
        return self.player

    # Mutator
    def add_stones(self, addedStones):
        self.collectedStones += addedStones


