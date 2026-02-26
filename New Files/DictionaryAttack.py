import time

print("\n" * 100)
bruteDictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890\|,<.>/?;:'@#~[{]}`¬!£$%^&*()-_=+"

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

bruteForce()
