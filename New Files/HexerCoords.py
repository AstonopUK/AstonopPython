import functools as f
coords = []

def hexify(a):
    return hex(a)

def output_coords(a,b,c,d,e,f):
    print("Your coordinates were: ", a, b, c, d, e, f)

part_func = f.partial(output_coords)

for x in range(6):
    a = input("Input a coordinate: ")
    if a.isalpha() == False:
        coords.append(int(a))
    else:
        print("Coordinate skipped")

while len(coords) != 6:
    match len(coords):
        case 1:
            a = input("Input missing coordinate: ")
            if a.isalpha() == False:
                coords.append(int(a))
        case 2:
            a = input("Input missing coordinate: ")
            if a.isalpha() == False:
                coords.append(int(a))
        case 3:
            a = input("Input missing coordinate: ")
            if a.isalpha() == False:
                coords.append(int(a))
        case 4:
            a = input("Input missing coordinate: ")
            if a.isalpha() == False:
                coords.append(int(a))
        case 5:
            a = input("Input missing coordinate: ")
            if a.isalpha() == False:
                coords.append(int(a))
        case _:
            pass

part_func(coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])

output = map(hexify, coords)
print(list(output))