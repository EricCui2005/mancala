import tkinter as tk

class BoardGUI():

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.pocket_frame = tk.Frame(self.root)

        # Creating buttons to represent each of the playable pockets
        # b1_0 is player 1's first playable pocket, b1_1 is player 1's second playable pocket,
        # b2_0 is player 2's first playable pocket, b2_1 is player 2's second playable pocket, etc.
        self.b1_0 = tk.Button(self.pocket_frame, text="b1_0", font=('Arial', 10))
        self.b1_1 = tk.Button(self.pocket_frame, text="b1_1", font=('Arial', 10))
        self.b1_2 = tk.Button(self.pocket_frame, text="b1_2", font=('Arial', 10))
        self.b1_3 = tk.Button(self.pocket_frame, text="b1_3", font=('Arial', 10))
        self.b1_4 = tk.Button(self.pocket_frame, text="b1_4", font=('Arial', 10))
        self.b1_5 = tk.Button(self.pocket_frame, text="b1_5", font=('Arial', 10))

        self.b2_0 = tk.Button(self.pocket_frame, text="b2_0", font=('Arial', 10))
        self.b2_1 = tk.Button(self.pocket_frame, text="b2_1", font=('Arial', 10))
        self.b2_2 = tk.Button(self.pocket_frame, text="b2_2", font=('Arial', 10))
        self.b2_3 = tk.Button(self.pocket_frame, text="b2_3", font=('Arial', 10))
        self.b2_4 = tk.Button(self.pocket_frame, text="b2_4", font=('Arial', 10))
        self.b2_5 = tk.Button(self.pocket_frame, text="b2_5", font=('Arial', 10))

        self.pocket_frame.grid(row=0, column=0)

        # l1.grid(row=0, column=0, sticky=W, pady=2)

        self.b1_0.grid(row=1, column=0, padx=5, pady=5)
        self.b1_1.grid(row=1, column=1, padx=5, pady=5)
        self.b1_2.grid(row=1, column=2, padx=5, pady=5)
        self.b1_3.grid(row=1, column=3, padx=5, pady=5)
        self.b1_4.grid(row=1, column=4, padx=5, pady=5)
        self.b1_5.grid(row=1, column=5, padx=5, pady=5)

        self.b2_5.grid(row=0, column=0, padx=5, pady=5)
        self.b2_4.grid(row=0, column=1, padx=5, pady=5)
        self.b2_3.grid(row=0, column=2, padx=5, pady=5)
        self.b2_2.grid(row=0, column=3, padx=5, pady=5)
        self.b2_1.grid(row=0, column=4, padx=5, pady=5)
        self.b2_0.grid(row=0, column=5, padx=5, pady=5)


        self.root.mainloop()

BoardGUI()