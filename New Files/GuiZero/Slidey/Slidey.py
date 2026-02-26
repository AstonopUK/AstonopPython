import subprocess
import sys
import random

try:
    from guizero import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])

swapCheck = False
btns = []

def swap(btn):
    global swapCheck
    global pics
    
    btns.append(btn)
    if swapCheck == False:
        swapCheck = True
    else:
        pics = [btn[0].image, btn[1].image_]
        btns[0].image = pics[1]
        btns[1].image = pics[0]
        swapCheck = False
        btns = []
        pics = []

emojis_dir = "images"
images = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]

app = App(title="Slidey Puzzle", layout = "grid", width=500, height=500)

buttons = []
for x in range(4):
    for y in range(4):
        buttons.append(PushButton(app, grid=[x,y], image=images[(x*4)+y], width=120, height=120, command=lambda:swap(self)))
app.display()