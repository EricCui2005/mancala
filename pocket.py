"""
Name: pocket.py
Author: Eric Cui
Created: December 2023
Description: Contains the Pocket class. The Pocket class contains all the logic for mancala pocket/mancala
representation and manipulation
"""
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

        # (int) The position of the pocket on board (0-13)
        self.position = position

    # Returns a comprehensive string representation describing all the pocket's information
    def __str__(self):

        # Returns a point-like string of the form (pocket_type, num_stones, player, position)
        return f"({self.type}, {self.num_stones}, {self.player}, {self.position}）"

    # Returns a simple representation of the pocket depicting the number of stones it has
    def simple_string(self):
        return f"({self.num_stones})"

    # Accessors
    def get_type(self):
        return self.type
    def get_stones(self):
        return self.num_stones
    def get_player(self):
        return self.player
    def get_position(self):
        return self.position

    # Mutators
    def empty(self):
        self.num_stones = 0

    # Adds one stone to the pocket (as in when it is "moved over" over the course of a move)
    def increment_stones(self):
        self.num_stones += 1

    # Sets the stone in the pocket
    def set_stones(self, stone_count):
        self.num_stones = stone_count
