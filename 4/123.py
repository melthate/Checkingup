import random

first = int(input("First number: "))
second = int(input("Second number: ")) 
interval = int(input("Intervals: "))
for i in range(first, second, interval):
    print(i)

input("Enter for end")
