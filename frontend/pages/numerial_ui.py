import tkinter as tk
from tkinter import ttk
from frontend.styles import styling

from backend.converters.numeral import numeral_converter
from frontend.constants.data_constants import NUMERIAL_VALUES


class NumerialConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.minsize(500, 380)
        self.root.title("Numerical Converter")

        styling(self.root)
        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        ttk.Label(
            self.root,
            text="Numerical Converter",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        ttk.Label(self.main_frame, text="Enter Decimal Number").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.num_entry = ttk.Entry(self.main_frame)
        self.num_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        ttk.Label(self.main_frame, text="Convert to").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.convert_from = ttk.Combobox(
            self.main_frame, values=NUMERIAL_VALUES, state="readonly"
        )
        self.convert_from.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.convert_from.current(0)

        self.result_label = ttk.Label(
            self.main_frame,
            text="Your result will appear here -->",
            font=("Tahoma", 12),
        )
        self.result_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=(10, 20), sticky="w"
        )

        ttk.Button(
            self.main_frame,
            text="Convert",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        ttk.Button(self.main_frame, text="Go Back", command=self.go_back).grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )

        for r in range(4):
            self.main_frame.rowconfigure(r, weight=1)
        for c in range(2):
            self.main_frame.columnconfigure(c, weight=1)

    def get_user_input(self):
        value = self.num_entry.get().strip()
        base_from = self.convert_from.get()

        return value, base_from

    def convert(self):
        value_str, base_from = self.get_user_input()

        if not value_str.isdigit():
            self.result_label.config(text="Invalid input for selected base!")
            return

        value = int(value_str)

        result = numeral_converter(value, base_from)

        self.result_label.config(text=f"Answer --> {result}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    NumerialConverter()
