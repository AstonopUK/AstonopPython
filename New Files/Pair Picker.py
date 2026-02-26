import random

print("Enter names:")
i = input()
names = []
while i!="d":
    names.append(i)
    i = input()
    
while len(names)>0:
    if len(names)>1:
        n1 = random.choice(names)
        names.remove(n1)
        n2 = random.choice(names)
        names.remove(n2)
        print(n1,"&",n2)
    else:
        print(names[0])
        names.pop(0)
