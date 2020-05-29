import serial
import time
from tkinter import *

def turn_on():
    arduinoData.write(b'1')

def set_lighting(intensity):
    if(intensity == 'A'):
        arduinoData.write('A')
    elif(intensity == 'B'):
        arduinoData.write('B')
    elif(intensity == 'C'):
        arduinoData.write('C')
    else:
        print("not relevant intensity")

arduinoData = serial.Serial('COM7', 9600)

window = Tk()
window.geometry('350x210')
window.title("Project")

btn_on = Button(window, text="ON", bg="green", fg="white", font=("Arial Bold", 15), command=turn_on)
btn_off = Button(window, text="OFF", bg="red", fg="white", font=("Arial Bold", 15))

lbl_pot = Label(window, text="Use Potentiometer", font=("Arial Bold", 12))


btn_on.place(x=100, y=50)
btn_off.place(x=200, y=50)
lbl_pot.place(x=110, y=100)

window.mainloop()