from guizero import *
import re

#Initialising variables
btnValue = 1
multipliers = 1
pasMult = 1
money = 0
passive = 0
upgCosts = [25,50,100,5000,75000,250000,1000000]
pasCosts = [100,250]
staffCosts = [1000, 50000]

#Showing money
def refresh():
    moneyText.value = ("Money:",round(float(money),2))

#Adding money based on button click
def addMoney(cheatMult):
    global money
    money+=(btnValue*multipliers)*cheatMult

#Same as buyItem, but disables the button after purchase
def buyThenDisable(btn, cost, costValue, nextUpg, nextUpgCost, effect):
    btn.disable()
    buyItem(btn, cost, costValue, nextUpg, nextUpgCost, effect)
    overwriteText(btn, nextUpg)

#Sets the text for a given button, overwriting other functions
def overwriteText(btn, nextUpg):
    btn.text = (nextUpg[0] + "Bought!")

#Purchases the next upgrade of a button
def buyItem(btn, cost, costValue, nextUpg, nextUpgCost, effect):
    global money
    global multipliers
    global passive
    global btnValue
    global pasMult
    
    if money >= cost[costValue]:
        money-=cost[costValue]
        if effect[0] == "p":
            passive+=float(effect[1:])
        if effect[0] == "u":
            btnValue+=float(effect[1:])
        if effect[0] == "m":
            multipliers*=float(effect[1:])
        if effect[0] == "s":
            pasMult+=float(effect[1:])
        cost[costValue] = cost[costValue]*nextUpgCost
        btn.text=str(nextUpg[nextUpg.index((re.sub(r'\d+', '', btn.text)).replace(".",""))+1]) + str(cost[costValue])
        if nextUpg.index((re.sub(r'\d+', '', btn.text)).replace(".","")) == 5:
            btn.disable()
            btn.text = nextUpg[nextUpg.index((re.sub(r'\d+', '', btn.text)).replace(".",""))] + "Bought!"

#Calculates passive income
def income():
    global money
    money+=(passive*pasMult)/20

#Initialising application
app = App(title="Default Incremental Game", height=800, width=1400)
app.font = "Bahnschrift Light"
app.text_size = 12
app.bg = "#B9B9B9"

#Setup application sorters
topBox = Box(app, width=app.width-20, height = 40)
introText = Text(topBox, align="left", text="Welcome to Default Incremental!")
fillerBox = Box(topBox, align="left", width=825, height="fill")
moneyText = Text(topBox, align="left", text="Money:")

#Setup money button
moneyButton = PushButton(app, text="Click to make money!", width=80, height=4, command=lambda:addMoney(1))

#----------------------------------------------------------------------------------------------------------------------------------------

#Upgrade row sorters
upgBox = TitleBox(app, text="Upgrades", width="fill")
upgRow = Box(upgBox, width="fill", layout="grid")
multRow = TitleBox(upgBox, text="Multipliers", width="fill", layout="grid")

#Layout for upgrades:
#buyItem(<button self reference>,<list for costs of items>,<index of initial cost in list>,
#        <list for upgrade names>,<cost multiplier per stage>,
#        <effect (m for multipliers, u for additional upgrade, p for additional passive, s for passive multiplier)

#Adding click addition upgrades
upg1List = ["🪙 Value Button - Cost: ", "🪙 Better Button - Cost: ", "🪙 Bronze Button - Cost: ", "🪙 Silver Button - Cost: ", "🪙 Gold Button - Cost: ", "🪙 Final Button - Cost: "]
upg1 = PushButton(upgRow, grid=[0,0], width="fill", text="🪙 Value Button - Cost: 25", align="left", command=lambda:buyItem(upg1, upgCosts, 0, upg1List, 3, "u1"))
upg3List = ["📃 Value Printer - Cost: ", "📃 Better Printer - Cost: ", "📃 Industrial Printer - Cost: ", "📃 Complex Printer - Cost: ", "📃 Quantum Printer - Cost: ", "📃 Final Printer - Cost: "]
upg3 = PushButton(upgRow, grid=[1,0], width="fill", text="📃 Value Printer - Cost: 100", align="left", command=lambda:buyItem(upg3, upgCosts, 2, upg3List, 5, "u2.5"))
upg4List = ["🏷 Basic Couponing - Cost: ", "🏷 Improved Couponing - Cost: ", "🏷 Advanced Couponing - Cost: ", "🏷 Multimonitor Couponing - Cost: ", "🏷 Brainwave Couponing - Cost: ", "🏷 Final Couponing - Cost: "]
upg4 = PushButton(upgRow, grid=[2,0], width="fill", text="🏷 Basic Couponing - Cost: 5000", align="left", command=lambda:buyItem(upg4, upgCosts, 3, upg4List, 10, "u10"))
upg5List = ["🔗 Blockchain Budgeting - Cost: ", "🔗 Enhanced Blockchain - Cost: ", "🔗 Internet Upgrade - Cost: ", "🔗 P2P Fibreoptics - Cost: ", "🔗 Etherium Flipping - Cost: ", "🔗 Final Blockchain - Cost: "]
upg5 = PushButton(upgRow, grid=[3,0], width="fill", text="🔗 Blockchain Budgeting - Cost: 75000", align="left", command=lambda:buyItem(upg5, upgCosts, 4, upg5List, 12.5, "u500"))
upg6List = ["⚙️ Basic Processing - Cost: ", "⚙️ Advanced Processing - Cost: ", "⚙️ Homogenous Processing - Cost: ", "🔗 P2P Fibreoptics - Cost: ", "🔗 Etherium Flipping - Cost: ", "🔗 Final Blockchain - Cost: "]
upg6 = PushButton(upgRow, grid=[4,0], width="fill", text="⚙️ Basic Processing - Cost: 250000", align="left", command=lambda:buyItem(upg6, upgCosts, 5, upg6List, 12.5, "u12500"))

