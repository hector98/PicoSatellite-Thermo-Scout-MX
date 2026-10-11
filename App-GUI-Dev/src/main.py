import tkinter as tk 
from tkinter import ttk


class WindowMain(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        print(f"ancho: {width} alto: {height}")
        
        self.title("Thermo Scout MX")
        self.geometry("1200x800")



def main():
    app = WindowMain()
    app.mainloop()


if __name__ == "__main__":
    main()
