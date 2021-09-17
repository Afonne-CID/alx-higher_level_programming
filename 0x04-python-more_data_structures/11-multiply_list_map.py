#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    ''' multiplies all elements of a list by a given number '''
    return (list(map(lambda x: x*number, my_list)))
