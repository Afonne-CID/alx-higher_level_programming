#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    sum = 0
    for arg in range(len(sys.argv) - 1):
        sum += int(sys.argv[arg + 1])
    print("{}".format(sum))
