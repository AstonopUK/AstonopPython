instructionSet = {
    "HLT": 0,
    "ADD": 1,
    "SUB": 2,
    "STO": 3,
    "LDA": 4,
    "BRA": 5,
    "BRZ": 6,
    "BRP": 7,
    "INP": 8,
    "OUT": 9
    }

registers = {
    "MDR": 0,
    "MAR": 0,
    "PC": 0,
    "ACC": 0
    }

mainMemory = []
for x in range(100):
    mainMemory.append(0)


        