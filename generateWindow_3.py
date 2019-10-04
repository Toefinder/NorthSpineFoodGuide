import datetime
from tkinter import *


def generateWindow_3():
    window = Toplevel()
    window.geometry('300x300')

    # print(userDate)
    # print(userTime)
    # print(type(userDate))
    # print(type(userTime))
    
    label = Label(window, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    label.pack()