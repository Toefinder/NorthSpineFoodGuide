import datetime
from tkinter import *
import pandas as pd
from generateWindow_4 import *
from generateWindow_5 import *

df = pd.read_csv('stallList.csv')
operatingHours = pd.read_csv('operatingHours.csv')
operatingHours = operatingHours.set_index('Stall') # set the column 'Stall' as index column

def breakfastOrLunchOrDinnerOrClosed(date, time, stallName, operatingHours):
    '''Input: 
    1) date and time defined by user (datetime.date and datetime.time objects)
    2) stallName is a string representing name of stall chosen by user
    3) operatingHours is a dataframe of all the operating hours of the stalls, with stall name as index
    Output: 
    1) Return 'Lunch' if it's lunchtime and 'Breakfast' and 'Dinner' and 'Closed' if closed
    '''
    # Return the day of the week as an integer, where Monday is 0 and Sunday is 6 
    dayOfWeek = date.weekday() 
    if dayOfWeek <= 4: 
        checkDate = 'Weekdays'
    elif dayOfWeek == 5:
        checkDate = 'Saturday' 
    else:
        checkDate = 'Sunday'
    
    openingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == checkDate]['Opening Time'][0]

    if openingTime == 'closed':
        print('Closed!')
        return 'Closed'
    openingTimeObject = datetime.datetime.combine(date, \
                        datetime.datetime.strptime(openingTime, '%H:%M').time())

    closingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == checkDate]['Closing Time'][0]
    closingTimeObject = datetime.datetime.combine(date, \
                        datetime.datetime.strptime(closingTime, '%H:%M').time())

    breakfastEndTimeObject = datetime.datetime.combine(date, datetime.time(11,0))

    lunchEndTimeObject = datetime.datetime.combine(date, datetime.time(17,0))
    
    userDefinedTime = datetime.datetime.combine(date, time)
    if openingTimeObject <= userDefinedTime < breakfastEndTimeObject:
        print("breakfast!")
        return 'Breakfast'
    elif breakfastEndTimeObject <= userDefinedTime <= lunchEndTimeObject:
        print('Lunch!')
        return 'Lunch'
    elif lunchEndTimeObject <= userDefinedTime <= closingTimeObject:
        print('Dinner!')
        return 'Dinner'
    else: 
        print('closed!')
        return 'Closed'

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
    numRow = df.shape[0]
    buttonDict ={}
    for i in range(numRow):
        print(i)
        buttonDict[i] = [0,0,0]
        row = df.iloc[i] # row Series
        stallName = row[0] # name of stall 

        #stallButtonCommand
        # print(breakfastOrLunchOrDinnerOrClosed(date=userDatePara, time=userTimePara, \
        #                                     stallName=stallName, operatingHours=operatingHours))

        statusMealTime = breakfastOrLunchOrDinnerOrClosed(date=userDatePara, time=userTimePara, \
                                                    stallName=stallName, operatingHours=operatingHours)
        if statusMealTime != 'Closed':
            photo = PhotoImage(file=row[4])
            print(row[3])
        else:
            photo = PhotoImage(file=row[3])
            print(row[4])


        buttonDict[i][1] = (lambda x=stallName : stallButtonFunction(userDatePara=userDatePara, userTimePara=userTimePara, \
                                                         stallName=x, statusMealTime=statusMealTime))
        buttonDict[i][0] = Button(bottomFrame, image=photo, command=buttonDict[i][1])
        buttonDict[i][2] = Label(bottomFrame, text=row[0])

        # row and column position for the stall buttons
        rowPosition = 2 * (i // 5)
        colPosition = i % 5

        buttonDict[i][0].grid(row=rowPosition, column=colPosition)
        buttonDict[i][2].grid(row=rowPosition+1,column=colPosition)

        
    


    # print(userDatePara)
    # print(userTimePara)
    # print(type(userDatePara))
    # print(type(userTimePara))
    
    # label = Label(window_3, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    # label.()