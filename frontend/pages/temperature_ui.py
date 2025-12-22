import tkinter as tk
from tkinter import ttk
from backend.converters.temperature import Temperature_convert
from frontend.constants.data_constants import TEMP_VALUES
from frontend.styles import styling


class TemperatureConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Temperature Converter")
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
            text="Temperature Converter",
        )
        self.page_label.pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Temperature entry handler and Create input fields
        ttk.Label(self.main_frame, text="Enter temperature").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.temp_entry = ttk.Entry(self.main_frame)
        self.temp_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Create a label for the unit and drop-down menu
        ttk.Label(self.main_frame, text="Select unit").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.unit_entry = ttk.Combobox(
            self.main_frame, values=TEMP_VALUES, state="readonly"
        )
        self.unit_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.unit_entry.current(1)

        # Create a label for the conversion to unit and drop-down menu
        ttk.Label(self.main_frame, text="Convert to unit").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.conversion_unit = ttk.Combobox(
            self.main_frame, values=TEMP_VALUES, state="readonly"
        )
        self.conversion_unit.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.conversion_unit.current(0)

        # Answer Label
        self.answer_label = ttk.Label(
            self.main_frame, text="Temperature will go here --> "
        )
        self.answer_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w"
        )

        self.convert_btn = ttk.Button(
            self.main_frame,
            text="Convert",
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
        temp = self.temp_entry.get()
        unit = self.unit_entry.get()
        conversion_unit = self.conversion_unit.get()

        return temp, unit, conversion_unit

    def convert(self):
        temp_str, unit, conversion_unit = self.get_user_input()

        if not temp_str.isdigit():
            self.answer_label.config(text="Invalid input, Numbers ONLY!")
            return

        if unit == conversion_unit:
            self.answer_label.config(
                text="From and To conversion Units are the same, Try again"
            )
            return

        temp = float(temp_str)

        result = Temperature_convert(temp, unit, conversion_unit)

        self.answer_label.config(text=f"Answer --> {result} {conversion_unit}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    TemperatureConverter()
