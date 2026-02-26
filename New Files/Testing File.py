import random
print("\033[1;31;40m Red")
colourList = ["\033[1;30;40m","\033[1;31;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m","\033[1;37;40m"]
for x in range(100):
    outputString = ""
    for x in range(100):
        outputString+=(colourList[random.randint(0,6)] + str(random.randint(0,1)))
    print(outputString)
