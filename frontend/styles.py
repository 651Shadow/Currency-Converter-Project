from tkinter import ttk

def styling(root):
    root.tk.call("source", "frontend/theme/theme.tcl")
    ttk.Style().theme_use("forest-dark")