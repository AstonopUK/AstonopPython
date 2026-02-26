#Lock Game
from guizero import *

def lockChecks():
    if slideKey.value > 25:
        dropdownLock.visible = True
    else:
        dropKey.value = ""
        dropdownLock.visible = False
        comboLock.visible = False
    if dropKey.value == "Key":
        comboLock.visible = True

def startGame():
    startButton.hide()
    slideLock.show()
    
def reduce(object):
    object.value = object.value-1

app = App(title="The Lock Game", width=200, height=200)

startButton = PushButton(app, text="Start game!", command=startGame)

slideLock = TitleBox(app, text="The First Lock", visible=False, width="fill")
slideKey = Slider(slideLock, width="fill")

dropdownLock = TitleBox(app, text="The Second Lock", visible=False, width="fill")
dropKey = Combo(dropdownLock, options=["","","","","","","","Key"], width="fill")

comboLock = TitleBox(app, text="The Third Lock", visible=False, width="fill")
clb1 = Box(comboLock)
text1 = TextBox(clb1, align="left", width=3)
text2 = TextBox(clb1, align="left", width=3)
text3 = TextBox(clb1, align="left", width=3)
text4 = TextBox(clb1, align="left", width=3)
clb2 = Box(comboLock)
entryBtn = PushButton(clb2, text="Click to enter code")


slideKey.repeat(100, lambda:reduce(slideKey))
startButton.repeat(100, lockChecks)
app.display()