import ctypes
import ctypes.wintypes
import random
import time

def _position():
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)

while True:
    x=0
    y=0
    x,y=_position()
    x+=random.randint(-10,10)
    y+=random.randint(-10,10)
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.001)