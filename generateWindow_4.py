from tkinter import *
import datetime
import pandas as pd
from generateWindow_5 import *
from generateWindow_6 import *

# stallList = pd.read_csv('stallList.csv')
allStallMenu = pd.read_csv('stallMenu.csv')

# Author: Le Quang Anh
def showMenu(frame, stallMenu, meal):
    ''' Input:
    1) frame: the frame to show the menu items in (tkinter.Frame() object)
    2) stallMenu: the menu for the particular store
    3) meal: breakfast or lunch or dinner
    Output: show the dishes available for that meal
    '''

    stallMenuParticularMeal = stallMenu[stallMenu['Availability'] == meal]
    numRow = stallMenuParticularMeal.shape[0]
    # print(meal)

    for i in range(numRow):
        dishLabel = Label(frame, text=meal+' dishes')
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

# Author: Le Quang Anh
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

    window_4 = Toplevel()
    window_4.title(stallName)

    particularStallMenu = allStallMenu[allStallMenu['Stall'] == stallName]
    
    topFrame = Frame(window_4)
    topFrame.pack()
    bottomFrame = Frame(window_4)
    bottomFrame.pack()

    if statusMealTime != 'Closed':    
        showMenu(frame=topFrame, stallMenu=particularStallMenu, meal=statusMealTime)
        waitingTimeButton = Button(bottomFrame, text='Estimate waiting time', padx=10, pady=5, bg="yellow", \
                                   fg="black", command=generateWindow_6)
        waitingTimeButton.pack()
    else:
        closedLabel = Label(topFrame, text='This store is currently closed. Would you like to check the operating time?')
        closedLabel.pack()

    operatingTimeButtonCommand = lambda: generateWindow_5(stallName=stallName)
    operatingTimeButton = Button(bottomFrame, text='Check operating time', padx=10, pady=5, bg="purple", fg="white", \
                                command=operatingTimeButtonCommand)
    operatingTimeButton.pack()
        


    