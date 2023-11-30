#!/usr/bin/python3
for alphabet in range(25, -1, -1):
    letter = alphabet + 65
    if alphabet % 2 == 1:
        letter += 32
    print("{:c}".format(letter), end="")
