import tkinter as tk
from tkinter import ttk, messagebox


class DynamicVolumeConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Dynamic Volume Converter")
        self.title_label = ttk.Label(
            master,
            text="Volume Unit Converter (Dynamic)",
            font=("Helvetica", 16, "bold"),
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.factors = {
            "m³ (Cubic Meters)": 1.0,
            "Liters": 0.001,
            "mL (Milliliters)": 0.000001,
            "Gallons (US liquid)": 0.00378541,
            "Gallons (UK imperial)": 0.00454609,
            "ft³ (Cubic Feet)": 0.0283168,
            "in³ (Cubic Inches)": 0.0000163871,
            "yd³ (Cubic Yards)": 0.764555,
        }
        self.units = list(self.factors.keys())
        self.input_value = tk.DoubleVar(value=1.0)
        self.input_unit = tk.StringVar(value="Liters")
        self.output_unit = tk.StringVar(value="Gallons (US liquid)")
        self.output_value_str = tk.StringVar(value="0.00 Gallons (US liquid)")
        self.create_widgets()
        self.setup_variable_tracing()

    def create_widgets(self):
        ttk.Label(self.master, text="Volume Value:", font=("Helvetica", 10)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.value_entry = ttk.Entry(
            self.master, textvariable=self.input_value, width=25, justify="right"
        )
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self.master, text="From Unit:", font=("Helvetica", 10)).grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        self.from_unit_menu = ttk.Combobox(
            self.master,
            textvariable=self.input_unit,
            values=self.units,
            state="readonly",
            width=22,
        )
        self.from_unit_menu.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(self.master, text="To Unit:", font=("Helvetica", 10)).grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        self.to_unit_menu = ttk.Combobox(
            self.master,
            textvariable=self.output_unit,
            values=self.units,
            state="readonly",
            width=22,
        )
        self.to_unit_menu.grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(
            self.master, text="Converted Result:", font=("Helvetica", 10, "bold")
        ).grid(row=4, column=0, padx=5, pady=10, sticky="w")
        self.result_label = ttk.Label(
            self.master,
            textvariable=self.output_value_str,
            font=("Helvetica", 14, "bold"),
            foreground="purple",
        )
        self.result_label.grid(row=4, column=1, padx=5, pady=10, sticky="w")
        self.convert()

    def setup_variable_tracing(self):
        """Sets up the variables to call the convert method automatically upon change."""
        self.input_value.trace_add("write", lambda *args: self.convert())
        self.input_unit.trace_add("write", lambda *args: self.convert())
        self.output_unit.trace_add("write", lambda *args: self.convert())
        self.value_entry.bind("<KeyRelease>", lambda event: self.convert())

    def convert(self, *args):
        """Performs the volume conversion logic: Input -> m³ -> Output."""
        try:
            value = self.input_value.get()
            from_unit = self.input_unit.get()
            to_unit = self.output_unit.get()
            if from_unit not in self.factors or to_unit not in self.factors:
                self.output_value_str.set("Invalid Unit Selection")
                return
            value_in_cub_meters = value * self.factors[from_unit]
            converted_value = value_in_cub_meters / self.factors[to_unit]
            self.output_value_str.set(f"{converted_value:,.6f} {to_unit}")
        except tk.TclError:
            self.output_value_str.set("Invalid Input")
            try:
                self.input_value.set(1.0)
            except:
                pass
        except Exception as e:
            self.output_value_str.set("Error")
            print(f"Conversion Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DynamicVolumeConverterApp(root)
    root.mainloop()
