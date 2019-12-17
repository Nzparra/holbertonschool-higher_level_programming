#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = list(tuple_a) + [0]*2
    b = list(tuple_b) + [0]*2
    d = [x + y for x, y in zip(c, b)]
    return tuple(d[0:2])
