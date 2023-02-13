#py -m pip install requests

import json
import requests
import random

print("\n" * 100)
response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
todos = list(json.loads(response.text))

playAgain = ""
print("Welcome to Hangman!\n")

while playAgain.lower() != "n":
    validWord = False
    while validWord == False:    
        randint = random.randrange(1, 370101)
        if len(todos[randint]) >= 4 and len(todos[randint]) <= 9:
            validWord = True
            
    targetWordString = todos[randint]
    targetWord = []
    guessedWord = []
    guessedLetters = []
    for char in range(len(todos[randint])):
        targetWord.append((todos[randint])[char])
        #print((todos[randint])[char])
        guessedWord.append("_")
        guessedWord.append(" ")
    isGuessed = False
    numTurnsLeft = 5 + (len(todos[randint]))//2
    print("\n")

    outputWord = ""
    for y in range(len(guessedWord)):
        outputWord += guessedWord[y]
    print(outputWord, "\n")


    while isGuessed == False:
        print("You have", numTurnsLeft, "turns remaining.\n")
        userChoice = input("Guess a (l)etter or a (w)hole word?\n")
        if userChoice == "l":
            outputWord = ""
            letterGuess = input("\nInput your letter to guess.\n")
            guessedLetters.append(letterGuess)
            for x in range(len(targetWord)):
                if targetWord[x] == letterGuess:
                    guessedWord[x*2] = targetWord[x]

            print("\n" * 100)
            for y in range(len(guessedWord)):
                outputWord += guessedWord[y]
            print("\n", outputWord, "\n")
            outputWord = ""
            for z in range(len(guessedLetters)):
                outputWord += guessedLetters[z] + "   "
            print("You have guessed:", outputWord, "\n")
            numTurnsLeft -= 1
        elif userChoice == "w":
            wordGuess = input("Input your guess for what the word is in lower case!\n")
            if wordGuess.lower() == targetWordString:
                print("Congratulations! You guessed the word correctly!\n")
                isGuessed = True
            else:
                print("Sorry, that wasn't it! You lose!\nThe word was", targetWordString)
                isGuessed = True
        else:
            print("Please input either (l) or (w).\n")

        if numTurnsLeft == 0:
            print("You ran out of turns! You lose!\nThe word was", targetWordString)      
            isGuessed = True

    playAgain = input("\n\nDo you want to play again? (y) or (n)\n")
    if playAgain == "y":
        print("\n" * 100)
