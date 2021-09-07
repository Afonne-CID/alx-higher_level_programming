#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_ver = str(number)
str_ver = str_ver[-1]
last_digit = int(str_ver)

if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(
        number, last_digit))
elif last_digit < 6 and not(0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
        number, last_digit))
