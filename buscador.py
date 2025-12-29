import serial.tools.list_ports

def obtenerPuerto(exclude="COM3"):
    ports = [port.device for port in serial.tools.list_ports.comports()]
     # Aca evitas el COM3
    ports = [p for p in ports if p.upper() != exclude.upper()]
    return ports[0] if ports else None

COM = obtenerPuerto()
BAUDRATE = 9600
TIMEOUT =.1

print(COM)
try:
    arduino = serial.Serial(port=COM, baudrate=BAUDRATE, timeout=TIMEOUT)
except serial.SerialException as e:
    print(f"Error al conectar con Arduino: {e}")
    exit()
