import random

def GameLoop():
    gameSize = int(input("Input the largest number you want the game to be able to generate.\n"))
    targetNum = random.randrange(0, gameSize)
    playerGuess = 0
    numOfTurns = 0
    while playerGuess != targetNum:
        playerGuess = int(input("Input your guess!\n"))
        if playerGuess > targetNum:
            if (playerGuess - (gameSize * 0.01)) < targetNum:
                print("You're close!\n")
            print("Too high!\n")
            numOfTurns+=1
        elif playerGuess < targetNum:
            if (playerGuess + (gameSize * 0.01)) > targetNum:
                print("You're close!\n")
            print("Too low!\n")
            numOfTurns+=1
        elif playerGuess == targetNum:
            print("You got it! The number was", str(targetNum) + ".\n It took you", str(numOfTurns) + " turns.\n")

decision = ""
while decision.upper() != "N":
    print("\n" * 100)
    GameLoop()
    decision = input("Want to play again? Y or N.\n")

