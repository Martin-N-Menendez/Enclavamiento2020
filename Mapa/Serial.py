import serial, time

def serial_main():
    arduino = serial.Serial('COM4', 19200)
    time.sleep(2)
    arduino.write(b'9')
    arduino.close()