def vendOutput(uInput):
    match uInput:
        case 1:
            return "Lemon Soda"
        case 2:
            return "Coca Cola"
        case 3:
            return "Schwepps"
        case 4:
            return "Beef Juice"
        case 5:
            return "Tomato Soup"
        case 6:
            return "Water"
        case 7:
            return "Guava and Lychee Presse"
        case 8:
            return "Goulash with Czpitke"
        case 9:
            return "Dr Pepper"
        case 10:
            return "Kool Aid Baja Blast"
        case _:
            return "Error"

selectChoice = ""
print("#" * 50)

while selectChoice != "Y":
    userInput = int(input("INPUT YOUR NUMBER:\n"))
    selectChoice = input("ARE YOU HAPPY WITH YOUR NUMBER? (Y) OR (N).\n")

if userInput > 10 or userInput < 1:
    print("ERROR! YOUR NUMBER IS OUTSIDE THE RANGE!")
else:
    print(("-" * 30) + "\nYOU HAVE PURCHASED THE\n" + vendOutput(userInput) + "\nTHANK YOU FOR YOUR PATRONAGE\n" + ("-" * 30))

print("#" * 50)
