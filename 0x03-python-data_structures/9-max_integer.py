#!/usr/bin/python3


def max_integer(my_list=[]):
    current_max = my_list[0]
    for each in my_list:
        if each < current_max:
            continue
        else:
            current_max = each
    return (current_max)
