#Downloading the libraries
from Tkinter import *
import time
from datetime import datetime

#Setup class
class Setup:

    #Initializing function for setup window
    def __init__(self, master):

        #Setting up frame(parent widget)
        frame = Frame(master)
        frame.pack()

        #Setting up the hour:minute text and text area
        self.hour_enter = Entry(width = 2)
        self.minute_enter = Entry(width = 2)
        self.hour = Label(text="Hour[0, 23]")
        self.minute = Label(text="Minute[00, 59]")
        self.colon = Label(text=":")

        self.hour.pack(side=LEFT)
        self.hour_enter.pack(side=LEFT)
        self.colon.pack(side=LEFT)
        self.minute.pack(side=LEFT)
        self.minute_enter.pack(side=LEFT)

        #Setting up the day text and text area
        self.day_enter = Entry(width = 2)
        self.day = Label(text="          Day[1, 31]")

        self.day.pack(side=LEFT)
        self.day_enter.pack(side=LEFT)

        #Setting up the month text and text area
        self.month_enter = Entry(width = 2)
        self.month = Label(text="Month[01, 12]")

        self.month.pack(side=LEFT)
        self.month_enter.pack(side=LEFT)

        #Setting up the year text and text area
        self.year_enter = Entry(width = 2)
        self.year = Label(text="Year[Last two digits only]")

        self.year.pack(side=LEFT)
        self.year_enter.pack(side=LEFT)

        #Setting up the OK button
        self.ok_button = Button(text = "OK", command = self.countdown)
        self.ok_button.pack(side=LEFT)

    #Setting up countdown
    def countdown(self):

        #Variables for inputs and formats
        hour = self.hour_enter.get()
        minute = self.minute_enter.get()
        day = self.day_enter.get()
        month = self.month_enter.get()
        year = self.year_enter.get()
        fmt = "%H; %M; %d; %m; %y;"
        date = hour + "; " + minute + "; " + day + "; " + month + "; " + year + ";"

        #Setting up time to count to
        t2 = time.strptime(date, fmt)

        i = 1
        while i == 1:

            #Printing countdown
            t1 = time.localtime()
            print(time.mktime(t2)-time.mktime(t1))

            #Checking if event is now
            if time.mktime(t2)-time.mktime(t1) == 0:
                print("All done")
                break

            time.sleep(1)


#Tkinter parent widget
root = Tk()
root.title("Enter Date")

#Initializing Setup window with root as the tkinter widget
setup = Setup(root)

#Running the tkinter instance and closing it to be safe
root.mainloop()
root.destroy()
