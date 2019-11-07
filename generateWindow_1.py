### the code below is for the main window of the foodApp

from tkinter import *

def generateWindow_1(now, nowButtonFunction, anotherTimeButtonFunction):
    '''Main window of the app
    Input: 
    1) now is the date and time to be displayed on the app interface
    2) nowButtonFunction: the command that executes when nowButton is pressed
    3) anotherTimeButtonFunction: the comman that executes when anotherTimeButton is pressed'''

    # current date and time
    currentDate = now.date()
    currentTime = now.time()

    # main window with appName as title, and geometry as specified (may adjust later)
    appName = 'Your North Spine Food Guide'
    window_1 = Tk()
    window_1.title(appName) 
    window_1.geometry('350x150+30+30')

    # welcome statement on the main window
    welcomeText = 'Hello user! Welcome to North Spine Food Guide!'
    welcomeLabel = Label(window_1, text= welcomeText, padx=10)
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
    askTimeText = '\nWhen are you planning to eat?'
    askTimeLabel = Label(window_1, text=askTimeText, padx=10)
    askTimeLabel.grid(row=3, column=0, columnspan=2, sticky=W)

    # button to choose to check the stores now, note that padding is used
    nowButtonCommand = lambda: nowButtonFunction(window=window_1, userDatePara=currentDate, \
                                                 userTimePara=currentTime)
    nowButton = Button(window_1, text="Check stores now!", padx=10, pady=5, bg="purple", fg="white",\
                    command=nowButtonCommand)
    nowButton.grid(row=4, column=0, sticky=W)

    # button to choose to check the stores at a user-defined date
    # note the use of lambda to make generateWindow_2(nowButtonFunction) a function name 
    anotherTimeButtonCommand = lambda: anotherTimeButtonFunction(window=window_1, \
                                                                currentDatePara=currentDate, \
                                                                currentTimePara=currentTime)
    anotherTimeButton = Button(window_1, text="Check stores at a different date & time", \
                            padx=10, pady=5, bg="yellow", fg="black", \
                            command=anotherTimeButtonCommand)
                            
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

    # showing an info box when window_1 is closed
    def onClosing():
        closingLine = 'Thank you for using Your North Spine Food Guide! See you next time!'
        closingWindowTitle = 'Exit'
        messagebox.showinfo(closingWindowTitle, closingLine)
        window_1.destroy()
    window_1.protocol('WM_DELETE_WINDOW', onClosing)

    window_1.mainloop()