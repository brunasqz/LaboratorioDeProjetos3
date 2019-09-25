import tkinter
import serial

arduino = serial.Serial('com5', 9600)

top = tkinter.Tk()
top.geometry("300x50")


def clockwiseCallback():
    arduino.write(str.encode('c' + grades.get()))


def anticlockwiseCallback():
    arduino.write(str.encode('a' + grades.get()))


grades = tkinter.StringVar()

inputGrades = tkinter.Entry(
    top, width=10, textvariable=grades)
inputGrades.place(x=10, y=10)

clockwiseBtn = tkinter.Button(
    top, text="Clockwise", command=clockwiseCallback, width=10, bg='white')
clockwiseBtn.place(x=110, y=10)

anticlockwiseBtn = tkinter.Button(
    top, text="Anticlockwise", command=anticlockwiseCallback, width=10, bg='white')
anticlockwiseBtn.place(x=210, y=10)

top.mainloop()
