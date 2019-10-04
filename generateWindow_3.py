import datetime
from tkinter import *


def generateWindow_3(window=None):
    '''
    Input (optional): a window
    Output: 
    1) the window passed as argument is iconified, 
    2) window_3 is created to show store information'''

    if window != None:
        window.iconify()
    window_3 = Toplevel()
    window_3.geometry('300x300')

    # print(userDate)
    # print(userTime)
    # print(type(userDate))
    # print(type(userTime))
    
    label = Label(window_3, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    label.pack()