import tkinter as tk
from tkinter import ttk


class Discount_ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Discount Calculator")
        self.root.minsize(500, 350)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):
        self.label = ttk.Label(
            self.root,
            text="Discount Calculator",
            padding=20,
            font=("Tahoma", 20, "bold"),
        ).pack()

        self.discount_frame = ttk.Frame(self.root, padding=20)
        self.discount_frame.pack(fill="both", expand=True)

        # The Enter Price label and the entry field
        ttk.Label(self.discount_frame, text="Enter Price").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.entry1 = ttk.Entry(self.discount_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # The Discount label and it's entry field
        ttk.Label(self.discount_frame, text="Enter Discount Percent").grid(
            row=1, column=0, padx=5, pady=(10, 20), sticky="w"
        )
        self.entry2 = ttk.Entry(self.discount_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.answer = ttk.Label(
            self.discount_frame, text="Final Price : 0", font=("Tahoma", 12)
        )
        self.answer.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # The Entry and backward buttons
        ttk.Button(self.discount_frame, text="Go Back").grid(
            row=3, column=0, padx=10, pady=15, sticky="ew"
        )
        ttk.Button(
            self.discount_frame,
            text="Calculate Discount",
            command=self.calc_discount,
        ).grid(row=3, column=1, padx=10, pady=15, sticky="ew")

        for row in range(3):
            self.discount_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.discount_frame.columnconfigure(col, weight=1)

    # Getting values entered from the user
    def get_user_input(self):
        price = self.entry1.get().strip()
        discount_percent = self.entry2.get().strip()

        return price, discount_percent

    # Discount Calculation Function
    def calc_discount(self):
        price, discount_percent = self.get_user_input()

        # Check whether price, discount percent is not a number
        if not price.isdigit():
            self.answer.config(text="Invalid price input, Numbers ONLY!")
            return
        if not discount_percent.isdigit():
            self.answer.config(text="Invalid discount percent input, Numbers ONLY!")
            return

        price = float(price)
        discount_percent = float(discount_percent)

        # Calculate the discounted price given the original price and discount percentage
        if discount_percent < 0 or discount_percent >= 100:
            self.answer.config(
                text="Invalid discount percent, must be between 0 and 100"
            )
            return

        # Calculate the discount amount
        discount = (discount_percent / 100) * price
        discounted_price = price - discount

        self.answer.config(text=f"Your Answer: {discounted_price: .2f}")


app = Discount_ui()
