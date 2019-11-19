#!/usr/bin/env python3
import serial
import platform


class Driver():
    port = '/dev/ttyUSB0'
    speed = 9600
    arduino = None

    def __init__(self):
        self.arduino = serial.Serial(self.port, self.speed)

    def engine1(self, grades):#Motor da lança
        if (grades > 0):
            s = str(chr(1<<1) + chr(grades))
            self.arduino.write(s.encode())
            print (grades)
        else:
            s = str(chr((1<<1)|1) + chr(abs(grades)))
            self.arduino.write(s.encode())

    def engine2(self, grades):#Motor Iça
        if (grades > 0):
            s = str(chr(2<<1) + chr(grades))
            self.arduino.write(s.encode())
            print (s)
        else:
            s = str(chr((2<<1)|1) + chr(abs(grades)))
            self.arduino.write(s.encode())
            print (s)

    def eletromag(self, state):
        if (state):
            s = str(chr(3<<1) + chr(1))
            self.arduino.write(s.encode())
        else:
            s = str(chr(3<<1) + chr(1))
            self.arduino.write(s.encode())        
