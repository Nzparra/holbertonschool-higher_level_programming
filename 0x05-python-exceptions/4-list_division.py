#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    idx = 0
    for c in range(list_length):
        try:
            div = my_list_1[c] / my_list_2[c]
        except TypeError:
            print("wrong type")
            idx = 1
        except ZeroDivisionError:
            print("division by 0")
            idx = 1
        except IndexError:
            print("out of range")
            idx = 1
        finally:
            if idx:
                idx = 0
                new_list.append(idx)
            else:
                new_list.append(div)
    return new_list
