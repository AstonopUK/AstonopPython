import time
import sys
import random
import webbrowser

answer=""
lives = 3
questions_answered = 0
secretcode = ""

questions = ["Question 1: What is the name of the translator that translates line by line?\n",
             "Question 2: What is the name of software specifically designed for a single client?\n",
             "Question 3: True or false - an assembler is the same type of translator as a compiler or interpreter.\n",
             "Question 4: How many times does a compiler need to do its job?\n1:Only once.\n2:Every time the user wants an executable version of the code.\n3:Every single new line that is added to the code.\n",
             "Question 5: What piece of software does a computer need to be able to interact with a new peripheral?\n",
             "Question 6: Which system utility is responsible for preventing malware from entering your file system before damage can be done?\n",
             "Question 7: Is ROM primary or secondary storage?\n",
             "Question 8: Would a system that has very limited resources use a RISC or CISC instruction set?\n",
             "Question 9: Identify which of the following is not a real logic gate: NOR NANT XOR OR AND NAND NOT\n",
             "Question 10: What is the airspeed velocity of an unladen swallow?\n"]

answers = [["interpreter","interpreter translator"], ["bespoke","bespoke software"], ["false","f"], ["2","two"], ["driver","driver software"], ["firewall","fire wall"], ["primary", "primary storage"], ["risc","risc set","risc instruction set"], ["nant"], ["african or european","african or european?"]]
deaths = ["You were crushed by a comically large boulder.",
          "You fell from a great height and splatted on the ground like raspberry jam.",
          "You ate a berry that made you hallucinate that you were god. You weren't, and perished.",
          "You fought a chicken in a mtch of bare-knuckle boxing. The chicken won.",
          "You ran too fast, fell over and ended up evaporating from the friction.",
          "You had one too many iron supplements and ended up becoming a lightning rod.",
          "You died to a spoon that had a bit too much ice cream on it. Seriously, you froze.",
          "You scrambled some eggs - they didn't appreciate it, and scrambled you back.",
          "You walked through a changinator and your bones randomised location in your body. Your hip bone is now your finger bone.",
          "You tried to sit down on a chair, but ended up falling through it into the afterlife.",
          "You took too deep of a breath in and popped.",
          "You succumbed to gravity and became a version of you that looks too much like an accordian.",
          "You instantaneously, spontaneously combusted and vanished simultaneously.",
          "You were abducted by aliens, who were then abducted by bigger aliens, who were then abducted by bigger aliens, who were then...",
          "You tied your shoelaces too tight and ended up having a heart attack due to poor blood circulation.",
          "You lost a game of Texas Hold Em to a toddler, who took your life as forfeit."]

def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.035)
    time.sleep(1)
        
delay_print("Welcome to the Very Easy (TM) Computer Systems Quiz!\n")
delay_print("In this quiz, you will be asked a number of questions. If you answer one incorrectly, you will lose a life!\n")
delay_print("You have three lives. Lose all three... and it's game over, man.\n")

while answer!="Y" and answer!="y":
    delay_print("Ready to start? Y or N.\n")
    answer=input()
    if answer.lower()=="n":
        delay_print("C'mon man, you're wasting my time here.\n")
    elif len(answer) == 1:
        if answer!="Y" and answer!="y":
            secretcode+=answer
            delay_print("Secret character entered.\n")
        if secretcode=="secret":
            webbrowser.open("https://pastebin.com/raw/yRT0CTBD")
    elif answer.lower() == "clear":
        delay_print("Secret code flushed.\n")
        secretcode=""

secretcode=""
delay_print("Good! Let's begin.\n")
time.sleep(2)

while lives>0 and questions_answered<10:
    print("\n"*100)
    delay_print("You have " + str(lives) + " lives left.\n")
    delay_print(questions[questions_answered])
    answer = str(input())
    if answer.lower() in answers[questions_answered]:
        if questions_answered != 9:
            delay_print("Well done! Moving on...\n")
            questions_answered+=1
        else:
            delay_print("I don't know! Wait...\n")
            time.sleep(1)
            delay_print("A\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\nH\n!")
            questions_answered+=1
    elif answer.lower() == "chief beef":
        webbrowser.open("https://pbs.twimg.com/media/CqIhEbdWEAATZ0H.jpg")
    elif answer.lower() == "literally who asked":
        delay_print("Ah. I see how it is. Cheater.\n")
        questions_answered=9
        lives = 99999
    else:
        delay_print("Oops. Not quite right.\n")
        lives-=1
    
print("\n"*100)
time.sleep(2)
if lives>0:
    delay_print("Congratulations! You made it through alive. See you for the next quiz sometime!\n")
else:
    delay_print(deaths[random.randint(0, len(deaths)-1)])