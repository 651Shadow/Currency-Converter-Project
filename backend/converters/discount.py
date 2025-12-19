import tkinter as tk
from tkinter import ttk


class Discount_ui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Discount Calculator")

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
            row=0, column=0, padx=5, pady=5, sticky="nsew"
        )
        self.entry1 = ttk.Entry(self.discount_frame)
        self.entry1.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # The Discount label and it's entry field
        ttk.Label(self.discount_frame, text="Enter Discount Percent").grid(
            row=1, column=0, padx=5, pady=5, sticky="nsew"
        )
        self.entry2 = ttk.Entry(self.discount_frame)
        self.entry2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.answer = ttk.Label(
            self.discount_frame, text="Final Price : 0", font=("Tahoma", 12)
        )
        self.answer.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # The Entry and backward buttons
        ttk.Button(self.discount_frame, text="Go Back").grid(
            row=3, column=0, padx=5, pady=5, sticky="nsew"
        )
        ttk.Button(
            self.discount_frame,
            text="Calculate Discount",
            command=self.calc_discount,
        ).grid(row=3, column=1, padx=4, pady=5, sticky="nsew")

        for row in range(3):
            self.discount_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.discount_frame.columnconfigure(col, weight=1)

    # Getting values entered from the user
    def get_user_input(self):
        # TODO: Add validation for empty inputs and incorrect characters (Abdelrahman)

        price = self.entry1.get()
        discount_percent = self.entry2.get()
        return price, discount_percent

    # Discount Calculation Function
    def calc_discount(self):
        price, discount_percent = self.get_user_input()

        # Calculate the discounted price given the original price and discount percentage
        if discount_percent < 0 or discount_percent >= 100:
            raise ValueError("Discount percent must be between 0 and 100")

        # Calculate the discount amount
        discount = (discount_percent / 100) * price
        discounted_price = price - discount

        self.answer.config(text=f"Your Answer: {discounted_price: .2f}")


app = Discount_ui()
