import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from generateWindow_1 import *
from generateWindow_2 import *
from generateWindow_3 import *


# get current date and time 
now = datetime.datetime.now()

generateWindow_1(now=now, nowButtonFunction=generateWindow_3, anotherTimeButtonFunction=generateWindow_2)

    # if now.weekday() == 0:
    #     label = Label(window_2, text="Chocolate cake\nStrawberry cake\nBlueberry cake")
    # else:
    #     label = Label(window_2, text="Non-Monday menu")
    # label.pack()
