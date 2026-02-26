from random import randint
import time
import sys

completeDeck = ["A H", "2 H", "3 H", "4 H", "5 H", "6 H", "7 H", "8 H", "9 H", "10 H", "J H", "Q H", "K H",
                "A C", "2 C", "3 C", "4 C", "5 C", "6 C", "7 C", "8 C", "9 C", "10 C", "J C", "Q C", "K C",
                "A S", "2 S", "3 S", "4 S", "5 S", "6 S", "7 S", "8 S", "9 S", "10 S", "J S", "Q S", "K S",
                "A D", "2 D", "3 D", "4 D", "5 D", "6 D", "7 D", "8 D", "9 D", "10 D", "J D", "Q D", "K D"]

name = ""
money = 0
skills = []
bet = 0
velocityMult = 1
betMult = 2
lossMult = 1
playing = True
skillList = [["DoubleOrNothing", 500, "Allows the user to choose to play a second game with an 8x bonus multiplier, but also a 3x loss multiplier. All bets from the first game are ignored, and you can only play a second game if you won the first."],
            ["LuckyGem", 250, "Adds a +1 to your permanent bonus multiplier."],
            ["Mystery", 1000, "Does... something?"],
            ["PowerHand", 150, "Draw 3 cards instead of two at the start of the game."],
            ["Joker", 10000, "Allows you to create a Joker in your hand equal to any value from 1-11. Destroyed on use."],
            ["Upscrew", 100,"Adds a card worth 1 score to your current hand. Destroyed on use."],
            ["NailDown", 175, "Reduces dealer's hand by 1 score. Destroyed on use."],
            ["Aerodynamics", 55000, "Adds 0.0001 to both multipliers for every piece of money you have."],
            ["Velocity", 100000, "Doubles your bet and loss multiplier after every consecutive win. Resets on loss."],
            ["UnstableCore", 8000, "Has a 50% chance each round to multiply your bet multiplier by 10, but also the same chance for your loss multiplier instead."]]

def readSave(sf):
    global name
    global skills
    count = 0
    for line in sf:
        if count == 0:
            name = line
        elif count == 1:
            moneytext = line
        else:
            if line[len(line)-2:] == "\n":
                line = line[:len(line)-2]
            skills.append(line)
        count+=1
    sf.close()
    return int(moneytext)

def writeSave(firstsave):
    sf = open("save.txt", "w")
    sf.write("")
    sf.close()
    sf = open("save.txt", "a")
    if firstsave == True:
        sf.write(name + "\n")
    else:
        sf.write(name)
    sf.write(str(money) + "\n")
    for item in skills:
        sf.write(str(item))
    sf.close()
    return

def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def showCards(hand):
    fullHand = []
    for card in hand:
        fullCard = ""
        value = card[:2]
        suit = card[len(card)-1:]
        match value:
            case "A ":
                fullCard += "Ace of "
            case "J ":
                fullCard += "Jack of "
            case "Q ":
                fullCard += "Queen of "
            case "K ":
                fullCard += "King of "
            case "U":
                fullCard += "Upscrew"
            case "N":
                fullCard += "Nail"
            case "JO":
                fullCard += "Joker"
            case "10":
                fullCard += (value + " of ")
            case _:
                fullCard += (value + "of ")
        match suit:
            case "H":
                fullCard += "Hearts"
            case "D":
                fullCard += "Diamonds"
            case "C":
                fullCard += "Clubs"
            case "S":
                fullCard += "Spades"
        fullHand.append(fullCard)
    print(fullHand)

def handValue(hand):
    totalValue = 0
    for card in hand:
        value = card[:2]
        match value:
            case "A ":
                totalValue += 11
            case "J ":
                totalValue += 10
            case "Q ":
                totalValue += 10
            case "K ":
                totalValue += 10
            case _:
                totalValue += int(value)
    return totalValue

