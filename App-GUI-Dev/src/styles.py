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
            },

            "light": {
                "bg": "#EEEEEE",
                "fg": "#111111"
            },

            "vintage": {
                "bg": "A48D47",
                "fg": "#FFEDB7"
            }
        }


    def apply_theme(self):
        color_bg = self.colors[self.theme_active]["bg"]
        color_fg = self.colors[self.theme_active]["fg"]

        self._apply_tk_colors(self.root, color_bg, color_fg)
        self._apply_ttk_colors(color_bg, color_fg)


    def _apply_tk_colors(self, widget, color_bg, color_fg):
        try:
            if isinstance(widget, tk.Button):
                widget.configure(activebackground=color_fg)
                widget.configure(activeforeground=color_bg)
            
            widget.configure(bg=color_bg)
            print(f"child= {widget} color: {color_bg}")
            #widget.configure(fg=color_fg)
            print("2..")
            widget.configure(bg=color_bg, fg=color_fg)
        except tk.TclError:
            print("Error al aplicar estilos a tk")
            pass 

            for child in widget.winfo_children():
                print(f"child: {child}")
                self._apply_tk_colors(child, color_bg, color_fg)


    def _apply_ttk_colors(self, color_bg, color_fg):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background=color_bg, foreground=color_fg)
        style.configure("Custom.TLabelframe", background=color_bg, foreground=color_fg)
        style.configure("Custom.TLabel", background=color_bg, foreground=color_fg)
        style.configure("Custom.TButton", background=color_bg, foreground=color_fg)
