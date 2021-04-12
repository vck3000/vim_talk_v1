import random

letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(20):
    line = ''

    for i in range(4):
        r = random.randint(0, 25)
        line += letters[r]

    for i in range(4):
        r = random.randint(0, 9)
        line += str(r)

    print(line)
