#!/usr/bin/python3
"""
This is ``2-matrix_divided.py`` module
--------------------------------------

The ``2-matrix_divided.py`` supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """ All elements of matrix are divided by div
    and the result is returned

    A corresponding Error is raise if not:
        div is an int or float and > 0
        All rows of matrix are of the same size.
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    for row in range(0, len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError(
                    "Each row of the matrix must have the same size")
        for value in matrix[row]:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
    return ([[round(x/div, 2) for x in row] for row in matrix])
