def PrimeCount():
    target = int(input("Input your target number.\n"))
    currentPrime = 0
    x = 0
    while currentPrime != target:
        x+=1
        if (x>3):
            if (x%2) != 0 and (x%3) != 0 and (x%5) != 0 and (x%7) != 0 and (x%9) != 0:
                currentPrime+=1
        else:
            currentPrime+=1

        if currentPrime == target:
            print("The", str(target) + "th", "prime number is", str(x) + ".\n")
                

def PrimeBetween():
    target = int(input("Input your target number.\n"))
    for x in range(target):
        if (x>3):
            if (x%2) != 0 and (x%3) != 0 and (x%5) != 0 and (x%7) != 0 and (x%9) != 0:
                print(x, "\n")

print("\n" * 100)
mode = input("Which mode would you like? (B)etween or (T)arget?\n")
if mode.upper() == "B":
    PrimeBetween()
elif mode.upper() == "T":
    PrimeCount()
else:
    print("Mode not specified.\n")

input()
