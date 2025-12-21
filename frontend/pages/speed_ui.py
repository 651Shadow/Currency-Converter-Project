import tkinter as tk
from tkinter import ttk
from backend.converters.speed import speed_converter
from frontend.constants.data_constants import SPEED_VALUES
from frontend.styles import styling


class SpeedConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Speed Calculator")
        self.root.minsize(500, 375)

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):
        # Label of the page
        self.page_label = ttk.Label(
            self.root,
            padding=20,
            font=("Arial", 20, "bold"),
            text="Speed Calculator",
        )
        self.page_label.pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Distance entry handler and Create input fields
        ttk.Label(self.main_frame, text="Enter distance").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.distance_entry = ttk.Entry(self.main_frame)
        self.distance_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Create a label for the time unit drop-down menu
        ttk.Label(self.main_frame, text="Select time unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.time_unit = ttk.Combobox(
            self.main_frame, values=SPEED_VALUES, state="readonly"
        )
        self.time_unit.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.time_unit.current(1)

        # Create a label for conversion speed unit
        ttk.Label(self.main_frame, text="Convert speed to").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.conversion_speed_unit = ttk.Combobox(
            self.main_frame, values=SPEED_VALUES, state="readonly"
        )
        self.conversion_speed_unit.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.conversion_speed_unit.current(0)

        # Answer Label
        self.answer_label = ttk.Label(
            self.main_frame, text="Speed result will appear here --> "
        )
        self.answer_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w"
        )

        self.convert_btn = ttk.Button(
            self.main_frame,
            text="Calculate",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        self.go_back_btn = tk.Button(self.main_frame, text="Go Back").grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )

        for row in range(4):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    def get_user_input(self):
        distance = self.distance_entry.get()
        time_unit = self.time_unit.get()
        conversion_speed_unit = self.conversion_speed_unit.get()

        return distance, time_unit, conversion_speed_unit

    def convert(self):
        distance_str, time_unit, conversion_speed_unit = self.get_user_input()

        if not distance_str.isdigit():
            self.answer_label.config(text="Invalid distance, numbers ONLY!")
            return

        distance = float(distance_str)

        result = speed_converter(distance, time_unit, conversion_speed_unit)

        self.answer_label.config(text=f"Answer --> {result} {conversion_speed_unit}")


if __name__ == "__main__":
    SpeedConverter()
