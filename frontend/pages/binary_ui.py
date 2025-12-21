import tkinter as tk
from tkinter import ttk
from backend.converters.binary import text_to_binary
from frontend.styles import styling


class BinaryConverter:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Binary Converter")
        self.root.minsize(500, 375)

        styling(self.root)

        self.build_ui()

        self.root.mainloop()

    def build_ui(self):
        # Add Ui elements here

        self.page_label = ttk.Label(
            self.root,
            padding=20,
            font=("Arial", 20, "bold"),
            text="Binary Converter",
        )
        self.page_label.pack()

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(fill="both", expand=True)

        # Input field and label
        ttk.Label(self.main_frame, text="Enter text / binary").grid(
            row=0, column=0, padx=5, pady=(10, 20), sticky="w"
        )

        self.input_entry = ttk.Entry(self.main_frame)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Answer Label
        self.answer_label = ttk.Label(
            self.main_frame, text="Result will appear here --> "
        )
        self.answer_label.grid(
            row=1, columnspan=2, column=0, padx=5, pady=5, sticky="w"
        )

        # Convert and Go Back Buttons
        ttk.Button(
            self.main_frame,
            text="Convert",
            style="Accent.TButton",
            command=self.convert,
        ).grid(row=2, column=1, padx=10, pady=15, sticky="ew")

        ttk.Button(self.main_frame, text="Go Back", command=self.go_back).grid(
            row=2, column=0, padx=10, pady=15, sticky="ew"
        )

        # Grid Stretch
        for row in range(2):
            self.main_frame.rowconfigure(row, weight=1)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

    def get_user_input(self):
        text = self.input_entry.get().strip()
        return text

    def convert(self):
        text_input = self.get_user_input()

        if not text_input.strip():
            self.answer_label.config(text="Wrong input, Try again")
            return

        text = str(text_input)
        result = text_to_binary(text)

        self.answer_label.config(text=f"Answer --> {result}")

    def go_back(self):
        from frontend.gui_main import App

        self.root.destroy()
        App(tk.Tk())


if __name__ == "__main__":
    BinaryConverter()
