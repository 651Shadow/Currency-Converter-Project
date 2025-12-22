import tkinter as tk
from tkinter import ttk

from backend.converters.mass import convert_mass
from frontend.styles import styling
from frontend.constants.data_constants import MASS_VALUES


class MassConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.minsize(500, 375)
        self.root.title("Mass Converter")

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):

        self.label = ttk.Label(
            self.root,
            text="Mass Converter",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        ttk.Label(self.main_frame, text="Enter Data Size").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.mass_entry = ttk.Entry(self.main_frame)
        self.mass_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        ttk.Label(self.main_frame, text="From Unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.convert_from = ttk.Combobox(
            self.main_frame, values=MASS_VALUES, state="readonly"
        )
        self.convert_from.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.convert_from.current(0)

        ttk.Label(self.main_frame, text="To Unit").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.convert_to = ttk.Combobox(
            self.main_frame, values=MASS_VALUES, state="readonly"
        )
        self.convert_to.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.convert_to.current(1)

        self.result_label = ttk.Label(
            self.main_frame, text="Your result will be here --> ", font=("Tahoma", 12)
        )
        self.result_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=(10, 20), sticky="w"
        )

        self.convert_button = ttk.Button(
            self.main_frame,
            text="Convert",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        self.go_back_button = ttk.Button(
            self.main_frame, text="Go Back", command=self.go_back
        ).grid(row=4, column=0, padx=10, pady=15, sticky="ew")

        for r in range(4):
            self.main_frame.rowconfigure(r, weight=1)
        for c in range(2):
            self.main_frame.columnconfigure(c, weight=1)

    def get_user_input(self):
        amount = self.mass_entry.get().strip()
        from_input = self.convert_from.get()
        to_input = self.convert_to.get()

        return amount, from_input, to_input

    def convert(self):
        amount_str, from_input, to_input = self.get_user_input()

        if not amount_str.isdigit():
            self.result_label.config(text="Invalid input, Try again")
            return

        if from_input == to_input:
            self.result_label.config(text="From and To Units are the same")
            return

        amount = float(amount_str)

        result = convert_mass(amount, from_input, to_input)
        self.result_label.config(text=f"Your result: {result:.2f} {to_input} ")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()

        App(tk.Tk())


if __name__ == "__main__":
    app = MassConverter()
