import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

# get current date and time 
now = datetime.datetime.now()

def generateWindow_2():
    '''Generate window to check stores at a prescribed time'''
    window_2 = Toplevel()
    window_2.title("Choose date & time")
    window_2.geometry('300x300')
            
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



    # if now.weekday() == 0:
    #     label = Label(window_2, text="Chocolate cake\nStrawberry cake\nBlueberry cake")
    # else:
    #     label = Label(window_2, text="Non-Monday menu")
    # label.pack()

def generateWindow_3():
    window = Toplevel()
    window.geometry('300x300')
    label = Label(window, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    label.pack()

def generateWindow_4():
    window = Toplevel()
    window.geometry('300x300')
    label = Label(window, text="Souffle\nIce Cream\nMatcha Pancakes")
    label.pack()


# some key variables
appName = "Your North Spine Food Guide"

# main window with appName as title, and geometry as specified (may adjust later)
window_1 = Tk()
window_1.title(appName) 
window_1.geometry('350x150+30+30')

# welcome statement on the main window
welcomeLabel = Label(window_1, text="Hello user! Welcome to North Spine Food Guide!", padx=10)
welcomeLabel.grid(row=0, column=0, columnspan=2, sticky=W)   #pack it in first row first column



# # function to keep updating the date and time label, for now let's not do this
# def changeLabel(self):
#     self.time2 = datetime.datetime.today()
#     clock.configure(text=self.time2)
#     window.after(200, changeLabel)  # it'll call itself continuously (cant work idk why)

# labels of current date and current time
currentDateLabel_1 = Label(window_1, text='Current date: ', padx=10)
currentDateLabel_1.grid(row=1, column=0, sticky=W)
currentDateLabel_2 = Label(window_1, text=now.strftime('%Y-%m-%d'))
currentDateLabel_2.grid(row=1, column=1, sticky=W)

currentTimeLabel_1 = Label(window_1, text='Current time: ', padx=10)
currentTimeLabel_1.grid(row=2, column=0, sticky=W)
currentTimeLabel_2 = Label(window_1, text=now.strftime('%H:%M') )
currentTimeLabel_2.grid(row=2, column=1, sticky=W)

# label to ask whether user wants to eat now or another user-defined time
askTimeLabel = Label(window_1, text='\nWhen are you planning to eat?', padx=10)
askTimeLabel.grid(row=3, column=0, columnspan=2, sticky=W)

# button to choose to check the stores now, note that padding is used
nowButton = Button(window_1, text="Check stores now!", padx=10, pady=5, bg="purple", fg="white",\
                   command=generateWindow_3)
nowButton.grid(row=4, column=0, sticky=W)

# button to choose to check the stores at a user-defined date
anotherTimeButton = Button(window_1, text="Check stores at a different date & time", \
                           padx=10, pady=5, bg="yellow", fg="black", command=generateWindow_2)
anotherTimeButton.grid(row=4, column=1, sticky=W)

# btn = Button(window_1, text="Pancake Shop!", bg="pink", fg="black", command=generate_new_window2)
# btn.grid(column=0, row=3)

# time2 = datetime.datetime.today().weekday()
# clock = Label(window_1, text=time2, font=('times',12,'bold'))
# clock.grid(column=0, row=4)

## show information of operating hours
# def info():
#    messagebox.showinfo("Operating Hours", "Weekdays: 8am-8pm\nWeekends: 8am-5pm")
# btn = Button(window_1, text = "Operating Hours", command = info)
# btn.grid(column=0, row=7)

# # button to quit the program, I am thinking of having a window to thank the user, but probably later
# btn = Button(window_1, text="Quit", command=window_1.destroy)
# btn.grid(column=0, row=10)




## set up "File" and "Edit" drop down menus (not so important)
# menu = Menu(window)
# window.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')


window_1.mainloop()