import serial
import time

# Especifica el puerto serial al que está conectado tu Arduino (puedes verificar en el IDE de Arduino)
puerto_serial = 'COM3'  # Cambia esto según tu sistema operativo y configuración

# Inicia la comunicación serial
arduino = serial.Serial(puerto_serial, 9600)
time.sleep(2)  # Espera a que se establezca la conexión

# Envía una cadena de texto al Arduino
mensaje = str(input("Introduce un mensaje: "))
arduino.write(mensaje.encode())

# Cierra la conexión
arduino.close()
