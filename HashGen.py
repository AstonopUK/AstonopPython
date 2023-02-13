import uuid
import base64

print(int.from_bytes(base64.b64decode(b'AAAAAAAAAAAAAAAAAAAAeg=='), byteorder='big'))

unhashedFile = open("C:\\Users\\ben_h\\OneDrive\\Desktop\\Python\\UnhashedFile.txt", "w")

macAddress = uuid.getnode()
chrList = []

hashChoice = input("Enter (H) for hash, (U) for unhash.\n")
if hashChoice == "H":
    hashInput = input("Enter the phrase you are looking to hash.\n")
    for char in hashInput:
        chrList.append(base64.b64encode((ord(char) * macAddress).to_bytes(16, byteorder='big')))
    output = ""
    for element in chrList:
        output += (str(element) + " ")
    print(output)

elif hashChoice == "U":
    hashInput = input("Enter the hash you are looking to decode.\n")
    iterator = 0
    output = ""
    previousLetter = 0
    
    for char in hashInput:
        iterator += 1
        if char == ' ':
            output += chr(int.from_bytes(base64.b64decode(hashInput[previousLetter: -(len(hashInput) - iterator)]), byteorder='big'))
            previousLetter = iterator

    print(output)
