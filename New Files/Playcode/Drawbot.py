#Drawbot
import ctypes
from ctypes import wintypes
from time import *
from os import *

def _moveClick(step,loop1,loop2,array,repeatNum):
    global x
    global y
    
    if array[(loop1*repeatNum)+loop2] == 1:
        ctypes.windll.user32.mouse_event(2,0,0,0,0)
        ctypes.windll.user32.mouse_event(4,0,0,0,0)
    x+=step
    ctypes.windll.user32.SetCursorPos(x, y)
    
def _position():
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)
    
startfile("C:\\Users\\b.hopgood\\AppData\\Local\\Microsoft\\WindowsApps\\Microsoft.Paint_8wekyb3d8bbwe\\pbrush.exe")
sleep(3)

drawGrid = [0,1,1,0,0,0,0,1,1,0,
            0,1,1,0,0,0,0,1,1,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            1,0,0,0,0,0,0,0,0,1,
            0,1,0,0,0,0,0,0,1,0,
            0,0,1,1,1,1,1,1,0,0]

repeatNum = 10
stepCount = 10

ctypes.windll.user32.SetCursorPos(int((ctypes.windll.user32.GetSystemMetrics(0)/2)-((round(repeatNum/2,0))*stepCount)),
                                  int((ctypes.windll.user32.GetSystemMetrics(1)/2)-((round(repeatNum/2,0))*stepCount)))

x,y = _position()

for z in range(repeatNum):
    for a in range(repeatNum):
        _moveClick(stepCount,z,a,drawGrid,repeatNum)
    x-=(repeatNum*stepCount)
    y+=stepCount
    ctypes.windll.user32.SetCursorPos(x, y)
quit()