from guizero import *

app = App(title = "Battleships", width = 900, height = 925, layout="grid")
startSequence = True

def btnPressed(btn):
    global startSequence
    global p1ShipLoc
    global p2ShipLoc
    
    if startSequence == True:
        btn.text = "🛥"

def startGame(startBtn, p1Grid, p2Grid,iTxt):
    global p1ShipLoc
    global p2ShipLoc
    p1ShipLoc = []
    p2ShipLoc = []
    
    startBtn.hide()
    p1Grid.enable()
    instructions.value = "Welcome to Battleships. Each player has a number of 'ships' the other player must sink.\nTo begin, Player 1 will choose the location of their 12 ships on the board.\n Then Player 2 will have the chance to place their ships."



p1Grid = TitleBox(app, text="P1 Grid", layout="grid", grid=[0,0])
p1Grid.bg="grey"
p2Grid = TitleBox(app, text="P2 Grid", layout="grid", grid=[0,1])
p2Grid.bg="grey"
p1Grid.disable()
p2Grid.disable()

p1Btns = []
p2Btns = []

for x in range(10):
    for y in range(10):
        p1Btns.append(PushButton(p1Grid, grid=[x,y], text="", width=2, command=lambda c=((x*10)+y): btnPressed(p1Btns[c])))
        p2Btns.append(PushButton(p2Grid, grid=[x,y], text="", width=2))
        
instructBox = TitleBox(app, grid=[1,0], width=470, height=450, text="Instructions")
instructions = Text(instructBox, text="To start the game, press the button in this box.")
startBtn = PushButton(instructBox, text="Start Game", command=lambda:startGame(startBtn, p1Grid, p2Grid, instructions))

app.display()