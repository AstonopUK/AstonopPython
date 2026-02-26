import subprocess
import sys
import random
import winsound
import math
from tkinter import ttk
import base64

try:
    from guizero import *
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "guizero"])

food = ["Sheep", "Scallops", "Air", "Sausages", "Bread", "Fish", "Ducks", "Chicken", "Potatoes", "Salmon", "Soup", "Pizzas", "Macaroni", "Tendies", "Geese", "Curry", "Limes", "Apples", "Dogs", "Cats", "Snails", "Crocodiles", "Horses", "Deer", "Cake", "Beans", "Frogs", "Human Limbs", "Biscuits", "Handbags", "Hams", "Giraffes", "Plutonium", "Evil Bugs", "Death Juice"]
adjectives = ["Decorative", "Juiced", "Squashed", "Flambeed", "Expensive", "Sausage-shaped", "Baked", "Fried", "Dry Frozen", "Jerkied", "Sizzled", "Hot", "Roasted", "Deconstructed", "Beefy", "Cheesy", "Golden", "Filleted", "Burnt", "Stack of", "Kilo of", "Broken", "Alive", "Stolen", "Curried", "Asbestos-laced", "Carcinogenic", "Poisoned", "Radioactive", "Reincarnated", "Thoroughly-Rizzed", "Reconstituted", "Chemicular", "Bruised", "Decaying", "Ancient"]
bonusadj = ["Harmful", "Decorative", "Decadent", "Spherical", "Obtuse", "Spanish", "British", "Italian", "German", "French", "African", "Malaysian", "American", "Mexican", "Philippino", "Peruvian", "Turkish"]
bestadj = ["Ultimate", "Giga", "Ultra", "The Best", "Monstrous", "Gargantuan", "Collosal", "Waitrose", "Wotsit-like", "Roblox Branded", "Intercontinental", "Silver-Plated", "Universally Fundamental", "Atomically-Fissioned", "Dramatically Accelerated", "Sonar-Emitting", "Bluetooth Compatible"]
combinations = [" with ", " con ", " a la ", " complemented by ", " drizzled with ", " coated with ", " with a sauce of ", " glazed with ", " with a reduction of ", " and ", " next to ", " lightly dusted with ", " flambeed with ", " liberally soused with ", " generously heaped with ", " served on a bed of ", " blessed with "]
inventory = []
achieves = [["🥸","Launch the game",True],["👀","Make your first\n100 money",False],["🤦","Somehow lose\nsome strength",False],["💪","Reach strength\nlevel 25",False],
            ["⁉","Find an item over\n50 characters long",False],["🧑‍🎓","Make over 10,000\nmoney",False],["👊","Successfully\nworkout",False],["💪","Reach strength\nlevel 50",False],
            ["💯","Buy 100 or\nmore items",False],["💰","Become a\nmillionaire",False],["🤢","Eat an item over\n500 characters long",False],["💪","Reach strength\nlevel 75",False]]

money = 50
strength = 1
gymProgress = 3
numItemsBought = 0

def removeBrackets(text):
    newText=text.replace("{","")
    newText=newText.replace("}","")
    return newText

def close(window):
    winsound.Beep(900,65)
    winsound.Beep(600,65)
    winsound.Beep(300,65)
    window.destroy()

