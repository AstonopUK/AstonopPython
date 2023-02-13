import json
import requests
import os

response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
todos = list(json.loads(response.text))

print("\n" * 100)

with open('verbs.txt', 'w') as y:
    for x in range(len(todos)):
        if todos[x][(len(todos[x]) - 3):(len(todos[x]))] == "ing":
            #print('"' + todos[x] + '"\: 1,')
            y.write('"' + todos[x] + '"\: 1,\n')
