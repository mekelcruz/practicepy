import random

def game():
    i = 1
    x = random.randint(1, 10000)
    while True:


        user = int(input("Guess The Number 1-10\n"))
        if user<x:
             print("taasan mo pa")
        elif user>x:
            print("babaan mo pa")
        else:
            print("nice one galing")
            break
        print(i, "count of guess")
        i+=1


while True:

    i = int(input("\nWanna Play?\n1. Yes\n2. No\n->"))
    if i == 1:
        game()
    else:
        print("Thank You for Playing!")
        break
