import subprocess, sys, random

try:
    from guizero import *
    from keyboard import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])

def move(btn):
    global coord
    match btn:
        case "⬅":
            items[coord].bg = "#ffffff"
            if coord < gridSize:
                coord = (coord-gridSize)+(gridSize**2)
            else:
                coord -= gridSize
            items[coord].bg = "#999999"
        case "⬆":
            items[coord].bg = "#ffffff"
            if coord%gridSize==0:
                coord=coord+(gridSize-1)
            else:
                coord -= 1
            items[coord].bg = "#999999"
        case "➡":
            items[coord].bg = "#ffffff"
            if coord > (((gridSize**2)-1)-gridSize):
                coord = (coord+gridSize)-(gridSize**2)
            else:
                coord += gridSize
            items[coord].bg = "#999999"
        case "⬇":
            items[coord].bg = "#ffffff"
            if (coord+1)%gridSize==0:
                coord=coord-(gridSize-1)
            else:
                coord += 1
            items[coord].bg = "#999999"
    print(coord)
    
coord = 0

add_hotkey('up', lambda:move("⬆"))
add_hotkey('down', lambda:move("⬇"))
add_hotkey('left', lambda:move("⬅"))
add_hotkey('right', lambda:move("➡"))

app = App(title="Jumper", width=450, height=600)

bigBox = Box(app, layout="grid", width="fill", height="fill")
items = []
size = 18
gridSize = 25
for x in range(gridSize):
    for y in range(gridSize):
        items.append(Box(bigBox, grid=[x,y], width=size, height=size))
        items[(x*gridSize)+y].bg="#ffffff"
        
items[coord].bg = "#999999"

littleBox = Box(app, layout="grid", width=125, height=100)
upBtn = PushButton(littleBox, grid=[1,0], text="⬆", command=lambda:move(upBtn.text))
leftBtn = PushButton(littleBox, grid=[0,1], text="⬅", command=lambda:move(leftBtn.text))
downBtn = PushButton(littleBox, grid=[1,1], text="⬇", command=lambda:move(downBtn.text))
rightBtn = PushButton(littleBox, grid=[2,1], text="➡", command=lambda:move(rightBtn.text))

app.display()