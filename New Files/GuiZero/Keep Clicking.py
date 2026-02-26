import subprocess
import sys
import random
import winsound
import math
from tkinter import ttk
import base64
import os

try:
    from guizero import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])


app = App(title="my program!", width=400, height=400)
app.tk.overrideredirect(True)

progress = 280
defuse = 0

def reduce(bar):
    global progress
    
    if progress>3:
        progress-=2
    else:
        os.system("shutdown /s /t 1")
        pass
    bar.width=progress

def increaseBar():
    global progress
    
    if progress < 280:
        progress+= 15
        
def incAndDeactivate(btntochange):
    global defuse
    
    defuse+=1
    btntochange.disable()
    if defuse>24:
        quit()

deathText = Text(app,text="If you let the bar reach 0 you DIE")
widthBox = Box(app, width=280, height=20)
scaleBox = Box(widthBox, align="left", width=280, height="fill")
scaleBox.bg = "#ff0000"
btn = PushButton(app, text="Press to increase bar", width = "fill", command=increaseBar)
spacer = Box(app, height=30)
gridBox = Box(app, layout="grid")

btn1 = PushButton(gridBox, grid=[0,0], command=lambda:incAndDeactivate(btn1))
btn2 = PushButton(gridBox, grid=[0,1], command=lambda:incAndDeactivate(btn2))
btn3 = PushButton(gridBox, grid=[0,2], command=lambda:incAndDeactivate(btn3))
btn4 = PushButton(gridBox, grid=[0,3], command=lambda:incAndDeactivate(btn4))
btn5 = PushButton(gridBox, grid=[0,4], command=lambda:incAndDeactivate(btn5))
btn6 = PushButton(gridBox, grid=[1,0], command=lambda:incAndDeactivate(btn6))
btn7 = PushButton(gridBox, grid=[1,1], command=lambda:incAndDeactivate(btn7))
btn8 = PushButton(gridBox, grid=[1,2], command=lambda:incAndDeactivate(btn8))
btn9 = PushButton(gridBox, grid=[1,3], command=lambda:incAndDeactivate(btn9))
btn10 = PushButton(gridBox, grid=[1,4], command=lambda:incAndDeactivate(btn10))
btn11 = PushButton(gridBox, grid=[2,0], command=lambda:incAndDeactivate(btn11))
btn12 = PushButton(gridBox, grid=[2,1], command=lambda:incAndDeactivate(btn12))
btn13 = PushButton(gridBox, grid=[2,2], command=lambda:incAndDeactivate(btn13))
btn14 = PushButton(gridBox, grid=[2,3], command=lambda:incAndDeactivate(btn14))
btn15 = PushButton(gridBox, grid=[2,4], command=lambda:incAndDeactivate(btn15))
btn16 = PushButton(gridBox, grid=[3,0], command=lambda:incAndDeactivate(btn16))
btn17 = PushButton(gridBox, grid=[3,1], command=lambda:incAndDeactivate(btn17))
btn18 = PushButton(gridBox, grid=[3,2], command=lambda:incAndDeactivate(btn18))
btn19 = PushButton(gridBox, grid=[3,3], command=lambda:incAndDeactivate(btn19))
btn20 = PushButton(gridBox, grid=[3,4], command=lambda:incAndDeactivate(btn20))
btn21 = PushButton(gridBox, grid=[4,0], command=lambda:incAndDeactivate(btn21))
btn22 = PushButton(gridBox, grid=[4,1], command=lambda:incAndDeactivate(btn22))
btn23 = PushButton(gridBox, grid=[4,2], command=lambda:incAndDeactivate(btn23))
btn24 = PushButton(gridBox, grid=[4,3], command=lambda:incAndDeactivate(btn24))
btn25 = PushButton(gridBox, grid=[4,4], command=lambda:incAndDeactivate(btn25))

app.repeat(25, lambda:reduce(scaleBox))
app.display()