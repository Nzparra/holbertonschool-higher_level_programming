#!/usr/bin/python3
def magic_calculation(a, b):
    value = 0
    for c in range(1, 3)
        try:
            if c > a:
                raise Exception("Too far")
            value += (a ** b) / c
        except:
            value = a + b
            break
    return value
