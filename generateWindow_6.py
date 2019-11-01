from tkinter import *
import tkinter as tk
import datetime
import pandas as pd

def generateWindow_6():
    window_6 = Tk()
    window_6.title('Waiting time')
    window_6.geometry('350x150+30+30')

    askingNumPeopleLabel = Label(window_6, text='Please enter number of people in the queue here for estimated waiting time.')
    askingNumPeopleLabel.grid(row=1,column=0,padx=2,pady=2)

    numPeopleEntry = Entry(window_6)
    numPeopleEntry.grid(row=1,column=1)

    def getwaitTime():
        numPeopleEntryStr = numPeopleEntry.get()
        print(numPeopleEntryStr)


        try:
            numPeopleEntryInt = int(numPeopleEntryStr)
            waitTime = numPeopleEntryInt*2

        except ValueError:
            status['text'] = 'Please check your input. Integer values only!'
        else:
            messagebox.showinfo(title="WaitTime", message="Please wait for "+str(waitTime)+" minutes.")



    okwaitTimeButton = Button(window_6, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getwaitTime)
    okwaitTimeButton.grid(row=2, column=1)
