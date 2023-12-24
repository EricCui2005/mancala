"""
Name: boardGUI.py
Author: Eric Cui
Created: December 2023
Description: Contains GUI framework for the mancala project
"""
import tkinter as tk


class BoardGUI:

    def __init__(self, play_board):

        # Initializing the root window, its geometry, and configuring its grid for the purposes of
        # subsequent frame centering
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Initializing a frame to nicely place the playable pocket buttons into
        self.pocket_frame = tk.Frame(self.root)

        # Initializing a list to hold the buttons for iterative placement into the pocket_frame grid
        self.playable_pockets = []

        # Placing pocket_frame into root (and leveraging row and column configuration to center it)
        self.pocket_frame.grid(row=1, column=1)

        # This label tracks which player's turn it is as well as if there is an endgame state
        self.game_state = tk.Label(self.root, text="Player 1 to move", font=('Arial', 20))
        self.game_state.grid(row=0, column=1, pady=10)

        # Initializing the internal representation of the game board
        self.play_board = play_board

        # Initializing the player
        self.current_player = 1

        # Iteratively placing the buttons into the pocket_frame grid
        for i in range(6):

            # Placing buttons for player1
            current_pocket = self.play_board.board[i]

            self.current_button = tk.Button(self.pocket_frame, text=self.play_board.board[i].simple_string(), font=('Arial', 10), height=2, width=8, command=lambda position=i: self.button_move(position))
            self.current_button.grid(row=1, column=i, padx=5, pady=5)

            # Placing buttons for player2
            self.current_button = tk.Button(self.pocket_frame, text=self.play_board.board[12 - i].simple_string(), font=('Arial', 10), height=2, width=8, command=lambda position=12 - i: self.button_move(position))
            self.current_button.grid(row=0, column=i, padx=5, pady=5)

        # Placing mancalas
        self.mancala_1 = tk.Label(self.root, text=self.play_board.board[6].simple_string(), font=('Arial', 20))
        self.mancala_2 = tk.Label(self.root, text=self.play_board.board[13].simple_string(), font=('Arial', 20))

        # Formatting
        self.mancala_1.grid(row=1, column=2, padx=50)
        self.mancala_2.grid(row=1, column=0, padx=50)

        self.root.mainloop()


    def button_move(self, position):
        """
        Function that is called when the user clicks on a pocket button
        :param position: (int) The pocket at the position that is being moved
        :return: (void)
        """
        # Displaying which player's turn it is
        self.root.grid_slaves(row=0, column=1)[0].configure(text=f"Player {self.current_player} to move")

        # Nothing happens if the current move is invalid
        if not self.play_board.valid_move(self.current_player, position):
            return

        # We switch players if the supposed current player has no valid moves (their playable pockets are empty)
        if self.play_board.empty_side(self.current_player):
            self.current_player = self.play_board.switch_player(self.current_player)

        # Performing the move and checking if the moving player landed in their mancala
        if not self.play_board.move(self.current_player, position):

            # We only switch players if the moving player did not land in their mancala
            self.current_player = self.play_board.switch_player(self.current_player)

        # Updating the boardGUI
        self.update_boardGUI()

        if self.play_board.check_end():
            self.root.grid_slaves(row=0, column=1)[0].configure(text="Game end")

    # Updates the text of the buttons and mancalas in the boardGUI
    def update_boardGUI(self):
        for i in range(6):
            widget = self.pocket_frame.grid_slaves(row=1, column=i)[0]
            widget.configure(text=self.play_board.board[i].simple_string())

            widget = self.pocket_frame.grid_slaves(row=0, column=i)[0]
            widget.configure(text=self.play_board.board[12 - i].simple_string())

        self.root.grid_slaves(row=1, column=2)[0].configure(text=self.play_board.board[6].simple_string())
        self.root.grid_slaves(row=1, column=0)[0].configure(text=self.play_board.board[13].simple_string())



