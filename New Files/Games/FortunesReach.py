import random
import time

class player:
    def __init__(self, moves, health, energy, name):
        self.moves = moves
        self.maxhealth = health
        self.maxenergy = energy
        self.health = self.maxhealth
        self.energy = self.maxenergy
        self.name = name
        self.inventory = ["Bread"]
        self.level = 1
        self.xp = 0
        self.nextLevel = 20
        self.gold = 10
        self.effect = [0, 0, 0] #Attack, Defence, Evasion
        self.equipped = ["Nothing +0","Nothing +0","Nothing +0"]
        self.xCoord = 2
        self.yCoord = 2
    
    def finalStats(self):
        print("Here are your final stats:")
        print()
        print("Name:", self.name)
        print("Level", self.level)
        print("XP to next level:", self.nextLevel)
        print("Max Health:", self.maxhealth)
        print("Max energy:", self.maxenergy)
        print("Inventory:", self.inventory)
        print("Equipped:", self.equipped)
        print("Gold:", self.gold)
        print()
        print("Thanks for playing!")
        
    def hit(self, damage):
        self.health -= damage
        print("You've been hit for", damage, "damage.")

    def useMove(self):
        print("Which move would you like to use? You have", str(self.energy) + " energy remaining. You can also type 'item' for items and 'run' to try and escape.")
        for x in range(len(self.moves)):
            print(self.moves[x][0] + ", Energy Cost:", str(self.moves[x][1]) + ", Damage:", str(self.moves[x][2]))
        match input().lower():
            case "1":
                if self.energy >= self.moves[0][1]:
                    self.energy-=self.moves[0][1]
                    print("You used",(self.moves[0][0])[3:]+".")
                    return(self.moves[0][2])
                else:
                    print("You don't have enough energy for this.")
                    return 0
            case "2":
                if self.energy >= self.moves[1][1]:
                    self.energy-=self.moves[1][1]
                    print("You used",(self.moves[1][0])[3:]+".")
                    return(self.moves[1][2])
                else:
                    print("You don't have enough energy for this.")
                    return 0
            case "3":
                if self.energy >= self.moves[2][1]:
                    self.energy-=self.moves[2][1]
                    print("You used",(self.moves[2][0])[3:]+".")
                    return(self.moves[2][2])
                else:
                    print("You don't have enough energy for this.")
                    return 0
            case "item":
                return -1
            case "run":
                return -2
            case _:
                print("That isn't an action! You skipped your turn.")
                return 0
            
    def useItem(self):
        global inFight
        print("What item would you like to use?")
        print(self.inventory)
        itemUse = input()
        if itemUse in self.inventory:
            match itemUse[0:len(itemUse)-3]:
                case "Ap":
                    print("You eat the apple and restore some health.")
                    self.health += 4
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    self.inventory.remove("Apple")
                case "Br":
                    print("You eat the bread and restore some health.")
                    self.health += 7
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    self.inventory.remove("Bread")
                case "W":
                    print("You drink the wine. While your health is fully restored, your energy decreases a little.")
                    self.health = self.maxhealth
                    self.energy -= 5
                    if self.energy <= 0:
                        self.energy = 1
                    self.inventory.remove("Wine")
                case "Coin Pu":
                    print("You open the coin purse and gain a random number of gold coins.")
                    self.gold += random.randint(1,100)
                    self.inventory.remove("Coin Purse")
                case "Glistening Sh":
                    print("You crush the shard in your palm and your body is invigorated with knowledge. You have gained 20xp.")
                    self.xp += 20
                    self.inventory.remove("Glistening Shard")
                case "Smoke B":
                    print("You throw the smoke bomb against the floor, masking your existence.")
                    self.effect[2] += 3
                    self.inventory.remove("Smoke Bomb")
                case "Smelling Sa":
                    print("While detrimental to your health, you feel energy coursing through your body.\nYou lose 3 health but gain an additional 2 strength and defence for the rest of this fight.")
                    self.effect[0] += 2
                    self.effect[1] += 2
                    self.health -= 3
                    self.inventory.remove("Smelling Salts")
                case "Orb of Rec":
                    match random.randint(1,3):
                        case 1:
                            print("Time warps around you. You recall a time of warriors, filled with vitality.")
                            print("Your health is entirely restored, and permanently increased by 10. You gain a temporary +10 attack and defence boost, if in battle.")
                            self.effect[0] += 10
                            self.effect[1] += 10
                            self.maxhealth += 10
                            self.health = self.maxhealth
                        case 2:
                            print("Time warps around you. You recall a time of mages, brimming with energy.")
                            print("Your energy is completely restored, and permanently increased by 10. You gain a temporary +10 attack and evasion boost, if in battle.")
                            self.effect[0] += 10
                            self.effect[2] += 10
                            self.maxenergy += 10
                            self.energy = self.maxenergy
                        case 3:
                            print("Time warps around you. You recall a time of shadows; unseen and untouched.")
                            print("Your health and energy are set to 200% of their maximum, until your next level. You also gain +10 to defence and evasion if in battle.")
                            self.effect[1] += 10
                            self.effect[2] += 10
                            self.health = self.maxhealth*2
                            self.energy = self.maxenergy*2
                        case _:
                            pass
                    self.inventory.remove("Orb of Recall")
                case "Rusty Knife":
                    if inFight == False:
                        print("You equipped the Rusty Knife.")
                        self.inventory.remove("Rusty Knife +1")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Rusty Knife +1")
                    else:
                        print("You can't equip this in battle!")
                case "Rusty Sword":
                    if inFight == False:
                        print("You equipped the Rusty Sword.")
                        self.inventory.remove("Rusty Sword +2")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Rusty Sword +2")
                    else:
                        print("You can't equip this in battle!")
                case "Rusty Shield":
                    if inFight == False:
                        print("You equipped the Rusty Shield.")
                        self.inventory.remove("Rusty Shield +1")
                        if self.equipped[1] != "Nothing +0":
                            self.inventory.append(self.equipped[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Rusty Shield +1")
                    else:
                        print("You can't equip this in battle!")
                case "Rusty Platebody":
                    if inFight == False:
                        print("You equipped the Rusty Platebody.")
                        self.inventory.remove("Rusty Platebody +2")
                        if self.equipped[1] != "Nothing +0":
                            self.equipped.append(self.inventory[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Rusty Platebody +2")
                    else:
                        print("You can't equip this in battle!")
                case "Uncommon Khopesh":
                    if inFight == False:
                        print("You equipped the Uncommon Khopesh.")
                        self.inventory.remove("Uncommon Khopesh +4")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Uncommon Khopesh +4")
                    else:
                        print("You can't equip this in battle!")
                case "Uncommon Kriegsmesser":
                    if inFight == False:
                        print("You equipped the Rusty Sword.")
                        self.inventory.remove("Uncommon Kriegsmesser +6")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Uncommon Kriegsmesser +6")
                    else:
                        print("You can't equip this in battle!")
                case "Uncommon Chainmail":
                    if inFight == False:
                        print("You equipped the Uncommon Chainmail.")
                        self.inventory.remove("Uncommon Chainmail +5")
                        if self.equipped[1] != "Nothing +0":
                            self.inventory.append(self.equipped[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Uncommon Chainmail +5")
                    else:
                        print("You can't equip this in battle!")
                case "Rare Longsword":
                    if inFight == False:
                        print("You equipped the Rare Longsword.")
                        self.inventory.remove("Rare Longsword +8")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Rare Longsword +8")
                    else:
                        print("You can't equip this in battle!")
                        
                case "Rare Halberd":
                    if inFight == False:
                        print("You equipped the Rare Halberd.")
                        self.inventory.remove("Rare Halberd +9")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Rare Halberd +9")
                    else:
                        print("You can't equip this in battle!")
                case "Legendary War Axe ":
                    if inFight == False:
                        print("You equipped the Legendary War Axe.")
                        self.inventory.remove("Legendary War Axe +15")
                        if self.equipped[0] != "Nothing +0":
                            self.inventory.append(self.equipped[0])
                            print(self.equipped[0], "added back to inventory.")
                        self.equipped[0] = ("Legendary War Axe +15")
                    else:
                        print("You can't equip this in battle!")
                case "Rare Cuirass":
                    if inFight == False:
                        print("You equipped the Rare Cuirass.")
                        self.inventory.remove("Rare Cuirass +8")
                        if self.equipped[1] != "Nothing +0":
                            self.inventory.append(self.equipped[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Rare Cuirass +8")
                    else:
                        print("You can't equip this in battle!")
                case "Rare Leg Guards":
                    if inFight == False:
                        print("You equipped the Rare Leg Guards.")
                        self.inventory.remove("Rare Leg Guards +9")
                        if self.equipped[1] != "Nothing +0":
                            self.inventory.append(self.equipped[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Rare Leg Guards +9")
                    else:
                        print("You can't equip this in battle!")
                case "Legendary Knights Set ":
                    if inFight == False:
                        print("You equipped the Legendary Knights Set.")
                        self.inventory.remove("Legendary Knights Set +20")
                        if self.equipped[1] != "Nothing +0":
                            self.inventory.append(self.equipped[1])
                            print(self.equipped[1], "added back to inventory.")
                        self.equipped[1] = ("Legendary Knights Set +20")
                    else:
                        print("You can't equip this in battle!")
                case _:
                    print("You cannot use this item.")
        else:
            print("This items doesn't exist in your inventory.")
    
    def status(self):
        print("")
        print("You are", self.name + ". You have", self.health, "out of a maximum of", self.maxhealth, "health, and", self.energy, "out of a maximum of", self.maxenergy, "energy.")
        print("You have", self.gold, "gold. Your currently equipped items are:", self.equipped)
        print("You are currently level", str(self.level) + ". You need", (self.nextLevel - self.xp), "xp in order to reach the next level.")
        print("")

class enemy:
    def __init__(self, damage, health, name, xp, loot):
        self.damage = damage
        self.health = health
        self.name = name
        self.xp = xp
        self.gold = random.randint(0,20)
        self.loot = loot[random.randint(0,21)]

    def damaged(self, damage):
        self.health-=damage
        print(self.name, "took", damage, "damage. It has", self.health, "health left.")

def fight(user, enemy):
    escape = False
    print("You have encountered the", enemy.name + "!")
    while user.health > 0 and enemy.health > 0 and escape == False:
        print()
        print("It is", user.name + "'s turn.")
        print(playerChar.name, "Health:", playerChar.health, "Energy:", playerChar.energy, "\n", enemy.name, "Health:", enemy.health)
        outcome = playerChar.useMove()
        if outcome == -2:
            if (random.randint(1,10))>6:
                print("Successful escape!")
                escape = True
            else:
                print("You attempt to flee, but your enemy is just too fast...")
        elif outcome == -1:
            playerChar.useItem()
        else:
            enemy.damaged(outcome+playerChar.effect[0])
            print()
        time.sleep(1)
        if enemy.health > 0 and escape == False:
            print("It is", enemy.name + "'s turn.")
            if enemy.damage < playerChar.effect[1]:
                print("The enemy attempts to attack, but your defence is to secure to get through.")
            else:
                if random.randint(1,10) - playerChar.effect[2] < 1:
                    print("The enemy attempts an attack, but you nimbly evade it!")
                else:
                    print(enemy.name, "attacks! He deals", str(enemy.damage-playerChar.effect[1]), "damage to you. You have", str(user.health-(enemy.damage-playerChar.effect[1])), "health remaining.")
                    user.health-=(enemy.damage-playerChar.effect[1])
            print()
        time.sleep(1)
    if user.health < 1:
        return 1
    elif enemy.health < 1:
        return 2
    elif escape == True:
        return 3

def initiateFight(enemies, playerChar):
    global playerDead
    global inFight
    inFight = True
    
    playerChar.effect = [int(playerChar.equipped[0][len(playerChar.equipped[0])-1:]), int(playerChar.equipped[1][len(playerChar.equipped[1])-1:]), int(playerChar.equipped[2][len(playerChar.equipped[2])-1:])]
    while len(enemies)>0 and playerDead == False:
        match fight(playerChar, enemies[0]):
            case 1:
                print("You lose the fight. The memory of", playerChar.name, "fades from existence.")
                playerDead = True
                for x in range(len(enemies)):
                    enemies.pop(0)
            case 2:
                playerChar.xp += enemies[0].xp
                playerChar.gold += (enemies[0].gold * playerChar.level)
                if enemies[0].loot != "None":
                    playerChar.inventory.append(enemies[0].loot)
                print(winText[random.randint(0,len(winText)-1)], "You have earned", enemies[0].xp, "xp. You have", playerChar.xp, "xp total.")
                print("You found", (enemies[0].gold * playerChar.level), "gold on the corpse of your enemy.")
                print("You looted the following from the enemy:", enemies[0].loot)
                enemies.pop(0)
            case 3:
                print("You got away with your life - narrowly.")
                for x in range(len(enemies)):
                    enemies.pop(0)
            case _:
                pass
    playerChar.effect = [0, 0, 0]

    while playerChar.nextLevel < playerChar.xp:
        playerChar.level += 1
        print("You leveled up! You are now level", str(playerChar.level) + ".")
        print("Your health and energy have been replenished and your max health and energy increase by 3.")
        
        playerChar.maxenergy += 3
        playerChar.energy = playerChar.maxenergy
        playerChar.maxhealth += 3
        playerChar.health = playerChar.maxhealth
        
        playerChar.xp -= playerChar.nextLevel
        playerChar.nextLevel = playerChar.nextLevel * 1.1
    inFight = False

def settlement(playerChar, settlementNum):
    global conversations
    global worldmap
    global storestock
    global rareloot
    global playerDead
    leave = False
    while leave == False:
        print("Welcome to", worldmap[playerChar.yCoord][playerChar.xCoord] + "!")
        if settlementNum == 0:
            print("What would you like to do? [Shop] [Train] [Talk] [Mystic] [Inn] [Leave]")
        else:
            print("What would you like to do? [Shop] [Talk] [Inn] [Leave]")
        match input().lower():
            case "shop":
                print("You have entered the", worldmap[playerChar.yCoord][playerChar.xCoord], "shop.")
                print("What would you like to do? [Buy] [Sell] [Leave]")
                match input().lower():
                    case "buy":
                        print("The store is currently selling the following:")
                        print(storestock)
                        print("")
                        print("You have", playerChar.gold,"gold. What would you like to buy?")
                        choice = input()
                        if choice in storestock:
                            if choice[len(choice)-1:].isnumeric() == True:
                                print("This item costs", 12*int(choice[len(choice)-1:]), "gold, would you like to buy it? [Y] [N]")
                                if input().upper() == "Y":
                                    if playerChar.gold > 12*int(choice[len(choice)-1:]):
                                        playerChar.gold -= 12*int(choice[len(choice)-1:])
                                        playerChar.inventory.append(choice)
                                        storestock.remove(choice)
                                    else:
                                        print("Not enough gold for this purchase!")
                            else:
                                print("This item costs 5 gold, would you like to buy it? [Y] [N]")
                                if input().upper() == "Y":
                                    if playerChar.gold > 5:
                                        playerChar.gold -= 5
                                        playerChar.inventory.append(choice)
                                        storestock.remove(choice)
                                    else:
                                        print("Not enough gold for this purchase!")
                        else:
                            print("Item not found!")
                                    
                    case "sell":
                        print("You currently have these items in your inventory:")
                        print(playerChar.inventory)
                        print("What would you like to sell?")
                        choice = input()
                        if choice in playerChar.inventory:
                            if int(choice[len(choice)-1:]) == int:
                                print("This item is worth", 10*int(choice[len(choice)-1:]), "gold, would you like to sell it? [Y] [N]")
                                if input().upper() == "Y":
                                    playerChar.gold += 10*int(choice[len(choice)-1:])
                                    playerChar.inventory.remove(choice)
                                    storestock.append(choice)
                            else:
                                print("This item is worth 3 gold, would you like to sell it? [Y] [N]")
                                if input().upper() == "Y":
                                        playerChar.gold += 5
                                        playerChar.inventory.remove(choice)
                                        storestock.append(choice)
                        else:
                            print("Item not found!")
                        
                    case _:
                        pass
            case "train":
                if settlementNum == 0:
                    if playerChar.gold > 1:
                        print("You have", playerChar.gold, "gold. Each gold gives you 0.5xp, so your training cost must be divisible by 2.")
                        cost = int(input("How much would you like to spend on training? "))
                        if cost%2 == 0 and cost < playerChar.gold:
                            playerChar.gold -= cost
                            playerChar.xp += cost/2
                            print("You spent", str(choice), "gold and received", str(choice/2), "experience in return.")
                            while playerChar.nextLevel < playerChar.xp:
                                playerChar.level += 1
                                print("You leveled up! You are now level", str(playerChar.level) + ".")
                                print("Your health and energy have been replenished and your max health and energy increase by 3.")
                                
                                playerChar.maxenergy += 3
                                playerChar.energy = playerChar.maxenergy
                                playerChar.maxhealth += 3
                                playerChar.health = playerChar.maxhealth
                                
                                playerChar.xp -= playerChar.nextLevel
                                playerChar.nextLevel = playerChar.nextLevel * 1.1
                        else:
                            print("Input not divisible by 2 or more than total gold.")
                    else:
                        print("You don't have enough gold to train!")
                else:
                    print("This service isn't available at this town. Try visiting Castle Holdent.")
            case "talk":
                print(conversations[settlementNum])
            case "mystic":
                if settlementNum == 0:
                    print("Ello me lovely. I'm the wandering mystic, though I've settled now. What can I do for you?")
                    print("The mystic can identify items for you. [Identify] [Leave]")
                    match input().lower():
                        case "identify":
                            print("You currently have these items in your inventory:")
                            print(playerChar.inventory)
                            print("What would you like to identify?")
                            choice = input()
                            if choice in playerChar.inventory:
                                match choice:
                                    case "Unidentified Weapon":
                                        playerChar.inventory.remove("Unidentified Weapon")
                                        item = rareloot[0][random.randint(0,2)]
                                        print("Your item was identified and was turned into a", item +"!")
                                        playerChar.inventory.append(item)
                                    case "Unidentified Armour":
                                        playerChar.inventory.remove("Unidentified Armour")
                                        item = rareloot[1][random.randint(0,2)]
                                        print("Your item was identified and was turned into a", item +"!")
                                        playerChar.inventory.append(item)
                                    case "Unidentified Item":
                                        playerChar.inventory.remove("Unidentified Item")
                                        item = rareloot[2][random.randint(0,1)]
                                        print("Your item was identified and was turned into a", item +"!")
                                        playerChar.inventory.append(item)
                                    case _:
                                        print("No item identified in inventory!")
                        case _:
                            pass
                else:
                    print("This service isn't available at this town. Try visiting Castle Holdent.")
            case "inn":
                print("You have", playerChar.gold, "gold.")
                print("Welcome to the inn! Do you wish to book a room for 10 gold pieces? [Y] [N]")
                if input().lower() == "y":
                    if playerChar.gold >= 10:
                        print("Thanks for your custom!")
                        input("You are now asleep. Press enter to wake up.")
                        print("\n"*100)
                        if (random.randint(0,100) < 99):
                            print("You wake up, feeling well rested. your health and energy are fully replenished.")
                            playerChar.health = playerChar.maxhealth
                            playerChar.energy = playerChar.maxenergy
                        else:
                            print("You had the worst sleep you've ever had. The mattress was brick hard, the bed frame was uneven, the room was cold and you're pretty sure a rat nibbled on your foot at some point. You lost 1 health.")
                            playerChar.health -= 1
                            if playerChar.health < 1:
                                playerDead = True
                        playerChar.gold -= 10
            case "inv":
                playerChar.useItem()
            case "stats":
                playerChar.status()
            case "leave":
                print("You left the settlement.")
                leave = True
            case _:
                print("Not an option - try again.")

worldmap = [["Castle Holdent","Wide Orchard","Rolling Fields","Urbos Hamlet","Western Badlands", "The Lunar Ocean", "Eaqeadore", "Gaglixar"],
            ["Grassy Grove","Rushly Village","Swampy Knoll","Kwarmi Jungle","The Expanse", "Iceglen", "The Rune Dominion", "Gleakiomund"],
            ["Arid Lowlands","Sand Banks","Vast Field","Pumpkin Patch","Northern Badlands", "Flellonet", "The Imagined Isle", "Strirranor"],
            ["Low-lying Mires","Waterlogged Village","Riverside Cliffs","High Peaks","The Pitch Black", "The Savage Plane", "The Phantom Valley", "The Mad Reach"],
            ["Hazey Frostlands","Frozen Lake","Snowy Town","Desolate Hills","Eastern Badlands", "The Miracle Territories", "The Final Moon", "Madmoor"],
            ["Garooreeg Tropics", "Lodcad Wetlands", "The Bush of Kisudogob", "Starruryon", "The Paradise of Ballirama", "The Mold", "The Feral Country"],
            ["Riverwich Village", "Buteca Wild", "The Volcanic Jungle", "Flameshore", "Crabbiothra", "Wiommolon", "The Legend Province"]]
winText = ["An empowering victory!", "Through suffering, you prevailed.", "A phyrric victory, but a victory nonetheless.", "Victory over your enemy, but at what cost?", "A harsh battle, but a positive outcome.", "Tribulations, rewards.", "Watch how the enemy falls!", "You cut swathes through their ranks."]
allMoves = [["Headbutt", 2, 3], ["Punch", 1, 2], ["Knee", 4, 4], ["Remold", 1, 3], ["Skew", 0, 1], ["Compress", 7, 6], ["1: Headbutt", 2, 3], ["2: Shin Impact", 1, 2], ["3: Crush", 3, 5], ["1: Quiet Strike", 0, 2], ["2: Bone Snap", 5, 7], ["3: Assassinate", 10, 15], ["1: Claw", 2, 3], ["2: Lacerate", 4, 6], ["3: Eviscerate", 9, 10]]
movelist = [[["1: Headbutt", 2, 3], ["2: Punch", 1, 2], ["3: Knee", 4, 4]], [["1: Remold", 1, 3], ["2: Skew", 0, 1], ["Compress", 7, 6]], [["Headbutt", 2, 3], ["Shin Impact", 1, 2], ["Crush", 3, 5]], [["Quiet Strike", 0, 2], ["Bone Snap", 5, 7], ["Assassinate", 10, 15]], [["Claw", 2, 3], ["Lacerate", 4, 6], ["Eviscerate", 9, 10]]]
enemyNames = ["Aigamuxa", "Antman Warrior", "Bunyip", "Ciguapa", "Cyclopes", "Lesser Dragon", "Lesser Fenrir", "Golem", "Vicious Gremlin", "Jersey Devil", "Kongamato", "Loch Ness Barracuda", "Nandi Bear", "Roc", "Orc", "Ogre", "Talos", "Troll", "Skeleton", "Draugr"]
conversations = ["Greetings, traveller. Welcome to the great castle. Nothing much happens here, so please enjoy your stay.", "Nice to have visitors in the hamlet. Not many of those nowadays. Please treat yourself to some bread from the local store - Ingrid, the baker, is quite the talent.", "Hullo! Nice little village we have here. 'ave yourself a looksee at the countryside while you're here, and rest your head at the inn.", "Stay back, wanderer. Those passing through cannot be trusted around here. We are settled close to great danger."]
raceStats = [[25,25],[20,30],[35,20],[15,40],[25,30]]
loot = ["None", "None", "None", "None", "None", "Rusty Knife +1", "Rusty Sword +2", "Rusty Shield +1", "Rusty Platebody +2", "Apple", "Bread", "Wine", "Coin Purse", "Glistening Shard", "Smoke Bomb", "Smelling Salts", "Uncommon Khopesh +4", "Uncommon Kriegsmesser +6", "Uncommon Chainmail +5", "Unidentified Weapon", "Unidentified Armour", "Unidentified Item"]
rareloot = [["Rare Longsword +8","Rare Halberd +9", "Legendary War Axe +15"],["Rare Cuirass +8","Rare Leg Guards +9","Legendary Knights Set +20"],["Glistening Shard","Orb of Recall"]]
legendaryloot = [("Vorpal Blade +" + str(random.randint(40,250))), ("Warped Armour +" + str(random.randint(40,250)))]
storestock = []
enemies = []
playerDead = False
inFight = False

print("Welcome to Fortune's Reach! What race would you like to play as?\n1: Human\n2: Variant\n3: Dwarf\n4: Drow\n5: Khajit\n6: Custom")
raceChoice = ""
while raceChoice.isnumeric() != True:
    raceChoice = input()
    if raceChoice.isnumeric() == False:
         print("Please enter a number relating to a race.")
if int(raceChoice) > 5:
    print("Welcome to the custom race creator. You will be asked a series of questions relating to your new race.")
    print("You will now enter your health and energy stats. The total of these stats cannot exceed 75.")
    customHealth = 1000
    customEnergy = 1000
    
    statConfirm = False
    while statConfirm == False:
        statTotal = 75
        customHealth = 1000
        customEnergy = 1000
        while customHealth > 75:
            print("Enter your health stat as a whole integer.")
            customHealth = int(input())
            if customHealth <= statTotal:
                statTotal -= customHealth
            else:
                print("Your stat total exceeds 75. Try again.")
                
        while customEnergy > statTotal:
            print("Enter your health stat as a whole integer.")
            customEnergy = int(input())
            if customEnergy <= statTotal:
                statTotal -= customEnergy
            else:
                print("Your stat total exceeds 75. Try again.")
    
    print("You will now select 3 moves from the total move pool. Choose wisely; your decisions are permanent!")
    customMoves = []
    for x in range(3):
        print("Select a move:")
        for x in range(len(allMoves)):
            print(x+1, allMoves[x])
        customMoves.append(allMoves(input()))
    
    print("Class created. And what will you name your character?")
    name = str(input())
    playerChar = player(movelist[race], customHealth, customEnergy, name)
else:
    race = int(raceChoice)-1
    print("I see. And what will you name your character?")
    name = str(input())
    playerChar = player(movelist[race], raceStats[race][0], raceStats[race][1], name)

print("Player created. You will now enter the world of Fortune's Reach. You can navigate this world by typing 'up', 'down', 'left' or 'right' at any time on the map.\nYou can also type 'inv' for your inventory, and 'stats' for your current status. Any other inputs, you will be prompted for. Good luck!\n\n")

while playerDead == False:
    if len(enemies) > 0:
        initiateFight(enemies, playerChar)
    if playerDead == False:
        print("You are currently stood in:", worldmap[playerChar.yCoord][playerChar.xCoord])
        match [playerChar.xCoord, playerChar.yCoord]:
            case [0,0]:
                print("Do you wish to enter the settlement? [Y] [N]")
                if input().upper() == "Y":
                    settlement(playerChar, 0)
            case [3,0]:
                print("Do you wish to enter the settlement? [Y] [N]")
                if input().upper() == "Y":
                    settlement(playerChar, 1)
            case [1,1]:
                print("Do you wish to enter the settlement? [Y] [N]")
                if input().upper() == "Y":
                    settlement(playerChar, 2)
            case [4,3]:
                print("Here lies a dangerous looking fortress. Do you wish to enter? [Y] [N]")
                if input().upper() == "Y":
                    print("You haven't the experience to enter here yet. You must come back when you are more ready to face great evil.")
            case [2,4]:
                print("Do you wish to enter the settlement? [Y] [N]")
                if input().upper() == "Y":
                    settlement(playerChar, 3)
            case [0,6]:
                print("Do you wish to enter the settlement? [Y] [N]")
                if input().upper() == "Y":
                    settlement(playerChar, 4)
            case _:
                pass
        storestock = ["Bread", "Wine", "Smoke Bomb", "Rusty Knife +1", "Rusty Shield +1", "Iron Ingot", "Wood Plank"]
            
        pInput = input("Which way do you want to go? ").lower()
        match pInput:
            case "up":
                playerChar.xCoord += 1
                if playerChar.xCoord > 6:
                    playerChar.xCoord = 0
                if ((random.randint(0,30)*(((playerChar.xCoord + 1) + (playerChar.yCoord + 1))/2)) > 35):
                    for x in range(random.randint(0,2)):
                        enemies.append(enemy(random.randint(1,(3+int(playerChar.level/2))), random.randint(5,10*(playerChar.level/2)), enemyNames[random.randint(0, len(enemyNames)-1)], random.randint(20,50+(2*playerChar.level)), loot))
            case "down":
                playerChar.xCoord -= 1
                if playerChar.xCoord < 0:
                    playerChar.xCoord = 6
                if ((random.randint(0,30)*(((playerChar.xCoord + 1) + (playerChar.yCoord + 1))/2)) > 35):
                    for x in range(random.randint(0,2)):
                        enemies.append(enemy(random.randint(1,(3+int(playerChar.level/2))), random.randint(5,20+(3+int(playerChar.level/2))), enemyNames[random.randint(0, len(enemyNames)-1)], random.randint(20,50+(2*playerChar.level)), loot))
            case "right":
                playerChar.yCoord += 1
                if playerChar.yCoord > 6:
                    playerChar.yCoord = 0
                if ((random.randint(0,30)*(((playerChar.xCoord + 1) + (playerChar.yCoord + 1))/2)) > 35):
                    for x in range(random.randint(0,2)):
                        enemies.append(enemy(random.randint(1,(3+int(playerChar.level/2))), random.randint(5,20+(3+int(playerChar.level/2))), enemyNames[random.randint(0, len(enemyNames)-1)], random.randint(20,50+(2*playerChar.level)), loot))
            case "left":
                playerChar.yCoord -= 1
                if playerChar.yCoord < 0:
                    playerChar.yCoord = 6
                if ((random.randint(0,30)*(((playerChar.xCoord + 1) + (playerChar.yCoord + 1))/2)) > 35):
                    for x in range(random.randint(0,2)):
                        enemies.append(enemy(random.randint(1,(3+int(playerChar.level/2))), random.randint(5,20+(3+int(playerChar.level/2))), enemyNames[random.randint(0, len(enemyNames)-1)], random.randint(20,50+(2*playerChar.level)), loot))
            case "inv":
                playerChar.useItem()
            case "stats":
                playerChar.status()
            case "help":
                print("You can navigate this world by typing 'up', 'down', 'left' or 'right' at any time on the map.\nYou can also type 'inv' for your inventory, and 'stats' for your current status. Any other inputs, you will be prompted for.\n")
            case _:
                print("Invalid input - try again.")
        

print("Game over. Maybe you will last longer in your next life.")
print()
print(playerChar.finalStats())