def buy(textToChange,emojiChange):
    global money, adjectives, bonusadj, bestadj, inventory, achieves, numItemsBought
    
    if money >= 20:
        if strength < 25:
            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
            fooditem = food[random.randint(0, len(food)-1)]
            changeText=("You purchased:\n"+str(adj1)+" "+str(fooditem)+".")
            textToChange.value=removeBrackets(changeText)
            itemtoadd = adj1 + " " + fooditem
            inventory.append(itemtoadd)
            money -= 20
        elif strength >= 25 and strength < 50:
            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
            fooditem = food[random.randint(0, len(food)-1)]
            changeText=("You purchased:\n"+str(adj1)+" "+str(adj2)+" "+str(fooditem)+".")
            textToChange.value=removeBrackets(changeText)
            itemtoadd = adj1 + " " + adj2 + " " + fooditem
            inventory.append(itemtoadd)
            money -= 20
        elif strength >= 50 and strength < 75:
            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
            adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
            fooditem = food[random.randint(0, len(food)-1)]
            changeText=("You purchased:\n"+str(adj1)+" "+str(adj2)+" "+str(adj3)+" "+str(fooditem)+".")
            textToChange.value=removeBrackets(changeText)
            itemtoadd = adj1 + " " + adj2 + " " + adj3 + " " + fooditem
            inventory.append(itemtoadd)
            money -= 20
        elif strength >= 75:
            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
            adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
            adj4 = bestadj[random.randint(0, len(bestadj)-1)]
            fooditem = food[random.randint(0, len(food)-1)]
            changeText=("You purchased:\n"+str(adj4)+" "+str(adj1)+" "+str(adj2)+" "+str(adj3)+" "+str(fooditem)+".")
            textToChange.value=removeBrackets(changeText)
            itemtoadd = adj4 + " " + adj1 + " " + adj2 + " " + adj3 + " " + fooditem
            inventory.append(itemtoadd)
            money -= 20
        match fooditem:
            case "Sheep":
                emojiChange.value="🐑"
            case "Scallops":
                emojiChange.value="🍥"
            case "Air":
                emojiChange.value="🍃"
            case "Sausages":
                emojiChange.value="🥒"
            case "Bread":
                emojiChange.value="🥖"
            case "Fish":
                emojiChange.value="🐟"
            case "Ducks":
                emojiChange.value="🦆"
            case "Chickens":
                emojiChange.value="🐓"
            case "Potatoes":
                emojiChange.value="🥔"
            case "Salmon":
                emojiChange.value="🧈"
            case "Soup":
                emojiChange.value="🍲"
            case "Pizzas":
                emojiChange.value="🍕"
            case "Macaroni":
                emojiChange.value="🥘"
            case "Tendies":
                emojiChange.value="🍤"
            case "Geese":
                emojiChange.value="🪿"
            case "Curry":
                emojiChange.value="🍛"
            case "Limes":
                emojiChange.value="🍋‍🟩"
            case "Apples":
                emojiChange.value="🍎"
            case "Dogs":
                emojiChange.value="🐕"
            case "Cats":
                emojiChange.value="🐈"
            case "Snails":
                emojiChange.value="🐌"
            case "Crocodiles":
                emojiChange.value="🐊"
            case "Horses":
                emojiChange.value="🐎"
            case "Deer":
                emojiChange.value="🦌"
            case "Cake":
                emojiChange.value="🍰"
            case "Beans":
                emojiChange.value="🫘"
            case "Frogs":
                emojiChange.value="🐸"
            case "Human Limbs":
                emojiChange.value="🦵"
            case "Biscuits":
                emojiChange.value="🍪"
            case "Handbags":
                emojiChange.value="👜"
            case "Hams":
                emojiChange.value="🍖"
            case "Giraffes":
                emojiChange.value="🦒"
            case "Plutonium":
                emojiChange.value="☢"
            case "Evil Bugs":
                emojiChange.value="🐛"
            case "Death Juice":
                emojiChange.value="🧉"
            case _:
                emojiChange.value="🍽"
        if len(itemtoadd) > 50:
            achieves[4][2] = True
        numItemsBought+=1
        if numItemsBought>99:
            achieves[8][2]=True
    else:
        textToChange.value=("You are too poor to buy\nanything. Do some work!")
        emojiChange.value="💸"
    return

def sellClose(window, item, textToChange, emojiChange):
    global inventory
    global money
    
    #print(len(item))
    if len(item)>1:
        try:
            totalPay = 0
            for i in item:
                money += len(i)/2
                totalPay += len(i)/2
            changeText=("You sold some items.\nYou earned "+str(totalPay)+" dollars.")
            textToChange.value=removeBrackets(changeText)
            emojiChange.value="💰"
            for i in item:
                inventory.remove(i)
        except:
            textToChange.value="Failed to sell item!"
            emojiChange.value="❎"
    else:
        try:
            money += len(item[0])/2
            changeText=("You sold the "+str(item[0])+".\nYou earned "+str(len(item[0])/2)+" dollars.")
            textToChange.value=removeBrackets(changeText)
            emojiChange.value="💰"
            inventory.remove(item[0])
            winsound.Beep(1750,120)
        except:
            textToChange.value="Failed to sell item!"
            emojiChange.value="❎"
            
    window.destroy()