def game(fulldeck):
    global money
    global skills
    global bet
    global lossMult
    global betMult
    global velocityMult
    
    deck = fulldeck
    pCards = []
    dCards = []
    gameRound = True
    
    try:
        for skill in skills:
            match skill:
                case "LuckyGem\n":
                    betMult += 1
                case "Mystery\n":
                    if randint(0,100) < 2:
                        betMult *= 10
                        lossMult *= 10
                case "PowerHand\n":
                    pCard = randint(0, len(deck)-1)
                    pCards.append(deck[pCard])
                    deck.remove(pCards[0])
                case "Aerodynamics":
                    betMult+=(money*0.0001)
                    lossMult+=(money*0.0001)
                case "Velocity":
                    betMult+=velocityMult
                case "UnstableCore":
                    if randint(0,1) == 1:
                        betMult*=10
                    else:
                        lossMult*=10
                case _:
                    pass
    except:
        pass
    
    print("\n"*100)
    slowprint("The game begins...\n\n")
    slowprint("You and the dealer draw cards.\n")
    
    validBet = False
    while validBet == False:
        try:
            slowprint("Enter a bet: \n")
            bet = int(input())
            if bet <= money:
                validBet = True
            else:
                slowprint("Betted more than in account! Try again.\n")
        except:
            slowprint("Non-integer input detected - please enter a whole number to bet.\n")
    
    for x in range(2):
        pCard = randint(0, len(deck)-1)
        dCard = randint(0, len(deck)-1)
        while dCard==pCard:
            dCard = randint(0, len(deck)-1)
        pCards.append(deck[pCard])
        dCards.append(deck[dCard])
        deck.remove(pCards[x])
        deck.remove(dCards[x])
    slowprint("Your cards are:\n")
    showCards(pCards)
    Pscore = handValue(pCards)
    Dscore = handValue(dCards)
        
    while Pscore < 22 and gameRound == True:
        try:
            for skill in skills:
                match skill:
                    case "Upscrew\n":
                        slowprint("Do you want to use your Upscrew? (Y) (N)\n")
                        choice = input()
                        if choice.upper() == "Y":
                            pCards.append("1 U")
                            skills.remove(skill)
                    case "Joker\n":
                        slowprint("Do you want to use your Joker? (Y) (N)\n")
                        choice = input()
                        if choice.upper() == "Y":
                            validJoker = False
                            jvalue = 0
                            while validJoker == False:
                                try:
                                    slowprint("Enter a card value: \n")
                                    jvalue = int(input())
                                    if jvalue <= 11 and jvalue >= 1:
                                        validJoker = True
                                    else:
                                        slowprint("Not a valid card value from 1-11.\n")
                                except:
                                    slowprint("Non-integer input detected - please enter a whole number.\n")
                            pCards.append(str(jvalue) + " JO")
                            skills.remove(skill)
                    case _:
                        pass
        except:
            pass
        
        slowprint("Hold or hit?\n")
        choice = input().upper()
        if choice == "HOLD":
            gameRound = False
        elif choice == "HIT":
            pCard = randint(0, len(deck)-1)
            pCards.append(deck[pCard])
            deck.remove(pCards[len(pCards)-1])
            slowprint("You picked up a card. Your new hand is:\n")
            showCards(pCards)
            if "Redraw" in skills:
                slowprint("Do you wish to discard and redraw the last card? (Y) (N): \n")
                choice = input().upper()
                if choice == "Y":
                    pCards.pop(len(pCards)-1)
                    pCard = randint(0, len(deck)-1)
                    pCards.append(deck[pCard])
                    deck.remove(pCards[len(pCards)-1])
                    slowprint("You picked up a card. Your new hand is:\n")
                    showCards(pCards)
            Pscore = handValue(pCards)
    
    dDraw = True
    while dDraw == True:
        if Dscore<21:
            if randint(1,int(Dscore/2)) < 4:
                dCard = randint(0, len(deck)-1)
                dCards.append(deck[dCard])
                deck.remove(dCards[len(dCards)-1])
                Dscore = handValue(dCards)
            else:
                dDraw = False
        else:
            dDraw = False
    
    if "NailDown" in skills:
        slowprint("Do you want to use your Naildown? (Y) (N)\n")
        choice = input()
        if choice.upper() == "Y":
            dCards.append("-1 N")
            skills.remove(skill)
    
    time.sleep(0.5)
    slowprint("\n\nThe round ends with a stake of " + str(bet) + ", a bet multiplier of " + str(betMult) + " & a loss multiplier of " + str(lossMult) + ".\n")
    time.sleep(0.5)
    slowprint("The player's final hand:\n")
    showCards(pCards)
    time.sleep(1)
    slowprint("\nThe dealer's final hand:\n")
    showCards(dCards)
    time.sleep(1)
    print("\n\n")
    
    if Pscore>21:
        slowprint("You went bust. You lose your bet of "+str(bet*lossMult)+".\n")
        money-=bet*lossMult
        velocityMult=1
    elif Dscore>21:
        slowprint("The dealer went bust. You win!\n")
        if "DoubleOrNothing\n" in skills:
            slowprint("Activate double or nothing mode? (Y) (N):\n")
            choice  = input().upper()
            if choice == "Y":
                betMult *= 8
                lossMult *= 3
                game(completeDeck)
            else:
                slowprint("You take your winnings of " + str(bet*betMult) + ".\n")
                money+=bet*betMult
                velocityMult*=2
        else:
            slowprint("You take your winnings of " + str(bet*betMult) + ".\n")
            money+=bet*betMult
            velocityMult*=2
    elif Pscore>Dscore:
        slowprint("You scored higher than the dealer! You win!\n")
        if "DoubleOrNothing\n" in skills:
            slowprint("Activate double or nothing mode? (Y) (N):\n")
            choice  = input().upper()
            if choice == "Y":
                betMult *= 8
                lossMult *= 3
                game(completeDeck)
            else:
                slowprint("You take your winnings of " + str(bet*betMult) + ".\n")
                money+=bet*betMult
                velocityMult*=2
        else:
            slowprint("You take your winnings of " + str(bet*betMult) + ".\n")
            money+=bet*betMult
            velocityMult*=2
    elif Dscore>Pscore:
        slowprint("You score lower than the dealer. You lose your bet of "+str(bet*lossMult)+"\n")
        money-=bet*lossMult
        velocityMult=1
    betMult = 2
    lossMult = 1
    input("Press enter to continue...")
    print("\n"*100)
    return

