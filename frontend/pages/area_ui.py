import tkinter as tk
from tkinter import ttk
from backend.converters.area import convert_area
from frontend.constants.data_constants import AREAS


class AreaConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Area Converter")
        self.root.minsize(500, 375)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):
        self.label = ttk.Label(
            self.root,
            text="Area Converter",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Add UI elements here

        # Price entry handler
        ttk.Label(self.main_frame, text="Enter Amount").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Drop-down From Area menu
        ttk.Label(self.main_frame, text="Select From Area").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.from_area_combobox = ttk.Combobox(
            self.main_frame, values=AREAS, state="readonly"
        )
        self.from_area_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.from_area_combobox.current(0)

        # Drop-down To Area menu
        ttk.Label(self.main_frame, text="Select To Area").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.to_area_combobox = ttk.Combobox(
            self.main_frame, values=AREAS, state="readonly"
        )
        self.to_area_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.to_area_combobox.current(1)

        # Answer Label
        self.answer_label = ttk.Label(
            self.main_frame, text="Answer will appear here --> ", font=("Tahoma", 12)
        )
        self.answer_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew"
        )

        # Convert & GO back buttons
        ttk.Button(self.main_frame, text="Go Back").grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )
        ttk.Button(self.main_frame, text="Convert", command=self.convert).grid(
            row=4, column=1, padx=10, pady=15, sticky="ew"
        )

        # Making rows and columns dynamic
        for row in range(4):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    def get_user_input(self):
        amount = self.amount_entry.get().strip()
        from_area = self.from_area_combobox.get()
        to_area = self.to_area_combobox.get()

        return amount, from_area, to_area

    def convert(self):
        amount_str, from_area, to_area = self.get_user_input()

        # checking whether the amount is a valid number
        if not amount_str.isdigit():
            self.answer_label.config(text="Invalid Amount, Only Digits")
            return

        amount = float(amount_str)
        result = convert_area(amount, from_area, to_area)

        self.answer_label.config(text=f"Your Answer --> {result} {to_area}")


if __name__ == "__main__":
    app = AreaConverter()
