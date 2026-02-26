import turtle
import math

#Here is a list of available colours: https://trinket.io/docs/colors
colours = ["white"]
turtle.bgcolor("black")
turtle.speed(0)

for x in range(25000):
    turtle.color(colours[x%1])
    turtle.width(x/100+1)
    turtle.forward(x**0.5)
    turtle.left(math.tau*(x+1*x+1))