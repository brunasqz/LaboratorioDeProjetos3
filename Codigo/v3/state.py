#!/usr/bin/env python3
import time
from driver import Driver
from threading import Timer


class CraneState:

    driver = None
    state = 'desligado'
    boomGrades = 0
    jibGrades = 0
    electromagnet = False

    def __init__(self):
        super().__init__()
        self.driver = Driver()

    def setState(self, action):
        if (self.state == 'desligado'):
            if (action == 'ligar'):
                self.state = 'parado'
            else:
                return False
        elif (self.state == 'parado'):
            if (action == 'desligar'):
                self.state = 'desligado'
            elif (action == 'ligar-ima'):
                self.state = 'ima'
            elif (action == 'ligar-lanca'):
                self.state = 'lanca'
            elif (action == 'ligar-fio'):
                self.state = 'fio'
            else:
                return False
        elif (self.state == 'ima'):
            if (action == 'desligar-ima'):
                self.state = 'parado'
            elif (action == 'ligar-lanca'):
                self.state = 'lanca-ima'
            elif (action == 'ligar-fio'):
                self.state = 'fio-ima'
            else:
                return False
        elif (self.state == 'lanca'):
            if (action == 'desligar-lanca'):
                self.state = 'parado'
            else:
                return False
        elif (self.state == 'lanca-ima'):
            if (action == 'desligar-lanca'):
                self.state = 'ima'
            else:
                return False
        elif (self.state == 'fio'):
            if (action == 'desligar-fio'):
                self.state = 'parado'
            else:
                return False
        elif (self.state == 'fio-ima'):
            if (action == 'desligar-fio'):
                self.state = 'ima'
            else:
                return False
        else:
            return False

        return True

    def turnOn(self, callback):
        if not self.setState('ligar'):
            print('invalid state')
            return
        callback()

    def turnOff(self, callback):
        if not self.setState('desligar'):
            print('invalid state')
            return
        callback()

    def turnOnElectromagnet(self, callback):
        if not self.setState('ligar-ima'):
            print('invalid state')
            return

        self.electromagnet = True
        self.driver.eletromag(self.electromagnet)
        callback()

    def turnOffElectromagnet(self, callback):

        if not self.setState('desligar-ima'):
            print('invalid state')
            return

        self.electromagnet = False
        self.driver.eletromag(self.electromagnet)
        callback()

    def setBoomGrades(self, grades, callback):

        if not self.setState('ligar-lanca'):
            print('invalid state')
            return

        if (grades < -180 or grades > 180):
            print('invalid grades')
            return

        self.boomGrades = grades
        self.driver.engine1(grades)

        callback()

        def finish():
            self.setState('desligar-lanca')
            callback()
            
        ttw = abs(grades) / 50 * 3

        t = Timer(ttw, finish)
        t.start()

    def setJibGrades(self, height, callback):

        if not self.setState('ligar-fio'):
            print('invalid state')
            return

        # 1cm = 180 grades ?
        grades = height

        self.jibGrades = height
        self.driver.engine2(grades)
        callback()

        def finish():
            self.setState('desligar-fio')
            callback()

        ttw = abs(height)*2

        t = Timer(ttw, finish)
        t.start()
