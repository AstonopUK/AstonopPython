import keyboard
import time
import turtle

screen = turtle.Screen()
turtle.speed(0)

#cMode = input("Choose input mode: (Rotational) (Ordinal) ")
cMode = "Ordinal"
if cMode == "Rotational":
    while True:
        moveVec = [0.0, 0.0]
        try:
            if keyboard.is_pressed('a'):
                moveVec[0]-=7.0
                time.sleep(0.001)
            if keyboard.is_pressed('d'):
                moveVec[0]+=7.0
                time.sleep(0.001)
            if keyboard.is_pressed('w'):
                moveVec[1]+=5.0
                time.sleep(0.005)
            if keyboard.is_pressed('s'):
                moveVec[1]-=5.0
                time.sleep(0.005)
            if keyboard.is_pressed('Esc'):
                exit()
            posList = list(turtle.pos())
            #+-400 y, +-470 x
            turtle.right(moveVec[0])
            turtle.forward(moveVec[1])
        except:
            break
elif cMode == "Ordinal":
    while True:
        try:
            if keyboard.is_pressed('a'):
                turtle.setheading(180)
                turtle.forward(5)
                time.sleep(0.005)
            if keyboard.is_pressed('d'):
                turtle.setheading(0)
                turtle.forward(5)
                time.sleep(0.005)
            if keyboard.is_pressed('w'):
                turtle.setheading(90)
                turtle.forward(5)
                time.sleep(0.005)
            if keyboard.is_pressed('s'):
                turtle.setheading(270)
                turtle.forward(5)
                time.sleep(0.005)
        except:
            break
