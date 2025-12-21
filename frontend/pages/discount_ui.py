import tkinter as tk
from tkinter import ttk
from backend.converters.discount import calc_discount
from frontend.styles import styling


class DiscountConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Discount Calculator")
        self.root.minsize(500, 375)

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):
        self.label = ttk.Label(
            self.root,
            text="Discount Calculator",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Add UI elements here

        # Price entry handler
        ttk.Label(self.main_frame, text="Enter Price").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.entry1 = ttk.Entry(self.main_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # The Discount label and it's entry field
        ttk.Label(self.main_frame, text="Enter Discount Percent").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.entry2 = ttk.Entry(self.main_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.answer = ttk.Label(
            self.main_frame, text="Final Price : 0", font=("Tahoma", 12)
        )
        self.answer.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Convert & GO back buttons
        ttk.Button(self.main_frame, text="Go Back", command=self.go_back).grid(
            row=3, column=0, padx=10, pady=15, sticky="ew"
        )
        ttk.Button(
            self.main_frame,
            text="Calculate Discount",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=3, column=1, padx=10, pady=15, sticky="ew")

        for row in range(3):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    # Getting values entered from the user
    def get_user_input(self):
        price = self.entry1.get().strip()
        discount_percent = self.entry2.get().strip()

        checks = []
        if not price.isdigit():
            self.answer.config(text="Invalid price input, Numbers ONLY!")
            checks.append(False)
        else:
            checks.append(True)

        if not discount_percent.isdigit():
            self.answer.config(text="Invalid discount percent input, Numbers ONLY!")
            checks.append(False)
        else:
            checks.append(True)

        if checks[0] is False and checks[1] is False:
            return None, None

        if checks[0] is False:
            return None, None

        if checks[1] is False:
            return None, None

        price = float(price)
        discount_percent = float(discount_percent)

        return price, discount_percent

    def convert(self):
        price, discount_percent = self.get_user_input()
        if price is None or discount_percent is None:
            return

        discounted_price = calc_discount(price, discount_percent)

        self.answer.config(text=f"Your Answer: {discounted_price: .2f} %")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    app = DiscountConverter()
