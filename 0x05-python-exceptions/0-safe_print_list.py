#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ret = ''.join(str(x) for x in my_list[:x])
        print(ret)
        return (int(ret))
    except IndexError as err:
        print(err)