upg7List = ["🧮 Nursery Maths Lessons - Cost: ", "🧮 KS1 Maths Lessons - Cost: ", "🧮 KS2 Maths Lessons - Cost: ", "🧮 KS3 Maths Lessons - Cost: ", "🧮 College Maths Lessons - Cost: ", "🧮 University Maths Lessons - Cost: "]
upg7 = PushButton(upgRow, grid=[0,1], width="fill", text="🧮 Nursery Maths Lessons - Cost: 100000", align="left", command=lambda:buyItem(upg7, upgCosts, 6, upg7List, 15, "u150000"))


upg2List = ["❌ Micro Multiplier - Cost: ", "❌ Macro Multiplier - Cost: ", "❌ Bronze Multiplier - Cost: ", "❌ Silver Multiplier - Cost: ", "❌ Gold Multiplier - Cost: ", "❌ Final Multiplier - Cost: "]
upg2 = PushButton(multRow, grid=[0,0], width="fill", text="❌ Micro Multiplier - Cost: 50", align="left", command=lambda:buyItem(upg2, upgCosts, 1, upg2List, 4, "m1.5"))

#----------------------------------------------------------------------------------------------------------------------------------------

#Passive row sorter
pasBox = TitleBox(app, text="Passives", width="fill")
pasRow = Box(pasBox, width="fill")
staffRow = TitleBox(pasBox, text="Staff", width="fill")

#Adding passive upgrades
pas1List = ["⏱ Value Passive - Cost: ", "⏱ Bronze Passive - Cost: ", "⏱ Silver Passive - Cost: ", "⏱ Gold Passive - Cost: ", "⏱ Platinum Passive - Cost: ", "⏱ Final Passive - Cost: "]
pas1 = PushButton(pasRow, text="⏱ Value Passive - Cost: 100", align="left", command=lambda:buyItem(pas1, pasCosts, 0, pas1List, 1.5, "p0.1"))
pas2List = ["🏗 Value Microfactory - Cost: ", "🏗 Factory Upgrade - Cost: ", "🏗 Factory Enlarger - Cost: ", "🏗 Iron Factory - Cost: ", "🏗 Steel Factory - Cost: ", "🏗 Final Factory - Cost: "]
pas2 = PushButton(pasRow, text="🏗 Value Microfactory - Cost: 250", align="left", command=lambda:buyItem(pas2, pasCosts, 1, pas2List, 3, "p2.5"))

#Adding passive multipliers
staff1List = ["👷🏿 Passivity Manager - Cost: ","👷🏿 Passivity Manager - Cost: "]
staff1 = PushButton(staffRow, text="👷🏿 Passivity Manager - Cost: 250", align="left", command=lambda:buyThenDisable(staff1, staffCosts, 0, staff1List, "s5"))
staff2List = ["👷🏿 Factory Manager - Cost: ","👷🏿 Factory Manager - Cost: "]
staff2 = PushButton(staffRow, text="👷🏿 Factory Manager - Cost: 50000", align="left", command=lambda:buyThenDisable(staff2, staffCosts, 0, staff2List, "s10"))

#----------------------------------------------------------------------------------------------------------------------------------------

#Calculating income based on passives and refreshing money label
moneyText.repeat(100, refresh)
moneyButton.repeat(50, income)
app.display()
