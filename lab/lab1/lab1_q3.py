import random

def create_permutation(n):
    lst = []
    while len(lst) != n:
        x = random.randint(0, n - 1)
        if x not in lst:
            lst.append(x)
    return lst



def scramble_word(word):
    indicies = create_permutation(len(word))
    s = ''
    for i in indicies:
        s += word[i]

    return s


print(scramble_word('pokemon'))

def main(word):
    scrambledWord = scramble_word(word)
    print("Unscarmble the word:", end = " ")
    for i in scrambledWord:
        print(i+"  ",end=" ")
    print(" ")
    x = True
    count = 1
    while x==True:
        y = input("try #" + str(count))
        if y == word:
            print("Correct!")
            x=False
        else:
            print("Wrong!")
            count+=1
        if count==4:
            x=False

main('pokemon' )

