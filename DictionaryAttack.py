import enchant
import json
import requests
import time

print("\n" * 100)
dictionary= enchant.Dict("en_UK")
response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
todos = list(json.loads(response.text))
repeatBool = ""
printPass = ""
attackType = ""
bruteDictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890\|,<.>/?;:'@#~[{]}`¬!£$%^&*()-_=+"

def dictionaryAttack():
    password = input("Input your password: ")
    printPass = input("Do you want to print each password guessed? (y) or (n): ")
    iterator = 0

    timeBefore = time.perf_counter()
    if dictionary.check(password) == False:
        print("\nWord is not in the dictionary.")
    else:    
        for item in todos:
            iterator += 1
            if printPass == "y" or printPass == "Y":
                print("Testing " + item + "...")
            if item == password or item.capitalize() == password:
                print("Your password is " + item)
                timeAfter = time.perf_counter()
                print("\nIt took " + str(timeAfter-timeBefore) + " seconds to crack the password.")
                break

def bruteForce():
    password = input("Input your password: ")
    printPass = input("Do you want to print each password guessed? (y) or (n): ")
    iterator = 0
    guessedPassList = [""]
    guessedPass = ""

    timeBefore = time.perf_counter()
    while guessedPass.join(guessedPassList) != password:
        for char in range(len(password)):
            for test in range(len(bruteDictionary)):
                if printPass == "y" or printPass == "Y":
                    print("Testing " + bruteDictionary[test] + " at position " + str(char) + "...")
                if bruteDictionary[test] == password[char]:
                    guessedPassList.append(bruteDictionary[test])
                    
    print("\nThe password was " + guessedPass.join(guessedPassList))
    timeAfter = time.perf_counter()
    print("\nIt took " + str(timeAfter-timeBefore) + " seconds to crack the password.")

while repeatBool != "n":
    attackType = input("\nWhich attack would you like demonstrated; brute force or dictionary? (b) or (d): ")
    if attackType == "b":
        bruteForce()
    elif attackType == "d":
        dictionaryAttack()
    else:
        print("\nPlease input either (b) or (d).")

    repeatBool = input("Do you want to try another password? (y) or (n).\n")
