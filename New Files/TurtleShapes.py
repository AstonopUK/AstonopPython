import turtle
import random

colours = [red,blue,green,orange,yellow,purple]

def triangle(length):
    for count in range(3):
        turtle.forward(length)
        turtle.left(120)
        
def square(length):
    for count in range(4):
        turtle.forward(length)
        turtle.left(90)

def pentagon(length):
    
    
def hexagon(length):
    

def heptagon(length):
    
    

turtle.color("blue")
turtle.width(10)


triangle(90)
square(90)
pentagon(90)
hexagon(90)
heptagon(90)

for x in range(12):
    for x in range(colours):
        turtle.color = colours[x]
        turtle.forward(5)
        turtle.left(5)
