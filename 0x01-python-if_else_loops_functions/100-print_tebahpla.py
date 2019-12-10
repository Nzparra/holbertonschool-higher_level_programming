#!/usr/bin/python3
c = 1
for i in range(122, 96, -1):
    if (c % 2 == 0):
        i -= 32
    c += 1
    print("{}".format(chr(i)), end="")
