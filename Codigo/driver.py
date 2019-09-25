#!/usr/bin/env python3
import serial

class Driver():
    port = 'com5'
    speed = 9600
    arduino = None
        
    def __init__(self):
        self.arduino = serial.Serial(self.port, self.speed)
        
    def boomClockwise(self, grades):
        print(grades)
        self.arduino.write(str.encode('c' + str(grades)))

    def boomAnticlockwise(self, grades):
        print(grades)
        self.arduino.write(str.encode('a' + str(grades)))
