import turtle as t
import random

colours = ["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
randnum = random.randint(1,359)
print(randnum)
t.left(randnum)
t.width(8)
t.speed(0)
t.bgcolor("black")
t.color("#A9A9A9")
x=0

while True:
    t.forward(10)
    if t.xcor()>474 or t.xcor()<-474:
        x = 180 - t.heading()
        if x < 0:
            x += 360
        t.left(x - t.heading())
        color = "#"
        for z in range(6):
            color += colours[random.randint(0,len(colours)-1)]
        t.color(color)

    if t.ycor()>395 or t.ycor()<-395:
        y = 360 - t.heading()
        if y < 0:
            y += 360
        t.left(y - t.heading())
        color = "#"
        for z in range(6):
            color += colours[random.randint(0,len(colours)-1)]
        t.color(color)
