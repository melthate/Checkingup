import random

print(
"""
Добро пожаловать в игру анаграммы!
Надо переставить буквы так. чтобы получилось осмысленное слово.
From vole to...
""")

correct = "love"

score = len(correct)

guess = str(input("\nПопробуй отгадать исходное слово: "))
while guess != correct and guess != "":
    print("nah", correct[score-1])
    score -= 1
    guess = input("Попробуй отгадать исходное слово: ")

if guess == correct:
    print("Score is ", score)
    print("\nCorrecto!\n")

input("\n\nEnter to escape")
