import random

while True:
    matrix = ""
    for x in range(165):
        matrix = matrix + str(random.randint(0,1))
    print(matrix)