def eatClose(window, item, textToChange, emojiChange):
    global inventory, strength, achieves
    totalStrength = 0
    
    #print(len(item))
    if len(item)>1:
        try:
            for i in item:
                strength += len(i)/100
                totalStrength += len(i)/100
                if len(i)>500:
                    achieves[10][2]=True
            changeText=("You sold some items.\nYou grew by "+str(totalStrength)+" strength.")
            textToChange.value=removeBrackets(changeText)
            emojiChange.value="💪"
            for i in item:
                inventory.remove(i)
        except:
            textToChange.value="Failed to eat item!"
            emojiChange.value="❎"
    else:
        try:
            strength += len(item[0])/100
            if len(item[0])>500:
                    achieves[10][2]=True
            changeText=("You ate the "+str(item[0])+".\nYou grew by "+str(len(item[0])/100)+" strength.")
            textToChange.value=removeBrackets(changeText)
            emojiChange.value="💪"
            inventory.remove(item[0])
            winsound.Beep(1750,120)
        except:
            textToChange.value="Failed to eat item!"
            emojiChange.value="❎"
    
    strength=round(strength,2)
    totalStrength=round(totalStrength,2)
    window.destroy()

def craftClose(window, item1, item2, textToChange, emojiChange):
    global inventory
    
    if item1 != item2:
        newitem = item1 + combinations[random.randint(0, len(combinations)-1)] + item2
        inventory.append(newitem)
        inventory.remove(item1)
        inventory.remove(item2)
        textToChange.value = "Items were combined!"
        emojiChange.value="✅"
    else:
        textToChange.value = "Failed to combine items!\nItems selected were the same."
        emojiChange.value="❎"
    window.destroy()

def sellItem():
    selectWindow = Window(app, title="Select your item(s) to sell")
    itemList = ListBox(selectWindow, width="fill", height="fill", multiselect=True, items=inventory)
    selectBtn = PushButton(selectWindow, width="fill", text="Sell Chosen Item(s)", command=lambda:sellClose(selectWindow, itemList.value, descText, imgText))

def eatItem():
    selectWindow = Window(app, title="Select your item(s) to eat")
    itemList = ListBox(selectWindow, width="fill", height="fill", multiselect=True, items=inventory)
    selectBtn = PushButton(selectWindow, width="fill", text="Eat Chosen Item(s)", command=lambda:eatClose(selectWindow, itemList.value, descText, imgText))

def craftItem():
    global inventory

    selectWindow = Window(app, title="Select two items to combine:", width=400, height=500, layout="grid")
    itemList1 = ListBox(selectWindow, grid=[0,0], width=200, height=435, multiselect=False, items=inventory)
    itemList2 = ListBox(selectWindow, grid=[1,0], width=200, height=435, multiselect=False, items=inventory)
    selectBtn = PushButton(selectWindow, grid=[0,1,2,1], width=42, height=2, text="Select Chosen Item", command=lambda:craftClose(selectWindow, itemList1.value, itemList2.value, descText, imgText))

def sellAllItems(textToChange, emojiChange):
    global inventory, money
    
    totalPay = 0
    for item in inventory:
        money += len(item)/2
        totalPay += len(item)/2
    inventory=[]
    changeText=("You sold some items.\nYou earned "+str(totalPay)+" dollars.")
    textToChange.value=removeBrackets(changeText)
    emojiChange.value="💰"
    winsound.Beep(1500,60)
    winsound.Beep(1750,60)
    
