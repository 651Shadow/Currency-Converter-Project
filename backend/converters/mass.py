import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class MassConverter(tk.Tk):
    CONVERSION_FACTORS = {
        "mg": 1 / 1000,
        "g": 1.0,
        "kg": 1000.0,
        "lb": 453.59237,
        "oz": 28.349523,
        "ton": 907185.0,
    }
    UNITS = list(CONVERSION_FACTORS.keys())

    def __init__(self):
        super().__init__()

        self.title(" Mass Converter")

        self.geometry("700x300")
        self.resizable(False, False)

        self._create_widgets()

    def mass_convert(self):
        try:
            source_value = float(self.input_var.get())
            source_unit = self.source_unit_var.get()

            target_unit = self.target_unit_var.get()

            if not source_unit or not target_unit:
                showerror(
                    title="Error", message="Please select both source and target units."
                )
                return

            source_to_g_factor = self.CONVERSION_FACTORS[source_unit]

            base_value_in_grams = source_value * source_to_g_factor
            g_to_target_factor = 1.0 / self.CONVERSION_FACTORS[target_unit]

            target_value = base_value_in_grams * g_to_target_factor

            self.result_var.set(f"{target_value:,.4f} {target_unit}")

        except ValueError:
            showerror(
                title="Error", message="Invalid input. Please enter a valid number."
            )

        except KeyError:
            showerror(title="Error", message="Invalid unit selection.")

    def _create_widgets(self):
        self.input_var = tk.StringVar(value="")
        self.result_var = tk.StringVar(value="0.0000")

        self.source_unit_var = tk.StringVar(value="kg")
        self.target_unit_var = tk.StringVar(value="g")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Value:").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        ttk.Entry(self, textvariable=self.input_var, width=15).grid(
            row=0, column=1, padx=10, pady=5, sticky="ew"
        )
        ttk.Label(self, text="From Unit:").grid(
            row=1, column=0, padx=10, pady=5, sticky="w"
        )

        source_combo = ttk.Combobox(
            self,
            textvariable=self.source_unit_var,
            values=self.UNITS,
            state="readonly",
            width=10,
        )
        source_combo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="To Unit:").grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )

        target_combo = ttk.Combobox(
            self,
            textvariable=self.target_unit_var,
            values=self.UNITS,
            state="readonly",
            width=10,
        )
        target_combo.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ttk.Button(self, text="Convert Mass", command=self.mass_convert).grid(
            row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew"
        )

        ttk.Label(self, text="Result:").grid(
            row=4, column=0, padx=10, pady=5, sticky="w"
        )
        ttk.Label(self, textvariable=self.result_var, font=("Arial", 12, "bold")).grid(
            row=4, column=1, padx=10, pady=5, sticky="e"
        )


if __name__ == "__main__":
    app = MassConverter()
    app.mainloop()
