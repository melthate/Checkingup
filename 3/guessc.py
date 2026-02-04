import random

guess = int(input("Enter from 1-100: "))
tries=0

while tries!=101:
    if tries == guess:
        print("your number is ", tries)
        tries = 101
    else:
        tries += 1

input("Enter for end")
