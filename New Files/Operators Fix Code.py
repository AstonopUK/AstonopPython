# FILL THE GAPS IN THE CODE BELOW

#User inputs a number to go to
number = input("Input a number to calculate to: ")

#Program loops for as many times as the number specified
for x in range(number):
    #For each number that has no remainder when divided
    #by 6, print the number
    if x / 6 == 0:
        print(x)
        
#IF COMPLETED, ADD ANOTHER CHECK IF THE NUMBER IS DIVISIBLE BY
#15 AND PRINT THE NUMBER FOLLOWED BY " BY 15 TOO"