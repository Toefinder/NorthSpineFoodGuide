from tkinter import *
import datetime
import pandas as pd

# Author: Lee Yi Hui Rachel
def generateWindow_6():
    window_6 = Tk()
    window_6.title('Waiting time')
    window_6.geometry('550x100')

    topFrame = Frame(window_6)
    topFrame.pack()

    askingNumPeopleLabel = Label(topFrame, text='Please enter number of people in the queue here for estimated waiting time:')
    askingNumPeopleLabel.grid(row=1,column=0,padx=2,pady=2)

    numPeopleEntry = Entry(topFrame)
    numPeopleEntry.grid(row=1,column=1)

    # *****status bar*****
    status = Label(window_6, text = 'Entering...', bd = 1, relief = SUNKEN, anchor= W)
    status.pack(side = BOTTOM, fill = X)

    def getWaitTime():
        numPeopleEntryStr = numPeopleEntry.get()

        try:
            numPeopleEntryInt = int(numPeopleEntryStr)
            waitTime = numPeopleEntryInt*2

        except ValueError:
            status['text'] = 'Please check your input. Integer values only!'
        else:
            if numPeopleEntryInt < 0:
                status['text'] = 'Please check your input. Integer value should be positive!'
            else:
                messagebox.showinfo(title="Estimated Waiting Time", message="Waiting time is estimated to be "+str(waitTime)+" minutes.")

    okwaitTimeButton = Button(topFrame, padx=10, pady=5, bg='purple', fg='white', text='OK', command=getWaitTime)
    okwaitTimeButton.grid(row=2, column=1)
