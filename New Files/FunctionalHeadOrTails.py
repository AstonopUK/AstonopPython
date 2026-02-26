l = [1,2,3,4,5,6,7,8,9]

def head(l):
    print(l[0])
    
def tail(l):
    nl = []
    for x in range(len(l)-1):
        nl.append(l[x+1])
    print(nl)
    
head(l)
tail(l)