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
        self.inventory = []
        self.level = 1
        self.xp = 0
        self.nextLevel = 20
        self.gold = 10
        self.effect = [0, 0, 0] #Attack, Defence, Evasion
        self.xCoord = 2
        self.yCoord = 2

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
        print("What item would you like to use?")
        print(self.inventory)
        itemUse = input()
        if itemUse in self.inventory:
            match itemUse:
                case "Apple":
                    print("You eat the apple and restore some health.")
                    self.health += 4
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    self.inventory.remove("Apple")
                case "Bread":
                    print("You eat the apple and restore some health.")
                    self.health += 7
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    self.inventory.remove("Bread")
                case "Wine":
                    print("You drink the wine. While your health is fully restored, your energy decreases a little.")
                    self.health = self.maxhealth
                    self.energy -= 5
                    if self.energy <= 0:
                        self.energy = 1
                    self.inventory.remove("Wine")
                case "Coin Purse":
                    print("You open the coin purse and gain a random number of gold coins.")
                    self.gold += random.randint(1,100)
                    self.inventory.remove("Coin Purse")
                case "Glistening Shard":
                    print("You crush the shard in your palm and your body is invigorated with knowledge. You have gained 20xp.")
                    self.xp += 20
                    self.inventory.remove("Glistening Shard")
                    pass
                case "Smoke Bomb":
                    print("You throw the smoke bomb against the floor, masking your existence.")
                    self.effect[2] = 3
                    self.inventory.remove("Smoke Bomb")
                    pass
                case "Smelling Salts":
                    print("While detrimental to your health, you feel energy coursing through your body.\nYou lose 3 health but gain an additional 2 strength and defence for the rest of this fight.")
                    self.effect[0] = 2
                    self.effect[1] = 2
                    self.health -= 3
                    self.inventory.remove("Smelling Salts")
                    pass
                case _:
                    print("You cannot use this item.")
        else:
            print("This items doesn't exist in your inventory.")

class enemy:
    def __init__(self, damage, health, name, xp, loot):
        self.damage = damage
        self.health = health
        self.name = name
        self.xp = xp
        self.gold = random.randint(0,100)
        self.loot = loot[random.randint(0,20)]

    def damaged(self, damage):
        self.health-=damage
        print(self.name, "took", damage, "damage. It has", self.health, "health left.")

def fight(user, enemy):
    escape = False
    print("You have encountered", enemy.name + "!")
    while user.health > 0 and enemy.health > 0:
        print()
        print("It is", user.name + "'s turn.")
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
            enemy.damaged(outcome)
            print()
        time.sleep(3)
        if enemy.health > 0:
            print("It is", enemy.name + "'s turn.")
            print(enemy.name, "attacks! He deals", str(enemy.damage), "damage to you. You have", str(user.health-enemy.damage), "health remaining.")
            user.health-=enemy.damage
            print()
        time.sleep(3)
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
    while len(enemies)>0 and playerDead == False:
        match fight(playerChar, enemies[0]):
            case 1:
                print("You lose the fight. The memory of", playerChar.name, "fades from existence.")
                playerDead = True
            case 2:
                playerChar.xp += enemies[0].xp
                print(winText[random.randint(0,len(winText)-1)], "You have earned", enemies[0].xp, "xp. You have", playerChar.xp, "xp total.")
                print("You looted the following from the enemy:", enemies[0].loot)
                enemies.pop(0)
            case 3:
                print("You got away with your life - narrowly.")
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
        
map = [["Castle Holdent","Wide Orchard","Rolling Fields","Urbos Hamlet","Western Badlands"],["Grassy Grove","Rushly Village","Swampy Knoll","Kwarmi Jungle","The Expanse"],["Arid Lowlands","Sand Banks","Vast Field","Pumpkin Patch","Northern Badlands"],["Low-lying Mires","Waterlogged Village","Riverside Cliffs","High Peaks","The Pitch Black"],["Hazey Frostlands","Frozen Lake","Snowy Town","Desolate Hills","Eastern Badlands"]]
winText = ["An empowering victory!", "Through suffering, you prevailed.", "A phyrric victory, but a victory nonetheless.", "Victory over your enemy, but at what cost?", "A harsh battle, but a positive outcome.", "Tribulations, rewards.", "Watch how the enemy falls!", "You cut swathes through their ranks."]
movelist = [[["1: Headbutt", 2, 3], ["2: Punch", 1, 2], ["3: Knee", 4, 4]], [["1: Remold", 1, 3], ["2: Skew", 0, 1], ["3: Compress", 7, 6]], [["1: Headbutt", 2, 3], ["2: Shin Impact", 1, 2], ["3: Crush", 3, 5]], [["1: Quiet Strike", 0, 2], ["2: Bone Snap", 5, 7], ["3: Assassinate", 10, 15]], [["1: Claw", 2, 3], ["2: Lacerate", 4, 6], ["3: Eviscerate", 9, 10]]]
enemyNames = ["Grognak", "Sloggum", "Krumbash", "Jorpa", "Treego", "Trunko", "Hampeet", "Muiglos", "Freejee"]
raceStats = [[25,25],[20,30],[35,20],[15,40],[25,30]]
loot = ["None", "None", "None", "None", "None", "Rusty Knife +1", "Rusty Sword +2", "Rusty Shield +1", "Rusty Platebody +2", "Apple", "Bread", "Wine", "Coin Purse", "Glistening Shard", "Smoke Bomb", "Smelling Salts", "Uncommon Khopesh +4", "Uncommon Kriegsmesser +6", "Uncommon Chainmail +5", "Unidentified Weapon"]
enemies = []
playerDead = False
inFight = False

print("Welcome to Dapplegrove! What race would you like to play as?\n1: Human\n2: Variant\n3: Dwarf\n4: Drow\n5: Khajit")
race = int(input())-1
print("I see. And what will you name your character?")
name = str(input())

playerChar = player(movelist[race], raceStats[race][0], raceStats[race][1], name)
print("Player created. You will now enter the world of Dapplegrove. You can navigate this world by typing 'up', 'down', 'left' or 'right' at any time on the map. Any other inputs, you will be prompted for. Good luck!\n\n")

while playerDead == False:
    if len(enemies) > 0:
        initiateFight(enemies, playerChar)
    print("You are currently stood in:", map[playerChar.yCoord][playerChar.xCoord])
    pInput = input("Which way do you want to go? ").lower()
    match pInput:
        case "up":
            playerChar.xCoord += 1
            if playerChar.xCoord > 4:
                playerChar.xCoord = 0
        case "down":
            playerChar.xCoord -= 1
            if playerChar.xCoord < 0:
                playerChar.xCoord = 4
        case "right":
            playerChar.yCoord += 1
            if playerChar.yCoord > 4:
                playerChar.yCoord = 0
        case "left":
            playerChar.yCoord -= 1
            if playerChar.yCoord < 0:
                playerChar.yCoord = 4
        case "inv":
            playerChar.useItem()
        case _:
            print("Invalid input - try again.")
    if ((random.randint(0,30)*(((playerChar.xCoord + 1) + (playerChar.yCoord + 1))/2)) > 35):
        for x in range(random.randint(0,3)):
            enemies.append(enemy(random.randint(1,5), random.randint(5,20), enemyNames[random.randint(0, len(enemyNames)-1)], random.randint(20,50), loot))   

print("Game over. Maybe you will last longer in your next life.")