def eatAllItems(textToChange, emojiChange):
    global inventory, strength, achieves
    
    totalStrength = 0
    for item in inventory:
        strength += len(item)/100
        totalStrength += len(item)/100
        if len(item)>500:
            achieves[10][2]=True
    inventory=[]
    strength=round(strength,2)
    totalStrength=round(totalStrength,2)
    changeText=("You ate some items.\nYou grew by "+str(totalStrength)+" strength.")
    textToChange.value=removeBrackets(changeText)
    emojiChange.value="💪"
    winsound.Beep(400,60)
    winsound.Beep(500,60)

def craftAllItems(textToChange, emojiChange):
    global inventory
    
    item1 = inventory[0]
    item2 = inventory[1]
    newItem = item1 + combinations[random.randint(0, len(combinations)-1)] + item2
    inventory.remove(item1)
    inventory.remove(item2)
    if len(inventory)>0:
        for item in inventory:
            newItem = newItem + combinations[random.randint(0, len(combinations)-1)] + item
        
    inventory=[newItem]
    textToChange.value=("You combined your items.")
    emojiChange.value="✅"
    winsound.Beep(400,60)
    winsound.Beep(500,60)
    
def work():   
    workWindow = Window(app, title="Work Interface", height=168, width=438, layout="grid")
    workWindow.bg = "#B9B9B9"
    workWindow.font = "OCR A Extended"
    
    problemText = Text(workWindow, text=(str(random.randint(1,9))+"+"+str(random.randint(1,9))), size=60, width=9, height="fill", grid=[0,0,2,1])
    answerBox = TextBox(workWindow, width=31, grid=[0,1,2,1])
    answerBox.text_size=18
    answerBox.bg="#ffffff"
    submitBtn = PushButton(workWindow, width=19, text="Submit answer", grid=[0,2], command=lambda:tryAnswer(answerBox, problemText))
    closeBtn = PushButton(workWindow, width=19, text="Stop working", grid=[1,2], command=lambda:close(workWindow))

def tryAnswer(answer, problem):
    global money
    num1=problem.value[0]
    operator=problem.value[1]
    num2=problem.value[2]
    total=0
    
    match operator:
        case "+":
            total=int(num1)+int(num2)
        case "-":
            total=int(num1)-int(num2)
        case "x":
            total=int(num1)*int(num2)
        case _:
            pass
    try:
        if int(answer.value)==total:
            winsound.Beep(600,75)
            winsound.Beep(800,75)
            money += math.trunc(5*strength)
        else:
            winsound.Beep(800,75)
            winsound.Beep(400,75)
    except:
        print("Nonint value parsed, skipping...")
    
    match random.randint(0,2):
        case 0:
            newProblem=str(random.randint(1,9))+"+"+str(random.randint(1,9))
        case 1:
            newProblem=str(random.randint(1,9))+"-"+str(random.randint(1,9))
        case 2:
            newProblem=str(random.randint(1,9))+"x"+str(random.randint(1,9))
    problem.value=newProblem
    answer.value=""

def gym():
    global gymProgress
    
    gymWindow = Window(app, title="GYM", height=168, width=438, layout="grid")
    gymWindow.bg = "#B9B9B9"
    gymWindow.font = "OCR A Extended"
    
    gymText = Text(gymWindow, text="Click 'workout' to get swole!", size=16, width="fill", height="fill", grid=[0,0,2,1])
    spacer1Box = Box(gymWindow, width="fill", height=10, grid=[0,1,2,1])
    fillBox = Box(gymWindow, width=400, height=40, border=1, grid=[0,2,2,1])
    
    progressBar = Box(fillBox, align="left", width=gymProgress, height="fill")
    progressBar.bg = "#ff0000"
    
    spacer2Box = Box(gymWindow, width="fill", height=40, grid=[0,3,2,1])
    workoutBtn = PushButton(gymWindow, width=19, text="Workout!", grid=[0,4], command=lambda:increaseGym(gymText))
    closeBtn = PushButton(gymWindow, width=19, text="Stop working out", grid=[1,4], command=lambda:close(gymWindow))
    
    progressBar.repeat(100, lambda:reduceGym(progressBar))

