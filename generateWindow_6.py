from tkinter import *
import datetime
import pandas as pd

def generateWindow_6():
    window_6 = Toplevel()
    window_6.title('Waiting time')

    askingNumPeopleLabel = Label(window_6, text='Please enter number of people in the queue here for estimated waiting time.')
    askingNumPeopleLabel.grid(row=1,column=0,padx=2,pady=2)

    numPeopleEntry = Entry(window_6)
    numPeopleEntry.grid(row=1,column=1)

