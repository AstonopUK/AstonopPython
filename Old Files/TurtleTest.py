import turtle
import os
from PIL import Image
from PIL import ImageColor
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print(ImageColor.getcolor('white', 'RGBA'))
tp = turtle.Pen()

Tk().withdraw()
filepath = askopenfilename(filetypes=[("Image files", "*.png"), ("All Files", "*.*")])
userImg = Image.open(filepath)
imgWidth, imgHeight = userImg.size
tp.screen.screensize(imgWidth, imgHeight)
tp.screen.setworldcoordinates(imgWidth, imgHeight, 0, 0)
tp.screen.bgcolor("black")

print(filepath)

if type(userImg.getpixel((0,0))) == int:
    tp.pencolor("white")
    tp.fillcolor("white")
    tp.pensize(10)
    tp.width(5)
    tp.speed(25000)
    tp.pu()
    
    for x in range(imgWidth):
        for y in range(imgHeight):
            if userImg.getpixel((x, y)) == 0:              
                tp.pu()
                tp.goto(x, y)
                tp.pd()
                tp.forward(1)
                
else:
    tp.pencolor("white")
    tp.fillcolor("white")
    tp.pensize(1)
    tp.width(1)
    tp.speed(100000)
    tp.pu()
    
    for x in range(imgWidth):
        for y in range(imgHeight):
            if userImg.getpixel((x, y)) <= (150, 150, 150, 255):
                tp.pu()
                tp.goto(x, y)
                tp.pd()
                tp.forward(1)
                tp.pu()
