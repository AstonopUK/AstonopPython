import time

print("\n" * 100)
file = open("Higuyfile.txt","r")
script = file.read()
file.close()

sleeper = 1
for x in range(len(script)):
    print(script[x])
    time.sleep(sleeper)
    sleeper -= 0.01
    if sleeper < 0.02:
        sleeper = 0.02
