import random

a=0
b=0
tries=0

while tries != 100:
    a = int(random.randint(1, 2))
    if a == 1:
        b = b + 1
    tries = tries + 1
    

print("решек ", b)

print("\nорлов ", 100 - b)        


input("Enter for end")
