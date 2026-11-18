import tkinter as tk 
from tkinter import ttk
from screeninfo import get_monitors
from  time import sleep
import threading

#--------------------------------------- 
from styles import Styles
#from serial_port import SerialPort
from seccion_serial import SeccionSerial
from seccion_cansat_data import SeccionCansatData


class WindowMain(tk.Tk):
    def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
       
        self.title("Thermo Scout MX")
        self.geometry(self.scale_window())
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)

        self.style_now = Styles(self)
        self.style_now.apply_theme()

        #self.serial_port = SerialPort()
        #print(f"serial en main: {self.serial_port}")

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
        #main.grid(row=0, column=0, sticky="ew", padx=1, pady=1)

        seccion_cansat_data = SeccionCansatData(main,
                                                text="CanSat Status Info")
        seccion_cansat_data.grid(row=1, column=0, sticky="ew", padx=1, pady=2)

        seccion_graphics = 0 # Valor 0 de momento


        #########################################
        seccion_serial = SeccionSerial(main,
                                       seccion_data=seccion_cansat_data,
                                       seccion_graphics=seccion_graphics,
                                       text="Configuracion Serial")
        seccion_serial.grid(row=0, column=0, sticky="ew", padx=1, pady=2)


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
