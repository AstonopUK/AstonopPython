import subprocess, sys, random

try:
    from guizero import *
    from keyboard import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])

def testWave():
    global counter
    littleBox.after(100, lambda:waveFunc(4))
        
def waveFunc(amount):
    global counter
    collision = []
    for x in range(1,amount):
        items[counter][gridSize-x].bg = "#ffffff"
    counter-=1
    for x in range(1,amount):
        if counter > -1:
            collision.append([counter, gridSize-x])
            items[counter][gridSize-x].bg = "#0059c1"
        else:
            counter = 24
    if  [coords[0],coords[1]] in collision:
        app.disable()
        for lists in items:
            for item in lists:
                item.hide()
    littleBox.after(100, lambda:waveFunc(amount))

def move(btn):
    global coords, gravity
    match btn:
        case "⬅":
            items[coords[0]][coords[1]].bg = "#ffffff"
            if coords[0]!=0:
                coords[0] -= 1
            items[coords[0]][coords[1]].bg = "#999999"
        case "⬆":
            if coords[1] == (gridSize-1):
                gravity-=gravCap
        case "➡":
            items[coords[0]][coords[1]].bg = "#ffffff"
            if coords[0] < gridSize-1:
                coords[0] += 1
            items[coords[0]][coords[1]].bg = "#999999"

def refresh():
    global coords, gravity
    if coords[1]!=(gridSize-1):
        if gravity<gravCap:
            gravity+=1
            
    if gravity!=0:
        items[coords[0]][coords[1]].bg="#ffffff"
        if coords[1]+gravity<gridSize-1:
            coords[1]+=gravity
        else:
            while coords[1]+gravity>gridSize-1:
                gravity-=1
            coords[1]+=gravity
            gravity=0
        items[coords[0]][coords[1]].bg="#999999"

size = 18
gridSize = 25
gravity=24
gravCap = 5
items = []
counter = gridSize-1
collision = []

add_hotkey('up', lambda:move("⬆"))
add_hotkey('left', lambda:move("⬅"))
add_hotkey('right', lambda:move("➡"))

add_hotkey('space', testWave)

app = App(title="Jumper", width=450, height=600)

bigBox = Box(app, layout="grid", width="fill", height="fill")

for z in range(gridSize):
    items.append([])
for x in range(gridSize):
    for y in range(gridSize):
        items[x].append(Box(bigBox, grid=[x,y], width=size, height=size, border=0))
        items[x][y].bg="#ffffff"

coords = [3,gridSize-1]
items[coords[0]][coords[1]].bg = "#999999"

littleBox = Box(app, layout="grid", width=125, height=100)
upBtn = PushButton(littleBox, grid=[1,0], text="⬆", command=lambda:move(upBtn.text))
leftBtn = PushButton(littleBox, grid=[0,1], text="⬅", command=lambda:move(leftBtn.text))
downBtn = PushButton(littleBox, grid=[1,1], text="    ", enabled=False)
rightBtn = PushButton(littleBox, grid=[2,1], text="➡", command=lambda:move(rightBtn.text))

bigBox.repeat(40, refresh)
app.display()