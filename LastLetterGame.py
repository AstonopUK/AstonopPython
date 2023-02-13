import random
import time
import json
import requests
import enchant
import os

dictionary = enchant.Dict("en_UK")
response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
todos = list(json.loads(response.text))
playAgain = "y"

while playAgain != "n":
    startTime = 0
    score = 0
    usedWords = []
    print ("\n" * 100)

    currentWord= todos[random.randint(1, len(todos))]
    lastLetter = currentWord[len(currentWord)-1]

    startTime = time.time()

    while (time.time() - startTime) < 45:
        print("Your current score is " + str(score) + "\n")
        print("Your word is " + (currentWord) + ", with your Last Letter being " + lastLetter + ".\n")

        userWord = str(input("Input your word!: "))
        if userWord[0] == lastLetter and dictionary.check(userWord.lower()) == True:
            checkIfUsed = False
            for o in range(len(usedWords)):
                if userWord.lower() == usedWords[o]:
                    checkIfUsed = True
            if checkIfUsed == False:
                print("Well done! You have gained points.\n")
                score = score + (len(userWord)//2)
                currentWord = userWord
                lastLetter = currentWord[len(currentWord)-1]
                usedWords.append(currentWord)
            if checkIfUsed == True:
                print("You used a word you've used before! Points have been subtracted.\n")
                score = score - len(userWord)
            
        else:
            if userWord[0] != lastLetter:
                print("The Last Letter and your first letter do not match!\n")
            if dictionary.check(userWord) != True:
                print("That isn't a real word!\n")

    print ("\n" * 100)
    if score<0:
        print("You got... a negative score of " + str(score) + "? How did you even manage that?")
    else:
        print("Well done! Your final score is " + str(score) + ".")

    playAgain = str(input("Do you want to play again? n for no, y for yes. "))
