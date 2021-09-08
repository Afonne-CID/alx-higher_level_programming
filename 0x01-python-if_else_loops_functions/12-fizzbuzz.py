#!/usr/bin/python3


def fizzbuzz():
    for digit in range(1, 101):
        if digit % 3 == 0 and digit % 5 == 0:
            print('FizzBuzz', end=" ")
        elif digit % 5 == 0:
            print('Buzz', end=" ")
        elif digit % 3 == 0:
            print('Fizz', end=" ")
        else:
            print(digit, end=" ")
