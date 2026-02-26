repeat = ""
while repeat != "N":
    loops = int(input("How many loops? "))

    for x in range(loops):
        print(loops-x)
    print("BLAST OFF!")
    
    repeat = input("Do you want to go again? Y/N ")