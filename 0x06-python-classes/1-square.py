#!/usr/bin/python3
'''Define a class, called Square'''


class Square:
    '''A class to represent a square.'''
    def __init__(self, size):
        '''We are keeping our instance attribute "size" private
        because in this case, we are creating a square which
        will require a size. Since the size of a square is crucial
        and things like area computation depend of it.
        '''
        self.__size = size
