#!/usr/bin/env python3
from tkinter import Tk, W, E, X, RAISED, StringVar, DISABLED, NORMAL, PhotoImage
from tkinter.ttk import Frame, Button, Entry, Style, Label
import os


class Screen(Frame):

    craneState = None
    boomVar = None
    jibVar = None
    stateVar = None
    electromagnetVar = None

    btnApplyBoom = None
    btnApplyJib = None
    btnTurnOn = None
    btnTurnOff = None
    btnTurnOnElectromagnet = None
    btnTurnOffElectromagnet = None

    def __init__(self, craneState):
        super().__init__()
        self.craneState = craneState
        self.stateVar = StringVar(self)
        self.boomVar = StringVar(self)
        self.jibVar = StringVar(self)
        self.electromagnetVar = StringVar(self)
        self.initUI()
        self.setEntries()

    def initUI(self):
        frame1 = Frame(self, relief=RAISED, borderwidth=1, pad=10)
        frame1.grid(row=1, columnspan=3, padx=10, pady=10)

        frame1.columnconfigure(0, pad=3)
        frame1.columnconfigure(1, pad=3)
        frame1.columnconfigure(2, pad=3)

        frame1.rowconfigure(0, pad=3)
        frame1.rowconfigure(1, pad=3)
        frame1.rowconfigure(2, pad=3)
        frame1.rowconfigure(3, pad=3)
        frame1.rowconfigure(4, pad=3)
        frame1.rowconfigure(5, pad=3)

        self.initHeader(frame1)
        self.initBoom(frame1)
        self.initElectromagnet(frame1)
        self.initJib(frame1)
        self.initTurnOn(frame1)
        self.setEntries()
        self.pack()

    def initHeader(self, frame1):
        self.master.title('Lab3 - 201902 - Grupo B')
        self.master.iconphoto(True, PhotoImage(
            file=os.path.abspath('./guindaste.png')))
        Style().configure('TButton', padding=(0, 5, 0, 5),
                          font='serif 10')

        labelTitle = Label(
            self, text='Guindaste', font='Helvetica 16 bold')
        labelTitle.grid(row=0, column=0, columnspan=3)

        labelState = Label(frame1, text='Estado')
        stateEntry = Entry(frame1, textvariable=self.stateVar)
        stateEntry.configure(state='readonly')
        labelState.grid(row=0, column=0)
        stateEntry.grid(row=0, column=1, columnspan=2, sticky=W+E)

    def initBoom(self, frame1):

        def applyBoom():
            self.craneState.setBoomGrades(
                int(self.boomVar.get()), self.setEntries)

        labelBoom = Label(frame1, text='Lança +Horário -Antihorário')
        boom = Entry(frame1, textvariable=self.boomVar)
        self.btnApplyBoom = Button(frame1, text='Aplicar', command=applyBoom)
        labelBoom.grid(row=1, column=0)
        boom.grid(row=2, column=0)
        self.btnApplyBoom.grid(row=3, column=0)

    def initJib(self, frame1):

        def applyJib():
            self.craneState.setJibGrades(
                int(self.jibVar.get()), self.setEntries)

        labelJib = Label(frame1, text='Altura eletroimã (cm)')
        jib = Entry(frame1, textvariable=self.jibVar)
        self.btnApplyJib = Button(frame1, text='Aplicar', command=applyJib)
        labelJib.grid(row=1, column=1)
        jib.grid(row=2, column=1)
        self.btnApplyJib.grid(row=3, column=1)

    def initElectromagnet(self, frame1):

        def turnOnElectromagnet():
            self.craneState.turnOnElectromagnet(self.setEntries)

        def turnOffElectromagnet():
            self.craneState.turnOffElectromagnet(self.setEntries)

        labelElectromagnet = Label(frame1, text='Eletroíma')
        electromagnetEntry = Entry(
            frame1, textvariable=self.electromagnetVar)
        self.btnTurnOnElectromagnet = Button(
            frame1, text='On', command=turnOnElectromagnet)
        self.btnTurnOffElectromagnet = Button(
            frame1, text='Off', command=turnOffElectromagnet)
        electromagnetEntry.configure(state='readonly')
        labelElectromagnet.grid(row=1, column=2)
        electromagnetEntry.grid(row=2, column=2)
        self.btnTurnOnElectromagnet.grid(row=3, column=2)
        self.btnTurnOffElectromagnet.grid(row=4, column=2)

    def initTurnOn(self, frame1):
        def turnOn():
            self.craneState.turnOn(self.setEntries)

        def turnOff():
            self.craneState.turnOff(self.setEntries)

        self.btnTurnOn = Button(frame1, text='Ligar', command=turnOn)
        self.btnTurnOff = Button(frame1, text='Desligar', command=turnOff)
        self.btnTurnOn.grid(row=5, column=0)
        self.btnTurnOff.grid(row=5, column=1)

    def setEntries(self):
        self.stateVar.set(self.craneState.state)
        self.boomVar.set(self.craneState.boomGrades)
        self.jibVar.set(self.craneState.jibGrades)
        self.electromagnetVar.set(self.craneState.electromagnet)

        if (self.craneState.state == 'desligado'):
            self.btnTurnOn.config(state=NORMAL)
            self.btnTurnOff.config(state=DISABLED)
            self.btnApplyBoom.config(state=DISABLED)
            self.btnApplyJib.config(state=DISABLED)
            self.btnTurnOnElectromagnet.config(state=DISABLED)
            self.btnTurnOffElectromagnet.config(state=DISABLED)
        elif (self.craneState.state == 'parado'):
            self.btnTurnOn.config(state=DISABLED)
            self.btnTurnOff.config(state=NORMAL)
            self.btnApplyBoom.config(state=NORMAL)
            self.btnApplyJib.config(state=NORMAL)
            self.btnTurnOnElectromagnet.config(state=NORMAL)
            self.btnTurnOffElectromagnet.config(state=DISABLED)
        elif (self.craneState.state == 'ima'):
            self.btnTurnOn.config(state=DISABLED)
            self.btnTurnOff.config(state=DISABLED)
            self.btnApplyBoom.config(state=NORMAL)
            self.btnApplyJib.config(state=NORMAL)
            self.btnTurnOnElectromagnet.config(state=DISABLED)
            self.btnTurnOffElectromagnet.config(state=NORMAL)
        elif (
                self.craneState.state == 'lanca' or
                self.craneState.state == 'lanca-ima' or
                self.craneState.state == 'fio' or
                self.craneState.state == 'fio-ima'):
            self.btnTurnOn.config(state=DISABLED)
            self.btnTurnOff.config(state=DISABLED)
            self.btnApplyBoom.config(state=DISABLED)
            self.btnApplyJib.config(state=DISABLED)
            self.btnTurnOnElectromagnet.config(state=DISABLED)
            self.btnTurnOffElectromagnet.config(state=DISABLED)
