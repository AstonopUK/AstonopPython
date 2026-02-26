from guizero import *

nightmode = False
app = App(title="Membership Calculator 1.0", height=570, width=500)
app.font = "OCR A Extended"
app.text_size = 11

def showOptions():
    if addFeatures.value == "Yes":
        print("Showing")
        #addOptions.enable()
        addOptions.show()
    else:
        print("Hiding")
        #addOptions.disable()
        addOptions.hide()
        addOptions.value = []
    app.update()
    
def calculateCost():
    if name.value != "":
        totalCost = 0.00
        totalCost += len(choices.value)
        totalCost *= 1 + (customers.value/10)
        if addOptions.value != None:
            for item in addOptions.value:
                totalCost += len(item)/3
        app.info(name.value + "'s Cost Assumption", "For the options you have selected, we estimate it will cost you £"+"{:.2f}".format(round(totalCost,2))+" per month for your membership.")
    else:
        app.error("Missing Information", "Please enter a suitable account name for your price estimation.")
        
def highlight(obj):
    obj.bg = "light blue"
    
def lowlight(obj):
    global nightmode
    if nightmode == False:
        obj.bg = None
    else:
        obj.bg = "#292929"
    
def invertColours():
    global nightmode
    if nightmode == False:
        app.bg = "#292929"
        nightmode = True
        app.text_color = "white"
        darkmode.text = "☀"
    else:
        app.bg=None
        nightmode = False
        app.text_color = None
        darkmode.text="🌙"

topBox = Box(app, width = app.width-20, height = 40)
logo = Picture(topBox, align="left", image="streamlylogo.gif")
darkmode = PushButton(topBox, align="right", text="🌙", command=invertColours, width=1)
darkmode.when_mouse_enters = lambda: highlight(darkmode)
darkmode.when_mouse_leaves = lambda: lowlight(darkmode)

ttlBox = TitleBox(app, text="Streamly Membership Calculator", width=app.width-20, height=app.height-50)
lbl1 = Text(ttlBox, text="Select your product:")
streamOptions = ["Streamly", "Streamly Plus", "Streamly Ultimate"]
choices = ButtonGroup(ttlBox, options=streamOptions, selected=streamOptions[0])

spacer1 = Box(ttlBox, height=20, width=1)
lbl2 = Text(ttlBox, text="How many members will be using your account?")
customers = Slider(ttlBox, start=1, end=8)

spacer2 = Box(ttlBox, height=20, width=1)
lbl3 = Text(ttlBox, text="What name would you like on the account?")
name = TextBox(ttlBox, width=50)

spacer3 = Box(ttlBox, height=20, width=1)
lbl4 = Text(ttlBox, text="Would you like any additional features?")
addFeatures = Combo(ttlBox, options=["No", "Yes"], command=showOptions)
options = ["Emoji Pack", "Additional Bandwidth", "Tip Jar", "Stream License", "Music License"]
addOptions = ListBox(ttlBox, items=options, multiselect=True, height=100, width=200)
addOptions.hide()

spacer4 = Box(ttlBox, height=20, width=1)
btnCost = PushButton(ttlBox, text="Click to calculate cost", command=calculateCost)
btnCost.when_mouse_enters = lambda: highlight(app)
btnCost.when_mouse_leaves = lambda: lowlight(app)

app.display()