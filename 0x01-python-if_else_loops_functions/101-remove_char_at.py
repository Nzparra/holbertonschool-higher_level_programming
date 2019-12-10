#!/usr/bin/python3
def remove_char_at(str, n):
    c = 0
    str1 = ""
    if n < 0:
        return(str)
    for i in str:
        if c == n:
            pass
        else:
            str1 += i
        c += 1
    return(str1)
