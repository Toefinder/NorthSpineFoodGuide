from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry
import datetime

now = datetime.datetime.now()

window_2 = Tk()

def generateWindow_3():
    pass
    
def enterDate():
    '''Let user set the date'''
    top = Toplevel(window_2)
    top.geometry('300x300+30+30')
    chooseDateLabel = Label(top, padx=10, pady=10, text='Choose date')
    chooseDateLabel.pack()

    mindate = currentDate
    maxdate = mindate + datetime.timedelta(days=365)
    print(mindate,maxdate)

    cal = Calendar(top, mindate=mindate, maxdate=maxdate, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    # cal.bind('<<CalendarSelected>>', print(cal.get_date()))
    def getUserDate():
        global userDate
        userDate = cal.selection_get()
        print('userDate now is ', userDate)
        dateLabel['text']=userDate  #update userDate in the dateLabel of window_2
        top.destroy()

    okDateButton = Button(top, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getUserDate)
    okDateButton.pack()

def enterTime():
    '''Let user set the time'''
    top = Toplevel(window_2)
    top.geometry('300x150+30+30')

    topFrame = Frame(top)
    topFrame.pack()
    bottomFrame = Frame(top)
    bottomFrame.pack()

    # *****status bar*****
    status = Label(top, text = 'Entering...', bd = 1, relief = SUNKEN, anchor= W)
    status.pack(side = BOTTOM, fill = X)

    label1 = Label(topFrame, padx=10, pady=5, text='Please input time in 24 hr format')
    label1.pack(side=LEFT)

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
            if 0<= hourEnteredInt <= 23 and 0<= minuteEnteredInt <= 59:
                global userTime
                userTime = datetime.time(hourEnteredInt, minuteEnteredInt)
                timeLabel['text'] = userTime.strftime('%H:%M')
                top.destroy()
            else:
                status['text'] = 'Please check your input. Use 24 hr format!'
        except ValueError:
            status['text'] = 'Please check your input. Integer values only!'


    okTimeButton = Button(bottomFrame, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getUserTime)
    okTimeButton.grid(row=2, column=1)



    # label2 = Button(top, padx=10, pady=5, bg='purple', fg='white', text='Ok', command=getUserDate)
    # label2.pack()

# default value of userDate and userTime
currentDate = now.date()
currentTime = now.time()
userDate = currentDate
userTime = currentTime

enterDateButton = Button(window_2, text='Enter Date', padx=10, pady=5, command=enterDate)
enterDateButton.grid(row=0, column=0)
dateLabel = dateLabel = Label(window_2, text=userDate, padx=10, pady=5)
dateLabel.grid(row=0, column=1,sticky=W)

enterTimeButton = Button(window_2, text='Enter Time', padx=10, pady=5, command=enterTime)
enterTimeButton.grid(row=1, column=0)
timeLabel = Label(window_2, text=userTime.strftime('%H:%M'), padx=10, pady=5)
timeLabel.grid(row=1, column=1,sticky=W)

okDateTimeButton = Button(window_2, padx=10, pady=5, bg='purple', fg='white', text='Ok', command = generateWindow_3)
okDateTimeButton.grid(row=2, column=0, columnspan=2)


window_2.mainloop()










