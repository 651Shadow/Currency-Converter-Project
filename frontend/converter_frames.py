import tkinter as tk
from tkinter import ttk


class Converter_frames:
    def __init__(self, root):
        self.root = root
        self.root.title("App Converter")

        self.txt = ttk.Label(root, text="Converter App!", font=("Tahoma", 23, "bold"))
        self.txt.pack(pady="25")

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        self.create_buttons()

    def create_buttons(self):
        # Getting all buttons with there photos (soon)
        buttons = [
            "Currency",
            "Mass",
            "Area",
            "Length",
            "Time",
            "Data",
            "Volume",
            "Temperature",
            "Speed",
            "Discount Calculator",
            "Numerical Systems",
        ]

        row = 0
        column = 0

        for btnName in buttons:
            btn = ttk.Button(self.main_frame, text=btnName, style="Accent.TButton")
            btn.grid(row=row, column=column, padx=25, pady=25, sticky="nsew")

            column += 1

            if column == 3:
                column = 0
                row += 1

        # Making the buttons expand in rows and in column while expanding our root ####
        for col in range(3):
            self.main_frame.columnconfigure(col, weight=1)

        for row in range(row + 1):
            self.main_frame.rowconfigure(row, weight=1)
