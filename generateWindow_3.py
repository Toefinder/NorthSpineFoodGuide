import datetime
from tkinter import *


def generateWindow_3(userDatePara, userTimePara, window=None):
    '''
    Input:
    1) a window (optional) to iconify
    2) userDatePara and userTimePara are parameters to display on the interface

    Output: 
    1) the window passed as argument is iconified, 
    2) window_3 is created to show store information'''

    if window != None:
        window.iconify()
    window_3 = Toplevel()
    window_3.geometry('300x300')

    displayDateLabel_1 = Label(window_3, text='Display date: ', padx=10)
    displayDateLabel_1.grid(row=1, column=0, sticky=W)
    displayDateLabel_2 = Label(window_3, text=userDatePara.strftime('%Y-%m-%d'))
    displayDateLabel_2.grid(row=1, column=1, sticky=W)

    displayTimeLabel_1 = Label(window_3, text='Display time: ', padx=10)
    displayTimeLabel_1.grid(row=2, column=0, sticky=W)
    displayTimeLabel_2 = Label(window_3, text=userTimePara.strftime('%H:%M') )
    displayTimeLabel_2.grid(row=2, column=1, sticky=W)
    # print(userDatePara)
    # print(userTimePara)
    # print(type(userDatePara))
    # print(type(userTimePara))
    
    # label = Label(window_3, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    # label.()