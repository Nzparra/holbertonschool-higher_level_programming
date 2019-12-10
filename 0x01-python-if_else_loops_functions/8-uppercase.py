#!/usr/bin/python3
def uppercase(str):
    n = len(str)
    c = 1
    for i in str:
        i = ord(i)
        if i >= 97 and i <= 123:
            i -= 32
            c += 1
        print(chr(i), end = '')
    print("\n",end = '')
