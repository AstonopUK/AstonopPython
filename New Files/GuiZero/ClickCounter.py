import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])

from guizero import *
clickCount=0
timer=0.0
prevTimer=1
dataType="Clicks"
scheme=False

def clicked():
    global clickCount
    clickCount+=1
    
def countdown(text,btn1,btn2):
    global timer
    global clickCount
    global dataType
    global prevTimer
    timer-=0.01
    text.value="You have "+"{:.2f}".format(round(timer,2))+" seconds left."
    if timer<=0:
        btn1.disable()
        if dataType=="Clicks":
            text.value="Your final score is: "+str(clickCount)
        else:
            text.value="Your CPS is: "+"{:.2f}".format(round(clickCount/prevTimer,2))
        btn2.enable()
        
def start(btn1,btn2,txtBox):
    global timer
    global prevTimer
    global clickCount
    clickCount=0
    btn1.disable()
    btn2.enable()
    timer=int(txtBox.value)
    prevTimer=timer
    
def flipValue(btn):
    global dataType
    if dataType=="Clicks":
        dataType="CPS"
        btn.text="CPS"
    else:
        dataType="Clicks"
        btn.text="Clicks"
        
def nightMode(app,btn):
    global scheme
    if scheme==False:
        scheme=True
        app.bg="#434343"
        app.text_color="white"
        btn.text="☀"
    else:
        scheme=False
        app.bg=None
        app.text_color="black"
        btn.text="🌙"
        
def close():
    app.destroy()
    
app=App(title="ClickCounter",width=250,height=200)
sortBox=Box(app)
inpBox=TextBox(sortBox,align="left",text="Replace this text with number of seconds",multiline=True,height=2,width=25)
startBtn=PushButton(sortBox,align="left",text="Start",command=lambda:start(startBtn,clickBtn,inpBox))
clickBtn=PushButton(app,text="Click!",width=32,height=4,command=clicked)
clickBtn.disable()
outText=Text(app,text="")
outText.repeat(10,lambda:countdown(outText,clickBtn,startBtn))
bottomBox=Box(app,width="fill",height="fill")
typeBtn=PushButton(bottomBox,align="left",text="Clicks",width="fill",height="fill",command=lambda:flipValue(typeBtn))
colourBtn=PushButton(bottomBox,align="left",text="🌙",command=lambda:nightMode(app,colourBtn))
closeBtn=PushButton(bottomBox,align="left",text="Close App",width="fill",height="fill",command=close)

app.display()