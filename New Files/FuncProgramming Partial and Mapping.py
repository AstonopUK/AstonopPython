import functools as f

def adder(a,b,c,d):
    return a*b/c-d

def mult(a):
    return a*10

g = [10,20,30,40,50]

e = f.partial(adder, d=4, b=5, c=6)

print(e(69420))

h = map(mult, g)
print(list(h))