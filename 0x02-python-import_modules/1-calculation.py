#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator.div(a, b)))
