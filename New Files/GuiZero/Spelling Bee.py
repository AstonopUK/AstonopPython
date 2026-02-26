import subprocess, sys, random, json

try:
    from guizero import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])

with open("dictionary.json") as f:
    d = json.load(f)

def processWord():
    global guess, guessedWords, guessedWordsList, points
    valid = True
    for char in guess:
        if char not in pickedLetters:
            valid = False
    if pickedLetters[3] not in guess:
        valid = False
    if valid == True:
        if guess.lower() in d:
            notG = True
            for word in guessedWordsList:
                if guess == word:
                    notG = False
            if notG == True:        
                addText = guess + " - " + str(len(guess)) + " points"
                guessedWordsList.append(guess)
                guessedWords.append(Text(guessedWordBox, text=addText, size=14))
                points+=len(guess)
                guess = ""
                wordGuess.value=guess
            else:
                wordGuess.value="Already guessed!"
                guess = ""
    else:
        wordGuess.value = "Invalid word"
        guess = ""
    scoreTxt.value = "Points: " + str(points)
    scaleBox.width = int(round(points*pointVal,0))
    if scaleBox.width>=280:
        gameWindow.hide()
        winScreen.show()
    
def addToGuess(button):
    global guess
    guess+=button.text
    wordGuess.value = guess
    
def difficulty(value):
    global pointVal
    pointVal = (280/barCalc)*value
    app.hide()
    gameWindow.show()
    
def clear():
    global guess
    guess = ""
    wordGuess.value = guess
    
def cheat():
    gameWindow.hide()
    winScreen.show()

guess = ""
points = 0
letters = list("STRLNDGBCMPFHYWVKJXZQ")
lettersCopy = list("STRLNDGBCMPFHYWVKJXZQ")
vowels = list("AEIOU")
pickedLetters = ""
guessedWords = []
guessedWordsList = []

for x in range(5):
    l = random.choice(letters)
    letters.remove(l)
    pickedLetters += l
    
for x in range(2):
    l = random.choice(vowels)
    vowels.remove(l)
    pickedLetters += l
    
totalLetterScore=0
for letter in pickedLetters:
    if letter not in "AEIOU":
        totalLetterScore+=lettersCopy.index(letter)
    
barCalc = 280-totalLetterScore
pointVal = 1

app = App(title = "Spelling Bee", bg="yellow", width=400, height=200)
app.font = "Consolas"
title = Text(app, text="Spelling Bee", size=32, bold = True)
difText = Text(app, text="Difficulty affects the amount\nof words you must find to win.\nSelect a difficulty:")
sortBox = Box(app)
dif1 = PushButton(sortBox, align="left", text="Easy", width=5, command=lambda:difficulty(8))
dif2 = PushButton(sortBox, align="left", text="Medium", width=5, command=lambda:difficulty(4))
dif3 = PushButton(sortBox, align="left", text="Hard", width=5, command=lambda:difficulty(2))

gameWindow = Window(app, title = "Spelling Bee", bg="yellow", width=400, height=700, visible=False)

title = Text(gameWindow, text="Spelling Bee", size=32, bold = True)

letterBox = Box(gameWindow, layout="grid")
letter1 = PushButton(letterBox, grid=[0,0], text=pickedLetters[0], command=lambda:addToGuess(letter1))
letter2 = PushButton(letterBox, grid=[0,1], text=pickedLetters[1], command=lambda:addToGuess(letter2))
letter3 = PushButton(letterBox, grid=[1,0], text=pickedLetters[2], command=lambda:addToGuess(letter3))
letter4 = PushButton(letterBox, grid=[1,1], text=pickedLetters[3], command=lambda:addToGuess(letter4))
letter4.bg = "black"
letter4.text_color = "white"
letter5 = PushButton(letterBox, grid=[1,2], text=pickedLetters[4], command=lambda:addToGuess(letter5))
letter6 = PushButton(letterBox, grid=[2,1], text=pickedLetters[5], command=lambda:addToGuess(letter6))
letter7 = PushButton(letterBox, grid=[2,2], text=pickedLetters[6], command=lambda:addToGuess(letter7))

wordGuess = Text(gameWindow, text="", size=16)
btnBox = Box(gameWindow)
submitBtn = PushButton(btnBox, align="left", text="Submit Answer", command=processWord)
clearBtn = PushButton(btnBox, align="left", text="Clear Answer", command=clear)
#cheatBtn = PushButton(btnBox, align="left", text="Cheat", command=cheat)
scoreTxt = Text(gameWindow, text="Points: 0", size=16)
widthBox = TitleBox(gameWindow, text="Win Progress", width=280, height=40)
scaleBox = Box(widthBox, align="left", width=1, height="fill")
scaleBox.bg = "#ff0000"
guessedWordBox = TitleBox(gameWindow, text="Guessed Words")

winScreen = Window(app, title="Spelling Bee", visible=False, bg="yellow")
winScreen.font="Consolas"
winText = Text(winScreen, text="Congratulations!\nYou win!", size=28, bold=True)
picture = Picture(winScreen, image="gif.gif", width=330, height=330)
closeBtn = PushButton(winScreen, text="Close the game", command=quit)

app.display()