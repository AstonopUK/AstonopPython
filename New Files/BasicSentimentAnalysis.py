hnWeight = ["hate", "awful", "worst", "terrible", "catastrophic", "idiot", "sucks", "sucked"]
lnWeight = ["bad", "lame", "yuck", "gross", "grim", "boring", "dull", "nerd", "geek", "negative"]
lpWeight = ["good", "happy", "fab", "lovely", "positive"]
hpWeight = ["wicked", "amazing", "brilliant", "fantastic", "exceptional", "majestic", "wonderful"]
messageWords = []
weighting = 0
exceptList = [" ", ".", ",", "'", "!", "?"]
word = ""

print("Enter the user's message: ")
message = input()

for char in range(len(message)):
    if message[char] not in exceptList:
        word+=message[char]
    else:
        messageWords.append(word)
        word = ""
messageWords.append(word)

for words in messageWords:
    if words.lower() in hnWeight:
        weighting-=3
    if words.lower() in lnWeight:
        weighting-=1
    if words.lower() in lpWeight:
        weighting+=1
    if words.lower() in hpWeight:
        weighting+=3

if weighting>0:
    print("Positive message! Sending...")
else:
    print("Bad message! Blocking!")