def shop():
    global skills
    global money
    global skillList
    
    choice = ""
    todaySkills = []
    exitShop = False
    
    print("\n"*100)
    slowprint("Welcome to the shop, " + name)
    for x in range(3):
        todaySkills.append(skillList[randint(0,len(skillList)-1)][0])
    while exitShop != True:
        slowprint("Here's the skills available in today's pick: \n\n")
        print(todaySkills)
        slowprint("\nWhat would you like to do? Type a skill name or Exit.\n")
        choice = input()
        listItem = 0
        if choice in todaySkills:
            slowprint("\n\n\n" + choice + "\n\n")
            for y in range(len(skillList)-1):
                if choice in skillList[y]:
                    listItem = y
            slowprint(skillList[listItem][2] + "\n")
            slowprint("Cost: " + str(skillList[listItem][1]) + "\n\n")
            slowprint("Purchase? (Y) (N)\n")
            choice = input()
            if choice.upper() == "Y":
                if money-skillList[listItem][1] > 0:
                    slowprint("Purchase complete!\n")
                    money-=skillList[listItem][1]
                    skills.append("\n"+skillList[listItem][0]+"\n")
                    todaySkills.remove(skillList[listItem][0])
                else:
                    slowprint("You can't afford this!\n\n")
        elif choice.upper() == "EXIT":
            slowprint("Thank you for visiting! Come again for new stock after your next round.\n")
            exitShop = True
        else:
            slowprint("Invalid input.\n")
    return

