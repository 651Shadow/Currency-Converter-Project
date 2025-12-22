import tkinter as tk
from tkinter import ttk
from backend.converters.time import convert_time
from frontend.constants.data_constants import TIME_UNITS
from frontend.styles import styling


class TimeConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Time Converter")
        self.root.minsize(500, 375)

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):

        self.label = ttk.Label(
            self.root,
            text="Time Calculator",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        ttk.Label(self.main_frame, text="Time Calculator").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.time_entry = ttk.Entry(self.main_frame)

        self.time_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # The from time conversion
        ttk.Label(self.main_frame, text="Enter From time").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.from_box = ttk.Combobox(self.main_frame, values=TIME_UNITS, state="readonly")
        self.from_box.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.from_box.current(0)

        # The to time conversion
        ttk.Label(self.main_frame, text="Enter To time").grid(
            row=2, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.to_box = ttk.Combobox(self.main_frame, values=TIME_UNITS, state="readonly")
        self.to_box.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.to_box.current(1)

        self.answer_label = ttk.Label(
            self.main_frame, text="Time converted --> ", font=("Tahoma", 12)
        )
        self.answer_label.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew"
        )

        # The Entry and backward buttons
        ttk.Button(self.main_frame, command=self.go_back, text="Go Back").grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )
        ttk.Button(
            self.main_frame,
            text="Convert Time",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        for row in range(4):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    def get_user_input(self):
        time = self.time_entry.get().strip()
        from_unit = self.from_box.get()
        to_unit = self.to_box.get()

        return time, from_unit, to_unit

    def convert(self):
        time_str, from_unit, to_unit = self.get_user_input()

        if not time_str.isdigit():
            self.answer_label.config(text="Invalid input. Please enter a valid number.")
            return

        if from_unit == to_unit:
            self.answer_label.config(
                text="From and To conversion Units are the same, Try again"
            )
            return

        time = float(time_str)
        result = convert_time(time, from_unit, to_unit)

        self.answer_label.config(text=f"Time converted --> {result} {to_unit}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    app = TimeConverter()
