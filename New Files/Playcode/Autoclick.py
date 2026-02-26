import ctypes
from guizero import *
from time import sleep
  
def autoclick(text1, text2):
    numclicks = int(text2.value)
    clickdelay = 1/(int(text1.value)*2)
    
    sleep(3)
    
    for x in range(numclicks):
        ctypes.windll.user32.mouse_event(2,0,0,0,0)
        sleep(clickdelay)
        ctypes.windll.user32.mouse_event(4,0,0,0,0)
        sleep(clickdelay)

app = App(title="Autoclicker 1.0", width=325, height=80)
app.font = "OCR A Extended"
app.text_size = 10
app.bg = "light grey"

topBox = Box(app, width="fill")
toplabel = Text(topBox, align="left", text="Clicks per second: ", width="fill")
clickSpeed = TextBox(topBox, align="left", text="", width="fill")
bottomBox = Box(app, width="fill")
toplabel = Text(bottomBox, align="left", text="Number of clicks: ", width="fill")
clickCount = TextBox(bottomBox, align="left", text="", width="fill")
start = PushButton(app, width="fill", text="Start clicking", command=lambda:autoclick(clickSpeed, clickCount))

app.display()