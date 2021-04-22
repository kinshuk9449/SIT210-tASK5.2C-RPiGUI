from tkinter import *

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

def red():
   GPIO.output(5,GPIO.HIGH)
   GPIO.output(3,GPIO.LOW)
   GPIO.output(8,GPIO.LOW)

def blue():
   GPIO.output(3,GPIO.HIGH)
   GPIO.output(5,GPIO.LOW)
   GPIO.output(8,GPIO.LOW)
   
def green():
   GPIO.output(8,GPIO.HIGH)
   GPIO.output(3,GPIO.LOW)
   GPIO.output(5,GPIO.LOW)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="RED", variable=var, value=1,
                  command=red)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="BLUE", variable=var, value=2,
                  command=blue)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="GREEN", variable=var, value=3,
                  command=green)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()