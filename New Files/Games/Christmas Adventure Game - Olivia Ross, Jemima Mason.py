print("Welcome to the Christmas adventure!")
child_name = input("Please,enter the child's name: ")

def introduce_child():
    print("Hello, " + child_name + "! Let's start our Christmas journey.")

def put_up_tree(child_name):
    print("Quest: Put up Christmas tree in the SITTING ROOM or OUTSIDE.")
    print("As " + child_name + " runs to the christmas store.")
    print(child_name + " buys the tree and takes it home.")
    treeLoop = True
    while treeLoop != False:
        print("Where do you want to put the tree")
        room = input()
        if room == ("sitting room"):
            print(child_name + " successfully puts up the Christmas tree in the sitting room.")
            print("Well done!")
            treeLoop = False
        if room == ("outside"):
            print(child_name + " successfully puts up the Christmas outside.")
            print("Well done!")
            treeLoop = False
        else:
            print("It's not going to fit there")
            print("Try again" + child_name)

def decorate_tree(child_name):
    print("Quest: Decorate the Christmas tree in the sitting room")
    print("Do you want bows or ballballs?")
    if input() == ("Bows"):
        print("Good idea! Let's do it")
    else:
        print("This will look so good. Good choice.:)")
    print(child_name + " decorates the Christmas tree. Its so pretty.")

def open_advent_calendar(child_name):
    print("Quest: Open the advent calendar in the dining room.")
    print(child_name + " finds a delightful chocolate surprise in the advent calendar.")

def make_christmas_list(child_name):
    print("Quest: Make a Christmas list in the bedroom.")
    print(child_name + " creates a long list of wishes for Christmas.")

def make_wreath(child_name):
    print("Quest: Make a wreath on the front porch.")
    print(child_name + " crafts a beautiful Christmas wreath.")

def find_elf_on_the_shelf(child_name):
    print("Quest: Find the elf on the shelf.Is it in the kitchen.")
    print("do you want to check the kitchen or the pantry")
    kitchenLoop = True
    while kitchenLoop != False:
        if input() == ("kitchen"):
            print("well done! You found the elf.")
            print("You discovered the mischievous elf cutting vegetables for Christmas day.")
            kitchenLoop = False
        else:
            print("Nice try. But the elf isnt here.")

def make_christmas_cookies(child_name):
    print("Quest: Make Christmas cookies in the kitchen.")
    print(child_name + " bakes delicious Christmas cookies.")

def put_out_cookies_and_port(child_name):
    print("Do you want to give santa port or milk?")
    drinkLoop = True
    while drinkLoop!= False:
        if input() == ("Port"):
            print("Santa will thank you")
            drinkLoop = False
    else:
        print("I don't think Santa wants that")
    print(child_name + " puts out cookies, port, and carrots in the sitting room.")

def go_to_sleep(child_name):
    print("It's Christmas Eve! Time for " + child_name + " to go to sleep in the bedroom.")
    print(child_name + " falls asleep with excitement for Christmas morning.")

def ending(child_name):
    print("It's Christmas morning!")
    print("Santa has left a letter for " + child_name + " saying thanks for the treats.")
    print("Merry Christmas!")
    print("Happy New Year")

# Main program
introduce_child()

put_up_tree(child_name)
decorate_tree(child_name)
open_advent_calendar(child_name)
make_christmas_list(child_name)
make_wreath(child_name)
find_elf_on_the_shelf(child_name)
make_christmas_cookies(child_name)
put_out_cookies_and_port(child_name)
go_to_sleep(child_name)
ending(child_name)
