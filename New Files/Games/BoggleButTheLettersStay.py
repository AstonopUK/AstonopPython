#65 is A, 90 is Z
import random
import time
import enchant
import os

replay = True

while replay == True:

    print ("\n" * 100)
    dictionary = enchant.Dict("en_UK")
    boggleList = []
    startTime = 0
    score = 0
    usedWords = []

    gridsize = int(input("Input the size of grid you want to play with! \n Please note that highscores are only recorded for a grid size of 4.\n"))
    startTime = time.time()

    for x in range(gridsize*gridsize):
        boggleList.append(random.randint(65,90))
        
    while (time.time() - startTime) < 45:
        print("\n")
        for y in range(gridsize):
            newString = ""
            for z in range(gridsize):
                newChar = ''
                if boggleList[(y*gridsize) + z] == 0:
                    newString = newString + "    "
                else:
                    newString = newString + chr(boggleList[(y*gridsize) + z]) + "   "
                 
            print(newString.center(20))
            print("\n")

        print("Current score: ", score, "\n")
        userWord = str(input("Input word:\n")).upper()
        userWordList = []
        if len(userWord) > 2 and dictionary.check(userWord) == True:
            validityCheck = 0
            
            for letters in userWord:
                    userWordList.append(ord(letters))
                    
            for integerX in range(len(userWordList)):
                for integerY in range(len(boggleList)):
                    if userWordList[integerX] == boggleList[integerY]:
                        validityCheck = validityCheck + 1
                        break
                continue

            if validityCheck == len(userWord):
                checkIfUsed = False
                for o in range(len(usedWords)):
                    if userWord == usedWords[o]:
                        checkIfUsed = True
                if checkIfUsed == False:
                    score += (len(userWord) * len(userWord))
                    usedWords.append(userWord)
                else:
                    print("Word already used!")
                
        else:
            print("Not a valid word - try again!\n")

    for y in range(gridsize):
            newString = ""
            for z in range(gridsize):
                newChar = ''
                if boggleList[(y*gridsize) + z] == 0:
                    newString = newString + "    "
                else:
                    newString = newString + chr(boggleList[(y*gridsize) + z]) + "   "
                 
            print(newString)
            print("\n")
    if gridsize == 4:
        file = open("C:\\Users\\ben_h\\OneDrive\\Desktop\\Python\\BoggleBTLSHiscore.txt", "w")
        linetowrite = ""
        for line in file:
            linetowrite += line + "\n"
        linetowrite += str(score) + "\n"
        file.writelines(linetowrite)
        file.close()

        file = open("C:\\Users\\ben_h\\OneDrive\\Desktop\\Python\\BoggleBTLSHiscore.txt", "r")
        hiscore = 0
        for line in file:
            print(line)
            if (int(line)) > hiscore:
                hiscore = int(line)
        file.close()

        print("Time's up! You got ", score, " points!")
        if score == hiscore:
            print("Congratulations! You got a new high score.")
        else:
            print("The high score is ", hiscore)    
    else:
        print("Time's up! You got ", score, " points!")

    playAgain = input("Do you want to play again? Please input Y or N.\n")
    if playAgain == "N":
        replay = False
    else:
        replay = True
