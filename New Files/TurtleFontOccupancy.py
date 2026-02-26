import os
from PIL import Image
from PIL import ImageColor
from tkinter import Tk
from tkinter.filedialog import askdirectory

gridSize = 64*64
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
occupancy = []
#print(ImageColor.getcolor('white', 'RGBA'))
filepath = askdirectory()

for z in range(26):
    letterpath = filepath + "/" + alphabet[z] + ".png"
    userImg = Image.open(letterpath)
    imgWidth, imgHeight = userImg.size

    #print(letterpath)
    
    appList = [alphabet[z],0,0]
    #if type(userImg.getpixel((0,0))) == int:
    if True:
        for x in range(imgWidth):
            for y in range(imgHeight):
                #print(userImg.getpixel((x,y)))
                if userImg.getpixel((x, y)) == (0,0,0,255):  
                    appList[1]+=1
    appList[2]=(appList[1]/gridSize)*100
    occupancy.append(appList)

maxOcc = 0
for y in range(len(occupancy)):
    if occupancy[y][2] > occupancy[maxOcc][2]:
        maxOcc = y
minOcc = 0
for z in range(len(occupancy)):
    if occupancy[z][2] < occupancy[minOcc][2]:
        minOcc = z
        #print(occupancy[y][2])
print("The largest letter in the font is", occupancy[maxOcc][0])
print("The smallest letter in the font is", occupancy[minOcc][0])