#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
represeinting the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle
    or empty list if n <= 0

    Args:
        n (int): An integer
    """
    if n <= 0:
        return []
    my_list = [[1]]
    while n > 1:
        for i in range(len(my_list[-1])):
            cnt = i - 1
            new_list = [1]
            while cnt > 0:
                new_list.append(1+(my_list[-1][cnt-1]))
                cnt -= 1
            new_list.append(1)
        my_list.append(new_list)
        n -= 1
    return my_list
