#!/usr/bin/python3
"""Peak finding algorithm with the lowest complexity
"""


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers

    Args:
        list_of_integers: List of integers
    """

    size = len(list_of_integers)

    if (list_of_integers == []):
        return None
    if (size == 1):
        return list_of_integers[0]

    if (size == 2):
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        elif list_of_integers[1] > list_of_integers[0]:
            return list_of_integers[1]
        else: list_of_integers[0]

    pivot = int(size / 2)
    peak = list_of_integers[pivot]

    if peak > list_of_integers[pivot - 1] and peak > list_of_integers[pivot + 1]:
        return peak
    elif peak < list_of_integers[pivot - 1]:
        return find_peak(list_of_integers[:pivot])
    else:
        return find_peak(list_of_integers[pivot + 1:])
