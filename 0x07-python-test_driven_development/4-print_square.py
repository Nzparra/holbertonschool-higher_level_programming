#!/usr/bin/python3


def print_square(size):

    if not isinstance(size, (float, int, bool)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for j in range(int(size)):
        print("#" * int(size))
