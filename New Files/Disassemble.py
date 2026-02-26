import dis

def exampleAdd():
    a = 7
    b = 12
    if a > b:
        print(True)
    elif b > a:
        print(False)

def numberAdd(a,b):
    totalNum = 0
    totalNum = a + b
    return totalNum

number1 = int(input("Input a number: "))
breakpoint()
number2 = int(input("Input a number: "))
breakpoint()

print("Your result is " + str(numberAdd(number1, number2)))
dis.dis(exampleAdd)