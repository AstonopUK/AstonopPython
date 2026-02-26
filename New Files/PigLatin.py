messageWords = []
messagePigged = []
exceptList = [" ", ".", ",", "'", "!", "?"]
vowels = ["a","e","i","o","u"]
word = ""
output = ""

print("Enter the user's message: ")
message = input()

for char in range(len(message)):
    if message[char] not in exceptList:
        word+=message[char]
    else:
        if word!="":
            messageWords.append(word)
            word = ""
            
messageWords.append(word)

firstWord = True
for words in messageWords:
    if words[0] not in vowels:
        newword = ""
        newword = words[1:len(words)] + words[0] + "ay"
        if firstWord==True:
            output+=newword.capitalize() + " "
            firstWord = False
        else:
            output+=newword.lower() + " "
    else:
        output+=words+"ay "
    
print(output)