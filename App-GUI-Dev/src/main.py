import tkinter as tk 
from tkinter import ttk
from screeninfo import get_monitors


class WindowMain(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        #print(f"ancho: {width} alto: {height}")
        
        self.title("Thermo Scout MX")
        self.geometry(self.scale_window())
        self.resizable(False, False)


    def scale_window(self):
        for m in get_monitors():
            if m.is_primary:
                max_width = m.width
                max_height = m.height

        return f"{max_width}x{max_height}"



def main():
    app = WindowMain()
    app.mainloop()


if __name__ == "__main__":
    main()
