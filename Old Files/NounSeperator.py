import json
import requests
import os

response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
todos = list(json.loads(response.text))

print("\n" * 100)

with open('nouns.txt', 'w') as y:
    y.write('{')
    for x in range(len(todos)):
        if todos[x][(len(todos[x]) - 3):(len(todos[x]))] != "ing" and todos[x][(len(todos[x]) - 2):(len(todos[x]))] != "ed" and len(todos[x]) > 3:
            #print('"' + todos[x] + '"\: 1,')
            y.write('\t"' + todos[x] + '": 1,\n')
    y.write('}')
