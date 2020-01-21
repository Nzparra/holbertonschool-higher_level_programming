#!/usr/bin/python3
def number_of_lines(filename=""):
    c = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            c += 1
    return c
