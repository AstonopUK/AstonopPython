def theSearcher(inputNum):
    iterator = 0
    isSolved = False
    isEven = False
    while isSolved == False:
        if int(inputNum) == int(iterator):
            print("Match! It's " + str(iterator) + "!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == '0':
                isEven = True
                isSolved = True
                print("It ends in 0!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "1":
                isEven = False
                isSolved = True
                print("It ends in 1!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "2":
                isEven = True
                isSolved = True
                print("It ends in 2!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "3":
                isEven = False
                isSolved = True
                print("It ends in 3!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "4":
                isEven = True
                isSolved = True
                print("It ends in 4!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "5":
                isEven = False
                isSolved = True
                print("It ends in 5!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "6":
                isEven = True
                isSolved = True
                print("It ends in 6!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "7":
                isEven = False
                isSolved = True
                print("It ends in 7!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "8":
                isEven = True
                isSolved = True
                print("It ends in 8!")
            if str(iterator)[len(str(iterator))-1:len(str(iterator))] == "9":
                isEven = False
                isSolved = True
                print("It ends in 9!")
        else:
            print("Your number isn't " + str(iterator) + "!")
            
        iterator += 1
		
    if isEven == True:
        print("It's even!")
        print("Wasn't that easy?")
        return
    elif isEven == False:	
        print("It's odd!")
        print("Wasn't that easy?")
        return

intInput = input("Please input your number below!:\n")
theSearcher(intInput)