def skillView():
    answer = ""
    while answer != "Exit":
        slowprint("Here are your current skills: \n")
        for item in skills:
            slowprint(item)
        slowprint("\n\nWhich skill would you like to inspect? Type skill name or Exit to exit\n")
        answer = input()
        if (answer+"\n") in skills:
            slowprint("\n\n\n" + answer + "\n\n")
            for y in range(len(skillList)-1):
                if answer in skillList[y]:
                    listItem = y
            slowprint(skillList[listItem][2] + "\n")
        elif answer.upper() == "EXIT":
            pass
        else:
            slowprint("Invalid input.\n")

def bingo():
    global bet
    global money
    
    slowprint("In Bingo, you will enter 5 numbers from 1-99, then place a bet.\n25 numbers will then be drawn at random. If your 5 numbers are in the 25... you win!\n")
    time.sleep(1)
    slowprint("Do you want to play? (Y) (N)\n")
    choice = input().upper()
    if choice == "Y":
        numlist = []
        while len(numlist)<5:
            slowprint("Input a number: ")
            try:
                numchoice = int(input())
                if numchoice>=1 and numchoice<=99:
                    numlist.append(numchoice)
                else:
                    slowprint("\nInvalid number selection! Must be between 1-99.\n")
            except:
                pass
        validBet = False
        while validBet == False:
            try:
                slowprint("Enter a bet: \n")
                bet = int(input())
                if bet <= money:
                    validBet = True
                else:
                    slowprint("Betted more than in account! Try again.\n")
            except:
                slowprint("Non-integer input detected - please enter a whole number to bet.\n")
        bingonums = []
        for x in range(25):
            num = randint(1,99)
            while num in bingonums:
                num = randint(1,99)
            slowprint(str(num)+"... ")
            bingonums.append(num)
            time.sleep(0.25)
        totalscore = 0
        for item in numlist:
            if item in bingonums:
                totalscore+=1
        if totalscore != 5:
            slowprint("\n\nToo bad...\n")
            money-=bet
        else:
            slowprint("\n\nWell done! You win!\n\n")
            money+=bet
    return

def slots():
    global money
    global bet
    symbols = ["💡", "📌", "🚀", "📞", "🦫", "🎲", "💀", "🫖", "💿", "💰"]
    slowprint("\nWelcome to slots! In slots, every spin is 10 money. If you line up three of the same symbol, you win!\nBetter symbols means bigger payouts. Press enter to spin, type Exit and press enter to leave.\n\n")
    choice = input()
    while choice.upper() != "EXIT":
        if money>10:
            money-=10
            outstr = ""
            num=[]
            for x in range(30):
                print("\n"*100)
                outstr=""
                for y in range(3):
                    outstr += symbols[randint(0,9)] + "  "
                print(outstr)
                time.sleep(0.025)
            num.append(symbols[randint(0,9)] + "  ")
            for x in range(30):
                print("\n"*100)
                outstr=num[0]
                for y in range(2):
                    outstr += symbols[randint(0,9)] + "  "
                print(outstr)
                time.sleep(0.025)
            num.append(symbols[randint(0,9)] + "  ")
            for x in range(30):
                print("\n"*100)
                outstr=num[0]+num[1]
                for y in range(1):
                    outstr += symbols[randint(0,9)] + "  "
                print(outstr)
                time.sleep(0.025)
            num.append(symbols[randint(0,9)] + "  ")
            print("\n"*100)
            print(num[0]+num[1]+num[2])
            if num[0] == num[1] and num[1] == num[2]:
                payout = symbols.index(num[0])
                if payout == 9:
                    slowprint("J A C K P O T !\n")
                    payout*=100
                slowprint("You won " + str(payout*10) + " credits!\n")
                money+=payout*100
            else:
                print("Too bad!")
        else:
            slowprint("Not enough money! Please exit...\n")
        choice = input()
    return

