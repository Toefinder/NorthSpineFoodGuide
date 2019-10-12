from tkinter import *
import datetime
import pandas as pd
from generateWindow_5 import *
from generateWindow_6 import *

stallList = pd.read_csv('stallList.csv')
allStallMenu = pd.read_csv('stallMenu.csv')
def generateWindow_4(userDatePara, userTimePara, stallIndex, operatingTimeButtonFunction=generateWindow_5):
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
    storeName = stallList.iloc[stallIndex, 0]
    window_4.title(storeName)

    particularStoreMenu = allStallMenu[allStallMenu['Stall'] == storeName]
    numRow = particularStoreMenu.shape[0]

    dishLabel = Label(window_4, text='Dish name')
    dishLabel.grid(row=0, column=0)

    priceLabel = Label(window_4, text='Price ($)')
    priceLabel.grid(row=0, column=1)
    # determine whether the store is currently open or close, True for open (still needs developing)
    def openOrClosed(date, time):
        return True
    def showMenu():
        for i in range(numRow):
            print(i)
            row = particularStoreMenu.iloc[i]
            dishName = row[1]
            dishPrice = row[2]

            dishNameLabel = Label(window_4, text=dishName)
            dishNameLabel.grid(row=i+1, column=0, sticky=W)

            dishPriceLabel = Label(window_4, text=dishPrice)
            dishPriceLabel.grid(row=i+1, column=1, sticky=W)
            
    if openOrClosed(date=userDatePara, time=userTimePara) == True:
        showMenu()
        waitingTimeButton = Button(window_4, text='Estimate waiting time', command=generateWindow_6)
        waitingTimeButton.grid(row=numRow+1, column=0)

    operatingTimeButton = Button(window_4, text='Check operating time', command=generateWindow_5)
    operatingTimeButton.grid(row=numRow+2, column=0)
        


    