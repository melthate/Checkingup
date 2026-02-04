import random

words = ["love", "future", "cry"]
answer1 = ""
letters = 0

word = random.choice(words)

print(len(word), " letters in the word")

while letters != 5:
    answer1 = input("Guess letter: ")
    for i in range(0,len(word)):
        if answer1 == word[i]:
            print("Correct")
        else:
            print("Try one more")
    letters += 1

answer2 = input("Final answer:")
if answer2 == word:
    print("Correcto")
else:
    print("Try next time")

input("Enter for end")
