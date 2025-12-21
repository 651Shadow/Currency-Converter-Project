# Placeholder module for the Conversion Calculator project.
import tkinter as tk
from tkinter import ttk

from frontend.converter_frames import Converter_frames
from frontend.styles import styling


class App:
    def __init__(self, root):
        self.root = root

        styling(self.root)
        Converter_frames(self.root)


if __name__ == "__main__":
    App()
