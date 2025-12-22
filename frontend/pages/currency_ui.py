import tkinter as tk
from tkinter import ttk

from frontend.constants.data_constants import CURRENCIES
from backend.converters.currency import convert_currency
from frontend.styles import styling


class CurrencyConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Length Calculator")
        self.root.minsize(500, 375)

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):

        self.label = ttk.Label(
            self.root,
            text="Currency Converter",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Add UI elements here

        # Price entry handler
        ttk.Label(self.main_frame, text="Enter Amount").grid(
            row=0, column=0, sticky="w"
        )
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Drop-down To Currency manu
        ttk.Label(self.main_frame, text="Select From Currency").grid(
            row=1, column=0, sticky="w"
        )

        self.from_currency_combobox = ttk.Combobox(
            self.main_frame, values=CURRENCIES, state="readonly"
        )
        self.from_currency_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.from_currency_combobox.current(0)

        # Drop-down To Currency menu
        ttk.Label(self.main_frame, text="Select To Currency").grid(
            row=2, column=0, sticky="w"
        )

        self.to_currency_combobox = ttk.Combobox(
            self.main_frame, values=CURRENCIES, state="readonly"
        )
        self.to_currency_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.to_currency_combobox.current(1)

        # Answer Label
        self.answer_label = ttk.Label(
            self.main_frame, text="Answer will appear here --> "
        )
        self.answer_label.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Convert & GO back buttons
        ttk.Button(
            self.main_frame,
            text="Convert",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=4, column=1, padx=10, pady=15, sticky="ew")

        ttk.Button(self.main_frame, text="Go Back", command=self.go_back).grid(
            row=4, column=0, padx=10, pady=15, sticky="ew"
        )

        # Making rows and columns dynamic
        for r in range(4):
            self.main_frame.rowconfigure(r, weight=1)
        for c in range(2):
            self.main_frame.columnconfigure(c, weight=1)

    # Getting all user inputs
    def get_user_input(self):
        amount = self.amount_entry.get()
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()

        return amount, from_currency, to_currency

    def convert(self):
        amount_str, from_currency, to_currency = self.get_user_input()

        # checking whether the amount is a valid number
        if not amount_str.isdigit():
            self.answer_label.config(text="Invalid Amount, Only Digits")
            return

        if from_currency == to_currency:
            self.answer_label.config(text="From and To conversion units are the same")
            return

        amount = float(amount_str)
        result = convert_currency(amount, from_currency, to_currency)

        self.answer_label.config(text=f"Your Answer --> {result} {to_currency}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    app = CurrencyConverter()
