import tkinter as tk 
from tkinter import ttk

from serial_port import SerialPort

class SeccionSerial(ttk.LabelFrame):
    def __init__(self, parent, *args, seccion_data, seccion_graphics, **kwars):
        super().__init__(parent, *args, **kwars)

        #Variables y objetos globales 
        self.serial_port = SerialPort
        self.seccion_data = seccion_data
        self.seccion_graphics = seccion_graphics


        label_aviable_ports = tk.Label(self,
                                       text = "Puertos COM Disponibles ->")
        label_aviable_ports.grid(row=0, column=0, padx=1, pady=1)

        self.port_combo = ttk.Combobox(self,
                                       width=15,
                                       state="readonly")
        self.port_combo.grid(row=0, column=1, padx=1, pady=1)

        btn_update_ports = ttk.Button(self,
                                      text="Refrescar puertos",
                                      command=self.list_ports)
        btn_update_ports.grid(row=0, column=2, padx=2, pady=1)

        self.btn_connect = ttk.Button(self,
                                 text="Conectar",
                                 state="normal",
                                 command=self.connect_port_serial)
        self.btn_connect.grid(row=0, column=3, padx=1, pady=1)

        self.label_connect_status = tk.Label(self,
                                             text="")
        self.grid(row=0, column=2, padx=2, pady=1)


        self.list_ports()


    def list_ports(self):
        print("List ports")
        list_ports = self.serial_port.get_list_ports()
        self.port_combo['values'] = list_ports
        if list_ports:
            self.port_combo.set(list_ports[0])


    def connect_port_serial(self):
        self.serial_port.connect(
            self.serial_port, 
            self,
            self.seccion_data, 
            self.seccion_graphics)



