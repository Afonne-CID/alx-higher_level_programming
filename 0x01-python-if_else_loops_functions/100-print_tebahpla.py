#!/usr/bin/python3
letter_was_not_cap = True
for letter in range(122, 96, -1):
    if letter_was_not_cap:
        letter_was_not_cap = False
    else:
        letter -= 32
        letter_was_not_cap = True
    print("{}".format(chr(letter)), end="")
