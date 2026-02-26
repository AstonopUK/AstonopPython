#importing files
import random

#initialising variables
playing = True
dice = [0,0,0,0,0]
turns = 3

#instantiating game loop
print("Welcome to Yacht Dice!")
while playing == True:
    #rerolling dice
    for x in range(len(dice)):
        dice[x-1] = random.randint(1,7)
    while turns > 0:
        print(dice)
        choice = input("Type the numbers of the dice you wish to reroll. Type 0 if you do not want to reroll.")
        for y in range(len(choice)):
            match choice[y-1]:
                case 1:
                    return
                case _: