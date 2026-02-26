import time
import math

timerLength = int(input("How long do you want your timer to be in seconds? "))
timeStart = math.trunc(time.time())
timeEnd = True

while timeEnd:
    if (math.trunc(time.time()) - timeStart) > timerLength and timeEnd == True:
        timeEnd = False
        
print("Timer up!")