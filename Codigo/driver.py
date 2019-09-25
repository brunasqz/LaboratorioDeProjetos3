#!/usr/bin/env python3
import serial
import platform


class Driver():
    port = None
    speed = 9600
    arduino = None

    def __init__(self):
        if platform.system() == 'Linux':
            port = '/dev/ttyUSB0'
        else:
            port = 'com5'
        self.arduino = serial.Serial(self.port, self.speed)
        
        
    def boomClockwise(self, grades):
        print(grades)
        self.arduino.write(str.encode('c' + str(grades)))

    def boomAnticlockwise(self, grades):
        print(grades)
        self.arduino.write(str.encode('a' + str(grades)))
