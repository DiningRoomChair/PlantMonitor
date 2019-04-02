# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import serial

serial = serial.Serial("/dev/ttyACM0", 9600)
serial.baudrate = 9600

def index(request):

    temp = 0
    light = 0
    humidity = 0

    for x in range(15):
        read_serial = serial.readline()[:-2]
        read_serial = str(read_serial).split('=')
        if read_serial[0][2:] == "Temp" and int(read_serial[1][:-1]) > 0:
            temp = int(read_serial[1][:-1])
        if read_serial[0][2:] == "Humidity" and int(read_serial[1][:-1]) > 0:
            humidity = int(read_serial[1][:-1])
        if read_serial[0][2:] == "Light" and int(read_serial[1][:-1]) > 0:
            light = int(read_serial[1][:-1])

    return HttpResponse("Temperature: " + str(temp) + "<br/>\
                        Light: " + str(light) + "<br/>\
                        Humidity: " + str(humidity))