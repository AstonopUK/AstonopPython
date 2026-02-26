from functools import reduce

def add(a,b):
    return a+b

mylist = [0,1,2,3,4,5]

print(reduce(add, mylist))



