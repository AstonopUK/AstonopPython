def latinizer(x):
    return lambda z:(z[1:len(z)]+z[0])+x

def lister(y):
    newlist = []
    newstring = ""
    for char in y:
        if char != " ":
            newstring += char
        else:
            newlist.append(newstring)
            newstring=""
    newlist.append(newstring)
    return newlist

customlatin = latinizer(input("Input your custom characters: "))
print(list(map(customlatin, lister(input("Enter a sentence: ")))))