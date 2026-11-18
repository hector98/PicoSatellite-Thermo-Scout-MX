import serial
import serial.tools.list_ports
from time import sleep
import threading

class SerialPort():
    def __init__(self):


    def get_list_ports():
        ports = []

        for port in serial.tools.list_ports.comports():
            port = str(port).split(" ")
            if port[2] != "n/a":
                ports.append(port)

        return ports

    def validate_number_float(self, number):
        number_float = ""
        
        i = 0
        point = 0

        while i < len(number):
            if i == 0 and number[i] == "-":
                number_float += number[i]

            elif point != 0 and number[i]:
                point += 1
                number_float += number[i]

            elif re.match(r"^[0-9]+$, number[i]"):
                number_float += number[i]

            try:
                number_float = round(float(number_float))

                return str(number_float)
            
            except:
                return "0.00"


    def response(self, liberar, calibra):
        if liberar:
            r = "<01>"


        self.serial_port.write(r.encode('utf-8'))



    def parse_data(self, data, data_seccion, graphics):
        liberar = True if data_seccion.liberar_status else False
        calibrar = True if data_seccion.calibrar else False

        if (data != ""):
            key, value = data.split(";")

            if(key == "00"):
                pass

            elif(key == "01"):
                # Temperatura
                temp = "Temperatura: " 
                + self.validate_number_float(value)
                + " °C"
                #->seccion 1 atmosferic widgets, widget = temperatura, nuevo valor
                data_seccion.update_values(1, "temperatura", temp)

        self.response(liberar, calibrar)

        
        
    def read_serial(self, data_seccion, graphics):
        while self.receiving_data and self.serial_port and self.serial_port.is_open:
            try:
                if self.serial_port.in_waiting > 0:
                    raw_bytes = self.serial_port.read(self.serial_port.in_waiting)
                    try:
                        data = raw_bytes.decode('utf-8', errors='ignore')
                    except:
                        data = raw_bytes.decode('latin-1', errors='ignore')

                    update_widgets = parse_data(data, data_seccion, graphics)

                time.sleep(0.2)
            
            except Exception as e:
                print(f"Error al leer los datos: {e}")
        
        
    def connect(self, s_serial, data, graphics):
        port = s_serial.port_combo.get()
        baudrate = 115200

        if not port:
            messagebox.showerror("Error", "Seleccione un puerto")
            return

        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=1)
            self.serial_conected = True
            self.receiving_data = True

            #Actualizar datos textuales y graficos
            s_serial.btn_connect.config(state=tk.DISABLED)
            #s_serial.btn_disconnect.config(state=tk.NORMAL)
            s_serial.label_serial_status.config(
                text="Estacion Terrestre: Conectada", 
                foreground="#50C225")

            # Iniciar Hilo para recibir datos
            hilo = threading.Thread(
                    target= self.read_serial,
                    args=(self, data, graphics), 
                    daemon=True)
            hilo.start()


        except serial.SerialException as e:
            print("Error", f"Error al conectar con el puerto {port}: {e}")

