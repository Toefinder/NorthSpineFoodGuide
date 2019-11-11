import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from generateWindow_1 import *
from generateWindow_2 import *
from generateWindow_3 import *

# get current date and time 
now = datetime.datetime.now()

generateWindow_1(now=now, nowButtonFunction=generateWindow_3, anotherTimeButtonFunction=generateWindow_2)

