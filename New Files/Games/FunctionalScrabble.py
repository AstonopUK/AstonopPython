def replace(inpstr):
    if inpstr.isalpha():
        alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        score = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
        output = 0
        for char in inpstr.lower():
            output+=(score[alph.index(char)])
        return output
    else:
        return 0    
def compare(word1, word2):
    if replace(word1) > replace(word2):
        return (word1 + " wins!")
    elif replace(word1) < replace(word2):
        return (word2 + " wins!")
    else:
        return ("It's a tie!")
print(compare(input("Enter scrabble word 1: "), input("Enter scrabble word 2: ")).capitalize())