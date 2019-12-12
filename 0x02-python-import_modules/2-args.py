#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if l - 1 > 0:
        print("{:d} arguments:".format(l - 1))
    else:
        print("0 arguments.")
    for i in range(1, l):
        print("{:d}: {}".format(i, sys.argv[i]))
