def check(x):
    return len(x) < 4

l = ["hello","this","is","two","towers"]
c = filter(lambda word:len(word)<4,l)
print(list(c))