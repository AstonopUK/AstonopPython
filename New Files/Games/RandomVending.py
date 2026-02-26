import random
import math

food = ["Sheep", "Scallops", "Air", "Sausages", "Bread", "Fish", "Ducks", "Chicken", "Potatoes", "Salmon", "Soup", "Pizzas", "Macaroni", "Tendies", "Geese", "Curry", "Limes", "Apples", "Dogs", "Cats", "Snails", "Crocodiles", "Horses", "Deer", "Cake", "Beans", "Frogs", "Human Limbs", "Biscuits", "Handbags", "Hams", "Giraffes", "Plutonium", "Evil Bugs", "Death Juice"]
adjectives = ["Decorative", "Juiced", "Squashed", "Flambeed", "Expensive", "Sausage-shaped", "Baked", "Fried", "Dry Frozen", "Jerkied", "Sizzled", "Hot", "Roasted", "Deconstructed", "Beefy", "Cheesy", "Golden", "Filleted", "Burnt", "Stack of", "Kilo of", "Broken", "Alive", "Stolen", "Curried", "Asbestos-laced", "Carcinogenic", "Poisoned", "Radioactive", "Reincarnated", "Thoroughly-Rizzed", "Reconstituted", "Chemicular", "Bruised", "Decaying", "Ancient"]
bonusadj = ["Harmful", "Decorative", "Decadent", "Spherical", "Obtuse", "Spanish", "British", "Italian", "German", "French", "African", "Malaysian", "American", "Mexican", "Philippino", "Peruvian", "Turkish"]
bestadj = ["Ultimate", "Giga", "Ultra", "The Best", "Monstrous", "Gargantuan", "Collosal", "Waitrose", "Wotsit-like", "Roblox Branded", "Intercontinental", "Silver-Plated", "Universally Fundamental", "Atomically-Fissioned", "Dramatically Accelerated", "Sonar-Emitting", "Bluetooth Compatible"]
combinations = [" with ", " con ", " a la ", " complemented by ", " drizzled with ", " coated with ", " with a sauce of ", " glazed with ", " with a reduction of ", " and ", " next to ", " lightly dusted with ", " flambeed with ", " liberally soused with ", " generously heaped with ", " served on a bed of ", " blessed with "]
inventory = []
money = 20
strength = 1

