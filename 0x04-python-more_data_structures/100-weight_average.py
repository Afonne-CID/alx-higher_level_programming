#!/usr/bin/python3


def weight_average(my_list=[]):
    """ weighted average"""
    sum_weigth = 0
    sum_percent = 0
    cnt = 0
    if (len(my_list) == 0):
        return (0)
    for each in my_list:
        cnt = each[0] * each[1]
        sum_weigth += cnt
        sum_percent += each[1]
    sum_weigth = sum_weigth / sum_percent
    return (sum_weigth)
