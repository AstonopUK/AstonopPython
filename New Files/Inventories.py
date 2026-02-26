inventory = []
interactables = []
roomItems = [["Dog", "Lighter"],["Cat"],["Beans"]]

def interact(inpstring):
    if inpstring in interactables:
        inventory.append(inpstring)
        print("You picked up the", inpstring)
        interactables.remove(inpstring)
    else:
        print("No such item!")
    
#inventory.append("Axe")
answer = input("There is a tree. Do you want to cut it down? ")
if answer == "Yes":
    if "Axe" in inventory:
        print("You chopped down the tree!")
        inventory.remove("Axe")
        inventory.append("Tree")
    else:
        print("You don't have an axe for this!")
        
for item in interactables:
    interactables.remove(item)
    
#Enter room
for item in roomItems[1]:
    interactables.append(item)

interact(input("What do you want to interact with?"))