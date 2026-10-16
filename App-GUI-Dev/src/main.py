import tkinter as tk 
from tkinter import ttk
from screeninfo import get_monitors

#--------------------------------------- 
from styles import Styles
from seccion_serial import SeccionSerial


class WindowMain(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
       
        self.title("Thermo Scout MX")
        self.geometry(self.scale_window())
        self.resizable(False, False)
        self.style_now = Styles(self)
        self.style_now.apply_theme()

        self.create_notebooks()


    def scale_window(self):
        for m in get_monitors():
            if m.is_primary:
                max_width = m.width
                max_height = m.height

        return f"{max_width}x{max_height}"

    
    def create_notebooks(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.notebook_main(notebook)
        self.notebook_historic_data(notebook)
        self.notebook_about(notebook)


    def notebook_main(self, notebook):
        main = ttk.Frame(notebook)
        notebook.add(main, text="View Data")
        seccion_serial = SeccionSerial(main, text="Configuracion Serial")
        seccion_serial.grid(row=0, column=0, padx=1, pady=2)


    def notebook_historic_data(self, notebook):
        historic_data = ttk.Frame(notebook)
        notebook.add(historic_data, text="Historic Data")


    def notebook_about(self, notebook):
        about = ttk.Frame(notebook)
        notebook.add(about, text="About of")



def main():
    app = WindowMain()
    app.mainloop()


if __name__ == "__main__":
    main()
