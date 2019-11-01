from tkinter import *
import datetime
import pandas as pd

operatingHours = pd.read_csv('operatingHours.csv')
operatingHours = operatingHours.set_index('Stall') # set the column 'Stall' as index column
def generateWindow_5(stallName):
    window_5 = Toplevel()
    window_5.title(stallName)

    descriptionLabel = Label(window_5, text='Operating time:')
    descriptionLabel.grid(row=0, column=0)
    
    listDay = ['Weekdays', 'Saturday', 'Sunday']
    for i in range(len(listDay)):
        dayOfWeek = listDay[i]
        dayLabel = Label(window_5, text=dayOfWeek)
        dayLabel.grid(row=i+1, column=0)

        openingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == dayOfWeek]['Opening Time'][0]
        print(openingTime)

        openingTimeLabel = Label(window_5, text=openingTime)
        openingTimeLabel.grid(row=i+1, column=1)

        closingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == dayOfWeek]['Closing Time'][0]
        print(closingTime)

        closingTimeLabel = Label(window_5, text=closingTime)
        closingTimeLabel.grid(row=i+1, column=2)