def cardGuess():
    global money
    global bet
    validBet = False
    slowprint("In card guesser, you guess what card the dealer draws from the deck. Simple, right?\nYour answer format should take the shape of the card value followed by the suit. Here are some examples:\nA D for Ace of Diamonds, 6 S for 6 of Spades, Q C for Queen of Clubs. Good luck!")
    while validBet == False:
        try:
            slowprint("Enter a bet: \n")
            bet = int(input())
            if bet <= money:
                validBet = True
            else:
                slowprint("Betted more than in account! Try again.\n")
        except:
            slowprint("Non-integer input detected - please enter a whole number to bet.\n")
    cardtoguess = completeDeck[randint(0,51)]
    slowprint("Input your card guess: ")
    cardguess = input()
    print("\n\n")
    time.sleep(1)
    slowprint("The card to guess was the " + cardtoguess + ". You guessed the " + cardguess + ".\n")
    if cardguess == cardtoguess:
        slowprint("Good guessing! You win your bet multiplied by 5!")
        money+=bet*5
    else:
        slowprint("Too bad! You lose your bet.")
        money-=bet
    return

def leave():
    writeSave(False)
    exit()

try:
    savefile = open("save.txt", "r")
    money = readSave(savefile)
    slowprint("Welcome back to Blackhack, " + name + "\n")
except:
    savefile = open("save.txt", "a")
    slowprint("Welcome to BlackHack!\n")
    slowprint("Enter your name: ")
    name = input()
    money = 100
    writeSave(True)
    savefile = open("save.txt", "r")
    money = readSave(savefile)

shopOpen = True
while playing == True:
    slowprint(name + "Money: " + str(money) + "\n\n")
    if money <=0:
        slowprint("...\n")
        time.sleep(1)
        slowprint("Looks like you've been through a poor string of luck.\n")
        time.sleep(1)
        slowprint("Interested in a bail out from the dealer? (Y) (N)\n\n")
        choice = input()
        if choice.upper() == "Y":
            slowprint("Atta boy. Here's 25 credits. Make it count.\n\n")
            money+=25
        else:
            slowprint("...then why are you here still? Bye bye!")
            quit()
    else:
        slowprint("What would you like to do? (Play) (Shop) (Skills) (Minigames) (Save) (Exit)\n")
        choice = input().upper()
        match choice:
            case "PLAY":
                game(completeDeck)
                shopOpen = True
            case "SHOP":
                if shopOpen == True:
                    shop()
                else:
                    slowprint("The shop is currently closed. Play another round to reopen it.")
                shopOpen = False
                input("Press enter to continue...")
                print("\n"*100)
            case "SKILLS":
                if len(skills) < 1:
                    slowprint("You have no skills.\n")
                else:
                    skillView()
                    input("Press enter to continue...")
                    print("\n"*100)
            case "MINIGAMES":
                slowprint("Which minigame would you like to play? (Slots) (Card Guesser) (Bingo) (Exit)\n")
                choice = input().upper()
                match choice:
                    case "BINGO":
                        bingo()
                    case "SLOTS":
                        slots()
                    case "CARD GUESSER":
                        cardGuess()
                    case _:
                        pass
                input("Press enter to continue...")
                print("\n"*100)
            case "RULES":
                slowprint("It's regular ol' blackjack, except twisted.\nNumber cards are equal to their value. Face cards are always 10, Aces are always 11.\nAll perks are permanent. If they apply a passive effect, it occurs every gameRound.\nAll active effects will prompt the player if they want to use them.\nThat's about it.\n")
                input("Press enter to continue...")
                print("\n"*100)
            case "HELP":
                slowprint("It's regular ol' blackjack, except twisted.\nNumber cards are equal to their value. Face cards are always 10, Aces are always 11.\nAll perks are permanent. If they apply a passive effect, it occurs every gameRound.\nAll active effects will prompt the player if they want to use them.\nThat's about it.\n")
                input("Press enter to continue...")
                print("\n"*100)
            case "SAVE":
                slowprint("\nSave the game? (Y) (N)\n")
                choice = input()
                if choice.upper() == "Y":
                    writeSave(False)
                    slowprint("\nGame saved.\n\n")
                else:
                    slowprint("\nSave aborted.\n")
                input("Press enter to continue...")
                print("\n"*100)
            case "EXIT":
                leave()
            case _:
                pass