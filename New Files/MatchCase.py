room = input("Where do you want to go?")

match room:
    case "Kitchen":
        print("You're in the kitchen.")
    case "Bedroom":
        print("You see a bed.")
    case _:
        pass