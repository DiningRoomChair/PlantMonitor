# get serial capability
import serial
# set up serial values
serial = serial.Serial("/dev/ttyACM0", 9600)
serial.baudrate = 9600

while True:
    read_serial = serial.readline()
    print(read_serial)