def increaseGym(textToChange):
    global gymProgress
    global strength
    global achieves
    
    gymProgress+=12
    if gymProgress>=400:
        achieves[6][2]=True
        gymProgress=0
        strength+=0.2
        strength=round(strength,2)
        textToChange.value = "Strength increased by 0.2."

def refresh():
    global achieves
    
    if money>=100:
        achieves[1][2]=True
    if money>=10000:
        achieves[5][2]=True
    if money>=1000000:
        achieves[9][2]=True
    
    if strength>=25:
        achieves[3][2]=True
    if strength>=50:
        achieves[7][2]=True
    if strength>=75:
        achieves[11][2]=True
        
    moneyText.value=("Money: "+str(money))
    strengthText.value=("Strength: "+str(strength))

def reduceGym(bar):
    global gymProgress
    
    if gymProgress>3:
        gymProgress-=3
    bar.width=gymProgress
    
def punch(textToChange, emojiChange):
    global strength, adjectives, bonusadj, bestadj, inventory, achieves, numItemsBought
    
    if strength>2:
        if random.randint(0,10)>7:
            if strength < 25:
                adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                fooditem = food[random.randint(0, len(food)-1)]
                changeText=("You found:\n"+str(adj1)+" "+str(fooditem)+".")
                textToChange.value=removeBrackets(changeText)
                itemtoadd = adj1 + " " + fooditem
                inventory.append(itemtoadd)
            elif strength >= 25 and strength < 50:
                adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                fooditem = food[random.randint(0, len(food)-1)]
                changeText=("You found:\n"+str(adj1)+" "+str(adj2)+" "+str(fooditem)+".")
                textToChange.value=removeBrackets(changeText)
                itemtoadd = adj1 + " " + adj2 + " " + fooditem
                inventory.append(itemtoadd)
            elif strength >= 50 and strength < 75:
                adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                fooditem = food[random.randint(0, len(food)-1)]
                changeText=("You found:\n"+str(adj1)+" "+str(adj2)+" "+str(adj3)+" "+str(fooditem)+".")
                textToChange.value=removeBrackets(changeText)
                itemtoadd = adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                inventory.append(itemtoadd)
            elif strength >= 75:
                adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                adj4 = bestadj[random.randint(0, len(bestadj)-1)]
                fooditem = food[random.randint(0, len(food)-1)]
                changeText=("You found:\n"+str(adj4)+" "+str(adj1)+" "+str(adj2)+" "+str(adj3)+" "+str(fooditem)+".")
                textToChange.value=removeBrackets(changeText)
                itemtoadd = adj4 + " " + adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                inventory.append(itemtoadd)
            match fooditem:
                case "Sheep":
                    emojiChange.value="🐑"
                case "Scallops":
                    emojiChange.value="🍥"
                case "Air":
                    emojiChange.value="🍃"
                case "Sausages":
                    emojiChange.value="🥒"
                case "Bread":
                    emojiChange.value="🥖"
                case "Fish":
                    emojiChange.value="🐟"
                case "Ducks":
                    emojiChange.value="🦆"
                case "Chickens":
                    emojiChange.value="🐓"
                case "Potatoes":
                    emojiChange.value="🥔"
                case "Salmon":
                    emojiChange.value="🧈"
                case "Soup":
                    emojiChange.value="🍲"
                case "Pizzas":
                    emojiChange.value="🍕"
                case "Macaroni":
                    emojiChange.value="🥘"
                case "Tendies":
                    emojiChange.value="🍤"
                case "Geese":
                    emojiChange.value="🪿"
                case "Curry":
                    emojiChange.value="🍛"
                case "Limes":
                    emojiChange.value="🍋‍🟩"
                case "Apples":
                    emojiChange.value="🍎"
                case "Dogs":
                    emojiChange.value="🐕"
                case "Cats":
                    emojiChange.value="🐈"
                case "Snails":
                    emojiChange.value="🐌"
                case "Crocodiles":
                    emojiChange.value="🐊"
                case "Horses":
                    emojiChange.value="🐎"
                case "Deer":
                    emojiChange.value="🦌"
                case "Cake":
                    emojiChange.value="🍰"
                case "Beans":
                    emojiChange.value="🫘"
                case "Frogs":
                    emojiChange.value="🐸"
                case "Human Limbs":
                    emojiChange.value="🦵"
                case "Biscuits":
                    emojiChange.value="🍪"
                case "Handbags":
                    emojiChange.value="👜"
                case "Hams":
                    emojiChange.value="🍖"
                case "Giraffes":
                    emojiChange.value="🦒"
                case "Plutonium":
                    emojiChange.value="☢"
                case "Evil Bugs":
                    emojiChange.value="🐛"
                case "Death Juice":
                    emojiChange.value="🧉"
                case _:
                    emojiChange.value="🍽"
            if len(itemtoadd) > 50:
                achieves[4][2] = True
            numItemsBought+=1
            if numItemsBought>99:
                achieves[8][2]=True
        else:
            strength-=1
            strength=round(strength,2)
            textToChange.value=("You damaged your knuckles.\nYour strength reduced by 1!")
            emojiChange.value="🆘"
            achieves[2][2]=True
    else:
        textToChange.value=("You are too weak to punch.")
        emojiChange.value="🚫"
        
