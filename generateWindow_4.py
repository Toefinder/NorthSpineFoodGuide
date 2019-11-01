from tkinter import *
import datetime
import pandas as pd
from generateWindow_5 import *
from generateWindow_6 import *

# stallList = pd.read_csv('stallList.csv')
allStallMenu = pd.read_csv('stallMenu.csv')

# operatingHours = pd.read_csv('operatingHours.csv')
# operatingHours = operatingHours.set_index('Stall') # set the column 'Stall' as index column

# def breakfastOrLunchOrDinnerOrClosed(date, time, stallName, operatingHours):
#     '''Input: 
#     1) date and time defined by user (datetime.date and datetime.time objects)
#     2) stallName is a string representing name of stall chosen by user
#     3) operatingHours is a dataframe of all the operating hours of the stalls, with stall name as index
#     Output: 
#     1) Return 'Lunch' if it's lunchtime and 'Breakfast' and 'Dinner' and 'Closed' if closed
#     '''
#     # Return the day of the week as an integer, where Monday is 0 and Sunday is 6 
#     dayOfWeek = date.weekday() 
#     if dayOfWeek <= 4: 
#         checkDate = 'Weekdays'
#     elif dayOfWeek == 5:
#         checkDate = 'Saturday' 
#     else:
#         checkDate = 'Sunday'
    
#     openingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == checkDate]['Opening Time'][0]

#     if openingTime == 'closed':
#         print('Closed!')
#         return 'Closed'
#     openingTimeObject = datetime.datetime.combine(date, \
#                         datetime.datetime.strptime(openingTime, '%H:%M').time())

#     closingTime = operatingHours.loc[stallName][operatingHours.loc[stallName, 'Day'] == checkDate]['Closing Time'][0]
#     closingTimeObject = datetime.datetime.combine(date, \
#                         datetime.datetime.strptime(closingTime, '%H:%M').time())

#     breakfastEndTimeObject = datetime.datetime.combine(date, datetime.time(11,0))

#     lunchEndTimeObject = datetime.datetime.combine(date, datetime.time(17,0))
    
#     userDefinedTime = datetime.datetime.combine(date, time)
#     if openingTimeObject <= userDefinedTime < breakfastEndTimeObject:
#         print("breakfast!")
#         return 'Breakfast'
#     elif breakfastEndTimeObject <= userDefinedTime <= lunchEndTimeObject:
#         print('Lunch!')
#         return 'Lunch'
#     elif lunchEndTimeObject <= userDefinedTime <= closingTimeObject:
#         print('Dinner!')
#         return 'Dinner'
#     else: 
#         print('closed!')
#         return 'Closed'


def showMenu(frame, stallMenu, meal):
    ''' Input:
    1) frame: the frame to show the menu items in (tkinter.Frame() object)
    2) stallMenu: the menu for the particular store
    3) meal: breakfast or lunch or dinner
    Output: show the dishes available for that meal
    '''

    stallMenuParticularMeal = stallMenu[stallMenu['Availability'] == meal]
    numRow = stallMenuParticularMeal.shape[0]

    for i in range(numRow):
        dishLabel = Label(frame, text='Dish name')
        dishLabel.grid(row=0, column=0)

        priceLabel = Label(frame, text='Price ($)')
        priceLabel.grid(row=0, column=1)

        row = stallMenu.iloc[i]
        dishName = row[1]
        dishPrice = row[2]

        dishNameLabel = Label(frame, text=dishName)
        dishNameLabel.grid(row=i+1, column=0, sticky=W)

        dishPriceLabel = Label(frame, text=dishPrice)
        dishPriceLabel.grid(row=i+1, column=1, sticky=W)

    waitingTimeButton = Button(frame, text='Estimate waiting time', command=generateWindow_6)
    waitingTimeButton.grid(row=numRow+1, column=0)


def generateWindow_4(userDatePara, userTimePara, stallName, statusMealTime, operatingTimeButtonFunction=generateWindow_5):
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



    # determine whether the store is currently open or close, True for open (still needs developing)
    
    topFrame = Frame(window_4)
    topFrame.pack()
    bottomFrame = Frame(window_4)
    bottomFrame.pack()

    # statusMealTime = breakfastOrLunchOrDinnerOrClosed(date=userDatePara, time=userTimePara, \
    #                                                   stallName=stallName, operatingHours=operatingHours)
    if statusMealTime != 'Closed':    
        showMenu(frame=topFrame, stallMenu=particularStallMenu, meal=statusMealTime)
    else:
        closedLabel = Label(topFrame, text='This store is currently closed. Would you like to check the operating time?')
        closedLabel.pack()

    operatingTimeButtonCommand = lambda: generateWindow_5(stallName=stallName)
    operatingTimeButton = Button(bottomFrame, text='Check operating time', command=operatingTimeButtonCommand)
    operatingTimeButton.pack()
        


    