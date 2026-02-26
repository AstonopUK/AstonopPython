# EmojiFight V0
import os
from guizero import *
from random import *

class emoji:
    def __init__(self, image, name):
        self.maxhealth = randint(30,50)
        self.attack = randint(5,20)
        self.spattack = randint(5,20)
        self.defence = randint(5,20)
        self.spdefence = randint(5,20)
        self.health = self.maxhealth
        
        self.image = image
        self.name = name
    
    def saveToFile(file):
        writeInfo = [self.name, self.image.value, self.health, self.attack, self.spattack, self.defence, self.spdefence]
        file.write(writeInfo)

emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]

party = []
names = []
with open("NameList.txt", 'r') as file:
    for line in file:
        names.append(line[:5])
print(names)

startSequence = True
textProgression = 0
introText = ["Hello! Welcome to Emoji Fight.",
             "You will encounter emojis in this world that want to fight.",
             "Some will fight for you, if you get to know them.",
             "See if you can collect all the emojis and make a powerful team!",
             "First, you'll need a starting emoji. Pick from one of these three."]

outroText = ["Your emoji will be an invaluable partner. Look after them.",
             "Now I will cast you into the world of emojis!",
             "Learn, explore and fight to become the strongest emoji owner!"]

def pickStartEmoji(ctBtn, startBox):
    ctBtn.hide()
    topchoicespacer = Box(app, align="top", height=15, width=0)
    choiceBox = TitleBox(app, align="top", text="Emoji Choices")
    
    choice1 = Box(choiceBox, align="left")
    emoji1 = PushButton(choice1, image=emojis[randint(0,len(emojis)-1)], align="top", command=lambda:emojiSelected(emoji1, choiceBox, startBox))
    text1 = Text(choice1, align="top", text="Placeholder")
    choicespacer1 = Box(choiceBox, align="left", width=10, height=0)
    
    choice2 = Box(choiceBox, align="left")
    emoji2 = PushButton(choice2, image=emojis[randint(0,len(emojis)-1)], align="top", command=lambda:emojiSelected(emoji2, choiceBox, startBox))
    text2 = Text(choice2, align="top", text="Placeholder")
    choicespacer2 = Box(choiceBox, align="left", width=10, height=0)
    
    choice3 = Box(choiceBox, align="left")
    emoji3 = PushButton(choice3, image=emojis[randint(0,len(emojis)-1)], align="top", command=lambda:emojiSelected(emoji3, choiceBox, startBox))
    text3 = Text(choice3, align="top", text="Placeholder")

def emojiSelected(btnEmoji, choiceBox, startBox):
    print(btnEmoji.image)
    party.append(emoji(btnEmoji.image, names[randint(0,len(names)-1)]))
    choiceBox.hide()
    choiceBox.disable()
    startBox.hide()
    startBox.disable()
    outro()

def progressText(textList, textLabel, closeEvent):
    global textProgression
    if textProgression+1!=len(textList):
        textProgression+=1
        textLabel.value=textList[textProgression]
    else:
        textProgression = 0
        closeEvent()

def start(e1Box):
    e1Text = TextBox(e1Box, text=introText[0], align="top", width=app.width-20, height=3, multiline=True)
    e1Text.disable()
    startspacer = Box(e1Box, align="top", height=15)
    contBtn = PushButton(e1Box, align="top", width=10, text="Continue", command=lambda: progressText(introText, e1Text, lambda:pickStartEmoji(contBtn, e1Box)))
    
def outro():
    e1Box = Box(app)
    e1Text = TextBox(e1Box, text=outroText[0], align="top", width=app.width-20, height=3, multiline=True)
    e1Text.disable()
    startspacer = Box(e1Box, align="top", height=15)
    contBtn = PushButton(e1Box, align="top", width=10, text="Continue", command=lambda: progressText(outroText, e1Text, lambda:initialiseGame(e1Box)))
    
def initialiseGame(startBox):
    startBox.disable()
    startBox.hide()
    global spacer1
    spacer1.hide()
    interfaceBox = Box(app)
    logo = Picture(interfaceBox, image="EmojiFight.png", height=80, width=256)
    
app = App(title = "Emoji Fight Ver 0.1", width = 500, height = 800)
app.font = "OCR A Extended"

spacer1 = Box(app, height=50, width="fill")
e1Box = Box(app)

if startSequence:
    start(e1Box)
else:
    initialiseGame(e1Box)

app.display()