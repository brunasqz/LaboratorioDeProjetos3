#!/usr/bin/env python3
import serial
import platform


class Driver():
    port = 'com3'  # '/dev/ttyUSB0'
    speed = 9600
    arduino = None

    def __init__(self):
        self.arduino = serial.Serial(self.port, self.speed)

    def makeMessage(self, op, signal, arg):
        total = (op << 9) | (signal << 8) | arg
        b = bytes([total >> 8, total & 255])
        print(total)
        return b

    def engine1(self, grades):  # Motor da lança
        if (grades > 0):
            s = self.makeMessage(1, 1, grades)
            self.arduino.write(s)
        else:
            s = self.makeMessage(1, 0, -grades)
            self.arduino.write(s)

    def engine2(self, grades):  # Motor Iça
        if (grades > 0):
            s = self.makeMessage(2, 1, grades)
            self.arduino.write(s)
        else:
            s = self.makeMessage(2, 0, -grades)
            self.arduino.write(s)

    def eletromag(self, state):
        if (state):
            s = self.makeMessage(3, 0, 1)
            self.arduino.write(s)
        else:
            s = self.makeMessage(3, 0, 0)
            self.arduino.write(s)
