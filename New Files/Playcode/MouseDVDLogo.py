import ctypes
import ctypes.wintypes
from time import *

def _position():
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)

def move(x,y):
    posX,posY=_position()
    ctypes.windll.user32.SetCursorPos(posX+x, posY+y)
    sleep(0.020)
distance = 50
currentState = "UL"
FAILSAFE = False
try:
    for x in range(500):
        x, y = _position()
        match currentState:
            case "UL":
                if x==0:
                    currentState="UR"
                elif y==0:
                    currentState="DL"
                else:
                    move(-distance,-distance)
            case "UR":
                if y==0:
                    currentState="DR"
                elif x==1919:
                    currentState="UL"
                else:
                    move(distance,-distance)
            case "DR":
                if x==1919:
                    currentState="DL"
                elif y==1079:
                    currentState="UR"
                else:
                    move(distance,distance)
            case "DL":
                if y==1079:
                    currentState="UL"
                elif x==0:
                    currentState="DR"
                else:
                    move(-distance,distance)
            case _:
                pass  
except KeyboardInterrupt:
    pass	