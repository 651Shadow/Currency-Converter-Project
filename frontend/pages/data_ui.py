import tkinter as tk
from tkinter import ttk

from backend.converters.data_unit import convert_data_unit
from frontend.constants.data_constants import DATA_VALUES
from frontend.styles import styling


class DataConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.minsize(500, 375)
        self.root.title("Data Converter")

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):

        self.label = ttk.Label(
            self.root,
            text="Data Converter",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # User Input number to convert
        ttk.Label(self.main_frame, text="Enter Data Size").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(
            row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew"
        )

        # User Input unit to convert from
        ttk.Label(self.main_frame, text="From Unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.convert_from = ttk.Combobox(
            self.main_frame, values=DATA_VALUES, state="readonly"
        )
        self.convert_from.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.convert_from.current(0)

        # User Input unit to convert to
        ttk.Label(self.main_frame, text="To Unit").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.convert_to = ttk.Combobox(
            self.main_frame, values=DATA_VALUES, state="readonly"
        )
        self.convert_to.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.convert_to.current(1)

        # Result label
        self.result_label = ttk.Label(
            self.main_frame, text="Your result will be here --> ", font=("Tahoma", 12)
        )
        self.result_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=(10, 20), sticky="w"
        )

        # Convert button
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
        amount = self.amount_entry.get().strip()
        from_input = self.convert_from.get()
        to_input = self.convert_to.get()

        return amount, from_input, to_input

    def convert(self):
        amount_str, from_input, to_input = self.get_user_input()

        # Implement conversion logic here
        if not amount_str.isdigit():
            self.result_label.config(text="Invalid input, Try again")
            return

        if from_input == to_input:
            self.result_label.config(
                text="From and To conversion Units are the same, Try again"
            )
            return

        amount = float(amount_str)

        result = convert_data_unit(amount, from_input, to_input)
        self.result_label.config(text=f"Your result: {result:.2f} {to_input} ")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    app = DataConverter()
