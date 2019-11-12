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
            s = 1 << 9 & grades
            self.arduino.write(chr(s))
        else:
            s = 2 << 9 & -grades
            self.arduino.write(chr(s))

    def engine2(self, grades):
        if (grades > 0):
            s = 3 << 9 & grades
            self.arduino.write(chr(s))
        else:
            s = 4 << 9 & -grades
            self.arduino.write(chr(s))

    def eletromag(self, state):
        if (state):
            s = 5 << 9
            self.arduino.write(chr(s))
        else:
            s = 6 << 9
            self.arduino.write(chr(s))        
