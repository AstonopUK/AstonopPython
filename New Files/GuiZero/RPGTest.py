from guizero import *

app = App(layout="grid", bg="#797979", height=335)
app.tk.overrideredirect(1)

def flipObj(obj):
    for item in obj:
        if item.visible == True:
            item.hide()
        else:
            item.show()

def Run():
    app.info("Run", "You escaped successfully!")
    app.destroy()

leftBox = Box(app, grid=[0,0], width = 270, height = 125)
enemyName = Text(leftBox, align="top", text="Charizard GMAX", color="white", bold=True, italic=True)
enemyHealthBox = Box(leftBox, align="top", width = 175, height = 20)
enemyHealthBox.bg = "dark grey"
enemyHealthBar = Drawing(enemyHealthBox, align="left", width="fill")
enemyHealthBar.rectangle(3, 3, 172, 17, color="red")
playerSprite = Picture(app, image="vgmax.png", width = 136, height = 112, grid=[0,1])


rightBox = Box(app, grid=[1,1], width = 270, height = 125)
spacerBoxRight = Box(rightBox, align="bottom", height=5)
playerHealthBox = Box(rightBox, align="bottom", width = 175, height = 20)
playerHealthBox.bg = "dark grey"
playerName = Text(rightBox, align="bottom", text="Venusaur GMAX", color="white", bold=True, italic=True)
playerHealthBar = Drawing(playerHealthBox, align="left", width="fill")
playerHealthBar.rectangle(3, 3, 172, 17, color="red")
enemySprite = Picture(app, image="cgmax.png", width = 136, height = 112, grid=[1,0])


moveBox = Box(app, grid=[0,2], width=270, height=90, border=True)
moveBox.bg = "light grey"

movesText = Text(moveBox, align="top", text="What will you do?		         ")

movesUpper = Box(moveBox, align="top")
movesUpper.bg = "light grey"
btnMove1 = PushButton(movesUpper, text="Move1", align="left", width = 16)
btnMove2 = PushButton(movesUpper, text="Move2", align="left", width = 16)
movesUpper.hide()

movesLower = Box(moveBox, align="top")
movesLower.bg = "light grey"
btnMove3 = PushButton(movesLower, text="Move3", align="left", width = 16)
btnMove4 = PushButton(movesLower, text="Move4", align="left", width = 16)
movesLower.hide()


menuBox = Box(app, grid=[1,2], width="fill")
menuBox.bg = "light grey"

menuBoxUpper = Box(menuBox, align="top")
menuBoxUpper.bg = "light grey"
btnBag = PushButton(menuBoxUpper, text="Bag", align="right", width = 10)
btnFight = PushButton(menuBoxUpper, text="Fight", align="right", width = 10, command=lambda:flipObj([movesLower, movesUpper, movesText]))

menuBoxLower = Box(menuBox, align="top")
menuBoxLower.bg = "light grey"
btnRun = PushButton(menuBoxLower, text="Run", align="right", width = 10, command=Run)
btnTeam = PushButton(menuBoxLower, text="Team", align="right", width = 10)

app.display()