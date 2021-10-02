#!/usr/bin/python3
"""
``5-text_indentation`` module
===============================

``5-text_indentation`` mudule supplies one function, text_indentation()
"""


def text_indentation(text):
    """ Prints 2 new lines after the occurence of each of . , ? and :

    Args:
        text: Bunch of text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    last = ""
    for i in text:
        if i in ".?:":
            if last != i:
                last = i
                print("{}\n".format(i))
        elif i == " " and last:
            last = ""
            continue
        else:
            last = ""
            print(i, end="")
