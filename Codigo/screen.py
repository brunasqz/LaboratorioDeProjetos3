#!/usr/bin/env python3

from tkinter import Tk, W, E, X, RAISED, StringVar
from tkinter.ttk import Frame, Button, Entry, Style, Label

class Screen(Frame):
    
    craneState = None
    stateVar = None
    electromagnetVar = None

    def __init__(self, craneState):
        super().__init__()
        self.craneState = craneState        
        self.stateVar = StringVar(self)
        self.electromagnetVar = StringVar(self)
        self.initUI()
    
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
        
        self.initHeader(frame1)

        labelBoom = Label(frame1, text="Braço")        
        boom = Entry(frame1)
        incBoom = Button(frame1, text="+1º")
        decBoom = Button(frame1, text="-1º")
        boom.configure(state='readonly')
        labelBoom.grid(row=1, column=0)
        boom.grid(row=2, column=0)
        incBoom.grid(row=3, column=0)
        decBoom.grid(row=4, column=0)

        labelJib = Label(frame1, text="Lança")
        jib = Entry(frame1)
        incJib = Button(frame1, text="+1cm")
        decJib = Button(frame1, text="-1cm")
        jib.configure(state='readonly')
        labelJib.grid(row=1,column=1)
        jib.grid(row=2, column=1)
        incJib.grid(row=3, column=1)
        decJib.grid(row=4, column=1)

        self.initElectromagnet(frame1)
        
        self.setEntries()

        self.pack()

    def initHeader(self, frame1):
        self.master.title("Lab3 - 201902 - Grupo B")

        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font='serif 10')

        labelTitle = Label(
            self, text="Guindaste", font='Helvetica 16 bold')
        labelTitle.grid(row=0, column=0, columnspan=3)
        
        labelState = Label(frame1, text="Estado")
        stateEntry = Entry(frame1, textvariable=self.stateVar)
        stateEntry.configure(state='readonly')
        labelState.grid(row=0, column=0)
        stateEntry.grid(row=0, column=1, columnspan=2, sticky=W+E)


    def initElectromagnet(self, frame1):      
        
        def turnOnElectromagnet():
            self.craneState.turnOnElectromagnet()
            self.setEntries()

        def turnOffElectromagnet():
            self.craneState.turnOffElectromagnet()
            self.setEntries()
            
        labelElectromagnet = Label(frame1, text="Eletroíma")
        electromagnetEntry = Entry(
            frame1, textvariable=self.electromagnetVar)
        btnTurnOnElectromagnet = Button(
            frame1, text="On", command=turnOnElectromagnet)
        btnTurnOfElectromagnet = Button(
            frame1, text="Off", command=turnOffElectromagnet)
        electromagnetEntry.configure(state='readonly')
        labelElectromagnet.grid(row=1, column=2)
        electromagnetEntry.grid(row=2, column=2)
        btnTurnOnElectromagnet.grid(row=3, column=2)
        btnTurnOfElectromagnet.grid(row=4, column=2)
        
    
        
    def setEntries(self):
        self.stateVar.set(self.craneState.state)
        self.electromagnetVar.set('Ligado' if self.craneState.electromagnet else 'Desligado')
