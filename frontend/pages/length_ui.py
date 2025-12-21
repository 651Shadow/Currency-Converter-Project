import tkinter as tk
from tkinter import ttk
from backend.converters.length import length_converter
from frontend.constants.data_constants import LENGTHS


class DiscountConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Length Calculator")
        self.root.minsize(500, 375)

        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        self.label = ttk.Label(
            self.root,
            text="Length Calculator",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # UI elements

        # Length entry handler
        ttk.Label(self.main_frame, text="Enter length").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.length_entry = ttk.Entry(self.main_frame)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # The length data type drop-down menu
        ttk.Label(self.main_frame, text="Enter the number unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.unit_entry = ttk.Combobox(
            self.main_frame, values=LENGTHS, state="readonly"
        )
        self.unit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.unit_entry.current(0)

        # The conversion unit drop-down menu
        ttk.Label(self.main_frame, text="Enter the conversion unit").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.conversion_unit_entry = ttk.Combobox(
            self.main_frame, values=LENGTHS, state="readonly"
        )
        self.conversion_unit_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.conversion_unit_entry.current(1)

        # Answer label
        self.answer = ttk.Label(
            self.main_frame, text="Final Length --> ", font=("Tahoma", 12)
        )
        self.answer.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Convert & GO back buttons
        ttk.Button(self.main_frame, text="Go Back").grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )

        ttk.Button(
            self.main_frame,
            text="Calculate Length",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        for row in range(4):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    # Getting values entered from the user
    def get_user_input(self):
        length = self.length_entry.get().strip()
        unit = self.unit_entry.get().strip()
        conversion_unit = self.conversion_unit_entry.get().strip()

        return length, unit, conversion_unit

    def convert(self):
        length_str, unit, conversion_unit = self.get_user_input()

        if not length_str.isdigit():
            self.answer.config(text="Invalid Amount, Only Digits")
            return

        length = float(length_str)

        converted_length = length_converter(length, unit, conversion_unit)

        self.answer.config(
            text=f"Final Length: {converted_length: .2f} {conversion_unit}"
        )


if __name__ == "__main__":
    app = DiscountConverter()
