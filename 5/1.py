import random

WORDS = ("1", "2", "3")
used = []

for i in WORDS:
    word = random.choice(WORDS)
    while word in used:
        word = random.choice(WORDS)
    used.append(word)
    print(word)

input("\n\nENTER")
