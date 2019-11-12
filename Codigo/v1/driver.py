#!/usr/bin/env python3
import serial
import platform


class Driver():
    port = 'com4'
    speed = 9600
    arduino = None

    def __init__(self):
        self.arduino = serial.Serial(self.port, self.speed)

    def engine1(self, grades):
        if (grades > 0):
            self.arduino.write(str.encode('c' + str(grades)))
        else:
            self.arduino.write(str.encode('a' + str(-grades)))

    def engine2(self, grades):
        if (grades > 0):
            self.arduino.write(str.encode('b' + str(grades)))
        else:
            self.arduino.write(str.encode('d' + str(-grades)))

    def eletromag(self, state):
        self.arduino.write(str.encode('m1' if state else 'm0'))