def achievements():
    achieveWindow = Window(app, title="Achievements Log", layout="grid", width=600, height=518)
    achieveWindow.bg = "#cfcfcf"
    
    ac1 = Box(achieveWindow, width=150, height=150, grid=[0,0], border=3, enabled=achieves[0][2])
    ac2 = Box(achieveWindow, width=150, height=150, grid=[1,0], border=3, enabled=achieves[1][2])
    ac3 = Box(achieveWindow, width=150, height=150, grid=[2,0], border=3, enabled=achieves[2][2])
    ac4 = Box(achieveWindow, width=150, height=150, grid=[3,0], border=3, enabled=achieves[3][2])
    
    ac5 = Box(achieveWindow, width=150, height=150, grid=[0,1], border=3, enabled=achieves[4][2])
    ac6 = Box(achieveWindow, width=150, height=150, grid=[1,1], border=3, enabled=achieves[5][2])
    ac7 = Box(achieveWindow, width=150, height=150, grid=[2,1], border=3, enabled=achieves[6][2])
    ac8 = Box(achieveWindow, width=150, height=150, grid=[3,1], border=3, enabled=achieves[7][2])
    
    ac9 = Box(achieveWindow, width=150, height=150, grid=[0,2], border=3, enabled=achieves[8][2])
    ac10 = Box(achieveWindow, width=150, height=150, grid=[1,2], border=3, enabled=achieves[9][2])
    ac11 = Box(achieveWindow, width=150, height=150, grid=[2,2], border=3, enabled=achieves[10][2])
    ac12 = Box(achieveWindow, width=150, height=150, grid=[3,2], border=3, enabled=achieves[11][2])
    
    icon1 = Text(ac1, text=achieves[0][0], size=60)
    text1 = Text(ac1, text=achieves[0][1])
    icon2 = Text(ac2, text=achieves[1][0], size=60)
    text2 = Text(ac2, text=achieves[1][1])
    icon3 = Text(ac3, text=achieves[2][0], size=60)
    text3 = Text(ac3, text=achieves[2][1])
    icon4 = Text(ac4, text=achieves[3][0], size=60)
    text4 = Text(ac4, text=achieves[3][1])
    
    icon5 = Text(ac5, text=achieves[4][0], size=60)
    text5 = Text(ac5, text=achieves[4][1])
    icon6 = Text(ac6, text=achieves[5][0], size=60)
    text6 = Text(ac6, text=achieves[5][1])
    icon7 = Text(ac7, text=achieves[6][0], size=60)
    text7 = Text(ac7, text=achieves[6][1])
    icon8 = Text(ac8, text=achieves[7][0], size=60)
    text8 = Text(ac8, text=achieves[7][1])
    
    icon9 = Text(ac9, text=achieves[8][0], size=60)
    text9 = Text(ac9, text=achieves[8][1])
    icon10 = Text(ac10, text=achieves[9][0], size=60)
    text10 = Text(ac10, text=achieves[9][1])
    icon11 = Text(ac11, text=achieves[10][0], size=60)
    text11 = Text(ac11, text=achieves[10][1])
    icon12 = Text(ac12, text=achieves[11][0], size=60)
    text12 = Text(ac12, text=achieves[11][1])
    
    closeBtn = PushButton(achieveWindow, grid=[0,3,4,1], text="Close Window", width=44, command=lambda:close(achieveWindow))
    closeBtn.text_size = 18

