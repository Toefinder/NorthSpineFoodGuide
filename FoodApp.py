import tkinter
import datetime
from tkinter import *
from tkinter import messagebox


now = datetime.datetime.today()

def changeLabel(self):
    self.time2 = datetime.datetime.today()
    clock.configure(text=self.time2)
    window.after(200, changeLabel)  # it'll call itself continuously (cant work idk why)

def generate_new_window():
    window = tkinter.Toplevel()
    window.title("Cake Shop!")
    window.geometry('300x300')

    if now.weekday() == 0:
        label = tkinter.Label(window, text="Chocolate cake\nStrawberry cake\nBlueberry cake")
    else:
        label = tkinter.Label(window, text="Non-Monday menu")


    label.pack()

def generate_new_window1():
    window = tkinter.Toplevel()
    window.geometry('300x300')
    label = tkinter.Label(window, text="Chocolate bread\nStrawberry bread\nBlueberry bread")
    label.pack()

def generate_new_window2():
    window = tkinter.Toplevel()
    window.geometry('300x300')
    label = tkinter.Label(window, text="Souffle\nIce Cream\nMatcha Pancakes")
    label.pack()


window = Tk()
window.title("Welcome to Food app")
window.geometry('300x300')
lbl = Label(window, text="Hello user, what would you like to have today?")
lbl.grid(column=0, row=0)
btn = Button(window, text="Cake Shop!", bg="blue", fg="black", command=generate_new_window)
btn.grid(column=0, row=1)
btn = Button(window, text="Bread Shop!", bg="yellow", fg="black", command=generate_new_window1)
btn.grid(column=0, row=2)
btn = Button(window, text="Pancake Shop!", bg="pink", fg="black", command=generate_new_window2)
btn.grid(column=0, row=3)

time2 = datetime.datetime.today().weekday()
clock = Label(window, text=time2, font=('times',12,'bold'))
clock.grid(column=0, row=4)

def info():
   messagebox.showinfo("Operating Hours", "Weekdays: 8am-8pm\nWeekends: 8am-5pm")
btn = Button(window, text = "Operating Hours", command = info)
btn.grid(column=0, row=7)

btn = Button(window, text="Quit", command=window.destroy)
btn.grid(column=0, row=10)




root = window
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
root.geometry("200x200")



root.mainloop()
