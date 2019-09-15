#!/usr/bin/env python3

from tkinter import Tk, W, E, X, RAISED
from tkinter.ttk import Frame, Button, Entry, Style, Label


class Screen(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Lab3 - 201902 - Grupo B")

        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font='serif 10')

        labelTitle = Label(
            self, text="Guindaste", font='Helvetica 16 bold')
        labelTitle.grid(row=0, column=0, columnspan=3)
        
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

        labelState = Label(frame1, text="Estado")
        state = Entry(frame1)
        state.configure(state='readonly')
        labelState.grid(row=0, column=0)
        state.grid(row=0, column=1, columnspan=2, sticky=W+E)

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


        labelElectromagnet = Label(frame1, text="Eletroíma")
        electromagnet = Entry(frame1)
        turnOnElectromagnet = Button(frame1, text="On")
        turnOfElectromagnet = Button(frame1, text="Off")
        electromagnet.configure(state='readonly')
        labelElectromagnet.grid(row=1, column=2)
        electromagnet.grid(row=2, column=2)
        turnOnElectromagnet.grid(row=3, column=2)
        turnOfElectromagnet.grid(row=4, column=2)

        self.pack()


def main():

    root = Tk()
    app = Screen()
    root.mainloop()


if __name__ == '__main__':
    main()
