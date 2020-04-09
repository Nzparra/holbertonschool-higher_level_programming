#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    leng = len(list_of_integers)
    med = int(leng * 0.5)
    lis = list_of_integers
    if med - 1 < 0 and med + 1 >= leng:
        return lis[med]
    elif med - 1 < 0:
        return lis[med] if lis[med] > lis[med + 1] else lis[med + 1]
    elif med + 1 >= leng:
        return lis[med] if lis[med] > lis[med - 1] else lis[med - 1]
    if lis[med - 1] < lis[med] > lis[med + 1]:
        return lis[med]
    if lis[med + 1] > lis[med - 1]:
        return find_peak(lis[med:])
    return find_peak(lis[:med])
