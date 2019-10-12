import datetime
from tkinter import *
import pandas as pd
from generateWindow_4 import *

df = pd.read_csv('stallList.csv')

def generateWindow_3(userDatePara, userTimePara, window=None, stallButtonFunction=generateWindow_4):
    '''
    Input:
    1) a window (optional) to iconify
    2) userDatePara and userTimePara are parameters to display on the interface

    Output: 
    1) the window passed as argument is iconified, 
    2) window_3 is created to show store information
    3) upon clicking on the store name, stallButtonFunction will be executed'''

    if window != None:
        window.iconify()
    window_3 = Toplevel()
    # window_3.geometry('650x300')

    topFrame = Frame(window_3)
    topFrame.pack()
    bottomFrame = Frame(window_3)
    bottomFrame.pack()

    displayDateLabel_1 = Label(topFrame, text='Display date: ', padx=10)
    displayDateLabel_1.grid(row=1, column=0, sticky=W)
    displayDateLabel_2 = Label(topFrame, text=userDatePara.strftime('%Y-%m-%d'))
    displayDateLabel_2.grid(row=1, column=1, sticky=W)

    displayTimeLabel_1 = Label(topFrame, text='Display time: ', padx=10)
    displayTimeLabel_1.grid(row=2, column=0, sticky=W)
    displayTimeLabel_2 = Label(topFrame, text=userTimePara.strftime('%H:%M') )
    displayTimeLabel_2.grid(row=2, column=1, sticky=W)

    # create a list containing the buttons for all the stores
    stallListButton = []
    numRow = df.shape[0]
    for i in range(numRow):
        print(i)
        row = df.iloc[i] # row Series
        stallButtonCommand = lambda: stallButtonFunction(userDatePara=userDatePara, userTimePara=userTimePara, \
                                                         stallIndex=i)
        stallButton = Button(bottomFrame, text=row[0], height=3, width=17, command=stallButtonCommand)
        # row and column position for the stall buttons
        rowPosition = i // 5    
        colPosition = i % 5
        stallButton.grid(row=rowPosition, column=colPosition)
        stallListButton.append(stallButton)
        
    


    # print(userDatePara)
    # print(userTimePara)
    # print(type(userDatePara))
    # print(type(userTimePara))
    
    # label = Label(window_3, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    # label.()