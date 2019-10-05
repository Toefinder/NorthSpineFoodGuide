import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from generateWindow_1 import *
from generateWindow_2 import *
from generateWindow_3 import *


# get current date and time 
now = datetime.datetime.now()

# default value of userDate and userTime
currentDate = now.date()
currentTime = now.time()
userDate = currentDate
userTime = currentTime


    # if now.weekday() == 0:
    #     label = Label(window_2, text="Chocolate cake\nStrawberry cake\nBlueberry cake")
    # else:
    #     label = Label(window_2, text="Non-Monday menu")
    # label.pack()


def generateWindow_4():
    window = Toplevel()
    window.geometry('300x300')
    label = Label(window, text="Souffle\nIce Cream\nMatcha Pancakes")
    label.pack()

generateWindow_1(now,generateWindow_3,generateWindow_2)
