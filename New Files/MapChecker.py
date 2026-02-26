import pygame
from pygame.locals import *

map = [[1,1,1,1,1,1,1],
       [1,0,0,0,0,0,1],
       [1,0,1,1,1,0,1],
       [1,0,1,0,1,0,1],
       [1,0,1,8,1,0,1],
       [1,0,1,0,1,0,1],
       [1,0,0,0,0,0,1],
       [1,1,1,1,1,1,1]]

playerLoc = [3,3]
while True:
    print("\n"*100)
    for x in range(8):
        outputText = ""
        for y in range(7):
            match map[x][y]:
                case 0:
                    outputText+="  "
                    pass
                case 1:
                    outputText+="# "
                    pass
                case 8:
                    outputText+="@ "
                    pass
                case _:
                    pass
        print(outputText)
    #direction = input("Pick a direction (u/d/l/r)")
        
    direction = ""
    for event in pygame.event.get():
        if (event.type == KEYLEFT):
            direction = "l"
        elif (event.type == KEYRIGHT):
            direction = "r"
        elif (event.type == KEYUP):
            direction = "u"
        elif (event.type == KEYDOWN):
            direction = "d"
        
    match direction:
        case "l":
            if map[playerLoc[0]][playerLoc[1]-1] == 1:
                print("Direction blocked")
            else:
                map[playerLoc[0]][playerLoc[1]] = 0
                playerLoc = [playerLoc[0], playerLoc[1]-1]
                map[playerLoc[0]][playerLoc[1]] = 8
                print("Moved to", playerLoc[0], playerLoc[1])
            pass
        case "r":
            if map[playerLoc[0]][playerLoc[1]+1] == 1:
                print("Direction blocked")
            else:
                map[playerLoc[0]][playerLoc[1]] = 0
                playerLoc = [playerLoc[0], playerLoc[1]+1]
                map[playerLoc[0]][playerLoc[1]] = 8
                print("Moved to", playerLoc[0], playerLoc[1])
            pass
        case "u":
            if map[playerLoc[0]-1][playerLoc[1]] == 1:
                print("Direction blocked")
            else:
                map[playerLoc[0]][playerLoc[1]] = 0
                playerLoc = [playerLoc[0]-1, playerLoc[1]]
                map[playerLoc[0]][playerLoc[1]] = 8
                print("Moved to", playerLoc[0], playerLoc[1])
            pass
        case "d":
            if map[playerLoc[0]+1][playerLoc[1]] == 1:
                print("Direction blocked")
            else:
                map[playerLoc[0]][playerLoc[1]] = 0
                playerLoc = [playerLoc[0]+1, playerLoc[1]]
                map[playerLoc[0]][playerLoc[1]] = 8
                print("Moved to", playerLoc[0], playerLoc[1])
            pass
        case _:
            pass
    
