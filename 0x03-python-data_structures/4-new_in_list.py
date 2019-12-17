#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if(my_list) is None:
        return (None)
    if(idx < 0):
        return (None)
    if(idx > len(my_list)):
        return (None)
    n_list = my_list[:]
    n_list[idx] = element
    return(n_list)
