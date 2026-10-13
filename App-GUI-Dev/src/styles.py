import tkinter as tk 
from  tkinter import ttk

class Styles:
    def __init__(self, root):
        self.root = root
        self.theme_active = "dark"

        self.colors = {
            "dark": {
                "bg": "#222222",
                "fg": "#CCCCCC"
            }
        }
