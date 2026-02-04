import random

word = input("word: ")
answer = ""

for i in range(0,len(word)):
    answer+=word[len(word)-i-1:len(word)-i]

print(answer)

input("Enter for end")
