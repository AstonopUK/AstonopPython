from guizero import *
import time

def greet():
    output.value = ("Hello, " + name.value)

def message():
    print("debug")
    
def stop():
    app.destroy()

app = App(title="Test App")

menuBar = MenuBar(app, toplevel=["Test", "Exit"], options=[[["Test Instruction", message]],[["Exit App", stop]]])

guiText = "Please enter your name."
message = Text(app, text=guiText)
name = TextBox(app)
button = PushButton(app, text="Press to greet.", command=greet)

picture = Picture(app, image="backpack.png", width = 128, height = 128)

output = Text(app)
output.text_size = 16
app.display()