import tkinter
import serial

arduino = serial.Serial('com4', 9600)
greenOn = False
yellowOn = False
redOn = False

top = tkinter.Tk()
top.geometry("300x50")

def greenCallback():
    global greenOn
    greenOn = not greenOn    
    arduino.write(str.encode('g1' if greenOn else 'g0'))    
    greenBtn.configure(bg = 'green' if greenOn else 'white')    

def yellowCallback():
    global yellowOn
    yellowOn = not yellowOn
    arduino.write(str.encode('y1' if yellowOn else 'y0'))
    yellowBtn.configure(bg = 'yellow' if yellowOn else 'white')    

def redCallback():
    global redOn
    redOn = not redOn
    arduino.write(str.encode('r1' if redOn else 'r0'))
    redBtn.configure(bg = 'red' if redOn else 'white')    

greenBtn = tkinter.Button(top, text = "Green", command = greenCallback, width = 10, bg = 'white')
greenBtn.place(x = 10, y = 10)

yellowBtn = tkinter.Button(top, text = "Yellow", command = yellowCallback, width = 10, bg = 'white')
yellowBtn.place(x = 110, y = 10)
    
redBtn = tkinter.Button(top, text = "Red", command = redCallback, width = 10, bg = 'white')
redBtn.place(x = 210, y = 10)

top.mainloop()