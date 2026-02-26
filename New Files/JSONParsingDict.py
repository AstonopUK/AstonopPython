import json, random

json_file = 'dictionary.json'

with open(json_file) as json_data:
    data = json.load(json_data)

word = ""
while len(word)<3 or len(word)>7:
    word = random.choice(list(data.keys()))
print(word)
#print(data[word])
wordList = list(word)

newWord = ""
while len(wordList)>0:
    newWord+=wordList.pop(random.randint(0, len(wordList)-1))
    
print(newWord)
lives = 3
won = False
while lives!=0:
    print("You have",lives,"lives left.")
    guess = input("Guess the word: ")
    if guess.upper() == word:
        won = True
        lives = 0
    else:
        print("Incorrect!")
        lives-=1
        
if won == True:
    print("Correct - you win!")
else:
    print("Out of lives - you lose!")