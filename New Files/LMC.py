RAM = []
ACC = 0
MDR = ""
MAR = ""
PC = 0
user_inp = ""

while user_inp != "HLT":
    user_inp = input()
    RAM.append(user_inp)

print("\nProgram saved. Executing...\n")

for x in range(len(RAM)-1):
    PC = x
    if len(RAM[PC]) > 3:
        MDR = RAM[PC].upper()[:3]
        MAR = int(RAM[PC].upper()[4:])
        match MDR:
            case "ADD":
                print("Adding contents of address",MAR,"to ACC.")
                ACC += int(RAM[MAR])
            case "SUB":
                print("Subtracting contents of address",MAR,"from ACC.")
                ACC -= int(RAM[MAR])
            case "LDA":
                print("Loading contents of address",MAR,"to ACC.")
                ACC = int(RAM[MAR])
            case _:
                pass
    else:
        MDR = RAM[PC].upper()
        match MDR:
            case "STA":
                RAM.append(ACC)
                print("Stored contents of ACC in memory address",len(RAM)-1)
            case "OUT":
                print(ACC)
            case "INP":
                user_inp = input("Awaiting user input: ")
                ACC = int(user_inp)
            case "HLT":
                print("Halting program...")
                break
            case _:
                pass
            
            
            
            