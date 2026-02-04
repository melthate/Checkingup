import random

guess = int(0)
a = random.randint(1, 9)
tries=0

while tries < 5:
    guess = int(input("Enter from 1-9: "))
    if guess == a:
        print("You won")
        tries+=10
    else:
        print("nah")
        tries+=1
    if tries == 5:
        print("lose")

input("Enter for end")
