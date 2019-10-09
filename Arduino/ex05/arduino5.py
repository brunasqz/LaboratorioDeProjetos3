import tkinter
import serial

arduino = serial.Serial('com4', 9600)

magnetState = False

top = tkinter.Tk()
top.geometry("400x80")


def clockwiseCallback():
    arduino.write(str.encode('c' + grades.get()))


def anticlockwiseCallback():
    arduino.write(str.encode('a' + grades.get()))


def clockwise2Callback():
    arduino.write(str.encode('d' + grades.get()))


def anticlockwise2Callback():
    arduino.write(str.encode('b' + grades.get()))


def magnetCallback():
    global magnetState
    magnetState = not magnetState
    arduino.write(str.encode('m1' if magnetState else 'm0'))
    magnetBtn.configure(bg='green' if magnetState else 'white')


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

clockwise2Btn = tkinter.Button(
    top, text="Clockwise", command=clockwise2Callback, width=10, bg='white')
clockwise2Btn.place(x=110, y=40)

anticlockwise2Btn = tkinter.Button(
    top, text="Anticlockwise", command=anticlockwise2Callback, width=10, bg='white')
anticlockwise2Btn.place(x=210, y=40)

magnetBtn = tkinter.Button(
    top, text="Magnet", command=magnetCallback, width=10, bg="white")
magnetBtn.place(x=310, y=10)

top.mainloop()
