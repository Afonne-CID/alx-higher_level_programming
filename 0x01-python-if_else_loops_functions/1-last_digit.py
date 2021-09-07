#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = abs(number) % 10
if number < 0:
    result = -result
print("Last digit of {} is {} and is ".format(number, result), end="")
if result > 5:
    print("greater than 5")
elif result == 0:
    print("0")
else:
    print("less than 6 and not 0")
