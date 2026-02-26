import functools as f

def mult(a,b):
    return a*b

num_list = []
user_num = int(input("Input an integer: "))
for x in range(user_num):
    num_list.append(x+1)
    
print(f.reduce(mult, num_list))