import tkinter as tk

class BoardGUI():

    def __init__(self):

        # Initializing the root window, its geometry, and configuring its grid for the purposes of
        # subsequent frame centering
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Initializing a frame to nicely place the playable pocket buttons into
        self.pocket_frame = tk.Frame(self.root)

        # Initializing a list to hold the buttons for iterative placement into the pocket_frame grid
        self.playable_pockets = []

        # Placing pocket_frame into root (and leveraging row and column configuration to center it)
        self.pocket_frame.grid(row=0, column=0)

        for i in range(6):
            self.playable_pockets.append(tk.Button(self.pocket_frame, text=f"b1_{i}", font=('Arial', 10)))
        for i in range(6):
            self.playable_pockets[i].grid(row=1, column=i, padx=5, pady=5)

        for i in range(6):
            self.playable_pockets.append(tk.Button(self.pocket_frame, text=f"b2_{5 - i}", font=('Arial', 10)))
        for i in range(6):
            self.playable_pockets[i + 6].grid(row=0, column=i, padx=5, pady=5)

        self.root.mainloop()

BoardGUI()
