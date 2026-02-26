#Imports libraries needed for the program to run
import turtle
import random
import time

#Create an empty list of horses
t = []
#Create variables to track distance and winner
num = 0
distance = 0
winner = 0
#Set up the screen to display the horses
screen = turtle.Screen()
turtles = 3
screen.bgcolor("limegreen")
lineturtle = turtle.Turtle()

locator = -400
for x in range(5):
    lineturtle.speed(0)
    lineturtle.penup()
    lineturtle.goto(-600, locator)
    lineturtle.pendown()
    lineturtle.forward(1200)
    locator+=200

#For loop for the number of horses in the race
for x in range(turtles):
    #Variable to measure distance between each horse
    num+=20
    #Adds a new turtle instance to the horse list
    t.append(turtle.Turtle())
    #Sets the turtles location for each horse one by one, lining up for the race
    t[x].pu()
    t[x].goto(-120, -275)
    t[x].forward(num)
    t[x].left(90)
    #Changes the pen size
    t[x].pensize(7)
    #Chooses the horse's colour randomly
    t[x].color("#" + str(random.randint(100000,999999)))

#The loop for the duration of the race
for x in range(60):
    #Loop to move each horse forward by a random amount
    for x in range(turtles):
        t[x].shape("turtle")
        time.sleep(0.1)
        t[x].pd()
        #Move the current horse forward by a random amount
        t[x].forward(random.randint(1,15))
        #print((x+1),":",t[x].ycor()) #Debugging code
        #Checks if the current horse is in the front of the pack. If it is, set it as the current winner.
        if t[x].ycor() > distance:
            distance = t[x].ycor()
            winner = x

#Create a turtle to write sentences
t.append(turtle.Turtle())
t[turtles].pu()
#Go to the bottom of the screen
t[turtles].goto(-150, -325)
t[turtles].pd()
#Write who the winner of the race was
t[turtles].write(("Winner: Turtle " + str(winner + 1)), True, "left", ("Arial", 20, "bold"))