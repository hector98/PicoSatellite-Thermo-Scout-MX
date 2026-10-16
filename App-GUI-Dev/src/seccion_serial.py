import tkinter as tk 
import tkinter as ttk 

class SeccionSerial(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwars):
        super().__init__(parent, *args, **kwars)


        label_aviable_ports = tk.Label(self,
                                       text = "Puertos COM Disponibles ->")
        label_aviable_ports.grid(row=0, column=0, padx=1, pady=1)
