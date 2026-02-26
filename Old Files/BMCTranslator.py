#‾|_

inputBit = input("Input your string of bits.\n")
previousBit = "2"
outputString = ""
doubleZero = False
bit = 0

for bit in range(len(inputBit)+1):
    if inputBit[bit-1] == "0":
        if previousBit == "2":
            outputString += ("|_ _")
            
        elif previousBit == "1":
            if doubleZero == True:
                outputString += ("|_ _")
                doubleZero = False
            elif doubleZero == False:
                outputString += ("|‾ ‾")
                doubleZero = True
                
        elif previousBit == "0":
            if doubleZero == True:
                outputString += ("|_ _")
                doubleZero = False
            elif doubleZero == False:
                outputString += ("|‾ ‾")
                doubleZero = True
                
        previousBit = inputBit[bit-1]

    if inputBit[bit-1] == "1":
        if previousBit == "0":
            
            if doubleZero == True:
                outputString += ("|_|‾")
            elif doubleZero == False:
                outputString += ("|‾|_")
                
        elif previousBit == "1":
            if doubleZero == True:
                outputString += ("|_|‾")
            elif doubleZero == False:
                outputString += ("|‾|_")
                
        elif previousBit == "2":
            outputString += ("|‾|_")
            
        previousBit = inputBit[bit-1]

print(outputString)
