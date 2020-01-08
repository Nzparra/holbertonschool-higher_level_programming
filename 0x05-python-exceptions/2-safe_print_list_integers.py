#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    times = 0
    try:
        for c in range(x):
            if isinstance(my_list[c], int):
                times = times + 1
                print("{:d}".format(my_list[c]), end="")
    except TypeError as er:
        print(er)
    else:
        print()
        return times
