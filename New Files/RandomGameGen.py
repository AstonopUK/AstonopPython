from time import sleep
from random import randint

games = ["Anagrams","Scrabble","Boggle","Crossword","Noughts and Crosses",
         "I Spy","Wordle","Spelling Bee","Hangman","Yacht Dice","Blackjack",
         "Battleships","Mastermind","Hungry Hippos","Chess"]
connectors = ["with","without"]
modifiers = ["double the players","betting","maths","numbers","cards","an open world",
             "levels","idle game mechanics","explosives","high stakes","FPS mechanics",
             "merging","turn-based combat","combat system","enemies","abilities/classes"]

while True:
    input("Press enter to spin the wheel of random games!")
    output = ""

    for x in range(30):
        print("\n"*100)
        print(games[randint(0,len(games)-1)]+" "+connectors[randint(0,len(connectors)-1)]+" "+modifiers[randint(0,len(modifiers)-1)])
        sleep(0.03)
    output+=games[randint(0,len(games)-1)]+" "
    for x in range(30):
        print("\n"*100)
        print(output,connectors[randint(0,len(connectors)-1)]+" "+modifiers[randint(0,len(modifiers)-1)])
        sleep(0.03)
    output+=connectors[randint(0,len(connectors)-1)]+" "
    for x in range(30):
        print("\n"*100)
        print(output,modifiers[randint(0,len(modifiers)-1)])
        sleep(0.03)
    output+=modifiers[randint(0,len(modifiers)-1)]
    
    print("\n"*100)
    print(output)
    