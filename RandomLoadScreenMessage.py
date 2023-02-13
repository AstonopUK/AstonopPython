import json
import requests
import os
import random

response1 = requests.get("https://raw.githubusercontent.com/AstonopUK/EnglishDictionaryVerbing/main/verbs.json")
verbs = list(json.loads(response1.text))
response2 = requests.get("https://raw.githubusercontent.com/AstonopUK/EnglishDictionaryVerbing/main/nouns.json")
nouns = list(json.loads(response2.text))
gotNoun = False
exitBool = False

while exitBool != True:
    print("\n" * 100)
    finalString = ""
    finalString += verbs[random.randint(1, len(verbs))].capitalize() + " the "

    nounTest = nouns[random.randint(1, len(nouns))]
    if nounTest[len(nounTest)-1:len(nounTest)] == "s":
        finalString += nounTest + "..."
    else:
        finalString += nounTest + "s ..."

    print(finalString)
    
    exitTest = input()
    if exitTest == "exit" or exitTest == "close" or exitTest == "n":
        exitBool = True
