import subprocess, sys, json, random

try:
    from guizero import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])
    
def addKey(letter):
    global guess
    if guessTracker<5:
        if len(guess)<5:
            guess += letter
        for x in range(len(guess)):
            text[(guessTracker*5)+x].value=guess[x]
        print(guess)

def createBtn(loc, letter):
    btn = PushButton(loc, text=alph[letter], align="left", width=2)
    btn.tk.configure(command=lambda:addKey(btn.text))
    return btn

def submitGuess():
    global guessTracker, guess
    if len(guess)==5:
        if guess.lower() in data:
            infText.value = "Enter another guess."
            for l in guess.lower():
                if l in list(word):
                    ind = list(word).index(l)
                    if ind == list(guess.lower()).index(l):
                        text[(guessTracker*5)+ind].bg="green"
                    else:
                        text[(guessTracker*5)+ind].bg="orange"
            guessTracker+=1
            
            if guess!=word and guessTracker>=5:
                app.disable()
                infText.value = "Game over!"
            guess=""
        else:
            infText.value = "Not a valid guess."
            guess=""
            for x in range(5):
                text[(guessTracker*5)+x].value=""
    else:
        infText.value = "Not enough letters in guess!"

json_file = 'dictionary.json'

with open(json_file) as json_data:
    data = json.load(json_data)
    
words = []
for item in list(data.keys()):
    if len(item)==5 and item.isalpha():
        words.append(item)

alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
buttons = []
guess = ""
word=random.choice(words)
print(word)
guessTracker = 0

app = App(title="Wordle",width=500,height=580)

# Guess Boxes ------------------------------------------------------------------------------------------------------------
wordsBox = TitleBox(app, text="Guesses", width=450, height=290, border=1)

guesses = []
for x in range(5):
    guesses.append(Box(wordsBox, width="fill"))
    
letters = []
text = []
for x in range(5):
    for y in range(5):
        letters.append(Box(guesses[x],align="left",width="fill"))
for x in range(5):
    for y in range(5):
        text.append(Text(letters[(x*5)+y],text="",width="fill"))
        
for item in text:
    item.text_size = 26
for item in letters:
    item.bg="#cccccc"

spacer1 = Box(app, height=30)
infText = Text(app, text="Enter a valid guess.")
spacer2 = Box(app, height=30)

# Keyboard ---------------------------------------------------------------------------------------------------------------
topRow = Box(app)
midRow = Box(app)
bottomRow = Box(app)

for x in range(10):
    buttons.append(createBtn(topRow, x))
for x in range(9):
    buttons.append(createBtn(midRow,x+10))
for x in range(7):
    buttons.append(createBtn(bottomRow, x+19))
    
guessBtn = PushButton(app, text="Submit Guess", width=20, command=submitGuess)

app.display()