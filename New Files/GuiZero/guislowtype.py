from guizero import *

tracker = 0
totalText = ""
def displayText():
    global tracker, totalText
    try:
        totalText+=sentence[tracker]
        tracker+=1
        text.value=totalText
        text.after(50, displayText)
    except:
        print("Failed!")

app = App()

sentence = "Hello and welcome to my gui based adventure game with slow text"
text = Text(app, text="")
btn = PushButton(app, text="press", command=displayText)

app.display()