def save():
    #print(money)
    saveString=(str(money*8.125)+"|"+str(strength*8.125)+"|"+str(inventory))
    #print(saveString)
    encoded=base64.b64encode(saveString.encode('utf-8'))
    
    copyWindow = Window(app, width=410, height=95, title="Save Screen", layout="grid")
    lblText = Text(copyWindow, grid=[0,0,2,1], text="Click the button below to copy\nyour save code to the clipboard.")
    clipBtn = PushButton(copyWindow, grid=[0,1], text="Copy to clipboard", width=20, command=lambda:clipboard(encoded))
    closeBtn = PushButton(copyWindow, grid=[1,1], text="Close window", width=20, command=lambda:close(copyWindow))
    
def load():
    loadWindow = Window(app, title="Load Screen", height=120, width=405, layout="grid")
    
    problemText = Text(loadWindow, text="Enter your load code below.", size=18, width=30, height="fill", grid=[0,0,2,1])
    codeBox = TextBox(loadWindow, width=31, grid=[0,1,2,1])
    codeBox.text_size=18
    codeBox.bg="#ffffff"
    submitBtn = PushButton(loadWindow, width=19, text="Load data", grid=[0,2], command=lambda:applyLoad(codeBox,loadWindow))
    closeBtn = PushButton(loadWindow, width=19, text="Close window", grid=[1,2], command=lambda:close(loadWindow))

def applyLoad(codeBox, window):
    global strength, money, inventory
    code = codeBox.value[2:-1]
    #print(code)
    loadCode = base64.b64decode(code)
    loadCode = loadCode.decode("utf-8")
    #print(loadCode)
    
    ldCodes = ["","",""]
    try:
        trackNum = 0
        for num in range(0,len(loadCode)-1):
            if loadCode[num] == "|":
                #print(loadCode[num])
                trackNum+=1
            else:
                ldCodes[trackNum]=ldCodes[trackNum]+loadCode[num]
        
        #print(ldCodes)
        ldCodes[0]=round(float(ldCodes[0])/8.125,2)
        ldCodes[1]=round(float(ldCodes[1])/8.125,2)
        
        money = ldCodes[0]
        strength = ldCodes[1]
        if ldCodes[2]!="":
            invDump = ldCodes[2]
            
            invItems = []
            flipper = False
            itemToAdd = ""
            for i in invDump:
                if i == "'":
                    if flipper == True:
                        flipper = False
                        invItems.append(itemToAdd)
                        itemToAdd=""
                    else:
                        flipper = True
                else:
                    if flipper == True:
                        itemToAdd+=i
            
            inventory = invItems
            #print(invItems[0])
    except:
        print("Error in loading save - aborted.")
    close(window)
    
def clipboard(code):
    subprocess.run("clip", text=True, input=str(code))
    
def helpbox():
    helpWindow = Window(app, title="Help Screen", width=500, height=650)
    
    info = "Welcome!\nThis is the world's worst vending machine. There are various options to get your journey started.\n\nBuying & Selling\nYou can buy items from the main screen, as well as sell them. Early on, this is not very effective to make money, but gets better later on.\n\nEating & Strength\nEating gives you some strength. The rarer the item, the more strength you get. Strength allows you to earn more money when you work and unlocks more items to buy every 25 strength.\n\nCrafting\nYou can make new items with crafting when you pick two items, or crat all items in your inventory together at once. Crafting increases rarity.\n\nPunching & Gym\nPunching has a chance to get you an item from the machine for free. However, there is a chance for something bad to happen instead. The Gym allows you to train your strength for free if you need to.\n\nSave & Load\nSaving gives you a code for your game. This saves your money, strength and items, but not your achievements. Keep this code safe, as you will need it to load your progress at a later date!\n\nGood luck!"
    infoTxt = TextBox(helpWindow, text=info, multiline=True, enabled=False, width="fill", height="fill")
    closeBtn = PushButton(helpWindow, text="Close Window", width="fill", command=lambda:close(helpWindow))
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Initialising application
app = App(title="The World's Worst Vending Machine", height=800, width=1000)
app.font = "Bahnschrift Light"
app.text_size = 12
app.bg = "#b6d1fc"

