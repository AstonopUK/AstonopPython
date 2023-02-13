#Example 1:
def hello_world():
    print("Hello world!")

hello_world()






#Example 2:
def add_two_nums():
    number1 = int(input("Input the first number.\n"))
    number2 = int(input("Input the second number.\n"))

    return number1 + number2

print("\n", add_two_nums())






#Example 3:
list = ["Tom", "Dick", "Harry"]
def print_all_names(listofnames):
    for names in listofnames:
        print(names)

print_all_names(list)






#Example 4:
def three_number_adder(alistofnumbers):
    sum = 0
    for integer in alistofnumbers:
        sum += integer

    return sum

listofnums= []
num1 = int(input("Input the first number.\n"))
num2 = int(input("Input the second number.\n"))
num3 = int(input("Input the third number.\n"))

listofnums.append(num1)
listofnums.append(num2)
listofnums.append(num3)

print(three_number_adder(listofnums))





#You do it task (Modify)

def item_price_adder(price1, price2):
    totalPrice = 0

    #Write your own code here that adds the two prices and sets the value to the totalPrice variable
    
    return totalPrice

priceofitem1 = int(input("Input the first number.\n"))
priceofitem2 = int(input("Input the second number.\n"))

print(item_price_adder(priceofitem1,priceofitem2)


