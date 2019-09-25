#!/usr/bin/env python3
import time
from driver import Driver
from threading import Timer

class CraneState:

    driver = None
    state = 'stopped'
    boomGrades = 0
    electromagnet = False

    def __init__(self):
        super().__init__()
        self.driver = Driver()

    def stop(self):
        self.state = 'stopped'
        print(self.state)

    def turnOnElectromagnet(self):
        self.electromagnet = True
        self.state = 'electromagnet'
        print(self.state)

    def turnOffElectromagnet(self):
        self.electromagnet = False
        self.state = 'stopped'
        print(self.state)

    def setBoomGrades(self, grades, callback):

        if (grades < -180 or grades > 180):
            print('invalid grades')
            return

        if (self.state != 'stopped'):
            print('invalid state')
            return

        delta = grades - self.boomGrades
        self.state = 'booming'
        self.boomGrades = grades
        callback()

        if delta > 0:
            self.driver.boomClockwise(delta)
        else:
            self.driver.boomAnticlockwise(-delta)

        def finish():
            self.state = 'stopped'
            callback()
            
        t = Timer(5.0, finish)
        t.start()