#Setting up sort boxes
leftBox = Box(app, align="left", border = 4, height="fill", width=500)
leftBox.bg = "#91bbff"
rightBox = TitleBox(app, align="left", border = 6, text="Menu", height="fill", width=500, layout="grid")
rightBox.bg = "#91bbff"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Leftmost box contents
statBox = Box(leftBox, align="top", width="fill", height=40)
moneyText = Text(statBox, align="left", text=("Money: "+str(money)))
strengthText = Text(statBox, align="right", text=("Strength: "+str(strength)))
imgText = Text(leftBox, align="top", size=240, text="🕋")
bufferText = Text(leftBox, align="bottom", text="\n\n\n\n\n\n\n\n")
descText = Text(leftBox, align="bottom", size=20, text="The weird vending machine\nhums at you ominously.", bold="True")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Rightmost box contents
buyBtn = PushButton(rightBox, width=35, grid=[0,0,2,1], text="Buy something from the machine!", command=lambda:buy(descText,imgText))
buyBtn.text_size = 18

sellBtn = PushButton(rightBox, width=18, grid=[0,1], text="Sell Item", command=lambda:sellItem())
sellBtn.text_size = 16
sellAllBtn = PushButton(rightBox, width=18, grid=[1,1], text="Sell All Items", command=lambda:sellAllItems(descText,imgText))
sellAllBtn.text_size = 16

eatBtn = PushButton(rightBox, width=18, grid=[0,2], text="Eat Item", command=lambda:eatItem())
eatBtn.text_size = 16
eatAllBtn = PushButton(rightBox, width=18, grid=[1,2], text="Eat All Items", command=lambda:eatAllItems(descText,imgText))
eatAllBtn.text_size = 16

spacer1 = Box(rightBox, height=50, width="fill", grid=[0,3,2,1])

workBtn = PushButton(rightBox, width=35, grid=[0,4,2,1], text="Work", command=lambda:work())
workBtn.text_size = 18

gymBtn = PushButton(rightBox, width=35, grid=[0,5,2,1], text="Gym", command=lambda:gym())
gymBtn.text_size = 18

punchBtn = PushButton(rightBox, width=35, grid=[0,6,2,1], text="Punch machine", command=lambda:punch(descText, imgText))
punchBtn.text_size = 18

craftBtn = PushButton(rightBox, width=18, grid=[0,7], text="Craft Item", command=lambda:craftItem())
craftBtn.text_size = 16
craftAllBtn = PushButton(rightBox, width=18, grid=[1,7], text="Craft All Items", command=lambda:craftAllItems(descText,imgText))
craftAllBtn.text_size = 16

spacer2 = Box(rightBox, height=60, width="fill", grid=[0,8,2,1])

achieveBtn = PushButton(rightBox, width=35, grid=[0,9,2,1], text="Achievements", command=lambda:achievements())
achieveBtn.text_size = 18
helpBtn = PushButton(rightBox, width=35, grid=[0,10,2,1], text="Help", command=lambda:helpbox())
helpBtn.text_size = 18

saveBtn = PushButton(rightBox, width=18, grid=[0,11], text="Save Game", command=lambda:save())
saveBtn.text_size = 16
loadBtn = PushButton(rightBox, width=18, grid=[1,11], text="Load Game", command=lambda:load())
loadBtn.text_size = 16

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

statBox.repeat(100, refresh)
app.display()