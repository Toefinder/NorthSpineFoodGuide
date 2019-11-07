### the code below is for a window for user to input date and time

import datetime
from tkinter import *
from tkcalendar import Calendar
from generateWindow_3 import *

# # get current date and time 
# now = datetime.datetime.now()




# window to choose time and date
def generateWindow_2(window, currentDatePara, currentTimePara, okButtonFunction=generateWindow_3):
    '''
    Input: 
    1) window object 2) okButtonFunction
    Output: 
    1) window object is iconify, and window_2 is opened for users to choose date and time,
    global userDate and userTime are updated
    2) The function passed in as a parameter points to the next interface'''
    
    window.iconify()
    window_2 = Toplevel()
    window_2.title("Choose date & time")
    window_2.geometry('240x130')

    # default value of userDate and userTime
    global userDate
    global userTime
    userDate = currentDatePara
    userTime = currentTimePara
            
    def enterDate():
        '''Let user set the date'''
        top = Toplevel(window_2)
        topText = 'Choose Date'
        top.title(topText)
        top.geometry('300x300+30+30')
        chooseDateText = 'Please click to choose a date'
        chooseDateLabel = Label(top, padx=10, pady=10, text=chooseDateText)
        chooseDateLabel.pack()

        mindate = currentDatePara
        maxdate = mindate + datetime.timedelta(days=365)
        # print(mindate,maxdate)

        cal = Calendar(top, mindate=mindate, maxdate=maxdate, width=12, background='darkblue',
                        foreground='white', borderwidth=2)
        cal.pack(padx=10, pady=10)
        # cal.bind('<<CalendarSelected>>', print(cal.get_date()))
        def getUserDate():
            global userDate
            userDate = cal.selection_get()
            # print('userDate now is ', userDate)
            dateLabel['text']=userDate  #update userDate in the dateLabel of window_2
            top.destroy()
            # end of getUserDate()

        okDateButton = Button(top, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getUserDate)
        okDateButton.pack()
        
        # end of enterDate()

    def enterTime():
        '''Let user set the time, for now still haven't handled the exception case where date entered is 
        the same but time is in the past, for example today but 1 hour ago '''
        top = Toplevel(window_2)
        topName = 'Choose time'
        top.title(topName)
        top.geometry('300x150+30+30')

        topFrame = Frame(top)
        topFrame.pack()
        bottomFrame = Frame(top)
        bottomFrame.pack()

        # *****status bar*****
        status = Label(top, text = 'Entering...', bd = 1, relief = SUNKEN, anchor= W)
        status.pack(side = BOTTOM, fill = X)

        chooseTimeText = 'Please input time in 24 hr format'
        chooseTimeLabel = Label(topFrame, padx=10, pady=5, text=chooseTimeText)
        chooseTimeLabel.pack(side=LEFT)

        hourLabel = Label(bottomFrame, padx=10, pady=5, text='Enter hour')
        hourLabel.grid(row=0, column=0)
        hourEntry = Entry(bottomFrame)
        hourEntry.grid(row=1, column=0)


        separatorLabel = Label(bottomFrame, padx=10, pady=5, text=' : ')
        separatorLabel.grid(row=1, column=1)
        
        minuteLabel = Label(bottomFrame, padx=10, pady=5, text='Enter minute')
        minuteLabel.grid(row=0, column=2)
        minuteEntry = Entry(bottomFrame)
        minuteEntry.grid(row=1, column=2)

        def getUserTime():
            hourEnteredStr = hourEntry.get()
            minuteEnteredStr = minuteEntry.get()

            try: 
                hourEnteredInt = int(hourEnteredStr) 
                minuteEnteredInt = int(minuteEnteredStr)
                if 0 <= hourEnteredInt <= 23 and 0 <= minuteEnteredInt <= 59:
                    global userTime
                    userTime = datetime.time(hourEnteredInt, minuteEnteredInt)
                    timeLabel['text'] = userTime.strftime('%H:%M')
                    top.destroy()
                else:
                    status['text'] = 'Please check your input. Use 24 hr format!'
            except ValueError:
                status['text'] = 'Please check your input. Integer values only!'

            # end of getUserTime()

        okTimeButton = Button(bottomFrame, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getUserTime)
        okTimeButton.grid(row=2, column=1)

        # end of enterTime()

    window2_maintext = "Choose Date and Time!"
    window2_mainLabel = Label(window_2, text=window2_maintext, fg='white', bg='black', padx=50)
    window2_mainLabel.config(height = 2)
    window2_mainLabel.grid(row=0, column=0, columnspan=2, sticky=N)

    enterDateButton = Button(window_2, text='Enter Date', command=enterDate)
    enterDateButton.config(height = 1, width = 10)
    enterDateButton.grid(row=1, column=0, sticky=W)
    dateLabel = dateLabel = Label(window_2, text=userDate, padx=10, pady=5)
    dateLabel.grid(row=1, column=1)

    enterTimeButton = Button(window_2, text='Enter Time', command=enterTime)
    enterTimeButton.config(height=1, width=10)
    enterTimeButton.grid(row=2, column=0, sticky=W)
    timeLabel = Label(window_2, text=userTime.strftime('%H:%M'), padx=10, pady=5)
    timeLabel.grid(row=2, column=1)

    # def functionAdjusted(fn):
    #     '''Close window_2 and carry out the function fn (carry out generateWindow_3)'''
    #     window_2.destroy()
    #     fn()
    
    okDateTimeButtonCommand = lambda: okButtonFunction(window=window_2, userDatePara=userDate, userTimePara=userTime)
    okDateTimeButton = Button(window_2, padx=100, pady=5, bg='purple', fg='white', text='OK', \
                              command=okDateTimeButtonCommand)
    okDateTimeButton.grid(row=3, column=0, columnspan=2, sticky = S+W)
    
    # end of generateWindow_2()