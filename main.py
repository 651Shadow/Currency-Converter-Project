import tkinter as tk
from frontend.gui_main import App


class Main:
    def __init__(self):
        self.root = tk.Tk()
        App(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    Main()
