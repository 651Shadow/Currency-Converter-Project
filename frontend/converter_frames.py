import tkinter as tk
from tkinter import ttk

from frontend.pages.currency_ui import CurrencyConverter

from frontend.pages.mass_ui import MassConverter
from frontend.pages.area_ui import AreaConverter
from frontend.pages.length_ui import LengthConverter
from frontend.pages.time_ui import TimeConverter
from frontend.pages.data_ui import DataConverter

# from frontend.pages.volume_ui import VolumeConverter
from frontend.pages.temperature_ui import TemperatureConverter
from frontend.pages.speed_ui import SpeedConverter
from frontend.pages.discount_ui import DiscountConverter
from frontend.pages.binary_ui import BinaryConverter

# from frontend.pages.numerial_ui import NumerialConverter

# Getting all buttons with their class to implement layout
buttons = {
    "Currency": CurrencyConverter,
    "Mass": MassConverter,
    "Area": AreaConverter,
    "Length": LengthConverter,
    "Time": TimeConverter,
    "Data": DataConverter,
    "Volume": None,
    "Temperature": TemperatureConverter,
    "Speed": SpeedConverter,
    "Discount Calculator": DiscountConverter,
    "Binary": BinaryConverter,
    "Numerical Systems": None,
}


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
        row = 0
        column = 0

        for btnName, btnFactionalty in buttons.items():
            btn = ttk.Button(
                self.main_frame,
                text=btnName,
                style="Accent.TButton",
                command=lambda f=btnFactionalty: self.navigate_to(f),
            )
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

    def navigate_to(self, navigate_to):
        self.root.destroy()
        navigate_to()
