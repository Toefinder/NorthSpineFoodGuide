from tkinter import *
import datetime
import pandas as pd
from generateWindow_5 import *
from generateWindow_6 import *

stallList = pd.read_csv('stallList.csv')
allStallMenu = pd.read_csv('stallMenu.csv')

openingHours = pd.read_csv('openingHours.csv')
openingHours = openingHours.set_index('Stall') #set the column 'Stall' as index column
def generateWindow_4(userDatePara, userTimePara, stallName, operatingTimeButtonFunction=generateWindow_5):
    '''
    Input:
    1) stallIndex is index of stall in the file 
    2) userDatePara and userTimePara are parameters to determine if store is open or closed and available menu
    3) operatingTimeButtonFunction is the function to call when the operatingTimeButton is pressed

    Output: 
    1) window_4 is created to show information of chosen store
    2) operatingTime
    '''
    # print(stallIndex)
    window_4 = Toplevel()
    # stallName = stallList.iloc[stallIndex, 0]
    print(stallName)
    window_4.title(stallName)

    particularStallMenu = allStallMenu[allStallMenu['Stall'] == stallName]
    numRow = particularStallMenu.shape[0]


    # determine whether the store is currently open or close, True for open (still needs developing)
    def openOrClosed(date=userDatePara, time=userTimePara):
        # Return the day of the week as an integer, where Monday is 0 and Sunday is 6 
        dayOfWeek = date.weekday() 
        if dayOfWeek <= 4: 
            checkDate = 'Weekdays' #checkDate is a variable used to access the excel operating time
        elif dayOfWeek == 5:
            checkDate = 'Saturday' 
        else:
            checkDate = 'Sunday'
        
        openingTime = openingHours.loc[stallName][openingHours.loc[stallName, 'Day'] == checkDate]['Opening Time'][0]
        print(openingTime)

        if openingTime == 'closed':
            print('Closed!')
            return False

        openingTimeObject = datetime.datetime.combine(date, \
                            datetime.datetime.strptime(openingTime, '%H:%M').time())
        closingTime = openingHours.loc[stallName][openingHours.loc[stallName, 'Day'] == checkDate]['Closing Time'][0]
        print(closingTime)
        closingTimeObject = datetime.datetime.combine(date, \
                            datetime.datetime.strptime(closingTime, '%H:%M').time())
       
        userDefinedTime = datetime.datetime.combine(date, time)
        if openingTimeObject <= userDefinedTime <= closingTimeObject:
            print("open!")
            return True
        else: 
            print('closed!')
            return False

    def showMenu(frame):
        for i in range(numRow):
            dishLabel = Label(frame, text='Dish name')
            dishLabel.grid(row=0, column=0)

            priceLabel = Label(frame, text='Price ($)')
            priceLabel.grid(row=0, column=1)

            row = particularStallMenu.iloc[i]
            dishName = row[1]
            dishPrice = row[2]

            dishNameLabel = Label(frame, text=dishName)
            dishNameLabel.grid(row=i+1, column=0, sticky=W)

            dishPriceLabel = Label(frame, text=dishPrice)
            dishPriceLabel.grid(row=i+1, column=1, sticky=W)

    topFrame = Frame(window_4)
    topFrame.pack()
    bottomFrame = Frame(window_4)
    bottomFrame.pack()
    if openOrClosed() == True:
        showMenu(frame = topFrame)
        waitingTimeButton = Button(window_4, text='Estimate waiting time', command=generateWindow_6)
        waitingTimeButton.grid(row=numRow+1, column=0)
    else:
        closedLabel = Label(topFrame, text='This store is currently closed. Would you like to check the operating time?')
        closedLabel.pack()

    operatingTimeButton = Button(bottomFrame, text='Check operating time', command=generateWindow_5)
    operatingTimeButton.pack()
        


    