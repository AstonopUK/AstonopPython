from tkinter import *
from tkinter.ttk import *
import random

# creates a Tk() object
master = Tk()
chars = "123456789abcdef"
# sets the geometry of main 
# root window

def disable_event():
    pass

def waithere():
    var = IntVar()
    master.after(30, var.set, 1)
    print("waiting...")
    master.wait_variable(var)

def openNewWindow():
    num = 2
    for x in range(100): 
        num = num + 1
        
        #Setting the height, width and location of windows to a random integer
        h = random.randint(200,1000)
        w = random.randint(200,1000)
        x = random.randint(0,1980)
        y = random.randint(0,1000)
        
        #Creating a random hexcode for a colour
        colourChange = '#'
        for i in range(6):
            colourChange += chars[random.randint(0,14)]
        
        waithere()
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        
        #Don't unhash this or you can't close the windows lol
        #newWindow.overrideredirect(True)
        newWindow.protocol("WM_DELETE_WINDOW", openNewWindow)
        
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
     
        # sets the geometry of toplevel
        newWindow.geometry("%dx%d+%d+%d" % (h,w,x,y))
        
        #sets colour of background to random hex code
        newWindow['background'] = colourChange
     
        # A Label widget to show in toplevel
        #Label(newWindow, text =str(num)).pack()
        
master.geometry("300x100+900+500")
#master.protocol("WM_DELETE_WINDOW", disable_event)

#Don't unhash this or you can't close the windows lol
#master.overrideredirect(True)
label = Label(master, text ="Don't click the button. You've been warned.")
 
label.pack(pady = 10)
 
# a button widget which will open a 
# new window on button click
btn = Button(master, text ="Don't click me!", command = openNewWindow)
btn.pack(pady = 10)
mainloop()