print("You have $" + str(money) + ". Your strength is at", strength, "points.")
userinp = input("What would you like to do? [Buy] [Work] [Sell] [Eat] [Punch] [Gym] [Craft] [Help] [Save] [Load] ")
while True:
    try:
        strength = round(strength, 2)
        match userinp.lower():
            case "buy":
                if money >= 20:
                    if money >= 100:
                        userinp = int(input("How many items do you wish to buy? "))
                        if userinp*20 > money:
                            print("You cannot afford that many.")
                        else:
                            for x in range(userinp):
                                if strength < 5:
                                    adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                                    fooditem = food[random.randint(0, len(food)-1)]
                                    print("You purchased a", adj1, fooditem + ".")
                                    itemtoadd = adj1 + " " + fooditem
                                    inventory.append(itemtoadd)
                                    money -= 20
                                elif strength >= 5 and strength < 10:
                                    adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                                    adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                                    fooditem = food[random.randint(0, len(food)-1)]
                                    print("You purchased a", adj1, adj2, fooditem + ".")
                                    itemtoadd = adj1 + " " + adj2 + " " + fooditem
                                    inventory.append(itemtoadd)
                                    money -= 20
                                elif strength >= 10 and strength < 25:
                                    adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                                    adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                                    adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                                    fooditem = food[random.randint(0, len(food)-1)]
                                    print("You purchased a", adj1, adj2, adj3, fooditem + ".")
                                    itemtoadd = adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                                    inventory.append(itemtoadd)
                                    money -= 20
                                elif strength >= 25:
                                    adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                                    adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                                    adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                                    adj4 = bestadj[random.randint(0, len(bestadj)-1)]
                                    fooditem = food[random.randint(0, len(food)-1)]
                                    print("You purchased a", adj4, adj1, adj2, adj3, fooditem + ".")
                                    itemtoadd = adj4 + " " + adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                                    inventory.append(itemtoadd)
                                    money -= 20
                    else:
                        if strength < 5:
                            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                            fooditem = food[random.randint(0, len(food)-1)]
                            print("You purchased a", adj1, fooditem + ".")
                            itemtoadd = adj1 + " " + fooditem
                            inventory.append(itemtoadd)
                            money -= 20
                        elif strength >= 5 and strength < 10:
                            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                            fooditem = food[random.randint(0, len(food)-1)]
                            print("You purchased a", adj1, adj2, fooditem + ".")
                            itemtoadd = adj1 + " " + adj2 + " " + fooditem
                            inventory.append(itemtoadd)
                            money -= 20
                        elif strength >= 10 and strength < 25:
                            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                            adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                            fooditem = food[random.randint(0, len(food)-1)]
                            print("You purchased a", adj1, adj2, adj3, fooditem + ".")
                            itemtoadd = adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                            inventory.append(itemtoadd)
                            money -= 20
                        elif strength >= 25:
                            adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                            adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                            adj3 = bonusadj[random.randint(0, len(bonusadj)-1)]
                            adj4 = bestadj[random.randint(0, len(bestadj)-1)]
                            fooditem = food[random.randint(0, len(food)-1)]
                            print("You purchased a", adj4, adj1, adj2, adj3, fooditem + ".")
                            itemtoadd = adj4 + " " + adj1 + " " + adj2 + " " + adj3 + " " + fooditem
                            inventory.append(itemtoadd)
                            money -= 20
                else:
                    print("You are too poor to buy anything. Do some work!")
            case "work":
                print("It's workin time.")
                while userinp.lower() != "leave":
                    print("You have $" + str(money) + ".")
                    print("Solve the following maths problem to earn, or type leave to exit work.")
                    num1 = random.randint(1,20)
                    num2 = random.randint(1,20)
                    print("What is", num1, "plus", num2, "?")
                    userinp = input()
                    if userinp != "leave":
                        if int(userinp) == (num1+num2):
                            print("Good work! Added", math.trunc(5 * strength),"dollars to account.")
                            money += math.trunc(5*strength)
                        else:
                            print("Oof. You got it wrong.")
                    else:
                        print("You decided to leave work.")
            case "sell":
                if len(inventory) > 0:
                    print("Which item would you want to sell? [Enter the number of the item in the list below]")
                    trackNum = 1
                    for item in inventory:
                        print(str(trackNum) + ": " + item)
                        trackNum+=1
                    userinp = int(input())
                    try:
                        money += len(inventory[userinp-1])/2
                        print("You sold the " + inventory[userinp-1] + ".")
                        print("You earned", len(inventory[userinp-1])/2, "dollars.")
                        inventory.pop(userinp-1)
                    except:
                        print("Failed to sell item!")
                else:
                    print("Your inventory is empty.")
            case "eat":
                if len(inventory) > 0:
                    print("Which item would you want to eat? [Enter the number of the item in the list below]")
                    trackNum = 1
                    for item in inventory:
                        print(str(trackNum) + ": " + item)
                        trackNum+=1
                    try:
                        userinp = int(input())
                        strength += len(inventory[userinp-1])/100
                        print("You ate the", inventory[userinp-1], "and gained", len(inventory[userinp-1])/100, "strength.")
                        inventory.pop(userinp-1)
                    except:
                        print("Failed to eat item!")
                else:
                    print("Your inventory is empty.")
            case "punch":
                randinteger = random.randint(0,100)
                if randinteger<50:
                    print("Your feeble fist cracks against the machine. Your strength is halved.")
                    strength = strength/2
                else:
                    print("The machine wobbles and drops a free item!")
                    adj1 = adjectives[random.randint(0, len(adjectives)-1)]
                    adj2 = adjectives[random.randint(0, len(adjectives)-1)]
                    fooditem = food[random.randint(0, len(food)-1)]
                    print("You get a", adj1, adj2, fooditem + ".")
                    itemtoadd = adj1 + " " + adj2 + " " + fooditem
                    inventory.append(itemtoadd)
            case "gym":
                print("Workout costs $" + str(100*strength) + " for 1 strength. Get swole?")
                userinp = input()
                if userinp.lower() == "yes":
                    if money >= (100*strength):
                        money-=(100*strength)
                        strength+=1
                        print("You worked out and gained a strength")
                    else:
                        print("You're too poor to work out.")
                else:
                    print("Maybe next time.")
            case "craft":
                if len(inventory) > 1:
                    num1 = 0
                    num2 = 0
                    print("Which items would you like to combine? [Enter the number of the item in the list below]")
                    trackNum = 1
                    for item in inventory:
                        print(str(trackNum) + ": " + item)
                        trackNum+=1
                    try:
                        num1 = int(input("Enter first number: "))
                        num2 = int(input("Enter second number: "))
                        item1 = inventory[num1-1]
                        item2 = inventory[num2-1]
                        newitem = item1 + combinations[random.randint(0, len(combinations)-1)] + item2 + "                             "
                        print("Crafted new item:", newitem)
                        inventory.append(newitem)
                        inventory.remove(item1)
                        inventory.remove(item2)
                    except:
                        print("Failed to merge items!")
                else:
                    print("Too few items in inventory!")
            case "help":
                print("Use the vending machine to get items. Each item costs $20.\nYou can work to get money by solving sums - each sum makes you $5.\nYou can sell items from the vending machine. Some items sell for more money than others.\nYou can eat items from the machine to gain strength - the stronger you are, the more money you make and the more items become available in the machine.")
            case "save":
                print("Save the game? Please note that this gives you a code which saves your strength and money, but not your items. Be sure to use or sell your items before saving. [Yes] [No]")
                if input().lower() == "yes":
                    print("Your load code is:")
                    print("<"+str(money*8.125)+"|"+str(strength*8.125)+">")
            case "load":
                print("Enter your load code from your previous save:")
                loadCode = input()
                if loadCode[0] == "<" and loadCode[len(loadCode)-1] == ">":
                    ldCodes = ["",""]
                    try:
                        trackNum = 0
                        for num in range(1,len(loadCode)-1):
                            if loadCode[num] != "|":
                                #print(loadCode[num])
                                ldCodes[trackNum]=ldCodes[trackNum]+loadCode[num]
                            else:
                                trackNum+=1
                        
                        #print(ldCodes)
                        ldCodes[0]=round(float(ldCodes[0])/8.125,2)
                        ldCodes[1]=round(float(ldCodes[1])/8.125,2)
                        
                        money = ldCodes[0]
                        strength = ldCodes[1]
                        
                        inventory = []
                    except:
                        print("Error in loading save - aborted.")
                else:
                    print("Invalid load code.")
            case _:
                print("Command not recognised!")
        
        money = round(money,2)
        strength = round(strength,2)
        
        print("\n"*3)
        print("You have $" + str(money) + ". Your strength is at", strength, "points.")
        userinp = input("What would you like to do? [Buy] [Work] [Sell] [Eat] [Punch] [Gym] [Craft] [Help] [Save] [Load] ")
    except:
        print("Oops! Something went wrong.")