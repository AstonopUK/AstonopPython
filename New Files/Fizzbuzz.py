inpnum = int(input("Input number range: "))

for x in range(inpnum):
    if (x+1)%5 == 0 and (x+1)%3 == 0:
        print("Fizzbuzz")
    elif (x+1)%5 == 0 and not (x+1)%3 == 0:
        print("Buzz")
    elif not (x+1)%5 == 0 and (x+1)%3 == 0:
        print("Fizz")
    elif not (x+1)%5 == 0 and not (x+1)%3 == 0:
        print((x+1))
