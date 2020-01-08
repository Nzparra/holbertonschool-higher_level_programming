#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for c in range(x):
            print("{}".format(my_list[c]), end="")
    except IndexError:
        return c
    else:
        return x
    finally:
        print()
