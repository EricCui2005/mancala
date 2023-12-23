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

        # Initializing the internal representation of the game board
        self.play_board = play_board

        # Iteratively placing the buttons into the pocket_frame grid
        for i in range(6):

            # Placing buttons for player1
            current_pocket = self.play_board.board[i]
            self.current_button = tk.Button(self.pocket_frame, text=current_pocket.simple_string(), font=('Arial', 10), height=2, width=8, command=lambda: self.button_move(True, current_pocket))
            self.current_button.grid(row=1, column=i, padx=5, pady=5)

            # Placing buttons for player2
            current_pocket = self.play_board.board[12 - i]
            self.current_button = tk.Button(self.pocket_frame, text=current_pocket.simple_string(), font=('Arial', 10), height=2, width=8, command=lambda: self.button_move(True, current_pocket))
            self.current_button.grid(row=0, column=i, padx=5, pady=5)

        # Placing mancalas
        self.mancala_1 = tk.Label(self.root, text=self.play_board.board[6].simple_string(), font=('Arial', 20))
        self.mancala_2 = tk.Label(self.root, text=self.play_board.board[13].simple_string(), font=('Arial', 20))

        # Formatting
        self.mancala_1.grid(row=1, column=2, padx=50)
        self.mancala_2.grid(row=1, column=0, padx=50)

        self.root.mainloop()


    def button_move(self, legal, pocket):
        """
        Function that is called when the user clicks on a pocket button
        :param legal: (bool) True if clicking the button (and consequently the move associated with it)
        is legal given the current game state
        :param pocket: (class Pocket) The Pocket we are moving from
        :return:
        """
        if legal == True:
            print(f"Moving pocket {pocket.get_position()}")
            self.play_board.move(pocket.get_player(), pocket.get_position())
            self.update_boardGUI()

    # Updates the text of the buttons and mancalas in the boardGUI
    def update_boardGUI(self):

        for i in range(6):
            widget = self.pocket_frame.grid_slaves(row=1, column=i)[0]
            widget.configure(text=self.play_board.board[i].simple_string())

            widget = self.pocket_frame.grid_slaves(row=0, column=i)[0]
            widget.configure(text=self.play_board.board[12 - i].simple_string())

        self.root.grid_slaves(row=1, column=2)[0].configure(text=self.play_board.board[6].simple_string())
        self.root.grid_slaves(row=1, column=0)[0].configure(text=self.play_board.board[13].simple_string())



