#!/usr/bin/python3
for i in range(0, 10):
    for d in range(0, 10):
        if i != d and i < d and i != 8:
            print("{:d}{:d}".format(i, d), end=', ')
        if i == 8 and i < d:
            print("{:d}{:d}".format(i, d))
