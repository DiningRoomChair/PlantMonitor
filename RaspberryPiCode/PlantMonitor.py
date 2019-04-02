# get serial capability
import serial
import time
# set up serial values
serial = serial.Serial("/dev/ttyACM0", 9600)
serial.baudrate = 9600

temp = 0
humidity = 0
light = 0

while True:
    read_serial = serial.readline()[:-2]
    read_serial = str(read_serial).split('=')
    if read_serial[0][2:] == "Temp":
        temp = int(read_serial[1][:-1])
    if read_serial[0][2:] == "Humidity":
        humidity = int(read_serial[1][:-1])
    if read_serial[0][2:] == "Light":
        light = int(read_serial[1][:-1])
    print(temp)
    time.sleep(1)
