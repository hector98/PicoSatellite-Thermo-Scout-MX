
import tkinter as tk 
from tkinter import ttk 

class SeccionCansatData(ttk.LabelFrame):
    def __init__(self, parent, *args, **kwars):
        super().__init__(parent, *args, **kwars)

        self.liberar_status = True
        self.calibrar = False

        #--> widgets <---------------------------
        self.status_widgets = {}
        self.atmosferic_widgets = {}
        self.gps_widgets = {}

        cansat_status_frame = ttk.LabelFrame(self, 
                                             text="CanSat Status")
        cansat_status_frame.grid(row=0, column=1, padx=1, pady=2)
        self.add_status_widgets(cansat_status_frame)

        atmosferic_frame = ttk.LabelFrame(self,
                                          text="Datos Atmosfericos:")
        atmosferic_frame.grid(row=0, column=2, padx=1, pady=2)
        self.add_atmosferic_widgets(atmosferic_frame)


    def liberar_cansat(self):
        self.liberar_status = True

    
    def calibrar_cansat(self):
        self.calibrar = True


    def add_status_widgets(self, frame):
        self.status_widgets = {
            "label_connection": tk.Label(frame,
                                      text="CanSat Desconectado"),
            "btn_calibrar": ttk.Button(frame,
                                       text="Calibrar CanSat",
                                       state="disabled",
                                       command=self.calibrar_cansat()),
            "label_calibration": tk.Label(frame,
                                 text=""),
            "btn_liberar": ttk.Button(frame,
                                      text="Liberar CanSat",
                                      state="disabled",
                                      command=self.liberar_cansat()),
            "label_liberacion_cansat": tk.Label(frame,
                                         text=""),
            "label_liberacion_paracaidas": tk.Label(frame,
                                                    text="")
        }
        #self.status_widgets.update(widgets)
        self.add_widgets(self.status_widgets)


    def add_atmosferic_widgets(self, frame):
        self.atmosferic_widgets = {
            "temperatura": tk.Label(
                frame,
                text="Temperatura: _________"
            ),

            "humedad": tk.Label(
                frame,
                text="Humedad: _______"
            ),

            "alt_relativa": tk.Label(
                frame,
                text="Altitud Relativa: __________"
            ),

            "alt_msnm": tk.Label(
                frame,
                text="Altitud MSNM: ____________"
            ),

            "presion": tk.Label(
                frame,
                text="Presion: ____________"
            ),

            "co2": tk.Label(
                frame,
                text="Dioxido de CO2: _________"
            )

        }

        self.add_widgets(self.atmosferic_widgets)



    def update_values(self, seccion, widget, value):
        if seccion == 0:
            # Holograma "Aun no implementado"
            pass
        
        elif seccion == 1:
            # Update status widgets
            self.status_widgets[widget].config(text=f"{value}")

        elif seccion == 2:
            # update atmosferic_widgets
            self.atmosferic_widgets[widget].config(text=f"{value}")


    def set_atmosferic_widgets(self, widget, value):
        self.atmosferic_widgets[widget].config(text=f"{value}")
        

    def add_widgets(self, widgets):
        row = 0

        for key, widget in widgets.items():
            widget.grid(row=row, column=0, padx=2, pady=5)
            row += 1
