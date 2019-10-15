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
                print('erro')
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
                print('erro')
        elif (self.state == 'ima'):
            if (action == 'desligar-ima'):
                self.state = 'parado'
            elif (action == 'ligar-lanca'):
                self.state = 'lanca-ima'
            elif (action == 'ligar-fio'):
                self.state = 'fio-ima'
            else:
                print('erro')
        elif (self.state == 'lanca'):
            if (action == 'desligar-lanca'):
                self.state = 'parado'
            else:
                print('erro')
        elif (self.state == 'lanca-ima'):
            if (action == 'desligar-lanca'):
                self.state = 'ima'
            else:
                print('erro')
        elif (self.state == 'fio'):
            if (action == 'desligar-fio'):
                self.state = 'parado'
            else:
                print('erro')
        elif (self.state == 'fio-ima'):
            if (action == 'desligar-fio'):
                self.state = 'ima'
            else:
                print('erro')
        else:
            print('erro')

    def turnOn(self, callback):
        self.setState('ligar')
        callback()

    def turnOff(self, callback):
        self.setState('desligar')
        callback()

    def stop(self):
        self.state = 'stopped'
        print(self.state)

    def turnOnElectromagnet(self, callback):
        self.electromagnet = True
        self.setState('ligar-ima')
        callback()

    def turnOffElectromagnet(self, callback):
        self.electromagnet = False
        self.setState('desligar-ima')
        callback()

    def setBoomGrades(self, grades, callback):

        if (grades < -180 or grades > 180):
            print('invalid grades')
            return

        self.boomGrades = grades
        self.setState('ligar-lanca')
        callback()

        def finish():
            self.setState('desligar-lanca')
            callback()

        t = Timer(2.0, finish)
        t.start()

    def setJibGrades(self, grades, callback):

        if (grades < -180 or grades > 180):
            print('invalid grades')
            return

        self.setState('ligar-fio')

        self.jibGrades = grades
        callback()

        def finish():
            self.setState('desligar-fio')
            callback()

        t = Timer(2.0, finish)
        t.start()
