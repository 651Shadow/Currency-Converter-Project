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

        # speed entry handler and Create input fields
        ttk.Label(self.main_frame, text="Enter Speed").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.speed_entry = ttk.Entry(self.main_frame)
        self.speed_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Create a label for the speed unit drop-down menu
        ttk.Label(self.main_frame, text="Select speed unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.speed_unit = ttk.Combobox(
            self.main_frame, values=SPEED_VALUES, state="readonly"
        )
        self.speed_unit.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.speed_unit.current(1)

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

        self.go_back_btn = tk.Button(
            self.main_frame, command=self.go_back, text="Go Back"
        ).grid(row=4, column=0, padx=10, pady=15, sticky="ew")

        for row in range(4):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    def get_user_input(self):
        speed = self.speed_entry.get().strip()
        speed_unit = self.speed_unit.get()
        conversion_speed_unit = self.conversion_speed_unit.get()

        return speed, speed_unit, conversion_speed_unit

    def convert(self):
        speed_str, speed_unit, conversion_speed_unit = self.get_user_input()

        if not speed_str.isdigit():
            self.answer_label.config(text="Invalid input, Numbers ONLY!")
            return

        if speed_unit == conversion_speed_unit:
            self.answer_label.config(
                text="From and To conversion Units are the same, Try again"
            )
            return

        speed = float(speed_str)

        result = speed_converter(speed, speed_unit, conversion_speed_unit)

        self.answer_label.config(text=f"Answer --> {result} {conversion_speed_unit}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    SpeedConverter()
